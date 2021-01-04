### 使用指南

#### batch_clb_ops.py 负责负载均衡相关操作

usage: batch_clb_ops.py [-h] --do
                        {prepare,create_listener,bind_cvm,export_report}

1. prepare，生成负载均衡与服务器的映射关系，输出Excel表记录映射结果。（依赖完成负载均衡和服务器的创建）
2. create_listener，根据prepare生成的映射关系，批量创建负载均衡监听器。一个监听器关联一台服务器。
3. bind_cvm，将负载均衡监听器与服务器一一绑定。
4. export_report，输出最终的Excel报告，记录公网IP、端口、登陆密码和服务器ID。

#### batch_cvm_ops.py 负责云服务器相关操作
usage: batch_cvm_ops.py [-h] --do
                        {create,destroy,power_on,power_off,reset_system_disk,reset_password}
                        [--nums NUMS]

1. create，批量创建指定数量的服务器，--nums必填参数。
2. destroy, 批量释放所有服务器。
3. power_on/power_off，批量开关机。
4. reset_system_disk，批量重装系统。
5. reset_password，批量重置密码。

### 操作流程
1. 批量创建服务器（确认所有服务器处于“运行中”状态）
python3 batch_cvm_ops.py --do create --nums 1500

2. 批量创建负载均衡（数量有限，控制台操作)

3. 生成负载均衡与服务器的映射关系
python3 batch_clb_ops.py --do prepare

4. 批量创建监听器
python3 batch_clb_ops.py --do create_listener

5. 批量绑定服务器
python3 batch_clb_ops.py --do bind_cvm

6. 批量重置密码
python3 batch_cvm_ops.py --do reset_password

7. 生成最终Excel报告
python3 batch_clb_ops.py --do export_report

8. 定期重装系统（重装系统会默认重置密码，须再次生成最终报告）
python3 batch_cvm_ops.py --do reset_system_disk


### 注意事项：
1.服务器属于同一个业务，不同业务请用项目空间隔离。
2.服务器采购以100为单位，实际存量>100。
3.无特殊说明，均以默认配置为准。
4.重装系统会重置密码，参考Excel表格，预计2分钟100台。
5.仅支持Python3.7，其他版本自行适配。
6.3000台批量关机耗时7分钟；3000台批量重置密码耗时40分钟；
7.脚本执行完成，不代表结果正确，实际以控制台展示为准，重点关注数量和状态两个指标；
8.存在部分类型云服务售罄的情况，大批量购买前请与腾讯云确认资源；:
