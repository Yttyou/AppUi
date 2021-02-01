import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from Common.path_config import testfiles_path, allure_report_path
from Common.email_config import *
from Common.ZenTaoApiToMysql import WriteToMysql, caps_path
from Common.get_to_bugdata import get_data, get_pdf_file
import yaml
import json
import datetime
import logging
import time


def sendEmail(title, text, filename=None):
    '''
    发送带附件的邮件
    :param title: 邮件标题
    :param text: 邮件正文
    :param send: 发送者邮箱
    :param passwd: 授权码
    :param to: 接收者邮箱
    :param smtp_server: 发送邮件的服务器
    :param file: 需要发送的附件
    :return:
    '''
    msg = MIMEMultipart()
    msg['From'] = from_mail
    msg['To'] = ','.join(to_mail)
    print(msg['To'])
    # 文字部分
    msg['Subject'] = title  # 主题
    strstr = text  # 文字内容
    att = MIMEText(strstr, 'html', 'utf-8')
    msg.attach(att)
    # 附件
    if filename:
        filepath = testfiles_path + '/' + filename
        att = MIMEApplication(open(filepath, 'rb').read())  # 你要发送的附件地址
        att.add_header('Content-Disposition', 'attachment', filename=filename)  # filename可随意取名
        msg.attach(att)
    server = smtplib.SMTP()
    try:
        server.connect(smtp_server)  # 连接smtp邮件服务器
        server.login(from_mail, mail_pass)  # 登录smtp邮件服务器
        server.sendmail(from_mail, msg['To'].split(','), msg.as_string())  # 发送
        server.close()  # 关闭
        print("郵件發送成功！")
    except:
        raise Exception("發送失敗！！！")


