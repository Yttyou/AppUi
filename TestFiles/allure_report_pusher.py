# -*- coding: UTF-8 -*-
# !/usr/bin/env python3

import json
import sys
import time
import datetime
import requests
import csv
import pymysql
import os
from TestFiles import git_handle
from Common import mysql_config

# 开始时间
start_time_stamp = time.time()
# BC 推送 WebHook（PO）
# PO_PUSH_WEB_HOOK = 'https://hook.bearychat.com/=bwD9B/incoming/b8e14da1dafcebef91b78b9779779f9f'
PO_PUSH_WEB_HOOK = 'https://hook.bearychat.com/=bwD9B/incoming/2d3ea8776cc6bf0a2d5f08c2b5e40ebc'
# BC 推送 WebHook（QA）
# QA_PUSH_WEB_HOOK = 'https://hook.bearychat.com/=bwD9B/incoming/03b1428356814cf5cad382b6b4567dd7'
QA_PUSH_WEB_HOOK = 'https://hook.bearychat.com/=bwD9B/incoming/2d3ea8776cc6bf0a2d5f08c2b5e40ebc'
# BC 推送 WebHook（DATABASE)
DATABASE_PUSH_WEB_HOOK = 'https://hook.bearychat.com/=bwD9B/incoming/2d3ea8776cc6bf0a2d5f08c2b5e40ebc'
# BUG 浏览传送门
BUG_BROWSE_GATEWAY = 'http://cf-issue.i-mocca.com/bug-browse-9.html'
# 建议收集传送门
ISSUE_GATEWAY = 'http://106.75.105.142:5555/web/#/27?page_id=732'
# 测试持续时间
testing_duration = {}
# 测试环境
testing_env_info = {}
# 提交信息
git_info = {}
# 测试覆盖率
coverage_rate = {}
# 概览
overview = {}
# 用户故事测试结果
results_by_story = []
# 缺陷列表
defect_list = []
# 推送消息体公共部分——消息表头
text_head = ''
# 推送消息体公共部分——测试环境
test_env = ''
# 推送消息体（PO）
po_text = ''
# 推送消息体（QA）TMC
qa_text = ''
# ShowDoc 保存内容
page_content_text = '|  序號 | 模塊  | 標題  | 嚴重程度  |\n| ------------ | ------------ | ------------ | ------------ |'
page_content_text_of_bug = ''

