# 监控APP内存
# 使用命令：adb shell dumpsys meminfo 被测APP包名

import os
import time
from Common.path_config import appmonitorindata_path
from Common.path_config import caps_path
import logging
import csv
import yaml

data = [("native", "dalvik","total","Sampling Time")]

class AppMonitorin:

    def app_ram(self,switch=True):
        time.sleep(30)
        curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
        while switch == True:
            interval_time = 3              #设置时间
            time.sleep(interval_time)       #获取内存信息的时间间隔
            desired_caps = yaml.load(open(caps_path + "/bc_app_config.yaml"))
            appPackage = desired_caps["appPackage"]         #从配置文件获取包名
            deviceName = desired_caps["deviceName"]
            # 获取TMC内存命令相关数据
            try:
                adb = "adb -s {} shell dumpsys meminfo {}".format(deviceName, appPackage)
                # 执行adb
                result = os.popen(adb).read()
                getTime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
                # 以','进行分割
                temp = ','.join(result.split())
                # 获取native值
                logging.info("temp的值:{}".format(temp))
                print(temp)
                native = temp.split('Native,Heap')[1].split(',')[1]
                # 获取dalvik值
                dalvik = temp.split('Dalvik,Heap')[1].split(',')[1]
                # 获取total值
                total = temp.split('TOTAL')[1].split(',')[1]
                data.append([native,dalvik,total,getTime])

                csvfile = open(appmonitorindata_path+"/ram_data_{}.csv".format(curTime),'w',encoding='utf8',newline='')
                writer = csv.writer(csvfile)
                writer.writerows(data)
                csvfile.close()
            except:
                time.sleep(10)
            else:
                switch = True


if __name__ == '__main__':
    AppMonitorin().app_ram()

