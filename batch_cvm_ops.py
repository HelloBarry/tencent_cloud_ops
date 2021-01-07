# -*- coding: utf-8 -*-
import os
import argparse
import random
import time
import logging


from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.cvm.v20170312 import cvm_client, models

# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

# 注意事项：
# 1.服务器属于同一个业务，不同业务请用项目空间隔离。
# 2.服务器采购以100为单位，实际存量>100。
# 3.无特殊说明，均以默认配置为准。
# 4.重装系统会重置密码，参考Excel表格，预计2分钟100台。
# 5.仅支持Python3.7，其他版本自行适配。
# 6.3000台批量关机耗时7分钟；3000台批量重置密码耗时40分钟；
# 7.脚本执行完成，不代表结果正确，实际以控制台展示为准，重点关注数量和状态两个指标；
# 8.存在部分类型云服务售罄的情况，大批量购买前请与腾讯云确认资源；

# 必填参数
REGION = "ap-shanghai"
TENCENTCLOUD_SECRET_ID = ""
TENCENTCLOUD_SECRET_KEY = ""

# 可选参数
IMAGE_ID = ""
INSTANCE_TYPE = "S5.LARGE8"
SYS_DISK_TYPE = "CLOUD_PREMIUM" # 高性能云硬盘

# 全局变量（内部使用）
TOTAL_CVM_INSTANCES = {}
ITEM_UNIT = 100
PW_LENGTH = 20
PW_CHARS = 'abcdefghijklmnopqrstuvwxyz'
PW_MAGIC_WORDS = "()`~!@#$%^&*-+=_|{}[]:;'<>,.?"
CVM_EXCEL_FILE = "CVM Info.xls"
CVM_EXCEL_SHEET = "云服务器信息汇总"


# 配置输出方式与日志级别
logging.basicConfig(filename='cvm.log', level=logging.INFO)

# 获取客户端句柄
def _get_cvm_client():
    cred = credential.Credential(TENCENTCLOUD_SECRET_ID, TENCENTCLOUD_SECRET_KEY)
    return cvm_client.CvmClient(cred, REGION)

# 判断请求是否成功
def _succeed(resp):
    if "Error" in resp.to_json_string():
        logging.warning(resp.to_json_string())
        return False
    return True

# 获取全量云服务器信息
# 异常无需处理
def _describe_instances():
    global TOTAL_CVM_INSTANCES
    TOTAL_CVM_INSTANCES.clear()

    client = _get_cvm_client()

    offset = 0
    while (True):
        req = models.DescribeInstancesRequest()
        req.Offset = offset
        req.Limit = ITEM_UNIT

        resp = client.DescribeInstances(req)
        for instance in resp.InstanceSet:
            TOTAL_CVM_INSTANCES[instance.InstanceId] = instance

        if len(resp.InstanceSet) < ITEM_UNIT:
            break
        offset = offset + ITEM_UNIT
        time.sleep(0.025)

# 生成Windows服务器随机密码
def _generate_instance_password():
    words = PW_CHARS + PW_CHARS.upper() + PW_MAGIC_WORDS
    return ''.join(random.sample(words, PW_LENGTH-1)) + random.choice(PW_MAGIC_WORDS)

# 导出实例信息到Excel
def _dump_to_excel():
    import xlwt

    # 创建 xls 文件对象
    wb = xlwt.Workbook()

    # 新增表单页
    sheet = wb.add_sheet(CVM_EXCEL_SHEET)

    # 然后按照位置来添加数据,第一个参数是行，第二个参数是列
    # 写入第一行数据
    sheet.write(0, 0, '实例ID')
    sheet.write(0, 1, '实例名称')
    sheet.write(0, 2, '内网IP')
    sheet.write(0, 3, '登陆密码')

    row = 1
    for instance in TOTAL_CVM_INSTANCES.values():
        sheet.write(row, 0, instance.InstanceId)
        sheet.write(row, 1, instance.InstanceName)
        sheet.write(row, 2, instance.PrivateIpAddresses)
        sheet.write(row, 3, instance.Password)
        row = row + 1

    # 保存文件
    wb.save(CVM_EXCEL_FILE)

# 批量重置服务器密码
def _reset_cvm_password():
    _describe_instances()

    client = _get_cvm_client()

    for instance_id, instance in TOTAL_CVM_INSTANCES.items():
        new_password = _generate_instance_password()
        req = models.ResetInstancesPasswordRequest()
        req.InstanceIds = [instance_id]
        req.Password = new_password
        req.ForceStop = True

        resp = client.ResetInstancesPassword(req)
        if not _succeed(resp):
            logging.warning("Fail to ResetInstancesPassword, need retry for %s" % instance_id)
            time.sleep(1)
            continue
        instance.Password = new_password

        time.sleep(0.1)

    _dump_to_excel()

