import json
import mitmproxy.http
import yaml
import os
import pymysql
import sys, time
import logging
import pandas as pd

# 模塊無法導入
# 项目文件根路径
base_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# 手机设备-APP配置文件路径
caps_path = os.path.join(base_path, "Caps")

# -----testrun_id获取------#
allure_report_path = os.path.join(base_path, "allure-report")
testrun_idpath = allure_report_path + '/html/data/duration.json'

# 取样次数及文件创建时间记录文件
monitor_path = os.path.join(base_path, "MonitorFlow")
monitor_times_path = monitor_path + "/monitor_times.json"

# 存放接口數據的csv文件後綴
file_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())

# 将文件名后缀记录在json文件
with open(monitor_times_path, 'r') as load_r:
    load_dict = json.load(load_r)
    load_dict['csv_time'] = file_time
    with open(monitor_times_path, "w") as dump_w:
        json.dump(load_dict, dump_w)


class GetLoginApiData:
    def __init__(self):
        write_to_mysql_msg = yaml.load(open(caps_path + "/bc_app_config.yaml"))
        self.pkg_msg = write_to_mysql_msg['appPackage']
        self.platform_msg = write_to_mysql_msg['platformName']

    def write_data_tocsv(self, data, time):
        pd.DataFrame(data).to_csv(monitor_path + '/testappend_{}.csv'.format(str(time)), index=False, mode='a',
                                  header=False)

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if "sp-api" in flow.request.url:
            flow.start_time = time.time()  # 获取请求开始时间

    def flow_transform(self, data):
        if "b" in data:
            return str(round(int(data.split("b")[0]) / 1024, 2)) + "k"
        else:
            return data

    def response(self, flow):
        if "sp-api" in flow.request.url:
            flow.end_time = time.time()
            # -------读取第幾次取樣-------#
            with open(monitor_times_path, 'r') as load_r:
                load_list = json.load(load_r)
                monitor_times = load_list['monitortimes']

            # ----读取testrun_id------#
            testrun_id = os.getenv('BUILD_NUMBER')
            url = flow.request.url
            method = flow.request.method
            params = flow.request.get_text()
            status_code = str(flow.response.status_code)
            print("安装包:", self.pkg_msg)
            print("设备名:", self.platform_msg)
            print("取样次数:", monitor_times)
            print("jenkins构建ID", testrun_id)
            print("接口地址:", url)
            print("请求类型:", method)
            print("参数:", params)
            print("响应码:", status_code)
            api_flow_upload = flow.request.headers.get('Content-Length') or '0'
            api_flow_download = flow.response.headers.get('Content-Length') or '0'
            api_flow_upload = int(api_flow_upload) / 1024
            api_flow_download = int(api_flow_download) / 1024

            print("上行流量：", api_flow_upload)
            print("下载流量：", api_flow_download)
            api_flow_download_2 = len(flow.response.content) / 1024
            print("响应字节(k)", api_flow_download_2)

            response_time = int(round((flow.end_time - flow.start_time) * 1000, 2))
            print("响应时间:", response_time)
            '''
            id pkg	platform testrun_id method api_url 
            request_param  api_flow api_flow_upload response_time api_flow_download
            '''
            pd_jk_data = {
                "pkg": [self.pkg_msg],
                "platform": [self.platform_msg],
                "seq": [monitor_times],
                "testrun_id": [testrun_id],
                "method": [method],
                "url": [url],
                "params": [str(params)],
                "api_flow_upload": [api_flow_upload],
                "response_time": [response_time],
                "api_flow_download": [api_flow_download]
            }
            self.write_data_tocsv(data=pd_jk_data, time=file_time)


addons = [GetLoginApiData()]