# 读取 JSON 文件
def load_jsons():
    global testing_duration, testing_env_info, git_info, coverage_rate, overview, results_by_story, defect_list
    # 测试周期
    testing_duration = json.load(open('./allure-report/html/data/duration.json', encoding='utf-8'))[0]
    # 测试环境
    properties = open('./allure-report/xml/environment.properties', encoding='utf-8')
    # properties 文件读取
    for line in properties:
        if line.find(':') > 0:
            string_array = line.replace('\n', '').split(': ')
            testing_env_info[string_array[0]] = string_array[1]
    properties.close()
    # 提交信息
    git_info = json.load(open('./allure-report/html/data/gitinfo.json', encoding='utf-8'))
    # 测试覆盖率
    coverage_rate = json.load(open('./allure-report/html/data/rate_data.json', encoding='utf-8'))
    # 测试结果
    overview = json.load(open('./allure-report/html/data/bytype.json', encoding='utf-8'))
    # 用户故事测试结果
    with open("./allure-report/html/data/behaviors.csv", 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        fieldnames = next(reader)
        csv_reader = csv.DictReader(f, fieldnames=fieldnames)
        for row in csv_reader:
            # Feature 是否已经存在
            exist = 0
            for result_by_story in results_by_story:
                if result_by_story.get('Feature') == row.get('Feature'):
                    exist = 1
                    result_by_story['FAILED'] = int(row.get('FAILED', 0)) + int(result_by_story.get('FAILED', 0))
                    result_by_story['BROKEN'] = int(row.get('BROKEN', 0)) + int(result_by_story.get('BROKEN', 0))
                    result_by_story['PASSED'] = int(row.get('PASSED', 0)) + int(result_by_story.get('PASSED', 0))
                    result_by_story['SKIPPED'] = int(row.get('SKIPPED', 0)) + int(result_by_story.get('SKIPPED', 0))
                    result_by_story['UNKNOWN'] = int(row.get('UNKNOWN', 0)) + int(result_by_story.get('UNKNOWN', 0))
                    break
            if exist == 1:
                continue
            else:
                results_by_story.append(row)
    # behaviors_csv.close()
    # 缺陷列表
    defect_list = json.load(open('./allure-report/html/data/bug_list.json', encoding='utf-8'))


def print_dicts():
    print('测试周期 testing_duration duration.json\n', testing_duration)
    print('测试环境 testing_env_info environment.properties\n', testing_env_info)
    print('提交信息 git_info gitinfo.json\n', git_info)
    print('测试覆盖率 coverage_rate rate_data.json\n', coverage_rate)
    print('测试结果 overview bytype.json\n', overview)
    print('用户故事测试结果 results_by_story behaviors.csv\n')
    for result_by_story in results_by_story:
        print(result_by_story)
    print('缺陷列表 defect_list bug_list.json\n', defect_list)


# 构造推送消息体（PO）
def init_po_push_payload():
    global po_text, text_head, test_env
    # 包
    testing_environment = testing_env_info.get('Testing.Environment')
    # 产品名
    product = 'Unknown'
    if testing_environment[:testing_environment.rfind('.')].endswith('sunpeople'):
        product = 'SP'
    elif testing_environment[:testing_environment.rfind('.')].endswith('teammember'):
        product = 'TMC'
    # 包名
    package_name = "{}-{}-{}".format(product,
                                     testing_env_info.get('Platform'),
                                     testing_environment[testing_environment.rfind('.') + 1:].upper())
    # 测试开始、结束时间
    start_time = datetime.datetime.strptime(testing_duration.get('Start Time'), '%Y-%m-%d %H:%M:%S')
    end_time = datetime.datetime.strptime(testing_duration.get('End Time'), '%Y-%m-%d %H:%M:%S')
    # 消息头、测试周期
    text_head = "**`{} 包` `功能回归` 测试报告**（测试时间：{} - {}）".format(package_name,
                                                              start_time.strftime("%H:%M"),
                                                              end_time.strftime("%H:%M"))
    po_text += text_head
    # 提交信息
    po_text += "\n---"
    git_info_text = ""
    for git_info_item in git_info:
        # 修改为获取最后一条提交信息
        git_info_text = "\n提交人：`{}` | 分支：`{}`" \
                         "\n提交信息：{}".format(git_handle.get_commit_dev(git_info_item.get('name')), git_info_item.get('branch'),
                                            git_info_item.get('commit'))
    if len(git_info_text) > 1:
        po_text += git_info_text
    else:
        po_text += "\n`未获取到分支提交信息`"
        # 测试环境
    test_env = "\n设备型号：`{}` | 系统版本：`{}`｜软件版本：`{}`".format(testing_env_info.get('Device.Model'),
                                                          testing_env_info.get('Platform.Version'),
                                                          testing_env_info.get('App.Version'))
    po_text += test_env
    po_text += "\n---" \
               "\nBug 相关：" # \
               # "\n发现 `1` 个可能造成崩溃的 Bug 分布在如下模块，请 PO 关注 [点击查看详情]" \
               # "(https://cf-jks.ngrok.io/view/Testing-Neptune/job/Android-SP-QA-Neptune-Run-Auto/allure/#bug_list)" \
               # "\n> 聊天: `1` (Mock 数据)"
    # "\n\n（上述为 Mock 数据，暂无获取方式）"
    # S1/S2 级 BUG 模块分布
    s1_s2_bug_modules = {}
    # S1/S2 级 BUG 总数
    s1_s2_bug_count = 0
    for defect in defect_list:
        if defect.get('Severity').startswith('S1') or defect.get('Severity').startswith('S2'):
            s1_s2_bug_count += 1
            s1_s2_bug_modules[defect.get('Module')] = s1_s2_bug_modules.get(defect.get('Module'), 0) + 1
    # 有 S1/S2 级 BUG
    if s1_s2_bug_count != 0:
        po_text += "\n发现 `{}` 个`S1/S2`级严重 Bug 分布在如下模块，请 PO 关注 [点击查看详情]" \
                   "(http://117.50.36.141/#/home/buglist)" \
            .format(s1_s2_bug_count)
        for module in s1_s2_bug_modules:
            po_text += "\n> {}：`{}`".format(module, s1_s2_bug_modules[module])
        po_text += "\n"
    # 无 S1/S2 级 BUG
    else:
        po_text += "\n>无 `S1/S2` 级 Bug\n"
    # 脚本覆盖率
    po_text += "\n脚本覆盖率(`不包括当前迭代新增和修改的功能`) [点击查看详情]" \
               "(http://117.50.36.141/#/home/cover)"
    if len(coverage_rate) != 0:
        po_text += "\n>"
        for module in coverage_rate:
            po_text += " {}: `{:g}%` |".format(module['Module'], round(float(module.get('Coverage Rate', 0)), 3) * 100)
        # 去掉最后一个"|"
        po_text = po_text[0:len(po_text) - 2]
        po_text += "\n"
    # 测试通过率
    po_text += "\n质量评估：测试通过率 [点击查看详情]" \
               "(http://117.50.36.141/#/home/result)"
    if len(coverage_rate) != 0:
        po_text += "\n>"
        for module in coverage_rate:
            po_text += " {}: `{:g}%` |".format(module['Module'], round(float(module.get('Passed Rate', 0)), 3) * 100)
        # 去掉最后一个"|"
        po_text = po_text[0:len(po_text) - 2]
        # po_text += "\n> 测试通过率：0-50% 可能出现比较严重问题" \
        #            "\n> 测试通过率：60-70% 可能出现功能性 bug" \
        #            "\n> 测试通过率：80-100% 可以正常发版\n"
    # 质量自动化建议传送门
    po_text += "\n\n---" \
               "\n[传送门：我有建议提给质量自动化]({})".format(ISSUE_GATEWAY)


# 构造消息推送体（QA）
def init_qa_push_payload():
    global qa_text
    # 消息头
    qa_text = text_head
    # 测试环境
    qa_text += test_env
    qa_text += '\n---' \
               '\n以下为脚本提交的问题:'
                # '\n以下为脚本提交的问题，请 QA 二次确认:'
    if len(defect_list) == 0:
        qa_text += '\n`N/A`'
    else:
        # 新增
        recur_n_s1s2 = []
        recur_n_s3 = []
        # 已存在
        recur_y_s1s2 = []
        recur_y_s3 = []
        # 再发生
        recur_d = []
        for defect_item in defect_list:
            # 判断新增、已存在、再发生
            if defect_item.get('Recur') == 'N':
                # 判断严重级
                if '1' in defect_item.get('Severity') or '2' in defect_item.get('Severity'):
                    recur_n_s1s2.append(defect_item.get('Bug ID'))
                elif '3' in defect_item.get('Severity'):
                    recur_n_s3.append(defect_item.get('Bug ID'))
            elif defect_item.get('Recur') == 'Y':
                if '1' in defect_item.get('Severity') or '2' in defect_item.get('Severity'):
                    recur_y_s1s2.append(defect_item.get('Bug ID'))
                elif '3' in defect_item.get('Severity'):
                    recur_y_s3.append(defect_item.get('Bug ID'))
            elif defect_item.get('Recur') == 'D':
                recur_d.append(defect_item.get('Bug ID'))
        qa_text += "\n`新增`：（新创建的 Bug）"
        qa_text += "\n> 没有新增 S1/S2 Bug" if len(recur_n_s1s2) == 0 else "\n> `发现 {} 个 S1/S2 Bug`, [传送门]({})" \
            .format(len(recur_n_s1s2), bugs_gateway(recur_n_s1s2))
        qa_text += "\n> 没有新增 S3 Bug" if len(recur_n_s3) == 0 else "\n> 发现 {} 个 S3 Bug, [传送门]({})" \
            .format(len(recur_n_s3), bugs_gateway(recur_n_s3))
        qa_text += "\n"
        qa_text += "\n`已存在`：（存在相同且未关闭的 Bug）"
        qa_text += "\n> 没有发现 S1/S2 Bug" if len(recur_y_s1s2) == 0 else "\n> `{} 个 S1/S2 Bug`, [传送门]({})" \
            .format(len(recur_y_s1s2), bugs_gateway(recur_y_s1s2))
        qa_text += "\n> 没有发现 S3 Bug" if len(recur_y_s3) == 0 else "\n> {} 个 S3 Bug, [传送门]({})" \
            .format(len(recur_y_s3), bugs_gateway(recur_y_s3))
        qa_text += "\n"
        qa_text += "\n`再发生`：（新创建，但已存在相同且关闭的 Bug）"
        qa_text += "\n> 没有发现关闭后又重现的 Bug" if len(recur_d) == 0 else "\n> `发现 {} 个已关闭又重现的 Bug`, [传送门]({})" \
            .format(len(recur_d), bugs_gateway(recur_d))
    # 质量自动化建议传送门
    qa_text += "\n\n---" \
               "\n[传送门：我有建议提给质量自动化]({})".format(ISSUE_GATEWAY)


# BUG 传送门
def bugs_gateway(bug_list):
    bug_list_string = ""
    for bug_id in bug_list:
        bug_list_string += bug_id
        bug_list_string += ","
    url_prefix = "http://cf-issue.i-mocca.com/bug-browse-{}.html?apiBugList=" \
        .format("9" if text_head.startswith("**`SP") else "14")
    return url_prefix + bug_list_string[: len(bug_list_string) - 1]


# 倍洽消息推送（PO）
def push_to_bearychat_po():
    # 设置 JSON 格式推送消息体
    push_payload = json.dumps({"text": po_text})
    header = {"Content-Type": "application/json"}
    requests.post(PO_PUSH_WEB_HOOK, data=push_payload, headers=header)


# 倍洽消息推送（QA）
def push_to_bearychat_qa():
    # 设置 JSON 格式推送消息体
    push_payload = json.dumps({"text": qa_text})
    header = {"Content-Type": "application/json"}
    requests.post(QA_PUSH_WEB_HOOK, data=push_payload, headers=header)


# 保存测试结果至数据库
def save_to_database():
    sql_host = mysql_config.host
    sql_user = mysql_config.user
    sql_password = mysql_config.passwd
    sql_database = mysql_config.database
    sql_port = mysql_config.port
    # 打开数据库连接
    db = pymysql.connect(sql_host, sql_user, sql_password,
                         sql_database,sql_port, connect_timeout=60)
    print('数据库连接成功')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 执行 sql 语句
        save_bp_data(cursor)
        save_bug_detail(cursor)
        save_rate_data(cursor)
        save_env_detail(cursor)
        save_flow_consum(cursor)
        save_mem_consum(cursor)
        # 提交修改
        db.commit()
        # 保存完成，推送至 BC
        push_text = "SP Android 数据存储完成。"
        print(push_text)
        push_payload = json.dumps({"text": push_text})
        header = {"Content-Type": "application/json"}
        requests.post(DATABASE_PUSH_WEB_HOOK, data=push_payload, headers=header)
    except Exception:
        # 输出异常信息
        info = sys.exc_info()
        exception_text = info[0], ":", info[1]
        print(exception_text)
        # 保存失败，推送至 BC
        push_text = "SP Android 数据存储失败。\n{}".format(exception_text)
        print(push_text)
        push_payload = json.dumps({"text": push_text})
        header = {"Content-Type": "application/json"}
        requests.post(DATABASE_PUSH_WEB_HOOK, data=push_payload, headers=header)
        # 发生错误时回滚
        db.rollback()
    db.close()


# 测试覆盖率、测试通过率的统计信息
def save_rate_data(cursor):
    for module in coverage_rate:
        # SQL 插入语句
        sql = "INSERT INTO rate_data(pkg, platform, testrun_id, module, coverage, passed)" \
              "VALUES ('%s', '%s', '%s', '%s', %f, %f)" % \
              (testing_env_info.get('Testing.Environment'),
               testing_env_info.get('Platform'),
               testing_duration.get('TestRun ID'),
               module.get('Module'),
               round(float(module.get('Coverage Rate', 0)), 3),
               round(float(module.get('Passed Rate', 0)), 3)
               )
        cursor.execute(sql)


# 测试数据发现的 BUG
def save_bug_detail(cursor):
    # Bug 序号
    count = 1
    for bug in defect_list:
        sql = "INSERT INTO bug_detail(pkg, platform, testrun_id, bug_id, module, title, severity, url, recur," \
              "exst_closed_bug, create_time)" \
              "VALUES ('%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s')" % \
              (testing_env_info.get('Testing.Environment'),
               testing_env_info.get('Platform'),
               testing_duration.get('TestRun ID'),
               bug.get('Bug ID'),
               bug.get('Module'),
               bug.get('Title'),
               bug.get('Severity'),
               bug.get('Defect Link'),
               bug.get('Recur'),
               bug.get('xBug ID'),
               bug.get('DateTime'))
        # 将 Bug 添加至 ShowDoc 内容中
        add_showdoc_bug(seq=count, module=bug.get('Module'), bug_title=bug.get('Title'),
                        bug_link=bug.get('Defect Link'),
                        severity=bug.get('Severity'))
        count += 1
        cursor.execute(sql)


# 测试覆盖详情、测试通过详情
def save_bp_data(cursor):
    testing_environment = testing_env_info.get('Testing.Environment')
    product = 'Unknown'
    if testing_environment[:testing_environment.rfind('.')].endswith('sunpeople'):
        product = 'SP'
    elif testing_environment[:testing_environment.rfind('.')].endswith('teammember'):
        product = 'TMC'
    bp_results_list = json.load(open('./allure-report/html/data/{}_BP_results.json'.format(product), encoding='utf-8'))
    for result in bp_results_list:
        sql = "INSERT INTO bp_data(pkg, platform, testrun_id, level_1, level_2, level_3, level_4, level_5," \
              "covered, results, EP)" \
              "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %d)" % \
              (testing_env_info.get('Testing.Environment'),
               testing_env_info.get('Platform'),
               testing_duration.get('TestRun ID'),
               result.get('1'),
               result.get('2'),
               result.get('3'),
               result.get('4'),
               result.get('5'),
               result.get('Covered'),
               result.get('Results'),
               round(float(result.get('Weight'))) if result.get('Weight') != '' else 0)
        cursor.execute(sql)


# 存储环境信息详情
def save_env_detail(cursor):
    if len(git_info) == 0:  # 防止 gitinfo 为空是，无法存入其它数据
        sql = "INSERT INTO testrun_info(testrun_id,start_time,end_time,pkg,platform,device," \
              "os_ver,pkg_ver) " \
              " VALUES('%s', '%s', '%s', '%s', '%s', '%s','%s','%s'); " % \
              (testing_duration.get('TestRun ID'),
               testing_duration.get('Start Time'),
               testing_duration.get('End Time'),
               testing_env_info.get('Testing.Environment'),
               testing_env_info.get('Platform'),
               testing_env_info.get('Device.Model'),
               testing_env_info.get('Platform.Version'),
               testing_env_info.get('App.Version')
               )
    else:
        for git_info_item in git_info:
            sql = "INSERT INTO testrun_info(testrun_id,start_time,end_time,pkg,platform,device," \
                  "os_ver,pkg_ver,submitter,branch,commit_info) " \
                  " VALUES('%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s','%s','%s'); " % \
                  (testing_duration.get('TestRun ID'),
                   testing_duration.get('Start Time'),
                   testing_duration.get('End Time'),
                   testing_env_info.get('Testing.Environment'),
                   testing_env_info.get('Platform'),
                   testing_env_info.get('Device.Model'),
                   testing_env_info.get('Platform.Version'),
                   testing_env_info.get('App.Version'),
                   git_info_item.get('name'),
                   git_info_item.get('branch'),
                   git_info_item.get('commit').replace("'", "''")
                   )
    cursor.execute(sql)


# 存储内存消耗监测数据
def save_mem_consum(cursor):
    app_monitor_data_file_path = './AppMonitorinData'
    for root, dirs, files in os.walk(app_monitor_data_file_path, topdown=False):
        for name in files:
            file = os.path.join(app_monitor_data_file_path, name)
            if file.endswith('.csv'):
                print(file)
                with open(file, 'r', encoding="utf-8") as f:
                    reader = csv.reader(f)
                    fieldnames = next(reader)
                    csv_reader = csv.DictReader(f, fieldnames=fieldnames)
                    for row in csv_reader:
                        print(row)
                        sql = "INSERT INTO mem_consum(testrun_id, pkg, platform, total, native," \
                              "dalvik, sampling_time)" \
                              "VALUES('%s', '%s', '%s', %d, %d, %d, '%s');" % \
                              (testing_duration.get('TestRun ID'),
                               testing_env_info.get('Testing.Environment'),
                               testing_env_info.get('Platform'),
                               int(row.get('total')),
                               int(row.get('native')),
                               int(row.get('dalvik')),
                               row.get('Sampling Time'))
                        cursor.execute(sql)
                os.remove(file)


# 存储流量消耗监测数据
def save_flow_consum(cursor):
    monitor_flow_data_file_path = './MonitorFlowData'
    for root, dirs, files in os.walk(monitor_flow_data_file_path, topdown=False):
        for name in files:
            file = os.path.join(monitor_flow_data_file_path, name)
            if file.endswith('.csv'):
                print(file)
                with open(file, 'r', encoding="utf-8") as f:
                    reader = csv.reader(f)
                    fieldnames = next(reader)
                    csv_reader = csv.DictReader(f, fieldnames=fieldnames)
                    for row in csv_reader:
                        print(row)
                        sql = "INSERT INTO flow_consum(testrun_id, pkg, platform, total, upload," \
                              "download, sampling_time, seq)" \
                              "VALUES('%s', '%s', '%s', %d, %d, %d, '%s', %d);" % \
                              (testing_duration.get('TestRun ID'),
                               testing_env_info.get('Testing.Environment'),
                               testing_env_info.get('Platform'),
                               int(row.get('Total')),
                               int(row.get('Upload_flow')),
                               int(row.get('Download_flow')),
                               row.get('Sampling Time'),
                               int(row.get('Test Run')))
                        cursor.execute(sql)
                os.remove(file)


# 向 ShowDoc 中添加 Bug
def add_showdoc_bug(seq, module, bug_title, bug_link, severity):
    global page_content_text_of_bug
    if seq != '' and module != '' and bug_title != '' and bug_link != '' and severity != '':
        severity_description = '严重 Bug'
        if '4' in severity:
            severity_description = '轻度 Bug'
        elif '3' in severity:
            severity_description = '中度 Bug'
        page_content_text_of_bug += '\n| {} | {} | [{}]({}) | {} |'.format(seq, module, bug_title, bug_link,
                                                                           severity_description)


# 保存 ShowDoc 页面
def save_showdoc_page():
    global page_content_text, page_content_text_of_bug
    # 登录请求参数
    login_param = {'username': 'yuheng.tian@cityfruit.io', 'password': '48551TYH', 'v_code': ''}
    # ShowDoc 请求所需的 cookies
    cookies = {'think_language': 'zh-CN', 'PHPSESSID': '73f43702596416d484e2cdaab9cbe9d1'}
    # 保存页面请求参数
    save_page_param = {'page_id': '780', 'item_id': '27', 's_number': '99', 'page_title': 'SP Android',
                       'page_content': '', 'cat_id': '172'}
    # 登录 ShowDoc
    login_response = requests.post(url='http://106.75.105.142:5555/server/index.php?s=/api/user/login',
                                   cookies=cookies, data=login_param)
    if login_response.status_code == 200:
        # 获取 Cookie 并保存
        set_cookie = login_response.headers.get('Set-Cookie')
        cookie_token = set_cookie[:set_cookie.index(';')]
        cookies.update({'cookie_token': cookie_token[cookie_token.index('=') + 1:]})
        print('登陆成功')
        # 文档末尾添加时间
        print(page_content_text_of_bug)
        if page_content_text_of_bug == '':
            page_content_text_of_bug = '\n| 無 Bug，可發佈 | | | | |'
        page_content_text += page_content_text_of_bug
        page_content_text += '\n{}'.format(time.strftime('%Y年%m月%d日 %H:%M:%S', time.localtime(time.time())))
        save_page_param.update({'page_content': page_content_text})
        # 更新 ShowDoc
        save_response = requests.post(url='http://106.75.105.142:5555/server/index.php?s=/api/page/save',
                                      cookies=cookies, data=save_page_param)
        if save_response.status_code == 200:
            print('写入成功')
        else:
            print('写入失败\n%s' % save_response.text)
            # 写入失败，向 BC 发送一条提醒
            requests.post(url='https://hook.bearychat.com/=bwD9B/incoming/2d3ea8776cc6bf0a2d5f08c2b5e40ebc',
                          data=json.dumps({"text": 'Showdoc 寫入異常，請檢查！'}),
                          headers={"Content-Type": "application/json"})
    else:
        print('登陆失败\n%s' % login_response.text)
        # 写入失败，向 BC 发送一条提醒
        requests.post(url='https://hook.bearychat.com/=bwD9B/incoming/2d3ea8776cc6bf0a2d5f08c2b5e40ebc',
                      data=json.dumps({"text": '登錄 Showdoc 異常，請檢查！'}),
                      headers={"Content-Type": "application/json"})


if __name__ == '__main__':
    # 读取 JSON 文件
    load_jsons()
    print_dicts()
    # 构造推送消息体（PO）
    # init_po_push_payload()
    # # 构造推送消息体（QA）
    # init_qa_push_payload()
    # # 倍洽消息推送（PO）
    # push_to_bearychat_po()
    # # 倍洽消息推送（QA）
    # push_to_bearychat_qa()
    # # 保存至数据库
    save_to_database()
    # 保存至 ShowDoc
    save_showdoc_page()
    # print('\n---------------------------')
    print(po_text)
    # print('\n---------------------------')
    # print(qa_text)
    # # 总耗时
    # print('\n---------------------------')
    # print('总耗时：%s s' % (time.time() - start_time_stamp))
