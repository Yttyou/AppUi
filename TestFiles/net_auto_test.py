import datetime
import time
import requests
import sys
import pycurl
import urllib3
import json
import os
import numpy

URL = "https://sp-api.i-mocca.com"  # 探测的目标URL
TEST_SERVER_URL = URL + "/api/hello"  # 服务器探测 URL
DOWNLOAD_URL = 'https://sp-api.i-mocca.com/test_download/MacVim.dmg'
# BC_URL = 'https://hook.bearychat.com/=bwD9B/incoming/2d3ea8776cc6bf0a2d5f08c2b5e40ebc'
BC_URL = 'https://hook.bearychat.com/=bwD9B/incoming/712c31e32db064f4c39dab549ac4a03e'


def get_delay_time(url=URL):
    c = pycurl.Curl()  # 创建一个Curl对象
    c.setopt(pycurl.URL, url)  # 定义请求的URL常量

    # 连接超时时间,5秒
    c.setopt(pycurl.CONNECTTIMEOUT, 5)  # 定义请求连接的等待时间

    # 下载超时时间,5秒
    c.setopt(pycurl.TIMEOUT, 5)  # 定义请求超时时间
    c.setopt(pycurl.FORBID_REUSE, 1)  # 屏蔽下载进度条
    c.setopt(pycurl.MAXREDIRS, 1)  # 完成交互后强制断开连接，不重用
    c.setopt(pycurl.NOPROGRESS, 1)  # 指定HTTP重定向的最大数为1
    c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)  # 设置保存DNS信息的时间为30秒
    f = open(os.path.dirname(os.path.realpath(__file__)) + "/content.txt", "wb")
    c.setopt(pycurl.WRITEHEADER, f)
    # 将返回的HTML内容定向到indexfile文 件对象
    c.setopt(pycurl.WRITEDATA, f)

    try:
        c.perform()  # 提交请求
    except Exception as e:
        print("connection error:" + str(e))
        c.close()
        f.close()
        sys.exit()  # 中止脚本运行

    total_time = round(c.getinfo(c.TOTAL_TIME) * 1000, 2)  # 获取传输的总时间, 单位ms
    http_code = c.getinfo(c.HTTP_CODE)  # 获取HTTP状态码

    print(f"HTTP状态码：{http_code}")
    print(f"传输结束总时间：{total_time}")

    # 关闭Curl对象
    c.close()
    f.close()
    return total_time


def get_speed(download_url=DOWNLOAD_URL):
    headers = {'Proxy-Connection': 'keep-alive'}
    r = requests.get(download_url, stream=True, headers=headers)

    count = 0
    count_tmp = 0
    start_time = time.time()
    time1 = time.time()
    num = 0
    length = float(r.headers['content-length'])
    mean_speed = 0

    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            count += len(chunk)  # 字节数
            current_time = time.time()
            if current_time - time1 > 2:
                num += 1
                p = round(count / length * 100, 2)
                speed = round((count - count_tmp) / 1024 / 1024 / (current_time - time1), 2)
                mean_speed = round(count / 1024 / 1024 / (current_time - start_time), 2)
                count_tmp = count
                time1 = current_time
                print(f'p: {p}%, speed: {speed}, mean_speed: {mean_speed}')
    return mean_speed


def notify_bc(url, speed, min_speed, median_speed, delay_time, max_delay_time, median_delay_time,
              package_title, remote_url):
    headers = {"Content-Type": "application/json"}

    http = urllib3.PoolManager()
    time = datetime.datetime.now()
    now_time = time.strftime('%H:%M:%S')
    issue_gate = 'http://cityfruit-doc.i-mocca.com/web/#/27?page_id=732'
    payload = "**`{}`网络环境异常警报**（时间：{}）\
                \n`自动化测试已中止，请及时处理!` \
                \n ------ \
                \n`当前下载网速中位数`：{} Mbps | `测得最小下载网速`：{} Mbps \
                \n > 最低下载速度不能小于 1 Mbps \
                \n\
                \n`当前网络延时中位数`：{} ms | `测得最大网络延迟` : {} ms \
                \n > 最高网络延迟不能大于 500 ms \
                \n\
                \n ------ \
                \n**处理完毕，[请点击此处]({}) 以恢复自动化测试执行** \
                \n ------\
                \n[传送门：我有建议提给质量自动化]({})".format(package_title, now_time, median_speed, min_speed,
                                                median_delay_time, max_delay_time, remote_url, issue_gate)
    # print(payload)
    requests.post(url, headers=headers, data=json.dumps({"text": payload}))
    # status = response.status
    # print(f'bc status: {status}')
    # response.release_conn()
    return


# 服务中断时发出预警
def server_down_notify_bc(package_title):
    headers = {"Content-Type": "application/json"}
    now_time = datetime.datetime.now().strftime('%H:%M:%S')
    remote_url = 'https://cf-jks.ngrok.io/job/Android-TMC-QA-Neptune-Run-Auto/build?token=TMC-Android'
    issue_gate = 'http://cityfruit-doc.i-mocca.com/web/#/27?page_id=732'
    payload = '**`{}` 服务中断警报**（时间：{}）\n' \
              '`自动化回归测试已停止，请及时处理!`\n' \
              '---\n' \
              '**`当前 QA 服务已挂起，请立即处理`**\n' \
              '---\n' \
              '**处理完毕，[请点击此处]({}) 以恢复自动化测试执行**\n' \
              '---\n' \
              '[传送门：我有建议提给质量自动化]({})'.format(package_title, now_time, remote_url, issue_gate)
    print('服务中断，向 BC 发出预警')
    requests.post(BC_URL, headers=headers, data=json.dumps({"text": payload}))


def run(test_num, package_title, remote_url):
    # 环境检测 - 服务中断时发出预警
    test_server = requests.get(TEST_SERVER_URL)
    if test_server.status_code >= 400:
        server_down_notify_bc(package_title)
        return 503
    delay_time_list = []
    speed_list = []
    for i in range(test_num):
        time.sleep(0.2)
        delay_time = get_delay_time()
        delay_time_list.append(delay_time)
        speed = get_speed()
        speed_list.append(speed)
    min_speed = min(speed_list)
    print(speed_list)
    median_speed = numpy.median(speed_list)  # 网速中位数
    speed = round(sum(speed_list) / len(speed_list), 2)
    max_delay_time = max(delay_time_list)
    delay_time = round(sum(delay_time_list) / len(delay_time_list), 2)
    median_delay_time = numpy.median(delay_time)  # 延迟中位数
    status = 200
    # if delay_time > 500 or speed < 1:
    if delay_time > 500 and median_speed < 0.8:
    # if delay_time > 0 or speed < 100:   # UAT settings
        status = 503
        notify_bc(BC_URL, speed, min_speed, median_speed, delay_time, max_delay_time, median_delay_time,
                  package_title, remote_url)
    return status


if __name__ == '__main__':
    remote = 'https://cf-jks.ngrok.io/job/Android-TMC-QA-Neptune-Run-Auto/build?token=TMC-Android'
    run(3, package_title='SP/TMC QA', remote_url=remote)
