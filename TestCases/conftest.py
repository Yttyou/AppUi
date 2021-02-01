__author__ = 'developer'
import pytest
from appium import webdriver
import yaml
import json
from Common.path_config import caps_path
from PageObjects.login_page import LoginPage
from PageObjects.chat_tab_page import ChatTabPage
from TestDatas import COMMON_DATA as CD
from PageObjects.setting_tab_page import SettingTabPage
from PageObjects.newdynamic_tab_page import NewDynamicTabPage as ndt
from PageObjects.chat_tab_page import ChatTabPage as ctp
from Common.BasePage import BasePage
from Common.path_config import testdatas_path
import time
import logging
from TestCases.test_chat_videa import data_dict,video_path_temp,video_name_temp
# from appium.webdriver.appium_service import AppiumService


# =====================一键运行，控制执行用例范围===============
# fixture装饰器scope参数作用范围说明：
# unction--函数、方法；
# class--每个类调用一次；
# module--一个py文件调用一次
# session--多个文件调用一次，可以跨.py文件调用
# ===========================================================


@pytest.fixture(scope='session')
def startApp_withReset():
    # AppiumService().start()            #启动 appium 服务
    # ReadIphoneConfig().write_capsini()                  #读取测试手机配置信息写入配置文件
    # ReadIphoneConfig().write_allure_env()               #读取测试手机配置信息写入Allure报告配置文件
    iphone_path = caps_path + "/bc_app_config.yaml"
    logging.info("读取当前执行测试机配置文件路径为：'{}'".format(iphone_path))
    desired_caps = yaml.load(open(iphone_path))
    desired_caps["deviceName"] = str(desired_caps["deviceName"])
    desired_caps["udid"] = str(desired_caps["deviceName"])
    desired_caps["platformVersion"] = str(desired_caps["platformVersion"])
    desired_caps["automationName"] = "UiAutomator2"
    desired_caps["unicodeKeyboard"] = True  # True --关闭软键盘
    desired_caps["resetKeyboard"] = True
    desired_caps["noReset"] = True  # True --应用重置
    logging.info("输出读取到的手机配置信息为：")
    logging.info(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    time.sleep(3)
    start_time = LoginPage(driver).get_system_time_time()       # 执行开始时间
    logging.info("脚本开始执行时间：{}".format(start_time))
    is_kick_out_confirm_button(driver)      # 处理被踢出提示弹框
    time.sleep(1)
    login(driver)     # 登录
    # front_data_photo(driver)                  # 判断相册有无10张图片，没有则拍摄10张
    yield driver
    # delete_test_personal_post(driver)         # 删除所有个人帖子
    # 后置处理
    signout(driver)   #登出
    # AppiumService().stop()      #关闭 appium 服务
    end_time = LoginPage(driver).get_system_time_time()         # 结束时间
    LoginPage(driver).get_time_interval_time(start_time,end_time)       # 统计执行脚本所耗费时间
    # driver.close_app()
    # driver.quit()

# # 登录APP
# def login(driver):
#     logging.info("登录APP，账号：{}，密码：{}".format(CD.user,CD.passwd))
#     LoginPage(driver).input_username(CD.user)
#     LoginPage(driver).input_passwd(CD.passwd)
#     LoginPage(driver).click_login()
#     #登录断言
#     assert ChatTabPage(driver).is_chat_tab() == True
#     time.sleep(3)

# 多账号登录APP
def login(driver):
    with open(testdatas_path + "/account_bumber.json", "r", encoding='utf-8') as f:
        data = json.load(f)
        f.close()
    logging.info("登录APP，账号：{}，密码：{}".format(data["user"],data["passwd"]))
    LoginPage(driver).input_username(data["user"])
    LoginPage(driver).input_passwd(data["passwd"])
    LoginPage(driver).click_login()
    #登录断言
    assert ChatTabPage(driver).is_chat_tab() == True
    time.sleep(3)

# 登出app
def signout(driver):
    SettingTabPage(driver).return_home()        # 后置处理
    SettingTabPage(driver).click_setting()
    #向上滑滑动屏幕
    time.sleep(2)
    size = driver.get_window_size()
    driver.swipe(size["width"]*0.5,size["height"]*0.8,size["width"]*0.5,size["height"]*0.2)
    SettingTabPage(driver).click_signout_button()
    logging.info("登出APP")


# 判断是否有弹出被踢出提示弹框，有则点击【确定】按钮
def is_kick_out_confirm_button(driver):
    if LoginPage(driver).get_out_confirm_button() == True:
        LoginPage(driver).click_kick_out_confirm_button()

# 删除执行脚本过程中产生的个人帖子
def delete_test_personal_post(driver):
    ndt(driver).return_home()               # 前置
    ndt(driver).click_newdynamic()                  # 點擊：【最新动态】
    ndt(driver).click_nf_personal_tab()             # 點擊【個人】tab
    ndt(driver).delete_personal_tab_all_post()      # 删除所有个人帖子

# 前置数据处理-拍摄10张照片
def front_data_photo(driver):
    ctp(driver).if_get_photo_Check_button_number()


@pytest.fixture(scope='session')
def startApp_withReset_demo():
    # AppiumService().start()            #启动 appium 服务
    # ReadIphoneConfig().write_capsini()                  #读取测试手机配置信息写入配置文件
    # ReadIphoneConfig().write_allure_env()               #读取测试手机配置信息写入Allure报告配置文件
    iphone_path = caps_path + "/bc_app_config.yaml"
    logging.info("读取当前执行测试机配置文件路径为：'{}'".format(iphone_path))
    desired_caps = yaml.load(open(iphone_path))
    desired_caps["deviceName"] = str(desired_caps["deviceName"])
    desired_caps["udid"] = str(desired_caps["deviceName"])
    desired_caps["platformVersion"] = str(desired_caps["platformVersion"])
    desired_caps["automationName"] = "UiAutomator2"
    desired_caps["unicodeKeyboard"] = True  # True --关闭软键盘
    desired_caps["resetKeyboard"] = True
    desired_caps["noReset"] = True  # True --应用重置
    logging.info("输出读取到的手机配置信息为：")
    logging.info(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    time.sleep(3)
    start_time = LoginPage(driver).get_system_time_time()       # 执行开始时间
    logging.info("脚本开始执行时间：{}".format(start_time))
    is_kick_out_confirm_button(driver)      # 处理被踢出提示弹框
    time.sleep(1)
    login(driver)     # 登录
    # front_data_photo(driver)                  # 判断相册有无10张图片，没有则拍摄10张
    yield driver
    # delete_test_personal_post(driver)         # 删除所有个人帖子
    # 后置处理
    signout_demo(driver)   #登出
    # AppiumService().stop()      #关闭 appium 服务
    end_time = LoginPage(driver).get_system_time_time()         # 结束时间
    LoginPage(driver).get_time_interval_time(start_time,end_time)       # 统计执行脚本所耗费时间
    # driver.close_app()
    # driver.quit()

# 登出app
def signout_demo(driver):
    SettingTabPage(driver).return_home_demo(video_path_temp,video_name_temp, data_dict)        # 后置处理
    SettingTabPage(driver).click_setting()
    #向上滑滑动屏幕
    time.sleep(2)
    size = driver.get_window_size()
    driver.swipe(size["width"]*0.5,size["height"]*0.8,size["width"]*0.5,size["height"]*0.2)
    SettingTabPage(driver).click_signout_button()
    logging.info("登出APP")


