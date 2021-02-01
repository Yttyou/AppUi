from Common.ZenTaoApiToMysql import WriteToMysql
from Common.path_config import allure_report_path
import os, time, datetime
import csv, json


class ApiTestDataToMysql:
    def get_csv_data(self):
        result_path = allure_report_path + '/html/data/suites.csv'
        try:
            with open(result_path, 'r', encoding='UTF-8') as f:
                reader = csv.reader(f)
                header_row = next(reader)  # 忽略首行的意思
                highs = []
                for row in reader:
                    highs.append(row)
                if not highs:
                    return "No Csv Data"
                return highs
        except:
            return "Error Csv Data"

    def trans_format(self, time_string, from_format='%a %b %d %H:%M:%S CST %Y', to_format='%Y-%m-%d %H:%M:%S'):
        """
        @note 时间格式转化
        :return:
        """
        time_struct = time.strptime(time_string, from_format)
        times = time.strftime(to_format, time_struct)
        return times

    def Date_sub(self, date1, date2):
        startTime = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
        endTime = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
        date = endTime - startTime
        seconds2 = date.seconds
        return seconds2

    def api_test_getdata(self, pkg=None, platform=None):
        '''
        測試結果、起止時間、響應時間、模塊名稱、測試類型、測試接口類型、用例名稱、用例描述
        '''
        result_dict = {'passed': 'Passed', 'broken': "Error", 'failed': 'Failed'}
        # build_id = os.getenv('BUILD_NUMBER')
        testing_duration = json.load(open(allure_report_path + '/html/data/duration.json', encoding='utf-8'))[0]
        build_id = testing_duration.get('TestRun ID')
        all_csv_data = self.get_csv_data()
        if "Csv Data" in all_csv_data:
            raise Exception("Csv文件無數據或存在錯誤數據,不能寫入！！！")
        try:
            all_data = []
            for data in all_csv_data:
                test_result = result_dict[data[0]]
                start_time = self.trans_format(str(data[1]))
                stop_time = self.trans_format(str(data[2]))
                response_time = self.Date_sub(str(start_time), str(stop_time))
                module = data[4]
                test_type = data[5]
                api_type = data[6]
                case_name = data[-2]
                case_desc = data[-1]
                single_data = (build_id, pkg, platform, test_result, start_time, stop_time,
                               response_time, module, test_type, api_type, case_name, case_desc)
                all_data.append(single_data)
            return all_data
        except:
            raise Exception("Csv數據格式規範有問題,不能寫入！！！")

    def api_test_result(self, pkg=None, platform=None):
        all_data = self.api_test_getdata(pkg=pkg, platform=platform)
        sql = 'INSERT INTO api_test_results (build_id,pkg, platform,' \
              'test_result, start_time, stop_time, api_request_time,' \
              'module,test_type,api_type,case_name,case_desc) VALUES ' \
              '(%s,%s, %s, %s, %s, %s,%s, %s, %s,%s,%s,%s)'
        WriteToMysql().ExcUpdateMany(sql, tuple(all_data))

    def api_testrun_info(self, pkg=None, platform=None):
        # build_id = os.getenv('BUILD_NUMBER')
        testing_duration = json.load(open(allure_report_path + '/html/data/duration.json', encoding='utf-8'))[0]
        build_id = testing_duration.get('TestRun ID')
        all_data = self.api_test_getdata(pkg=pkg, platform=platform)
        min_start_time = min([i[4] for i in all_data])
        max_stop_time = max(i[5] for i in all_data)
        sql = 'INSERT INTO api_testrun_info (build_id,pkg, platform, ' \
              'start_time, end_time) VALUES ("%s","%s", "%s", "%s", "%s")' \
              % (build_id, pkg, platform, min_start_time, max_stop_time)
        WriteToMysql().ExcUpdate(sql)

if __name__ == '__main__':

    ApiTestDataToMysql().api_testrun_info('SunPeople', 'All')
    ApiTestDataToMysql().api_test_result('SunPeople', 'All')

