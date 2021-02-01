from Common.path_config import monitorflow_path
import csv
import json
from Common.ZenTaoApiToMysql import WriteToMysql

# ------登录接口请求数据脚本---------
flow_py_path = monitorflow_path + '/' + 'app_api_monitor.py'
# -------取样次数及csv文件后缀名----------
runtimes_file = monitorflow_path + '/monitor_times.json'


# 流量数据写入Mysql类
class FlowDataToMysql:
    def get_flow_csv_data(self):
        # -------读取csv文件后缀名---------------
        with open(runtimes_file, 'r') as load_r:
            load_dict = json.load(load_r)
            file_Suffix = load_dict['csv_time']
        # ------登录接口数据csv路径-------------
        flow_csv_path = monitorflow_path + '/' + 'testappend_{}.csv'.format(file_Suffix)
        try:
            with open(flow_csv_path, 'r', encoding='UTF-8') as f:
                reader = csv.reader(f)
                # header_row = next(reader)  # 忽略首行的意思
                highs = []
                for row in reader:
                    highs.append(row)
                if not highs:
                    raise Exception('csv文件无内容,抛出异常！！！')
                return highs
        except:
            raise Exception('读取csv文件失败,数据不规范或文件存在问题！')

    def write_flow_data_tomysql(self):
        all_data = self.get_flow_csv_data()
        all_data = [tuple(i) for i in all_data]
        sql = 'INSERT INTO api_flow_detail (pkg,platform,seq,testrun_id,method, api_url, ' \
              'request_param,api_flow_upload,response_time,api_flow_download) VALUES (%s, %s, %s,%s,%s, %s, %s,%s,%s,%s)'
        WriteToMysql().ExcUpdateMany(sql, tuple(all_data))
