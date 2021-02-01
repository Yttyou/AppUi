from MonitorFlow import app_action
from MonitorFlow.monitor_flow import MonitorFlow
from Common.path_config import monitorflowdata_path
import logging
import threading
import csv
import time
import inspect
import ctypes
import signal

run_time = time.strftime("%Y-%m-%d %H%M", time.localtime())       # 生成文件时间=开始获取数据时间


def child_thread1():
    """ APP数据加载 """
    app_action.app_login()                 # 登录
    app_action.app_action()              # 等待数据加载
    app_action.app_signout()             # 登出
    time.sleep(15)


def child_thread2(test_run,collection_time,data):
    """ 获取流量数据 """
    MonitorFlow().monit_flow(test_run,collection_time,data)

def _async_raise(tid, exctype):
    """引发异常，必要时执行清除"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def parent_thread(run,collection_time):
    """ run:运行次数  """
    """ collection_time:获取流量时间间隔  """
    #         上传流量       下载流量         流量总和       获取时间           运行次数
    data = [("Upload_flow", "Download_flow", "Total", "Sampling Time", "Test Run")]
    number = 1
    while number <=run:
        logging.info("这是第{}次循环".format(number))
        run2 = threading.Thread(target=child_thread2,args=[number,collection_time,data])
        run2.setDaemon(True)
        number = number + 1
        run2.start()
        child_thread1()
        stop_thread(run2)

    csvfile = open(monitorflowdata_path + "/flow_data_{}.csv".format(run_time), 'w+', encoding='utf8', newline='')
    writer = csv.writer(csvfile)
    writer.writerows(data)
    csvfile.close()
    app_action.quit_app()                     # 关闭app




if __name__ == '__main__':
    """" 这里配置参数 """
    """" 注意：执行前在配置文件SP_app_config.yaml中替换测试机参数 """
    """" 参数1：APP运行次数 """
    """" 参数2：获取APP消耗流量时间间隔 """
    parent_thread(3,3)
