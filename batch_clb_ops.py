# -*- coding: utf-8 -*-
import os
import argparse
import random
import time
import logging

import xlwt
import xlrd

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.cvm.v20170312 import cvm_client
from tencentcloud.cvm.v20170312 import models as cvm_models
from tencentcloud.clb.v20180317 import clb_client
from tencentcloud.clb.v20180317 import models as clb_models


# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

# 注意事项：
# 1.无特殊说明，均以默认配置为准。
# 2.仅支持Python3.7，其他版本自行适配。

# 必填参数
REGION = "ap-shanghai"
TENCENTCLOUD_SECRET_ID = ""
TENCENTCLOUD_SECRET_KEY = ""

# 全局变量（内部使用）
TOTAL_CVM_INSTANCES = {}
TOTAL_CLB_INSTANCES = {}
ITEM_UNIT = 100
CLB_LISTENER_NUM = 50
PORT_START = 8000
CLB_EXCEL_FILE = 'CLB Info.xls'
CLB_EXCEL_SHEET = '负载均衡信息汇总'
CVM_EXCEL_FILE = "CVM Info.xls"
CVM_EXCEL_SHEET = "云服务器信息汇总"
REPORT_EXCEL_FILE = "Final Report.xls"
REPORT_EXCEL_SHEET = "汇总信息"


# 配置输出方式与日志级别
logging.basicConfig(filename='clb.log', level=logging.INFO)

# 获取客户端句柄
def _get_cvm_client():
    cred = credential.Credential(TENCENTCLOUD_SECRET_ID, TENCENTCLOUD_SECRET_KEY)
    return cvm_client.CvmClient(cred, REGION)

def _get_clb_client():
    cred = credential.Credential(TENCENTCLOUD_SECRET_ID, TENCENTCLOUD_SECRET_KEY)
    return clb_client.ClbClient(cred, REGION)

# 判断请求是否成功
def _succeed(resp):
    if "Error" in resp.to_json_string():
        logging.warning(resp.to_json_string())
        return False
    return True

# 获取全量云服务器信息
# 异常无需处理
def _describe_cvm_instances():
    global TOTAL_CVM_INSTANCES
    TOTAL_CVM_INSTANCES.clear()

    client = _get_cvm_client()
    offset = 0

    while (True):
        req = cvm_models.DescribeInstancesRequest()
        req.Offset = offset
        req.Limit = ITEM_UNIT

        resp = client.DescribeInstances(req)
        for instance in resp.InstanceSet:
            TOTAL_CVM_INSTANCES[instance.InstanceId] = instance

        if len(resp.InstanceSet) < ITEM_UNIT:
            break
        offset = offset + ITEM_UNIT
        time.sleep(0.025)

# 获取全量CLB实例
# 异常无需处理
def _describe_clb_instances():
    global TOTAL_CLB_INSTANCES
    TOTAL_CLB_INSTANCES.clear()

    req = clb_models.DescribeLoadBalancersRequest()
    client = _get_clb_client()
    resp = client.DescribeLoadBalancers(req)
    total_count = resp.TotalCount

    offset = 0
    while (True):
        req = clb_models.DescribeLoadBalancersRequest()
        req.Offset = offset
        req.Limit = ITEM_UNIT

        resp = client.DescribeLoadBalancers(req)
        for instance in resp.LoadBalancerSet:
            TOTAL_CLB_INSTANCES[instance.LoadBalancerId] = instance

        if len(resp.LoadBalancerSet) < ITEM_UNIT:
            break
        offset = offset + ITEM_UNIT
        time.sleep(0.05)

# 批量创建监听器
def _batch_create_clb_listener():
    wb = xlrd.open_workbook(CLB_EXCEL_FILE)
    sheet = wb.sheet_by_name(CLB_EXCEL_SHEET)

    results = {}
    for i in range(1, sheet.nrows):
        clb_id = sheet.row(i)[0].value
        listener_name = sheet.row(i)[3].value
        listener_port = int(sheet.row(i)[4].value)
        if clb_id not in results:
            results[clb_id] = {"ListenerNames": [], "Ports": []}
        results[clb_id]["ListenerNames"].append(listener_name)
        results[clb_id]["Ports"].append(listener_port)

    client = _get_clb_client()
    for k, v in results.items():
        req = clb_models.CreateListenerRequest()
        req.LoadBalancerId = k
        req.Ports = v["Ports"]
        req.Protocol = "TCP"
        req.ListenerNames = v["ListenerNames"]

        resp = client.CreateListener(req)
        if not _succeed(resp):
            logging.warning("Fail to CreateListener, need retry for %s" % k)
        time.sleep(0.05)

