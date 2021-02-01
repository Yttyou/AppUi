# 监控APP流量：上行、下行、总和

# 1.获取被测应用的uid：adb shell dumpsys package '应用包名' | grep userId
# 2.通过应用uid，获取应用当前消耗的流量：
# --上行流量：adb shell cat /proc/uid_stat/10080/tcp_snd
# --下行流量 adb shell cat /proc/uid_stat/10080/tcp_rcv
# Modified by Areo @ 2020.03.07
# 3. 第 2 个方法对于高版本的手机不适用改为 adb shell cat /proc/net/xt_qtaguid/stats | grep {uid}

import os
import time
from Common.path_config import monitorflowdata_path
from Common.path_config import caps_path
import logging
import csv
import yaml


class MonitorFlow():
    def monit_flow(self, test_run, collection_time, data):
        """ test_run：APP运行次数 """
        """ collection_time：监控App流量时间间隔 """
        """ data：App流量数据 """

        switch = True
        time.sleep(2)
        desired_caps = yaml.load(open(caps_path + "/bc_app_config.yaml"))
        appPackage = desired_caps["appPackage"]  # 从配置文件获取包名
        deviceName = desired_caps["deviceName"]  # 从配置文件设备 ID

        # 获取被测试APP流量消耗数据
        uid_adb = "adb -s {} shell dumpsys package {} | grep userId".format(deviceName, appPackage)
        uid_text = os.popen(uid_adb).read()
        uid = str(uid_text.split('=')[1]).strip()
        logging.info("uid的值'{}'".format(uid))
        output_adb = "adb -s {} shell cat /proc/net/xt_qtaguid/stats | grep {}".format(deviceName, uid)
        output = os.popen(output_adb).read()
        print(output)
        read_ini = self.read_flow(output, uid)
        # Upload_adb = "adb shell cat /proc/uid_stat/{}/tcp_snd".format(uid)
        Upload_init_flow = read_ini[1]  # 初始上行流量
        logging.info("初始上行流量:{}".format(Upload_init_flow))
        # Download_adb = 'adb shell cat /proc/uid_stat/{}/tcp_rcv'.format(uid)
        Download_init_flow = read_ini[0]  # 初始下行流量
        logging.info("初始下行流量:{}".format(Download_init_flow))

        while switch == True:
            time.sleep(collection_time)  # 采集时间间隔
            getTime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
            try:
                output_sample = os.popen(output_adb).read()
                print(output_sample)
                read_sample = self.read_flow(output_sample, uid)
                send_sample = read_sample[1]
                rec_sample = read_sample[0]
                Upload_flow = (int(send_sample) - int(Upload_init_flow)) // 1024  # 上行流量
                logging.info("上行流量:{}".format(Upload_flow))
                Download_flow = (int(rec_sample) - int(Download_init_flow)) // 1024  # 下行流量
                logging.info("下行流量:{}".format(Download_flow))
                flow_sum = Upload_flow + Download_flow  # 消耗总流量
                logging.info("消耗总流量:{}".format(flow_sum))
                data.append([Upload_flow, Download_flow, flow_sum, getTime, test_run])
            except:
                time.sleep(3)

    def read_flow(self, output, uid):
        rec = 0
        send = 0
        if len(output) > 0 and 'No such file or directory' not in output:
            lines = output.strip().split('\n')
            # print('lines:{}'.format(lines))
            for line in lines:
                line = line.strip().split(' ')
                if len(line) > 8 and ('wlan' in line[1] or 'rmnet_data' in line[1]):
                    # print('line:{}'.format(line))
                    rec += int(line[5])
                    send += int(line[7])
            return rec, send
        else:
            return rec, send  # 当读取不到数据的时候返回 0
