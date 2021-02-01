# encoding='utf-8'
# 读取测试机相关配置类

import uiautomator2 as u2
from TestDatas import iphone_whitelist
from Common import logger
import logging
import random
import os
import re
import time
# from appium.webdriver.appium_service import AppiumService
import shutil
import json
import requests


appPackage_name = ''
versionCode = ''
versionName = ''
appActivity_name = ''
platformVersion = ''
deviceName = ''
phoneInfo = ''


# 初始化：
# 1. Caps
# 2. Allure Environment info
class ReadIphoneConfig:

    # 获取apk路径及命名
    def get_apk_name_path(self):
        # def ini_env(self):
        # def __init__(self):
        # appium_service = AppiumService()  # 初始化 appium 服务
        # 从Jenkins本地安装最新的分支包
        # jk_apk = '/Users/cf/Workspace/appium/android_auto/'
        jk_apk = '/Users/ytt/Desktop/'
        # jk_apk = '/Users/areo/Downloads/apktest/'
        # 复制 git 代码提交信息
        # shutil.copy('/Users/cf/.jenkins/workspace/Android-SP-QA-Neptune-Build-Auto/gitinfo.csv', 'TestFiles/gitinfo.csv')


        files = os.listdir(jk_apk)
        # localpath = '/Users/areo/Downloads/apktest'
        for file in sorted(files):  # 根据路径读取APK文件名
            if os.path.splitext(file)[1] == '.apk':
                filename = file
                ApkFileName = filename

        # 文件若是存在则形成完整apk路径
        if len(filename) > 1:
            # 获取 apk 路径
            apkpath = jk_apk + filename
        else:
            exit(1)

        # # 看手机是否在线§
        # try:
        #     # connect_device = u2.connect_usb()
        #     # connect_device = u2.connect_wifi('172.21.42.92') # S8
        #     # connect_device = u2.connect_wifi('172.21.42.49')  # 舒淇 S9
        #     # connect_device = u2.connect_wifi('172.21.42.83')  # Note10
        #
        #     # connect_device.app_install('https://download.fir.im/apps/5db8fec6b2eb4642a799d6b7/install?download_token=9a40ffbc79be1c6c9f8b6cd88439f8f5&release_id=5de6002c23389f548c9f37da')
        #     phoneInfo = connect_device.device_info
        #     platformVersion = phoneInfo["version"]
        #     deviceName = phoneInfo["serial"]
        # except:
        #     push_payload = json.dumps({"text": "Jenkins 未检测到手机，请检查手机是否连接"})
        #     header = {"Content-Type": "application/json"}
        #     requests.post('https://hook.bearychat.com/=bwD9B/incoming/2d3ea8776cc6bf0a2d5f08c2b5e40ebc', data=push_payload,
        #                   headers=header)
        #     exit(101)
        return apkpath,filename

    # 重新安装apk
    def install_test_apk(self):
        iphone_data = self.get_whitelist_iphone()
        apkpath = self.get_apk_name_path()[0]
        # 获取 aapt 所在路径
        if "ANDROID_HOME" in os.environ:
            root_dir = os.path.join(os.environ["ANDROID_HOME"], "build-tools")
            for path, subdir, files in os.walk(root_dir):
                if "aapt" in files:
                    aapt_path = os.path.join(path, "aapt")
        else:
            print("ANDROID_HOME dose not exist")
        # 读取 apk 信息，获取测试对象信息
        output = os.popen(aapt_path + " d badging %s" % apkpath).read()
        # 信息匹配
        match = re.compile(
            "package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)' ([\s\S]*)launchable-activity: name='(\S+)'").match(
            output)
        # 获取 apk 包中的信息
        global appPackage_name
        global versionCode
        global versionName
        global appActivity_name
        appPackage_name = match.group(1)
        versionCode = match.group(2)
        versionName = match.group(3)
        appActivity_name = match.group(5)
        logging.info("appPackage_name的值为：'{}'".format(appPackage_name))
        logging.info("appActivity_name的值为：'{}'".format(appActivity_name))

        # 看手机是否在线
        try:
            # 卸载已安装的测试对象，防止上轮测试异常未登出导致测试失败 + 指定设备安装和卸载 by Areo @ 2020.04.01
            os.system("adb -s " + iphone_data[0] + " uninstall " + appPackage_name)
            # 安装测试包
            os.system("adb -s " + iphone_data[0] + " -d install -r -d -g " + apkpath)
        except:
            push_payload = json.dumps({"text": "Jenkins 上的测试手机已离线，请检查！"})
            header = {"Content-Type": "application/json"}
            requests.post('https://hook.bearychat.com/=bwD9B/incoming/2d3ea8776cc6bf0a2d5f08c2b5e40ebc', data=push_payload,
                          headers=header)
            exit(101)
        else:
            print("APK installed successfully")
        self.select_write_capsini(iphone_data[1], iphone_data[0])  # 将机型写入配置文件

    # 检测连接打包机的手机是否加入执行脚本白名单
    def testing_iphone_whitelist(self):
        """
        :return: 返回元祖，第一个元素为当前连接打包机已加入白名单列表；第二个元素为未加入名单
        """
        get_iphone_devices = os.popen("adb devices").read().replace('\n', '').replace('\r', '')
        list = re.split("attached|	device", get_iphone_devices)
        # 去掉首尾两个元素（多余的字符和空格）
        del (list[0])
        del (list[-1])

        # 获取手机设备型号（只能查单台手机）
        # adb shell getprop ro.product.model
        iphone_dict = iphone_whitelist.whitelist
        logging.info("检查到连接打包机上的Android设备数有：{}台".format(len(list)))
        logging.info("设备列表：{}".format(list))
        whitelist = []  # 存储已加入白名单的手机
        blacklist = []  # 存储未加入白名单的手机

        flag = 0
        for i in list:
            for j in iphone_dict:
                if i == j:
                    flag = flag + 1
            if flag > 0:
                whitelist.append(i)
                flag = 0
            else:
                blacklist.append(i)
        return whitelist,blacklist

    # 读取检测出已加入白名单设备，写入bc_app_config.yaml文件
    def get_whitelist_iphone(self):
        Second_level_iphone = iphone_whitelist.Second_level_iphone
        logging.info("读取到二级机型为：{}".format(Second_level_iphone))
        iphone_list = self.testing_iphone_whitelist()[0]   # 检测出已经加入白名单的设备
        try:
            assert len(iphone_list) >= 1     # 检测出插在打包机上的白名单手机大于1个
            logging.info("检测出插在打包机上并加入白名单的手机有{}个".format(len(iphone_list)))
            logging.info("白名单的手机列表为：{}".format(iphone_list))
        except:
            logging.exception("没有检测到手机或手机未加入测试白名单，请检查！！！")
            raise
        else:
            if str(iphone_list).find(Second_level_iphone) != -1:                     # 判断现有的设备中是否有二级机型
                Version = self.get_iphone_Version(Second_level_iphone)      # 获取对应设备的Android版本号
                logging.info("检测到二级机型...")
                logging.info("读取二级机型为：设备号 '{}'  版本号 '{}'".format(Second_level_iphone, Version))
                device = Second_level_iphone
            else:
                logging.info("没有检测到二级设备！！！")
                logging.info("正在选取其他设备来执行脚本。。。")
                device = random.sample(iphone_list, 1)                          # 随机选择一个设备（已加入白名单）
                Version = self.get_iphone_Version(device)               # 获取对应设备的Android版本号
                logging.info("随机选取到非二级机型是：设备号 '{}'  版本号 '{}'".format(device,Version))
                self.select_write_capsini(Version, device)              # 将非二级机型写入配置文件
            return device,Version

    # 获取指定设备的系统版本号
    def get_iphone_Version(self,iphone_Device):
        """
        :param iphone_Device: Android手机的设备号
        :return: 手机系统版本号
        """
        connect_device = u2.connect_usb(iphone_Device)
        global phoneInfo
        phoneInfo = connect_device.device_info
        global platformVersion
        platformVersion = phoneInfo["version"]    # 转换成浮点型
        return platformVersion

    # 筛选出当前需要执行的设备，写入配置文件中
    def select_write_capsini(self,platformVersion,deviceName):  # 將測試執行手機的配置信息寫如‘bc_app_config.yaml’文件中
        """
        :param platformVersion:筛选后的手机Android版本号
        :param deviceName: 筛选后的Android手机的设备号
        :return:
        """
        appActivity = appActivity_name
        appPackage = appPackage_name
        logging.info("写入的appActivity值为'{}'".format(appActivity))
        logging.info("写入的appActivity值为'{}'".format(appPackage))
        f = open("Caps/bc_app_config.yaml", "w")
        f.write("platformName: Android\n")
        f.write("appActivity: " + appActivity + "\n")
        f.write("appPackage: " + appPackage + "\n")
        f.write("platformVersion: " + platformVersion + "\n")
        f.write("deviceName: " + deviceName + "\n")
        f.close()

    # 初始化Caps，动态生成bc_app_config.yaml文件
    def write_capsini(self):  # 將測試執行手機的配置信息寫如‘bc_app_config.yaml’文件中
        f = open("Caps/bc_app_config.yaml", "w")
        f.write("platformName: Android\n")
        f.write("appActivity: " + appActivity_name + "\n")
        f.write("appPackage: " + appPackage_name + "\n")
        f.write("platformVersion: " + platformVersion + "\n")
        f.write("deviceName: " + deviceName + "\n")
        f.close()

    # 初始化environment.properties，for Allure Report
    def write_allure_env(self):  # 配置信息寫入Allure中環境變量
        # appInfo = self.connect_device.app_info('com.suncity.sunpeople.qa')
        deviceModel = phoneInfo["model"]
        appVersion = versionName
        testEnv = appPackage_name
        f = open("Allure-Report/xml/environment.properties", "w")
        f.write("Platform: Android\n")
        f.write("Platform.Version: " + platformVersion + "\n")
        f.write("Device.Model: " + deviceModel + "\n")
        f.write("App.Version: " + appVersion + "\n")
        f.write("Testing.Environment: " + testEnv + "\n")
        f.close()

    # 通过系统变量获取 aapt 位置
    def get_aapt(self):
        if "ANDROID_HOME" in os.environ:
            root_dir = os.path.join(os.environ["ANDROID_HOME"], "build-tools")
            for path, subdir, files in os.walk(root_dir):
                if "aapt" in files:
                    return os.path.join(path, "aapt")
        else:
            return "ANDROID_HOME dose not exist"

    def appium_up(self, port_num, platform):
        if platform.upper() == 'WIN':
            p = os.popen(f'netstat  -aon|findstr {port_num}')
            p0 = p.read().strip()
            if p0 != '' and 'LISTENING' in p0:
                p1 = int(p0.split('LISTENING')[1].strip()[0:4])  # 获取进程号
                os.popen(f'taskkill /F /PID {p1}')  # 结束进程
                print('appium server已结束')
        elif platform.upper() == 'MAC':
            p = os.popen(f'lsof -i tcp:{port_num}')
            p0 = p.read()
            if p0.strip() != '':
                p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
                os.popen(f'kill {p1}')  # 结束进程
                print('appium server已结束')

        cmd_dict = {
            'WIN': f' start /b appium -p {port_num} ',
            'MAC': f'appium -p {port_num} --log-level error & '
        }
        os.system(cmd_dict[platform.upper()])
        time.sleep(3)  # 等待启动完成
        print('appium启动成功')

    # file:csv to json
    def transjson(self, jsonpath, csvpath):
        fw = open(jsonpath, 'w', encoding='utf-8')  # 打开csv文件
        fo = open(csvpath, 'r', newline='', encoding='utf-8')  # 打开csv文件

        ls = []
        for line in fo:
            line = line.replace("\n", "")  # 将换行换成空
            ls.append(line.split(","))  # 以，为分隔符
        # print(ls)
        # 写入
        for i in range(1, len(ls)):  # 遍历文件的每一行内容，除了列名
            ls[i] = dict(zip(ls[0], ls[i]))  # ls[0]为列名，所以为key,ls[i]为value,
        # zip()是一个内置函数，将两个长度相同的列表组合成一个关系对

        json.dump(ls[1:], fw, sort_keys=True, indent=4)
        # 将Python数据类型转换成json格式，编码过程
        # 默认是顺序存放，sort_keys是对字典元素按照key进行排序
        # indet参数用语增加数据缩进，使文件更具有可读性

        # 关闭文件
        fo.close()
        fw.close()


