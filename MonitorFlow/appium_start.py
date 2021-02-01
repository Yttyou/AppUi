# -*-coding:utf8-*-
import os
import time


def appium_up(port_num, platform):
    if platform.upper() == 'WIN':
        p = os.popen(f'netstat  -aon|findstr {port_num}')
        p0 = p.read().strip()
        if p0 != '' and 'LISTENING' in p0:
            p1 = int(p0.split('LISTENING')[1].split("\n")[0].strip())  # 获取进程号
            os.popen(f'taskkill /F /PID {p1}')  # 结束进程
            print("进程号:",p1)
            print('appium server已结束')
    elif platform.upper() == 'MAC':
        p = os.popen(f'lsof -i tcp:{port_num}')
        p0 = p.read()
        if p0.strip() != '':
            p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
            os.popen(f'kill {p1}')  # 结束进程
            print('appium server已结束')

    cmd_dict = {
        'WIN': f'start /b appium -a 127.0.0.1 -p {port_num} & ',
        'MAC': f'appium -a 127.0.0.1 -p {str(port_num)} --log-level error & '
    }
    os.system(cmd_dict[platform.upper()])
    #a = os.system(f'start /b appium -a 127.0.0.1 -p 4027 --log-level error & ')
    print("命令是:",cmd_dict[platform.upper()])
    time.sleep(3)  # 等待启动完成
    print('appium 启动成功')
