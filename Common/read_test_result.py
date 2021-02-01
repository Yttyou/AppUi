import datetime
import json
import re
import os
import time

import requests
import uiautomator2 as u2
import yaml
from TestDatas.iphone_whitelist import iphone_test_model
from Common.path_config import base_path
from Common.path_config import caps_path
from Common.Case_bug_ZenTao import get_iphone_info,app_Version
from Common.video_upload_download import run_upload_object_file,create_bucket


# 获取设备机型
def get_iphone_name():
    desired_caps = yaml.load(open(caps_path + "/bc_app_config.yaml"))
    deviceName = desired_caps["deviceName"]
    iphone_name = iphone_test_model.get(str(deviceName), None)
    return iphone_name

# 推送预警到BC ，设置阀值
def before_read_data():
    iphone_name = get_iphone_name()
    file_path = os.path.join(base_path, "HtmlTestReport/pytest_result.html")
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
        if re.search('type="checkbox"/><span class="failed">(\d+) failed</span>', data):
            failed_num = re.search('type="checkbox"/><span class="failed">(\d+) failed</span>', data).group(1)
        if re.search('type="checkbox"/><span class="error">(\d+) errors</span>', data):
            error_num = re.search('type="checkbox"/><span class="error">(\d+) errors</span>', data).group(1)
        all_num = int(failed_num) + int(error_num)
        if all_num > 0:
                # push_payload = json.dumps(
                #     {"text": ":warning: **Neptune Warning ** ：{} 机型，执行 SP 预发版包全量自动化测试，发现 {} 个测试脚本可能失效，请及时排查！@zhenghongwei @ytt".format(iphone_name, all_num)})
                # header = {"Content-Type": "application/json"}
                # requests.post("https://hook.bearychat.com/=bwD9B/incoming/f8305400e9d90bc3ad5f5a6509d6ad76",
                #               data=push_payload, headers=header)
                # scene_get_bug(iphone_name)
            push_payload = json.dumps(
                {"text": ":warning: **Neptune Warning ** ：{} 机型，执行 SP 预发版包全量自动化测试，发现 {} 个测试脚本可能失效，请及时排查！@zhenghongwei @ytt".format(iphone_name, all_num)})
            header = {"Content-Type": "application/json"}
            requests.post("https://hook.bearychat.com/=bwD9B/incoming/81cf5d716369000085cb1ae14ebe6ed3",
                          data=push_payload, headers=header)
            scene_get_bug(iphone_name)
        else:
            push_payload = json.dumps(
                {"text": ":warning: **Neptune Warning ** ： {} 机型，执行 SP 预发版包全量自动化测试，没有测试脚本失效，机械师干得漂亮 ！@zhenghongwei @ytt".format(iphone_name, all_num)})
            header = {"Content-Type": "application/json".format(iphone_name)}
            requests.post("https://hook.bearychat.com/=bwD9B/incoming/81cf5d716369000085cb1ae14ebe6ed3",
                          data=push_payload, headers=header)

# 场景二，接警
def scene_get_bug(iphone_name):
    push_payload = json.dumps(
        {"text": ":warning: **Neptune 机械师**已接到预警消息，已开始排查并修复 {} 机型脚本，4 小时内修复完成！@<-channel->".format(iphone_name)})
    header = {"Content-Type": "application/json"}
    requests.post("https://hook.bearychat.com/=bwD9B/incoming/81cf5d716369000085cb1ae14ebe6ed3",
              data=push_payload, headers=header)

# 处置完成，触发测试
def scene_repair_bug():
    new_file_path = os.path.join(base_path, "Neptune-runcase.txt")
    if os.path.exists(new_file_path):
        os.system("rm {} ".format(new_file_path))
    iphone_name = get_iphone_name()
    push_payload = json.dumps(
        {"text": ":warning: **Neptune 机械师**已完成 {} 机型脚本维护工作，现在进行全量测试，执行时间约 3 小时左右！@<-channel->".format(iphone_name)})
    header = {"Content-Type": "application/json"}
    requests.post("https://hook.bearychat.com/=bwD9B/incoming/81cf5d716369000085cb1ae14ebe6ed3",
                  data=push_payload, headers=header)

