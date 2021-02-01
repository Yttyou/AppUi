"""  测试数据记录报BUG到禅道方法  """
import os
import allure
import logging
import json

import yaml

from TestDatas import COMMON_DATA
from Common.path_config import testdatas_path, caps_path
from Common.path_config import allure_report_path
from TestDatas.iphone_whitelist import iphone_test_model

# 从allure文件中读取测试手机信息
def get_iphone_info():
    iphone_info = {}
    properties = open(allure_report_path+'/xml/environment.properties', encoding='utf-8')
    # properties 文件读取
    for line in properties:
        if line.find(':') > 0:
            string_array = line.replace('\n', '').split(': ')
            iphone_info[string_array[0]] = string_array[1]
    properties.close()
    return iphone_info

iphone_info = get_iphone_info()
# 获取设备名称
iphone_name = iphone_info["Device.Model"]
# 获取设备机型
desired_caps = yaml.load(open(caps_path + "/bc_app_config.yaml"))
deviceName = desired_caps.get("deviceName",None)
iphine_model = iphone_test_model[str(deviceName)]
# 获取设备系统（Android）版本号
iphone_Version = iphone_info["Platform.Version"]
# 测试app版本号
app_Version = iphone_info["App.Version"]
# 执行脚本的测试账号
with open(testdatas_path + "/account_bumber.json", "r", encoding='utf-8') as f:
    data = json.load(f)
    f.close()
test_code = '账号：{},密码：{}'.format(data["user"],data["passwd"])


# 记录用例执行步骤
def case_step(step):
    """
    :param step: 详细执行步骤
    :return:
    """
    case_step = ""
    with allure.step(step):
        case_step = case_step + "<br/>{}".format(step)
    return case_step

# 测试环境-发现BUG写入禅道格式
def case_condition(case_Preposition):
    """
    :param case_Preposition: 测试用例的前提条件
    :return: 记录测试环境及步骤
    """
    case_step = ""
    case_step = case_step + "<B><FONT COLOR='#04B45F'>[测试设备]  </FONT></B> 设备：{0}，型号：{1}".format(iphine_model,iphone_name)
    case_step = case_step + "<br/><B><FONT COLOR='#04B45F'>[系统版本]  </FONT></B> Android v{}".format(iphone_Version)
    case_step = case_step + "<br/><B><FONT COLOR='#04B45F'>[App版本]  </FONT></B> {}".format(app_Version)
    case_step = case_step + "<br/><B><FONT COLOR='#04B45F'>[测试网络]  </FONT></B> WIFI"
    case_step = case_step + "<br/><B><FONT COLOR='#04B45F'>[前提条件]  </FONT></B> {}".format(case_Preposition)
    case_step = case_step + "<br/><B><FONT COLOR='#04B45F'>[测试账号]  </FONT></B> {}".format(test_code)
    case_step = case_step + "<br/><B><FONT COLOR='#04B45F'>[操作步骤]  </FONT></B> : "
    return case_step

# 测试结果-发现BUG写入禅道格式
def case_result(actual,expect,video_url):
    """
    :param actual: 实际结果
    :param expect: 期望结果
    :param video_url: 用例执行步骤录屏
    :return:记录测试环境及步骤
    """
    case_step = ""
    case_step = case_step + "<br/>"
    case_step = case_step + "<br/><B><FONT COLOR='#04B45F'>[实际结果]  </FONT></B> *"
    case_step = case_step + "<br/>{}".format(actual)
    case_step = case_step + "<br/>"
    # case_step = case_step + "<br/><a href='{}'><FONT COLOR='#FE642E'>点我查看bug录屏</FONT></a>".format(video_url)
    # case_step = case_step + "<br/>"
    case_step = case_step + "<br/><B><FONT COLOR='#04B45F'>[预期结果]  </FONT></B> *"
    case_step = case_step + "<br/>{}".format(expect)
    case_step = case_step + "<br/>"
    case_step = case_step + "<br/><B><FONT COLOR='#04B45F'>[用例链接]  </FONT></B> *"
    url = "无"
    case_step = case_step + "<br/>{}".format(url)
    case_step = case_step + "<br/>"
    case_step = case_step + "<br/><B><FONT COLOR='#FE642E'>BUG复现步骤录屏如下（动图）：  </FONT></B>"
    case_step = case_step + "<br/>"
    html_text = '<img src="{0}" alt style="width: 400px;">'.format(video_url)
    case_step = case_step + '<br/>{}'.format(html_text)
    logging.exception(actual)
    return case_step
