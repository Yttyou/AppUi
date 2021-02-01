"""   执行文本   """

# 执行文件--执行脚本在该页面运行
# 筛选用例执行规则：@pytest.mark.xxx ；在test_xx函数（即用例）添加对应标签，在下列参数中加入标签名泽执行对用用例
# =====================  参数说明  ============================================
# "-m" 指需要指定某些需要跑的用例
# "login" 指@pytest.mark.login 打标签的login，那么就指定有打login标签的用例需要跑
#  "--reruns","2" 指错误的用例需要重跑2次
# "--reruns-delay", "5" 指重跑错误用例的间隔时间为5秒
# "--html="+file_path 指生成报告的路径
import threading
import json
import time
import logging
from Common import logger
from Common.path_config import testdatas_path
from AppMonitorin.ram import AppMonitorin
from TestDatas.account_data import account_list
from Common.write_excel import wtite_data
from Common.read_test_result import before_read_data, end_read_data, scene_repair_bug,end_read_data_regression_test



# PS：
#       pytest.main(["-m", "ttt", "--reruns","2", "--reruns-delay", "5","--html=HtmlTestReport/pytest_result.html",
#             "--junitxml=HtmlTestReport/result.xml","--alluredir","./allure-report/xml"])
# ==============================================================================
# appium -p 4723 --log-level error &

# 全量脚本执行测试
def child_thread1():
    pytest.main(["-m", "all", "--html=HtmlTestReport/pytest_result.html",
                 "--junitxml=HtmlTestReport/result.xml", "--alluredir", "./allure-report/xml"])

# 内存监控测试
def child_thread2():
    AppMonitorin().app_ram()

# 救命清单回归测试
def regression_testing():
    pytest.main(["-m", "ddd", "--html=HtmlTestReport/pytest_result.html",
                 "--junitxml=HtmlTestReport/result.xml", "--alluredir", "./allure-report/xml"])

def parent_thread():
    run1 = threading.Thread(target=child_thread1)
    run2 = threading.Thread(target=child_thread2)
    run2.setDaemon(True)
    run1.start()
    run2.start()

# 全量测试
def double_account():
    account_number = (len(account_list))
    for i,new_dict in enumerate(account_list):
        logging.info("...检测到共有{}个账户...".format(account_number))
        logging.info("使用第{}个账号'{}'登录执行脚本。。。".format(i+1,new_dict))
        with open(testdatas_path+"/account_bumber.json", "w") as f:
            json.dump(new_dict, f)
            f.close()
            logging.info("登录账号信息写入json文件已完成...")
        child_thread1()             # 全量测试
        time.sleep(10)

# 救命清单快速回归测试
def regression_account_demo():
    account_number = (len(account_list))
    for i,new_dict in enumerate(account_list):
        logging.info("...检测到共有{}个账户...".format(account_number))
        logging.info("使用第{}个账号'{}'登录执行脚本。。。".format(i+1,new_dict))
        with open(testdatas_path+"/account_bumber.json", "w") as f:
            json.dump(new_dict, f)
            f.close()
            logging.info("登录账号信息写入json文件已完成...")
        regression_testing()        # 救命清单回归测试
        time.sleep(10)


""" 救命清单执行测试方法 """
def regression_demo_test():
    # scene_repair_bug()
    regression_account_demo()
    # end_read_data_regression_test()
    # before_read_data()

""" 全量脚本执行测试方法 """
def all_amount_test():
    scene_repair_bug()
    double_account()
    end_read_data()
    before_read_data()

import pytest
if __name__ == '__main__':
    regression_demo_test()