def get_email_msg():
    '''
    獲取發送郵件時必要的數據
    :return:
    '''
    # Bug 详情地址
    bug_details_link = 'http://117.50.36.141/#/home/buglist'
    # 详细报告地址
    overall_link = 'http://117.50.36.141/#/home/overall'

    # -------獲取testrun_id----#
    testrun_idpath = allure_report_path + '/html/data/duration.json'
    try:
        with open(testrun_idpath, 'r') as load_r:
            load_list = json.load(load_r)
            testrun_id = load_list[0]['TestRun ID']
    except:
        logging.error("testrun_id獲取失敗，請檢查該文件是否有誤")
        raise Exception("testrun_id獲取失敗，請檢查該文件是否有誤")

    # -------包名生成邏輯------#
    write_to_mysql_msg = yaml.load(open(caps_path + "/bc_app_config.yaml"))
    pkg_msg = write_to_mysql_msg['appPackage']
    platform_msg = write_to_mysql_msg['platformName']
    pkg_list = (pkg_msg, platform_msg)
    if pkg_list == ('com.suncity.sunpeople.qa', 'Android'):
        filename = 'SP-Android-QA包'
    elif pkg_list == ('com.suncity.sunpeople.uat', 'Android'):
        filename = 'SP-Android-UAT包'
    elif pkg_list == ('com.suncity.sunpeople.qa', 'iOS'):
        filename = 'SP-iOS-QA包'
    elif pkg_list == ('com.suncity.sunpeople.uat', 'iOS'):
        filename = 'SP-iOS-UAT包'
    else:
        raise Exception("bc_app_config.yaml存在不正確的包名或設備名")

    # ----------郵件標題生成邏輯-----------#
    sql_pkg_detail = "SELECT device,os_ver,pkg_ver,start_time,end_time FROM testrun_info " \
                     "WHERE testrun_id = {} and pkg = '{}' and platform = '{}';".format(
        testrun_id, pkg_msg, platform_msg)
    pkg_msg = WriteToMysql().ExcQuery(sql=sql_pkg_detail)
    if not pkg_msg:
        logging.error("testrun_id、appPackage、platformName錯誤或不存在")
        raise Exception("testrun_id、appPackage、platformName錯誤或不存在")

    start_time = datetime.datetime.strftime(pkg_msg[0][-2], '%H:%M')
    title_start_time = datetime.datetime.strftime(pkg_msg[0][-2], '%Y/%m/%d %H:%M:%S')
    end_time = datetime.datetime.strftime(pkg_msg[0][-1], '%H:%M')

    # -------測試設備等獲取邏輯---------#
    device_name, os_ver, pkg_ver = pkg_msg[0][0], pkg_msg[0][1], pkg_msg[0][2]

    # -------------獲取郵件標題內容-----------#
    """
    邮件标题：根据 6 的包名 + TestRun_id + 测试开始时间，
    如 SP-Android-QA-#513 測試報告 @2020/04/14 19:03:04
    """
    #email_title = filename + "-#" + str(testrun_id) + "-" + str(title_start_time) + " 測試報告"
    email_title = filename + "-#" + str(testrun_id) + " 測試報告" + " @" + str(title_start_time)

    # -------獲取BuG總數量及各版塊的bug數量--------#
    bug_list = get_data(testrun_id)
    len_bug = len(bug_list) - 1  # bug數量
    if len_bug >= 1:
        bug_state = 1
        bug_tab_list = []  # 獲取對應的板塊數量
        for i in bug_list[1:]:
            bug_tab_list.append(i[-1])
        bug_list_quchong = list(set(bug_tab_list))
        content_tab_bug = []
        for i in bug_list_quchong:
            content_tab_bug.append("{} {}個".format(i, bug_tab_list.count(i)))
        content_tab_bug_str = "|".join(content_tab_bug)

        # ------------生成最終版的郵件內容------------#
        email_content = """
        <div><b>{filename}</b> 功能回歸<b>測試報告</b>（測試時間：{start_time} - {end_time}）</div>
        <hr width= "500px" align="left">
        <div>測試設備：{device_name} | {os_ver}`｜軟件版本：`{pkg_ver}`</div>
        <hr width= "500px" align="left">
        <div><b>影響發版的問題：</b></div>
        <div>發現 {len_bug} 個 Bug ，<a href="{bug_details_link}" style="color: cornflowerblue">点击可查看详情</a></div>
        <div>{content_tab_bug_str}</div>
        <div></div>
        <hr width= "500px" align="left">
        <div><a href="{overall_link}" style="color: cornflowerblue">點擊可查看詳細報告</a></div>
        """.format(filename=filename, start_time=start_time, end_time=end_time,
                   device_name=device_name, os_ver=os_ver, pkg_ver=pkg_ver, len_bug=len_bug, bug_details_link = bug_details_link,
                   content_tab_bug_str=content_tab_bug_str, overall_link=overall_link)

    else:
        bug_state = 0
        email_content = """
        <div><b>{filename}</b> 功能回歸<b>測試報告</b>（測試時間：{start_time} - {end_time}）</div>
        <hr width= "500px" align="left">
        <div>測試設備：{device_name} | {os_ver}`｜軟件版本：`{pkg_ver}`</div>
        <hr width= "500px" align="left">
        <div><b>測試 100% 通過，軟件可正常發佈</b></div>
        <hr width= "500px" align="left">
        <div><a href="{overall_link}" style="color: cornflowerblue">點擊可查看詳細報告</a></div>
        """.format(filename=filename, start_time=start_time, end_time=end_time,
                   device_name=device_name, os_ver=os_ver, pkg_ver=pkg_ver, overall_link=overall_link)

    detail_msg = [filename, start_time, end_time, device_name, os_ver, pkg_ver,
                  len_bug if bug_state else "", content_tab_bug_str if bug_state else ""]
    return [email_title, detail_msg, email_content + "<style>a{text-decoration:none}</style>"]  # 去掉a標籤下劃線


def main_pdf_email():  # 調用此方法實現寫入pdf及發送郵箱功能
    pdf_result = get_pdf_file()
    if "OK" in pdf_result:
        filename = pdf_result[1]
    if "Error" in pdf_result:
        raise Exception('PDF寫入失敗!!!,無法發送測試報告')
    if "PASS" in pdf_result:
        filename = None
    time.sleep(2)
    email_msg = get_email_msg()
    sendEmail(title=email_msg[0], text=email_msg[-1], filename=filename)


if __name__ == '__main__':
    main_pdf_email()
