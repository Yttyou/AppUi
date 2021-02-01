from MonitorFlow import app_action
from Common.path_config import monitorflow_path, caps_path
import logging
import threading
import time
import os, yaml, socket
import json
from MonitorFlow.write_flowdata_tomysql import FlowDataToMysql

# ------登录接口请求数据脚本---------
flow_py_path = monitorflow_path + '/' + 'app_api_monitor.py'
# -------取样次数及csv文件后缀名----------
runtimes_file = monitorflow_path + '/monitor_times.json'


# 登录场景类
class FlowAction:

    def child_thread_login(self, run, mitm_port, platform):
        """ APP数据加载 """
        number = 1
        while number <= run:
            logging.info("开始进行脚本登录取样...")
            logging.info("这是第{}次循环".format(number))
            self.write_times(number)
            time.sleep(1)
            app_action.app_login()  # 登录
            app_action.app_action()  # 等待数据加载
            app_action.app_signout()  # 登出
            number += 1
        time.sleep(1)
        app_action.quit_app()
        time.sleep(1)
        self.kill_mitmdump_sever(mitm_port, platform)  # 殺死mitmdummp服務
        time.sleep(5)
        FlowDataToMysql().write_flow_data_tomysql()
        time.sleep(2)
        self.delete_phone_vpn()

    def child_thread_apiflow(self, mitm_port):
        """ 获取http流量数据 """
        """ mitmdump 加载py脚本 """
        logging.info("实时获取app接口请求脚本正在加载...")
        os.system("mitmdump -p {} -s {}".format(mitm_port, flow_py_path))
        time.sleep(5)

    def kill_mitmdump_sever(self, port_num, platform):
        if platform.upper() == 'WIN':
            p = os.popen(f'netstat  -aon|findstr {port_num}')
            p0 = p.read().strip()
            if p0 != '' and 'LISTENING' in p0:
                p1 = int(p0.split('LISTENING')[1].split("\n")[0].strip())  # 获取进程号
                os.popen(f'taskkill /F /PID {p1}')  # 结束进程
                print("进程号:", p1)
                print('mitmdump server已结束')
        elif platform.upper() == 'MAC':
            p = os.popen(f'lsof -i tcp:{port_num}')
            p0 = p.read()
            if p0.strip() != '':
                p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
                os.popen(f'kill {p1}')  # 结束进程
                print('mitmdump server已结束')

    def write_times(self, number):
        # -------------写入当前为第几次取样------------
        try:
            with open(runtimes_file, 'r') as load_r:
                load_dict = json.load(load_r)
                load_dict['monitortimes'] = number
                with open(runtimes_file, "w") as dump_w:
                    json.dump(load_dict, dump_w)
        except:
            raise Exception("文件配置出错,请按照规定配置monitor_times.json文件！！！")

    def parent_thread(self, mitm_port, run, platform):
        self.set_phone_vpn(mitm_port)
        time.sleep(1)
        self.kill_mitmdump_sever(mitm_port, platform)
        time.sleep(2)
        t1 = threading.Thread(target=self.child_thread_apiflow, args=[mitm_port])
        t1.setDaemon(True)
        t1.start()
        time.sleep(2)
        t2 = threading.Thread(target=self.child_thread_login, args=[run, mitm_port, platform])
        t2.start()

    def get_hostip(self):
        # ----- 获取主机IP ----#
        addrs = socket.getaddrinfo(socket.gethostname(), None)
        host_ip = [item[4][0] for item in addrs if ':' not in item[4][0] and "127.0.0.1" not in item[4][0]][-1]
        print('主机外网ip:', host_ip)
        return host_ip

    def set_phone_vpn(self, mitm_port):
        # ----- 获取设备名device ------#
        device_msg = yaml.load(open(caps_path + "/bc_app_config.yaml"))['deviceName']
        # ----- 获取主机ip--------#
        host_ip = self.get_hostip()
        # ----- 设置指定设备代理-------#
        f = os.popen(r"adb -s {} shell settings put global http_proxy {}:{}"
                     .format(str(device_msg), str(host_ip), str(mitm_port)), "r")
        shuchu = f.read()
        f.close()
        print("结果", shuchu)

    def delete_phone_vpn(self):
        '''
        # 执行删除代理操作
        1、adb [-s deviceName] shell settings delete global http_proxy
        2、adb [-s deviceName] shell settings delete global global_http_proxy_host
        3、adb [-s deviceName] shell settings delete global global_http_proxy_port
        :return:
        '''
        device_msg = yaml.load(open(caps_path + "/bc_app_config.yaml"))['deviceName']
        del_1 = os.popen(r"adb -s {} shell settings delete global http_proxy".format(device_msg))
        time.sleep(1)
        del_2 = os.popen(r"adb -s {} shell settings delete global global_http_proxy_host".format(device_msg))
        time.sleep(1)
        del_3 = os.popen(r"adb -s {} shell settings delete global global_http_proxy_port".format(device_msg))
        reboot = os.popen(r"adb -s {} shell reboot".format(device_msg))
        time.sleep(15)
        retry_times = 1
        while retry_times <= 50:
            f = os.popen(r"adb devices".format(device_msg))
            shuchu = f.read()
            f.close()
            if str(device_msg) in str(shuchu) and "device" in str(shuchu):
                print("重启完毕,设备名称为{}的手机代理已经被清除".format(device_msg))
                break
            else:
                retry_times += 1
                time.sleep(5)
                print("设备名称为{}的手机代理尚未重启完毕,5s后重新确认".format(device_msg))


if __name__ == '__main__':
    """" 这里配置参数 """
    """  注意1：执行前在配置文件SP_app_config.yaml中替换测试机参数 """
    """  注意2：执行前确保手机上的WLAN代理服务端口等配置正确 """
    """  注意3：get_hostip方法获取主机IP，***mac环境是否可用待检验*** """
    """  参数1：指定mitmproxy服务器端口 """
    """  参数2：APP运行次数 """
    """  参数3：设备类型:win/mac """
    FlowAction().parent_thread(mitm_port=4721, run=2, platform="mac")