# 正式测试推送到BC
def end_read_data():
    iphone_name = get_iphone_name()
    file_path = os.path.join(base_path, "HtmlTestReport/pytest_result.html")
    bucket_name = str(datetime.date.today().strftime("%Y%m%d"))
    create_bucket(bucket_name)
    new_file_path = os.path.join(base_path,"Neptune-runcase.txt")
    download_url = run_upload_object_file(bucket_name,"Neptune-runcase.txt",new_file_path)[0]
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
        if re.search('type="checkbox"/><span class="failed">(\d+) failed</span>', data):
            failed_num = re.search('type="checkbox"/><span class="failed">(\d+) failed</span>', data).group(1)
            print(failed_num)
        if re.search('type="checkbox"/><span class="error">(\d+) errors</span>', data):
            error_num = re.search('type="checkbox"/><span class="error">(\d+) errors</span>', data).group(1)
            print(error_num)
        if re.search('type="checkbox"/><span class="passed">(\d+) passed</span>',data):
            passed_num = re.search('type="checkbox"/><span class="passed">(\d+) passed</span>',data).group(1)
        sum_num = int(failed_num)+int(error_num)+int(passed_num)
        all_num = int(failed_num) + int(error_num)
        number = int(all_num/sum_num*100)
        if all_num > 0:
            push_payload = json.dumps(
                {"text": "**Neptune 任务执行完毕** :triangular_flag_on_post: {} 机型，执行 SP Android 端 v{} 预发版包全量自动化测试，本次测试共执行了 {} 个用例，{}% 测试脚本执行`未通过` :x: ，发现 {} 个 Bug   :ant:  ，已提交至禅道。@<-channel->\n---\n[Neptune 测试日志传送门](<{}>)".format(
                        iphone_name, app_Version, sum_num, number, all_num,download_url)})
            header = {"Content-Type": "application/json"}
            requests.post("https://hook.bearychat.com/=bwD9B/incoming/f8305400e9d90bc3ad5f5a6509d6ad76",
                          data=push_payload, headers=header)
    os.system("rm {} ".format(new_file_path))

# 回归测试救命清单推送BC消息
def end_read_data_regression_test():
    iphone_name = get_iphone_name()
    file_path = os.path.join(base_path, "HtmlTestReport/pytest_result.html")
    bucket_name = str(datetime.date.today().strftime("%Y%m%d"))
    create_bucket(bucket_name)
    new_file_path = os.path.join(base_path,"Neptune-runcase.txt")
    download_url = run_upload_object_file(bucket_name,"Neptune-runcase.txt",new_file_path)[0]
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
        if re.search('type="checkbox"/><span class="failed">(\d+) failed</span>', data):
            failed_num = re.search('type="checkbox"/><span class="failed">(\d+) failed</span>', data).group(1)
            print(failed_num)
        if re.search('type="checkbox"/><span class="error">(\d+) errors</span>', data):
            error_num = re.search('type="checkbox"/><span class="error">(\d+) errors</span>', data).group(1)
            print(error_num)
        if re.search('type="checkbox"/><span class="passed">(\d+) passed</span>',data):
            passed_num = re.search('type="checkbox"/><span class="passed">(\d+) passed</span>',data).group(1)
        sum_num = int(failed_num)+int(error_num)+int(passed_num)
        all_num = int(failed_num) + int(error_num)
        number = int(all_num/sum_num*100)
        if all_num > 0:
            push_payload = json.dumps(
                {"text": "**Neptune 救命清单任务执行完毕** :triangular_flag_on_post:  {} 机型，执行 SP Android 端 v{} 救命清单自动化回归测试，本次测试共执行了 {} 个用例，{}% 测试脚本执行`未通过` :x: ，发现 {} 个 Bug   :ant:  ，已提交至禅道。@<-channel->\n---\n[Neptune 测试日志传送门](<{}>)".format(
                        iphone_name, app_Version, sum_num, number, all_num, download_url)})
            header = {"Content-Type": "application/json"}
            requests.post("https://hook.bearychat.com/=bwD9B/incoming/f8305400e9d90bc3ad5f5a6509d6ad76",
                          data=push_payload, headers=header)
    os.system("rm {} ".format(new_file_path))
