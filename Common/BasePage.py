
"""  公用部分：等待、点击、获取文本等等Action  """

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy as Mb
from Common.path_config import screenshot_path, caps_path
from PageLocators.newdynamic_tab_locator import NewdynamicTabLocator as ntl
from PageLocators.chat_tab_locator import ChatTabLocator as ctl
from appium.webdriver.common.touch_action import TouchAction
import yaml
import os
import time
from Common.video_upload_download import upload_file_object
from Common.video_upload_download import create_bucket
import random
import string
import shutil
from Common import logger
import time
import logging
import datetime
import os


# noinspection PyBroadException
class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    """     环境读取及处理前置方法     """

    # 获取APP环境,返回关键词（关键词：AUT、QA）
    def get_app_environment(self):
        appPackage = ntl.appPackage
        app_environmen = str(appPackage.split(".", 3)[-1])
        return app_environmen.upper()

    # 每条用例的前置条件---返回home方法     #说明：在有效次数10次内查找，超过10次退出执行
    def return_home(self):
        self.Stop_recording()           # 终断录屏
        self.delete_android_video()     # 删除Android本地视频
        a = 0
        while self.is_home() == False:
            self.driver.keyevent(4)
            a = a + 1
            logging.info("第{}次物理返回".format(a))
            if self.find_abandon_post_button() == True:
                name = '点击：[放棄發佈]按鈕'
                self.text_find_and_click('放棄發佈', model=name)
                time.sleep(2)
            if self.find_cancel_track_prompt() == True:
                name = '查找："取消追踪"弹框-【取消】'
                self.click_element(ntl.cancel_track_prompt, model=name)
                time.sleep(1)
            if a >= 6:
                break

    # 每条用例的前置条件---返回home方法     #说明：在有效次数10次内查找，超过10次退出执行
    def return_home_demo(self, android_video_path, video_name, temp_dict):
        # self.Stop_recording()  # 终断录屏
        self.get_bug_video_url_demo(android_video_path, video_name, temp_dict)     # 终断上传视频
        self.delete_android_video()  # 删除Android本地视频
        a = 0
        while self.is_home() == False:
            self.driver.keyevent(4)
            a = a + 1
            logging.info("第{}次物理返回".format(a))
            if self.find_abandon_post_button() == True:
                name = '点击：[放棄發佈]按鈕'
                self.click_element(ntl.abandon_post_button, model=name)
                time.sleep(2)
            if self.find_cancel_track_prompt() == True:
                name = '查找："取消追踪"弹框-【取消】'
                self.click_element(ntl.cancel_track_prompt, model=name)
                time.sleep(1)
            if a >= 6:
                break

    # 查找：[放棄發佈]按鈕是否存在
    def find_abandon_post_button(self):
        name = '查找：[放棄發佈]按鈕是否存在'
        time.sleep(2)
        try:
            self.text_find("放棄發布")
            logging.info("已经找到[放棄發佈]按鈕")
            return True
        except:
            logging.exception("未找到[放棄發佈]按鈕")
            return False

    # 查找："取消追踪"弹框-【取消】
    def find_cancel_track_prompt(self):
        time.sleep(2)
        try:
            self.get_element(ntl.cancel_track_prompt)
            logging.info("已经找到[取消追踪]按鈕")
            return True
        except:
            logging.exception("未找到[取消追踪]按鈕")
            return False

    """    以下为公共部分基础action方法   """

    # 等待元素可見-不拋出異常
    def wait_ele_visible_pass(self, locator, wait_times=20, poll_frequency=0.5, model=""):
        logging.info("等待元素可见...")
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds  # 等待元素可见所花时间
            logging.info("{0}: 元素 {1} 已可见,等待起始时间：{2},等待时长：{3}".format(model, locator, start, wait_times))
        except:
            logging.exception("等待元素-{}可见异常! ".format(locator))
            self.screenshot(model)

    # 等待元素可见
    # locator=元素点位；wait_times=可等待的总时长；poll_frequency=等待周期
    def wait_eleVisible(self, locator, wait_times=40, poll_frequency=0.5, model=""):
        logging.info("等待元素可见...")
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds  # 等待元素可见所花时间
            logging.info("{0}: 元素 {1} 已可见,等待起始时间：{2},等待时长：{3}".format(model, locator, start, wait_times))
        except:
            logging.exception("等待元素-{}可见异常！".format(locator))
            self.screenshot(model)
            raise

    # 等待元素可见（不抛异常）
    # locator=元素点位；wait_times=可等待的总时长；poll_frequency=等待周期
    def wait_eleVisible_pass(self, locator, wait_times=30, poll_frequency=0.5, model=""):
        logging.info("等待元素可见...")
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds  # 等待元素可见所花时间
            logging.info("{0}: 元素 {1} 已可见,等待起始时间：{2},等待时长：{3}".format(model, locator, start, wait_times))
        except:
            logging.exception("等待元素-{}可见异常！".format(locator))
            self.screenshot(model)

    # 等待元素不可見-不拋出異常
    def wait_ele_invisible_pass(self, locator, wait_times=60, poll_frequency=0.5, model=""):
        logging.info("等待元素不可见...")
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.invisibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds  # 等待元素可见所花时间
            logging.info("{0}: 元素 {1} 已不可见,等待起始时间：{2},等待时长：{3}".format(model, locator, start, wait_times))
        except:
            logging.exception("等待元素-{}不可见异常！-- pass ".format(locator))
            self.screenshot(model)

    # 等待元素消失
    def wait_element_vanish(self, locator, wait_times=60, poll_frequency=0.5, model=""):
        logging.info("等待元素消失...")
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times, poll_frequency).until_not(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds  # 等待元素消失所花时间
            logging.info("{0}: 元素 {1} 已消失,等待起始时间：{2},等待时长：{3}".format(model, locator, start, wait_times))
        except:
            logging.exception("等待元素-{}消失异常！".format(locator))
            self.screenshot(model)
            raise

    # 等待元素不可见
    # locator=元素点位；wait_times=可等待的总时长；poll_frequency=等待周期
    def wait_eleInvisible(self, locator, wait_times=20, poll_frequency=0.5, model=""):
        logging.info("等待元素不可见...")
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.invisibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds  # 等待元素可见所花时间
            logging.info("{0}: 元素 {1} 已不可见,等待起始时间：{2},等待时长：{3}".format(model, locator, start, wait_times))
        except:
            logging.exception("等待元素-{}不可见异常！".format(locator))
            self.screenshot(model)
            raise

    # 等待元素存在
    def wait_elePrences(self, locator, wait=30, requence=0.5, model=""):
        logging.info("等待元素存在...")
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait, requence).until(EC.presence_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info("{0}: 元素 “{1}” 已存在,等待起始时间：{2},等待时长：{3}".format(model, locator, start, wait_times))
        except:
            logging.exception("等待元素-{}存在异常！！".format(locator))
            self.screenshot(model)
            raise

    # 等待元素存在
    def wait_until_not(self, locator, wait=30, requence=0.5, model=""):
        logging.info("等待元素不存在存在...")
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait, requence).until_not(EC.presence_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info("{0}: 元素 “{1}” 不存在,等待起始时间：{2},等待时长：{3}".format(model, locator, start, wait_times))
        except:
            logging.exception("等待元素-{}不存在异常！！".format(locator))
            self.screenshot(model)
            raise

    # 查找元素，返回元素属性
    def get_element(self, locator, model=""):
        logging.info("{0}：开始查找元素：{1}".format(model, locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素-{}失败！！".format(locator))
            self.screenshot(model)
            raise

    # 查找元素，返回元素属性,不报异常
    def get_element_pass(self, locator, model=""):
        logging.info("{0}：开始查找元素：{1}".format(model, locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素-{}失败！！".format(locator))
            self.screenshot(model)

    # 查找多个元素，已列表形式返回
    def find_elements(self, locator, model=""):
        logging.info('{0}：开始查找符合表达式的所有元素："{1}"'.format(model, locator))
        try:
            return self.driver.find_elements(*locator)
        except:
            logging.exception("查找元素{}失败!!".format(locator))
            self.screenshot(model)
            raise

    # 输入文本
    # text=文本内容
    def input_text(self, locator, text, model=""):
        # 找到元素
        ele = self.get_element(locator, model)
        logging.info('{0}: 元素：{1} 输入内容-"{2}"'.format(model, locator, text))
        try:
            ele.send_keys(text)
        except:
            logging.exception('{0}: 元素：{1} 输入--"{2}" 操作失败：'.format(model, locator, text))
            self.screenshot(model)
            raise

    # 输入文本-adb命令方式（当设备UI无法识别时用此方法）
    def adb_keycode(self, key):
        self.driver.press_keycode(key)
        return self

    # 点击操作
    def click_element(self, locator, model=""):
        # 找到元素
        ele = self.get_element(locator, model)
        # 点击操作
        logging.info("{0}: 元素：{1} 点击操作。".format(model, locator))
        try:
            ele.click()
        except:
            logging.exception('元素："{0}" 点击失败！！：'.format(locator))
            self.screenshot(model)
            raise

    # 双击对象
    def Action_double_tap(self, locator, model=""):
        el = self.get_element(locator, model)
        try:
            TouchAction(self.driver).tap(el,count=2).release().perform()
            logging.info("双击对象成功。")
        except:
            logging.exception("双击对象-‘{}’失败!".format(locator))
            raise

    # 长按：聊天窗口长按弹出操作项
    def long_press_chat_message(self, locator, model=""):
        time.sleep(3)
        el = self.find_elements(locator, model)[-1]
        try:
            TouchAction(self.driver).long_press(el, duration=2000).release().perform()
            logging.info("長按‘{}’操作".format(locator))
        except:
            logging.exception("长按对象-‘{}’2秒失败".format(locator))
            raise

    # 长按操作
    def long_press_action(self, locator, model=""):
        el = self.get_element(locator, model)
        try:
            TouchAction(self.driver).long_press(el, duration=4000).release().perform()
            logging.info("長按‘{}’操作".format(locator))
        except:
            logging.exception("长按对象-‘{}’3秒失败".format(locator))

    # 短按操作
    def short_press_action(self, locator, model=""):
        el = self.get_element(locator, model)
        try:
            TouchAction(self.driver).long_press(el, duration=500).release().perform()
            logging.info("短按‘{}’操作".format(locator))
        except:
            logging.exception("短按对象-‘{}’0.5秒失败".format(locator))
            raise

    # 长按操作-上滑取消
    def long_press_action_slide_cancel(self, locator, model=""):
        el = self.get_element(locator, model)
        size = self.driver.get_window_size()
        try:
            TouchAction(self.driver).long_press(el, duration=3000).move_to(x=size["width"] * 0.5,
                                                                           y=size["height"] * 0.5).release().perform()
            logging.info("長按‘{}’操作後上滑取消".format(locator))
        except:
            logging.exception("长按对象-‘{}’3秒後操作後上滑取消失败".format(locator))
            raise

    # 获取元素的属性（如：ID，class，文本）
    # attr_name=元素的属性类型
    def get_element_attribute(self, locator, attr_name, model=""):
        # 找到元素
        ele = self.get_element(locator, model)
        logging.info('{0}: 获取元素--"{1}" 的属性：{2}'.format(model, locator, attr_name))
        try:
            value = ele.get_attribute(attr_name)
            logging.info("{0}: 元素--{1} 的属性{2} 值为：{3}".format(model, locator, attr_name, value))
            return value
        except:
            logging.exception("获取元素：{0} 的属性{1} 失败!!异常信息如下：".format(locator, attr_name))
            self.screenshot(model)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, model=""):
        # 找到元素
        ele = self.get_element(locator, model)
        # 获取元素的文本内容
        logging.info("{0}：获取元素--{1} 的文本内容".format(model, locator))
        try:
            text = ele.text
            logging.info("{0}：元素--{1} 的文本内容为：'{2}'".format(model, locator, text))
            return text
        except:
            logging.exception("获取元素--{0} 的文本内容失败!!报错信息如下：".format(locator))
            self.screenshot(model)
            raise

    # toast获取（通过模糊文本匹配）--适用加载缓慢类型
    def get_toastMsg(self, part_str, model="model"):
        # xpath表达式
        xpath_loc = '//*[contains(@text,"{0}")]'.format(part_str)
        logging.info("{0}: 获取toast提示，表达式为--{1}".format(model, xpath_loc))
        try:
            WebDriverWait(self.driver, 5, 0.2).until(EC.presence_of_element_located((Mb.XPATH, xpath_loc)))
            return self.get_text((Mb.XPATH, xpath_loc), model=model)
        except:
            logging.exception("获取toast失败！！")
            self.screenshot(model)
            raise

    # toast获取（通过模糊文本匹配）--适用加载缓慢类型
    def get_toastMsg1(self, toast_message, model="model"):
        # xpath表达式
        message = '//*[@text=\'{}\']'.format(toast_message)
        logging.info("{0}: 获取toast提示，表达式为--{1}".format(model, message))
        try:
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(message))
            logging.info("获取toast提示成功！")
        except:
            logging.exception("获取toast失败！！")
            self.screenshot(model)
            raise

    # toast获取（通过模糊文本匹配）--适用加载缓慢类型
    def get_toastMsg_Long(self, part_str, model="model", sleep_time=30):
        # xpath表达式
        xpath_loc = '//*[contains(@text,"{0}")]'.format(part_str)
        logging.info("{0}: 获取toast提示，表达式为--{1}".format(model, xpath_loc))
        try:
            WebDriverWait(self.driver, sleep_time, 0.2).until(EC.presence_of_element_located((Mb.XPATH, xpath_loc)))
            return self.get_text((Mb.XPATH, xpath_loc), model=model)
        except:
            logging.exception("获取toast失败！！")
            self.screenshot(model)
            raise

    # toast获取（通过模糊文本匹配）--适用操作提示快速类型
    def get_toast_tips(self, part_str, model="model"):
        # xpath表达式
        xpath_loc = '//*[contains(@text,"{0}")]'.format(part_str)
        logging.info("{0}: 获取toast提示，表达式为--{1}".format(model, xpath_loc))
        try:
            WebDriverWait(self.driver, 3, 0.2).until(EC.presence_of_element_located((Mb.XPATH, xpath_loc)))
            return self.get_text((Mb.XPATH, xpath_loc), model=model)
        except:
            logging.exception("获取toast失败！！")
            self.screenshot(model)
            raise

    # 搜索
    def keyboard_search(self, model="model"):
        # WebDriver.keyevent("84")     #84=代表搜索键
        try:
            self.driver.execute_script("mobile:performEditorAction", {'action': 'search'})
            logging.info("触发系统底层搜索功能..")
        except:
            logging.exception("系统底层搜索功能异常！！")
            self.screenshot(model)
            raise

    # 系统返回
    def return_button(self):
        logging.info("物理按键返回")
        self.driver.keyevent("4")
        time.sleep(1)
        return self

    # 通过文本查找元素
    def text_find(self, findtext, model="model"):
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"{}")]'.format(findtext))
            logging.info("{}：通过文本内容-'{}'查找元素成功".format(model, findtext))
        except:
            logging.exception("通过文本‘{}’查找元素失败！！".format(findtext))
            self.screenshot(model)
            raise

    # 通过text属性来点击元素
    def text_find_and_click(self, findtext, model="model"):
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"{}")]'.format(findtext)).click()
            logging.info("{}：通过文本内容-'{}'点击元素成功".format(model, findtext))
        except:
            logging.exception("通过文本‘{}’点击元素失败！！".format(findtext))
            self.screenshot(model)
            raise

    # 滑动屏幕(单次滑动)，传入坐标参数；如（0.5，0.6,0.5,0.5）向上滑动一小段
    def swipe_screen(self, x1, y1, x2, y2, model="model"):
        size = self.driver.get_window_size()
        try:
            self.driver.swipe(size["width"] * x1, size["height"] * y1, size["width"] * x2, size["height"] * y2)
            logging.info("{0}屏幕滑动：起点（{1}，{2}）--终点（{3}，{4}）".format(model, x1, y1, x2, y2))
        except:
            logging.exception("滑动屏幕失败！")
            raise

    # 点击：通过相对坐标点击（页面元素识别不到时用到）
    def tap_click_ele(self, x1, y1,model="model"):
        size = self.driver.get_window_size()
        try:
            TouchAction(self.driver).press(x=size["width"] * x1, y=size["height"] * y1).release().perform()
            logging.info("相对位置点击正常")
        except:
            logging.exception("相对位置点击失敗！")
            raise

    # 截图方法
    def screenshot(self, model_name):
        # 时间
        filePath = screenshot_path + "/{0}_{1}.png".format(model_name, time.strftime("%Y%m%d_%H%M%S"))
        self.driver.save_screenshot(filePath)
        logging.info("截图成功，图片路径为：{0}".format(filePath))
        return filePath

    # 查找APP主页导航栏可见，True==可见，False==不可见
    def is_home(self):
        self.wait_ele_visible_pass(ctl.chat_tab, wait_times=2, poll_frequency=1)
        try:
            self.get_element(ctl.chat_tab)
            return True
        except:
            return False

    # 授权弹框允许权限
    def allow_authorization(self, model_name):
        time.sleep(1)
        try:
            self.driver.execute_script("mobile:acceptAlert")
            logging.info("获取权限成功")
            return self
        except:
            logging.exception("权限异常")
            self.screenshot(model_name)
            raise

    # 獲取當前系統時間（时-分）
    def get_system_time(self):
        return time.strftime("%H:%M", time.localtime(time.time()))

    # 獲取當前系統時間（年-月-日）
    def get_system_time_day(self):
        return time.strftime("%Y-%m-%d", time.localtime(time.time()))

    # 獲取當前系統時間（年-月-日 时-分-秒）
    def get_system_time_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    # 获取时间戳间隔时间
    def get_time_interval_time(self,start_time,end_time):
        start = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        end = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        delta = (end - start).seconds
        hour = delta // 3600        # 时
        div = (delta % 3600) // 60  # 分
        mod = (delta % 3600) % 60   # 秒
        logging.info("执行脚本所花时间：")
        logging.info("{}小时{}分钟{}秒".format(hour, div, mod))
        return self

    # 回归测试-demo所花时间
    def demo_get_time_interval_time(self, start_time, end_time):
        start = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        end = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        delta = (end - start).seconds
        hour = delta // 3600  # 时
        div = (delta % 3600) // 60  # 分
        mod = (delta % 3600) % 60  # 秒
        logging.info("执行到当前场景所耗时：")
        logging.info("time {}小时{}分钟{}秒".format(hour, div, mod))
        return self

    # 时间差（时：分）
    def get_difference(self,start_time,end_time):
        d1 = datetime.datetime.strptime(start_time, '%H:%M')
        d2 = datetime.datetime.strptime(end_time, '%H:%M')
        delta = d2 - d1
        return delta.seconds     # 返回时间单位为S

    # 获取demo时间戳间隔时间
    def get_demo_time_interval_time(self, start_time, end_time):
        start = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        end = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        delta = (end - start).seconds           # 所得单位：s
        return delta

    # 随机生成字符串
    def random_str_share_china(self):
        val = random.randint(0x4e00, 0x9fbf)
        return chr(val)

    # 随机生成数字
    def random_int(self, index):  # 数据数范围（0,index）
        return random.randint(0, index)

    # 随机生成数字
    def random_int_one(self, index):  # 数据数范围（1,index）
        return random.randint(1, index)

    # 随机生成英文字母
    def random_english_letter(self):
        s = string.ascii_lowercase
        # 大写string.ascii_uppercase
        # 小写string.ascii_lowercase
        return random.choice(s)

    # 【返回】物理按键（一步）
    def return_button_one(self):
        self.return_button()
        return self

    # 文件大小单位换算
    def sizeConvert(self,size):  # 单位换算
        K, M, G = 1024, 1024 ** 2, 1024 ** 3
        if size >= G:
            return str(int(size / G)) + 'G'
        elif size >= M:
            return str(int(size / M)) + 'M'
        elif size >= K:
            return str(int(size / K)) + 'K'
        else:
            return str(size) + 'Bytes'

    def get_filesize(self,filename):
        """
        获取文件大小（M: 兆）
        """
        file_byte = os.path.getsize(filename)
        return self.sizeConvert(file_byte)

    # 通过文件大小，给与指定时间
    def get_video_ou_gif_time(self,filename):
        data = self.get_filesize(filename)  # 文件大小
        print(data)
        if data.find("M") > 0:
            video_size = int(data.split("M")[0])
            if video_size <= 30:
                return 6
            elif 30 < video_size <= 50:
                return 10
            elif 50 < video_size <= 70:
                return 15
            elif 70 < video_size <= 90:
                return 18
            elif 90 < video_size <= 120:
                return 24
            elif video_size > 120:
                return 30
        else:
            return 5

    # 获取配置文件的设备号
    def get_iphone_deviceName(self):
        desired_caps = yaml.load(open(caps_path + "/bc_app_config.yaml"))
        deviceName = desired_caps["deviceName"]
        return deviceName

    # 开始Android录屏(最长时长180s)
    def Start_recording(self):
        """
        :return: screen_recording_file =返回存储在Android手机上的录屏绝对路径；data：视频名称（生成时间命名）
        """
        deviceName = self.get_iphone_deviceName()  # 获取当前执行设备号
        os.popen("adb -s {} shell mkdir /sdcard/.nomedia".format(deviceName))  # 创建Android中隐藏文件夹来存放视频
        time.sleep(1)
        data = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        os.popen('adb -s {0} shell screenrecord --bit-rate 9000000 --time-limit 180 /sdcard/.nomedia/{1}.mp4'.format(deviceName, data))
        screen_recording_file = "/sdcard/.nomedia/{}.mp4".format(data)  # 存储录屏路径
        process_list = os.popen('ps -ef | grep "adb -s {}"'.format(deviceName)).read()
        adb_list = process_list.split("\n")
        video_adb = ''
        for i, adb in enumerate(adb_list):  # 遍历查找录屏进程
            if adb.find("shell screenrecord") >= 0:
                video_adb = adb
        logging.info("获取到录屏的adb进程信息：'{}'".format(video_adb))
        strip_list = video_adb.strip()
        if strip_list.find("shell screenrecord") >= 0:
            logging.info("启动录屏功能...")
        else:
            logging.info("录屏功能异常！！！")
        return screen_recording_file, data

    # 终断Android录屏
    def Stop_recording(self):
        deviceName = self.get_iphone_deviceName()  # 获取当前执行设备号
        process_list = os.popen('ps -ef | grep "adb -s {}"'.format(deviceName)).read()
        logging.info("终断前,指定设备 '{}' 所有adb进程：".format(deviceName))
        logging.info(process_list)
        adb_list = process_list.split("\n")
        video_adb = ''
        for i, adb in enumerate(adb_list):
            if adb.find("shell screenrecord") >= 0:
                video_adb = adb
        strip_list = video_adb.strip()
        logging.info("录屏的adb进程信息：'{}'".format(strip_list))
        if len(video_adb) > 1:
            logging.info("设备 {} 持续录屏中。。。".format(deviceName))
            b = strip_list.split(" ")[1]
            logging.info("终止指定的adb为==== '{}'".format(b))
            adb = 'kill -9 {}'.format(b)
            os.popen(adb).read()  # 关闭录屏指定进程
            logging.info("终止录屏adb为：{}".format(adb))
            time.sleep(5)
            process_list = os.popen('ps -ef | grep "adb -s {}"'.format(deviceName)).read()  # 查看指定设备当前adb所有进程
            logging.info("终断后设备 '{}' adb所有线程：".format(deviceName))
            logging.info(process_list)
            A = process_list.split("\n")[0].strip()
            if A.find('time-limit') < 0:
                logging.info("终断录屏功能成功！")
            else:
                logging.info("终断录屏功能视频")
        else:
            logging.info("已经被停止录制或录屏时间已经超过3分钟！")

    # 将Android中生成的手机录屏文件pull到mac本地指定路径中
    def android_pull_mac(self, android_video_path, video_name, pull_time):
        """
        :param video_path: android 测试机生成的视频绝对路径
        :return: 生成gif路径
        """
        # 项目文件根路径
        deviceName = self.get_iphone_deviceName()  # 获取当前执行设备号
        base_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
        Superior_path = os.path.dirname(base_path)  # 项目文件父路径
        video_folder_path = os.path.join(Superior_path, "test_case_video_S9")  # mac本地存储视频的路径
        logging.info("存储视频的文件夹：'{}'".format(video_folder_path))
        if 'test_case_video_S9' not in os.listdir(Superior_path):
            logging.info("没有找到路径'{}'".format(video_folder_path))
            os.mkdir(video_folder_path)  # 没有路径则创建
            logging.info("创建视频存放路径'{}'".format(video_folder_path))
        else:
            shutil.rmtree(video_folder_path)
            os.mkdir(video_folder_path)  # 有路径并清空
            logging.info("找到路径'{}'，并清空了该文件夹".format(video_folder_path))
        os.popen("adb -s {0} pull {1} {2}/".format(deviceName, android_video_path, video_folder_path))
        time.sleep(pull_time)  # pull所花时间
        mac_video_path = os.path.join(video_folder_path, "{}.mp4".format(video_name))
        logging.info("生成视频的本地路径为：'{}'".format(mac_video_path))
        video_at_gif_time = self.get_video_ou_gif_time(mac_video_path)  # 通过视频大小得到转化为gif的时间
        # 将视频转换为gif
        # 生成gif的路径
        gif_mac_path = os.path.join(video_folder_path, "{}.gif".format(video_name))
        logging.info("视频转化成gif图等待时间 {} s".format(video_at_gif_time))
        os.popen("ffmpeg -i {0} -s 720x1440 -b:v 700k {1}".format(mac_video_path, gif_mac_path))
        time.sleep(video_at_gif_time)
        return gif_mac_path

    # 上传视频至服务器
    def upload_video(self, mac_video_path):
        """
        :param file: mac本机上视频文件绝对路径
        :return: 下载视频url
        """
        video_folder = "9" + time.strftime("%Y%m%d", time.localtime(time.time()))  # 使用当天日期做为存储视频的文件夹
        create_bucket(video_folder)  # 创建存储视频的文件夹
        logging.info("创建的文件夹为：{}".format(video_folder))
        video_name = os.path.split(mac_video_path)[-1]  # 视频文件名
        logging.info("视频文件名值：{}".format(video_name))
        url_tuple = upload_file_object(video_folder, video_name, mac_video_path)
        if url_tuple != "12158":
            logging.info("上传视频成功")
            logging.info("文件夹、视频名、路径：{}、{}、{}".format(video_folder, video_name, mac_video_path))
            logging.info("url_tuple的值：{}".format(url_tuple))
            download_url = url_tuple[0]  # 视频下载连接
            logging.info("生成的录屏下载地址：{}".format(download_url))
            file_url = url_tuple[1]  # 视频访问连接
            logging.info("录屏访问连接：{}".format(file_url))
            return download_url, file_url  # 下载视频连接
        else:
            logging.info("上传录屏gif图至服务器失败了！！")

    # 删除android本地录屏
    def delete_android_video(self):
        deviceName = self.get_iphone_deviceName()  # 获取当前执行设备号
        os.popen("adb -s {} shell rm /sdcard/.nomedia/*.mp4".format(deviceName))
        logging.info("android 本地视频删除成功")

    # 停止Android录屏-拷贝视频至mac本地-上传视频至服务器-删除android本地录屏
    def get_bug_video_url(self, android_video_path, video_name, pull_time=20):
        """
        :param android_video_path: android 本地生成的录屏路径
        :return:    录屏访问url
        """
        time.sleep(2)
        self.Stop_recording()  # 停止Android录屏
        mac_video_path = self.android_pull_mac(android_video_path, video_name, pull_time)  # 拷贝视频至mac本地
        url_list = self.upload_video(mac_video_path)
        logging.info("类型：{}".format(type(url_list)))
        if isinstance(url_list, tuple):
            download_url = url_list[0]  # 上传视频至服务器获取下载url
            # file_url = self.upload_video(mac_video_path)[1]                # 预览url
            return download_url
        else:
            logging.info("上传视频到服务器遇到问题")

    # 停止Android录屏-拷贝视频至mac本地-上传视频至服务器-删除android本地录屏
    def get_bug_video_url_demo(self, android_video_path, video_name, temp_dict, pull_time=20):
        """
        :param android_video_path: android 本地生成的录屏路径
        :return:    录屏访问url
        """
        time.sleep(2)
        self.Stop_recording()  # 停止Android录屏
        if video_name != '':
            mac_video_path = self.android_pull_mac_demo(android_video_path, video_name, pull_time)  # 拷贝视频至mac本地
            url_list = self.upload_video(mac_video_path)
            logging.info("类型：{}".format(type(url_list)))
            if isinstance(url_list, tuple):
                download_url = url_list[0]  # 上传视频至服务器获取下载url
                temp_dict[video_name] = download_url
                # file_url = self.upload_video(mac_video_path)[1]                # 预览url
                return download_url
            else:
                logging.info("上传视频到服务器遇到问题")
        else:
            logging.info("当前没有生成视频")

    # 上传视频至服务器
    def upload_video_demo(self, mac_video_path):
        """
        :param file: mac本机上视频文件绝对路径
        :return: 下载视频url
        """
        video_folder = "900" + time.strftime("%Y%m%d", time.localtime(time.time()))  # 使用当天日期做为存储视频的文件夹
        create_bucket(video_folder)  # 创建存储视频的文件夹
        logging.info("创建的文件夹为：{}".format(video_folder))
        video_name = os.path.split(mac_video_path)[-1]  # 视频文件名
        logging.info("视频文件名值：{}".format(video_name))
        url_tuple = upload_file_object(video_folder, video_name, mac_video_path)
        if url_tuple != "12158":
            logging.info("上传视频成功")
            logging.info("文件夹、视频名、路径：{}、{}、{}".format(video_folder, video_name, mac_video_path))
            logging.info("url_tuple的值：{}".format(url_tuple))
            download_url = url_tuple[0]  # 视频下载连接
            logging.info("生成的录屏下载地址：{}".format(download_url))
            file_url = url_tuple[1]  # 视频访问连接
            logging.info("录屏访问连接：{}".format(file_url))
            return download_url, file_url  # 下载视频连接
        else:
            logging.info("上传录屏gif图至服务器失败了！！")

    # 将Android中生成的手机录屏文件pull到mac本地指定路径中
    def android_pull_mac_demo(self, android_video_path, video_name, pull_time):
        """
        :param video_path: android 测试机生成的视频绝对路径
        :return: 生成gif路径
        """
        # 项目文件根路径
        deviceName = self.get_iphone_deviceName()  # 获取当前执行设备号
        base_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
        Superior_path = os.path.dirname(base_path)  # 项目文件父路径
        video_folder_path = os.path.join(Superior_path, "test_case_video_S009")  # mac本地存储视频的路径
        logging.info("存储视频的文件夹：'{}'".format(video_folder_path))
        if 'test_case_video_S009' not in os.listdir(Superior_path):
            logging.info("没有找到路径'{}'".format(video_folder_path))
            os.mkdir(video_folder_path)  # 没有路径则创建
            logging.info("创建视频存放路径'{}'".format(video_folder_path))
        else:
            shutil.rmtree(video_folder_path)
            os.mkdir(video_folder_path)  # 有路径并清空
            logging.info("找到路径'{}'，并清空了该文件夹".format(video_folder_path))
        logging.info("执行adb命令pull视频")
        logging.info("adb -s {0} pull {1} {2}/{3}.mp4".format(deviceName, android_video_path, video_folder_path,video_name))
        os.popen("adb -s {0} pull {1} {2}/{3}.mp4".format(deviceName, android_video_path, video_folder_path,video_name))
        time.sleep(pull_time)  # pull所花时间
        mac_video_path = os.path.join(video_folder_path, "{}.mp4".format(video_name))
        logging.info("生成视频的本地路径为：'{}'".format(mac_video_path))
        video_at_gif_time = self.get_video_ou_gif_time(mac_video_path)  # 通过视频大小得到转化为gif的时间
        # 将视频转换为gif
        # 生成gif的路径
        gif_mac_path = os.path.join(video_folder_path, "{}.gif".format(video_name))
        logging.info("视频转化成gif图等待时间 {} s".format(video_at_gif_time))
        os.popen("ffmpeg -i {0} -s 720x1440 -b:v 700k {1}".format(mac_video_path, gif_mac_path))
        time.sleep(video_at_gif_time)
        return gif_mac_path