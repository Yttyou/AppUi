__author__ = 'Areo'
from Common.read_Iphone_config import ReadIphoneConfig
from TestFiles import net_auto_test, file_clean
import time

if __name__ == '__main__':
    # ReadIphoneConfig().write_capsini()                  #读取测试手机配置信息写入配置文件
    ReadIphoneConfig().install_test_apk()                   # 筛选读取手机二级手机及其他
    ReadIphoneConfig().write_allure_env()               #读取测试手机配置信息写入Allure报告配置文件
    ReadIphoneConfig().appium_up(4725, 'MAC')

    # 清理旧的结果数据
    file_clean.del_files('allure-report/xml/')
    file_clean.del_files('MonitorFlowData/')