# 批量绑定服务器
def _batch_bind_clb_with_cvm():
    _describe_clb_instances()

    client = _get_clb_client()

    clbs = list(TOTAL_CLB_INSTANCES.keys())
    for clb_id in clbs:
        req = clb_models.DescribeListenersRequest()
        req.LoadBalancerId = clb_id
        resp = client.DescribeListeners(req)

        if not _succeed(resp):
            logging.warning("Fail to DescribeListeners, need retry for %s" % clb_id)

        req = clb_models.BatchRegisterTargetsRequest()
        req.LoadBalancerId = clb_id
        req.Targets = []

        for listener in resp.Listeners:
            listener_id = listener.ListenerId
            cvm_instance_id = listener.ListenerName
            req.Targets.append({"ListenerId": listener_id, "Port": 3389, "InstanceId": cvm_instance_id, "Weight": 100})

        resp = client.BatchRegisterTargets(req)
        if not _succeed(resp):
            logging.warning("Fail to BatchRegisterTargets, need retry for %s" % clb_id)

        time.sleep(1)

# 生成负载均衡监听器配置
def _prepare():
    _describe_clb_instances()
    _describe_cvm_instances()

    clbs = list(TOTAL_CLB_INSTANCES.keys())
    cvms = list(TOTAL_CVM_INSTANCES.keys())

    if len(clbs)*CLB_LISTENER_NUM != len(cvms):
        raise Exception("CLB(%d)和CVM(%d)数量不匹配。" % (len(clbs), len(cvms)))

    # 创建 xls 文件对象
    wb = xlwt.Workbook()

    # 新增两个表单页
    sheet = wb.add_sheet(CLB_EXCEL_SHEET)

    # 然后按照位置来添加数据,第一个参数是行，第二个参数是列
    # 写入第一行数据
    sheet.write(0, 0, '负载均衡ID')
    sheet.write(0, 1, '负载均衡IP')
    sheet.write(0, 2, '监听器ID')
    sheet.write(0, 3, '监听器名称')
    sheet.write(0, 4, '监听器端口')

    for i in range(0, len(clbs)):
        for j in range(0, CLB_LISTENER_NUM):
            sheet.write(i*CLB_LISTENER_NUM+j+1, 0, clbs[i])
            sheet.write(i*CLB_LISTENER_NUM+j+1, 1, TOTAL_CLB_INSTANCES[clbs[i]].LoadBalancerVips[0])
            sheet.write(i*CLB_LISTENER_NUM+j+1, 2, '')
            sheet.write(i*CLB_LISTENER_NUM+j+1, 3, cvms[i*CLB_LISTENER_NUM+j])
            sheet.write(i*CLB_LISTENER_NUM+j+1, 4, PORT_START+j)

    # 保存文件
    wb.save(CLB_EXCEL_FILE)

# 生成最终的对外汇总信息
def _export_report():
    # 读取CVM密码映射
    cvms = {}
    wb_cvm = xlrd.open_workbook(CVM_EXCEL_FILE)
    sheet_cvm = wb_cvm.sheet_by_name(CVM_EXCEL_SHEET)

    for i in range(1, sheet_cvm.nrows):
        cvm_instance_id = sheet_cvm.row(i)[0].value
        cvm_instance_pwd = sheet_cvm.row(i)[3].value
        cvms[cvm_instance_id] = cvm_instance_pwd

    # 读取负载均衡配置
    listeners = {}
    wb_clb = xlrd.open_workbook(CLB_EXCEL_FILE)
    sheet_clb = wb_clb.sheet_by_name(CLB_EXCEL_SHEET)

    for i in range(1, sheet_clb.nrows):
        clb_vip = sheet_clb.row(i)[1].value
        clb_port = sheet_clb.row(i)[4].value
        clb_listener = sheet_clb.row(i)[3].value
        listeners[clb_listener] = {"VIP": clb_vip, "Port": clb_port, "Password": cvms[clb_listener]}

    # 生成最终汇总信息
    wb_report = xlwt.Workbook()

    sheet_report = wb_report.add_sheet(REPORT_EXCEL_SHEET)

    # 然后按照位置来添加数据,第一个参数是行，第二个参数是列
    # 写入第一行数据
    sheet_report.write(0, 0, '公网IP')
    sheet_report.write(0, 1, '公网端口')
    sheet_report.write(0, 2, '登陆密码')
    sheet_report.write(0, 3, '服务器ID')

    i = 1
    for k, v in listeners.items():
        sheet_report.write(i, 0, v["VIP"])
        sheet_report.write(i, 1, v["Port"])
        sheet_report.write(i, 2, v["Password"])
        sheet_report.write(i, 3, k)
        i = i + 1

    # 保存文件
    wb_report.save(REPORT_EXCEL_FILE)

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--do", dest="do", required=True,
                            choices=["prepare", "create_listener", "bind_cvm", "export_report"])
        args = parser.parse_args()
        if args.do == "prepare":
            _prepare()
        elif args.do == "create_listener":
            _batch_create_clb_listener()
        elif args.do == "bind_cvm":
            _batch_bind_clb_with_cvm()
        elif args.do == "export_report":
            _export_report()
        else:
            parser.print_help()

    except TencentCloudSDKException as err:
        print(err)

if __name__=="__main__":
    main()
