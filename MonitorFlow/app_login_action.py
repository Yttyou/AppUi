# app操作，UI层识别数据是否加载完成

import yaml
from Common.path_config import caps_path
from PageObjects.page_objects import PageObject as PL
from appium import webdriver
from TestDatas import COMMON_DATA as CD
import logging
import time

desired_caps = yaml.load(open(caps_path + "/bc_app_config.yaml"))
desired_caps["automationName"] = "UiAutomator2"
desired_caps["unicodeKeyboard"] = True  # True --关闭软键盘
desired_caps["resetKeyboard"] = True
desired_caps["noReset"] = True  # True --应用重置
desired_caps["newCommandTimeout"] = 200
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(7)


def start_app_action():
    app_login(driver)  # 登錄
    app_action(driver)  # 加載
    app_signout(driver)  # 登出


def app_login(driver):
    if PL(driver).get_out_confirm_button() == True:  # 处理被踢出提示弹框
        PL(driver).click_kick_out_confirm_button()
    time.sleep(1)
    logging.info("登录APP，账号：{}，密码：{}".format(CD.user, CD.passwd))
    PL(driver).input_username(CD.user)
    PL(driver).input_passwd(CD.passwd)
    PL(driver).click_login()
    # 登录断言
    try:
        assert PL(driver).is_chat_tab() == True
        logging.info("登入成功")
    except:
        logging.exception("登入异常！")


def app_signout(driver):
    PL(driver).click_setting()
    # 向上滑滑动屏幕
    time.sleep(2)
    size = driver.get_window_size()
    driver.swipe(size["width"] * 0.5, size["height"] * 0.8, size["width"] * 0.5, size["height"] * 0.2)
    time.sleep(2)
    PL(driver).click_signout_button()
    logging.info("登出APP")


def app_action(driver):
    time.sleep(30)
    PL(driver).wait_msg()  # 讯息同步
    time.sleep(30)
    PL(driver).enter_personal_chat_page()  # 通讯录
    time.sleep(30)
    # 最新动态


def quit_app(driver):
    driver.close_app()
    driver.quit()  # 退出app