# 批量开机
def _power_cvm_on():
    _describe_instances()

    client = _get_cvm_client()
    instance_ids = list(TOTAL_CVM_INSTANCES.keys())
    if len(instance_ids) == 0:
        return

    iter = len(instance_ids) / ITEM_UNIT
    left = len(instance_ids) % ITEM_UNIT

    count = 0
    while (count <= iter):
        req = models.StartInstancesRequest()
        if count < iter:
            req.InstanceIds = instance_ids[count*ITEM_UNIT : (count+1)*ITEM_UNIT]
        elif left:
            req.InstanceIds = instance_ids[-left:]
        else:
            break

        resp = client.StartInstances(req)
        if not _succeed(resp):
            logging.warning("Fail to StartInstances, need retry manually")
        count = count + 1
        time.sleep(0.1)

# 批量关机
def _power_cvm_off():
    _describe_instances()

    client = _get_cvm_client()
    instance_ids = list(TOTAL_CVM_INSTANCES.keys())
    if len(instance_ids) == 0:
        return

    iter = len(instance_ids) / ITEM_UNIT
    left = len(instance_ids) % ITEM_UNIT

    count = 0
    while (count <= iter):
        req = models.StopInstancesRequest()
        req.ForceStop = True
        req.StoppedMode = "STOP_CHARGING" # 关机不收费
        if count < iter:
            req.InstanceIds = instance_ids[count * ITEM_UNIT : (count + 1) * ITEM_UNIT]
        elif left:
            req.InstanceIds = instance_ids[-left:]
        else:
            break

        resp = client.StopInstances(req)
        if not _succeed(resp):
            logging.warning("Fail to StopInstances, need retry manually")
        count = count + 1
        time.sleep(0.1)

# 批量重装系统
def _reset_cvm_system_disk():
    _describe_instances()

    client = _get_cvm_client()

    for instance_id, instance in TOTAL_CVM_INSTANCES.items():
        new_password = _generate_instance_password()
        req = models.ResetInstanceRequest()
        req.InstanceId = instance_id
        req.LoginSettings = {"Password": new_password}

        resp = client.ResetInstance(req)
        if not _succeed(resp):
            logging.warning("Fail to ResetInstance, need retry %s" % instance_id)
            time.sleep(5)
            continue
        instance.Password = new_password

        time.sleep(1)

    _dump_to_excel()

# 批量创建云服务器
def _create_cvm(nums):
    client = _get_cvm_client()

    if nums <= 0:
        raise Exception("Fail to create cvm[%d]" % nums)

    if not IMAGE_ID:
        raise Exception("Empty Image ID")

    iter = nums / ITEM_UNIT
    left = nums % ITEM_UNIT

    count = 0
    while (count <= iter):
        req = models.RunInstancesRequest()
        req.ImageId = IMAGE_ID
        req.InstanceChargeType = "POSTPAID_BY_HOUR"
        req.InstanceType = INSTANCE_TYPE
        req.SystemDisk = {"DiskType": SYS_DISK_TYPE, "DiskSize": 50}
        req.VirtualPrivateCloud = {"VpcId": "DEFAULT", "SubnetId": "DEFAULT"}
        req.InstanceCount = ITEM_UNIT if count < iter else left

        resp = client.RunInstances(req)

        if not _succeed(resp):
            logging.warning(resp.to_json_string())

        count = count + 1
        time.sleep(0.1)

# 批量销毁全部云服务器
def _destroy_cvm():
    _describe_instances()

    client = _get_cvm_client()
    instance_ids = list(TOTAL_CVM_INSTANCES.keys())
    if len(instance_ids) == 0:
        return

    iter = len(instance_ids) / ITEM_UNIT
    left = len(instance_ids) % ITEM_UNIT

    count = 0
    while (count <= iter):
        req = models.TerminateInstancesRequest()
        if count < iter:
            req.InstanceIds = instance_ids[count*ITEM_UNIT : (count+1)*ITEM_UNIT]
        elif left:
            req.InstanceIds = instance_ids[-left:]
        else:
            break

        resp = client.TerminateInstances(req)
        if not _succeed(resp):
            logging.warning("Fail to TerminateInstances, need retry manually")
        count = count + 1
        time.sleep(0.1)

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--do", dest="do", required=True,
                            choices=["create", "destroy", "power_on", "power_off", "reset_system_disk", "reset_password"])
        parser.add_argument("--nums", dest="nums", required=False, default=0)
        args = parser.parse_args()
        if args.do == "create" and args.nums:
            _create_cvm(int(args.nums))
        elif args.do == "destroy":
            _destroy_cvm()
        elif args.do == "power_on":
            _power_cvm_on()
        elif args.do == "power_off":
            _power_cvm_off()
        elif args.do == "reset_system_disk":
            _reset_cvm_system_disk()
        elif args.do == "reset_password":
            _reset_cvm_password()
        else:
            parser.print_help()

    except TencentCloudSDKException as err:
        print(err)

if __name__=="__main__":
    main()
