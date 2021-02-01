__author__ = 'developer'

import os

# 项目文件根路径
base_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

# 测试用例集路径
testcases_path = os.path.join(base_path, "TestCases")

# 测试数据路径
testdatas_path = os.path.join(base_path, "TestDatas")

# 测试报告-html路径
testreport_path = os.path.join(base_path, "HtmlTestReport")

# 手机设备-APP配置文件路径
caps_path = os.path.join(base_path, "Caps")

# 脚本运行log路径
logs_path = os.path.join(base_path, "Logs")

# 截图存放路径
screenshot_path = os.path.join(base_path, "ScreenShot")

# 存储监控app数据文件路径
appmonitorindata_path = os.path.join(base_path, "AppMonitorinData")

# 存储监控app数据文件路径
monitorflowdata_path = os.path.join(base_path, "MonitorFlowData")

# 測試文件存放路徑
testfiles_path = os.path.join(base_path, "TestFiles")

allure_report_path = os.path.join(base_path,"allure-report")

# 流量监控文件存放路径
monitorflow_path = os.path.join(base_path,"MonitorFlow")

