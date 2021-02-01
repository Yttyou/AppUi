import pandas as pd
# import pytest
import re
import json
import time
import os, zipfile, shutil
import datetime


# 根據腳本名稱返回對應的模塊名稱
def script2module(script_name):
    if script_name == "test_chat":
        module_name = "聊天"
    elif script_name == "test_search":
        module_name = "最新動態"
    else:
        module_name = ""
    return module_name


def scritp2modulepath(test_suit, test_class):
    module_name = script2module(test_suit)
    if module_name == "聊天":
        if test_class == "TestAddConversation":
            module_path = "聊天/訊息/新增"
        elif test_class == "TestArchiveList":
            module_path = "聊天/訊息/聊天/個人"
        elif test_class == "TestBookllexpend":
            module_path = "聊天/通訊錄"
        elif test_class == "TestBookSearch":
            module_path = "聊天/通訊錄"
        elif test_class == "TestChatMore":
            module_path = "聊天/更多"
        elif test_class == "TestInputDiverse":
            module_path = "聊天/訊息/聊天/個人"
        elif test_class == "TestNewGroup":
            module_path = "聊天/訊息/新增"
        elif test_class == "TestPeopleList":
            module_path = "聊天/通訊錄/人員列表"
        elif test_class == "TestSort":
            module_path = "聊天/訊息/搜索"
        elif test_class == "TestPersonalChat":
            module_path = "聊天/訊息/聊天/個人"
        elif test_class == "TestPersonalChatMore":
            module_path = "聊天/訊息/聊天/個人"
        elif test_class == "TestGroupChat":
            module_path = "聊天/訊息/聊天/群組"
        else:
            module_path = ""
    elif module_name == "最新動態":
        if test_class == "TestPostsList":
            module_path = "最新動態/全部"
        elif test_class == "TestSort":
            module_path = "最新動態/搜索"
        else:
            module_path = ""
    else:
        module_path = ""

    return module_path


# @pytest.mark.caldata
def category_cal(testrunid):
    df = pd.DataFrame(pd.read_csv(r'allure-report/html/data/suites.csv', encoding='utf-8', keep_default_na=False))
    total = df['Status'].count()
    # print(total)
    passed = df[df.Status == 'passed']['Status'].count()
    failed = df[df.Status == 'failed']['Status'].count()
    error = df[df.Status == 'broken']['Status'].count()

    passrate = passed / total
    failrate = failed / total
    errorate = error / total

    data = {'Type': ['Passed', 'Failed', 'Error'], 'QTY': [passed, failed, error], 'Total': [total, total, total],
            'Rate': [passrate, failrate, errorate]}

    # # 根据 Jenkins 构建的 ID 作为 Test Run ID
    # job_path = "/Users/cf/.jenkins/jobs/Android-SP-QA-Neptune-Run-Auto/builds"
    # files = os.listdir(job_path)
    # files = sorted(files, key=lambda x: os.path.getctime(os.path.join(job_path, x)))
    # # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
    # # os.path.getmtime() 函数是获取文件最后修改时间
    # # os.path.getctime() 函数是获取文件最后创建时间
    # for file in files:
    #     if os.path.isdir(job_path + "/" + file):
    #         testRunID = file

    starttime = time.strptime(df['Start Time'].min(), "%a %b %d %H:%M:%S %Z %Y")
    endtime = time.strptime(df['Stop Time'].max(), "%a %b %d %H:%M:%S %Z %Y")
    starttime = time.strftime("%Y-%m-%d %H:%M:%S", starttime)
    endtime = time.strftime("%Y-%m-%d %H:%M:%S", endtime)
    duration = {'TestRun ID': [testrunid], 'Start Time': [starttime], 'End Time': [endtime]}

    df_buglist = pd.DataFrame(pd.read_csv(r'TestFiles/bug_list.csv', encoding='utf-8'))
    df_buglist['DateTime'] = pd.to_datetime(df_buglist['DateTime'])
    df_buglist = df_buglist[df_buglist['DateTime'] > starttime]
    df_buglist = df_buglist[df_buglist['DateTime'] < endtime]

    # print(df_buglist)
    for index, row in df_buglist.iterrows():
        # print(df_buglist['Severity'][index])
        if df_buglist['Severity'][index] == 1:
            df_buglist['Severity'][index] = 'S1-功能不可用'
        elif df_buglist['Severity'][index] == 2:
            df_buglist['Severity'][index] = 'S2-功能有問題'
        elif df_buglist['Severity'][index] == 3:
            df_buglist['Severity'][index] = 'S3-功能有瑕疵'
        elif df_buglist['Severity'][index] == 4:
            df_buglist['Severity'][index] = 'S4-给PO優化建議'
        else:
            # df_buglist['Severity'][index] = 'Unknown'
            df_buglist['Severity'][index].set_value('Unknown')


    df_buglist = df_buglist.sort_values(by=['Module', 'Severity'])
    df_buglist.to_csv(r'allure-report/html/data/bug_list.csv', index=False)
    pd.DataFrame(data).to_csv(r'allure-report/html/data/bytype.csv', index=False)
    pd.DataFrame(duration).to_csv(r'allure-report/html/data/duration.csv', index=False)

    transjson('allure-report/html/data/bytype.json', 'allure-report/html/data/bytype.csv')
    transjson('allure-report/html/data/duration.json', 'allure-report/html/data/duration.csv')
    transjson('allure-report/html/data/bug_list.json', 'allure-report/html/data/bug_list.csv')


# @pytest.mark.caldata
def covered():
    df_base = pd.DataFrame(pd.read_csv(r'TestFiles/SP_BP.csv', encoding='utf-8'))
    df_data = pd.DataFrame(pd.read_csv(r'allure-report/html/data/suites.csv', encoding='utf-8', keep_default_na=False))
    df_data_passed = df_data[df_data['Status'] == 'passed']
    df_data_error = df_data[df_data['Status'] == 'broken']
    df_data_failed = df_data[df_data['Status'] == 'failed']

    # Passed 结果遍历
    # 按结果数据按行遍历以获取用例名字
    for index, row in df_data_passed.iterrows():
        key_search = re.split(':', df_data_passed['Name'][index])[0]
        key_module = script2module(df_data_passed['Suite'][index])
        key_module_path = re.split('/', scritp2modulepath(df_data_passed['Suite'][index],
                                                          df_data_passed['Sub Suite'][index]))

        # --- 修改增加 allure.parent_suite，allure.suite，allure.sub_suite 写法后的数据处理逻辑
        if key_module_path[0] == '':  # 如果没有获取到路径，则数组第一个值为空
            for i, ele in enumerate(['Parent Suite', 'Suite', 'Sub Suite']):
                if df_data_passed[ele][index] != "":
                    if i == 0:
                        key_module_path[0] = df_data_passed[ele][index]  # 把第一个空值替换为模块顶层名称
                    else:
                        key_module_path.append(df_data_passed[ele][index])  # 因为前面获取路径失败已经定型了数组长度，在此拓展

        path_len = len(key_module_path) + 1

        # 按blueprint文件的行和列变量来匹配测试覆盖到的用例名字
        for index_base, row_base in df_base.iterrows():
            i = 1
            condition = ""
            flag = True
            while i < path_len:
                condition = condition + "'" + str(i) + "'"
                if df_base[str(i)][index_base] != key_module_path[i - 1]:
                    flag = False
                i = i + 1
                if i != path_len:
                    condition = condition + ", "
            if flag:
                for columns, col in df_base.iteritems():
                    if columns not in condition:
                        if key_search == df_base[columns][index_base]:
                            df_base['Covered'][index_base] = 'Y'
                            df_base['Results'][index_base] = 'Passed'
            else:
                continue
    # Error 结果遍历
    # 按结果数据按行遍历以获取用例名字
    for index, row in df_data_error.iterrows():
        key_search = re.split(':', df_data_error['Name'][index])[0]
        key_module = script2module(df_data_error['Suite'][index])
        key_module_path = re.split('/', scritp2modulepath(df_data_error['Suite'][index],
                                                          df_data_error['Sub Suite'][index]))

        # --- 修改增加 allure.parent_suite，allure.suite，allure.sub_suite 写法后的数据处理逻辑
        if key_module_path[0] == '':  # 如果没有获取到路径，则数组第一个值为空
            for i, ele in enumerate(['Parent Suite', 'Suite', 'Sub Suite']):
                if df_data_error[ele][index] != '':
                    if i == 0:
                        key_module_path[0] = df_data_error[ele][index]  # 把第一个空值替换为模块顶层名称
                    else:
                        key_module_path.append(df_data_error[ele][index])  # 因为前面获取路径失败已经定型了数组长度，在此拓展

        path_len = len(key_module_path) + 1
        # 按blueprint文件的行和列变量来匹配测试覆盖到的用例名字
        for index_base, row_base in df_base.iterrows():
            i = 1
            condition = ""
            flag = True
            while i < path_len:
                condition = condition + "'" + str(i) + "'"
                if df_base[str(i)][index_base] != key_module_path[i - 1]:
                    flag = False
                i = i + 1
                if i != path_len:
                    condition = condition + ", "
            if flag:
                for columns, col in df_base.iteritems():
                    if columns not in condition:
                        if key_search == df_base[columns][index_base]:
                            df_base['Covered'][index_base] = 'Y'
                            df_base['Results'][index_base] = 'Error'
            else:
                continue

    # Failed 结果遍历
    # 按结果数据按行遍历以获取用例名字
    for index, row in df_data_failed.iterrows():
        key_search = re.split(':', df_data_failed['Name'][index])[0]
        key_module = script2module(df_data_failed['Suite'][index])
        key_module_path = re.split('/', scritp2modulepath(df_data_failed['Suite'][index],
                                                          df_data_failed['Sub Suite'][index]))

        # --- 修改增加 allure.parent_suite，allure.suite，allure.sub_suite 写法后的数据处理逻辑
        if key_module_path[0] == '':  # 如果没有获取到路径，则数组第一个值为空
            for i, ele in enumerate(['Parent Suite', 'Suite', 'Sub Suite']):
                if df_data_failed[ele][index] != "":
                    if i == 0:
                        key_module_path[0] = df_data_failed[ele][index]  # 把第一个空值替换为模块顶层名称
                    else:
                        key_module_path.append(df_data_failed[ele][index])  # 因为前面获取路径失败已经定型了数组长度，在此拓展

        path_len = len(key_module_path) + 1
        # 按blueprint文件的行和列变量来匹配测试覆盖到的用例名字
        for index_base, row_base in df_base.iterrows():
            i = 1
            condition = ""
            flag = True
            while i < path_len:
                condition = condition + "'" + str(i) + "'"
                if df_base[str(i)][index_base] != key_module_path[i - 1]:
                    flag = False
                i = i + 1
                if i != path_len:
                    condition = condition + ", "
            if flag:
                for columns, col in df_base.iteritems():
                    if columns not in condition:
                        if key_search == df_base[columns][index_base]:
                            df_base['Covered'][index_base] = 'Y'
                            df_base['Results'][index_base] = 'Failed'
            else:
                continue


    df_base.to_csv('allure-report/html/data/SP_BP_results.csv', index=False)
    transjson('allure-report/html/data/SP_BP_results.json', 'allure-report/html/data/SP_BP_results.csv')


# @pytest.mark.caldata
def rate_cal():
    df_cal = pd.DataFrame(pd.read_csv('allure-report/html/data/SP_BP_results.csv', encoding='utf-8'))
    # df_setting = df_cal[df_cal['1'] == '設定']
    df_ess = df_cal[df_cal['1'] == 'ESS員工自助']
    df_assist = df_cal[df_cal['1'] == '太陽助理']
    df_chat = df_cal[df_cal['1'] == '聊天']
    df_nf = df_cal[df_cal['1'] == '最新動態']
    df_crm = df_cal[df_cal['1'] == 'CRM']

    # total_setting = df_setting['1'].count()
    # covered_setting = list(df_setting['Covered']).count('Y')
    # passed_setting = list(df_setting['Results']).count('Passed')
    # error_setting = list(df_setting['Results']).count('Error')
    # failed_setting = list(df_setting['Results']).count('Failed')

    total_ess = df_ess['1'].count()
    covered_ess = list(df_ess['Covered']).count('Y')
    passed_ess = list(df_ess['Results']).count('Passed')
    error_ess = list(df_ess['Results']).count('Error')
    failed_ess = list(df_ess['Results']).count('Failed')

    total_assist = df_assist['1'].count()
    covered_assist = list(df_assist['Covered']).count('Y')
    passed_assist = list(df_assist['Results']).count('Passed')
    error_assist = list(df_assist['Results']).count('Error')
    failed_assist = list(df_assist['Results']).count('Failed')

    total_chat = df_chat['1'].count()
    total_chat_weight = df_chat['Weight'].sum()
    covered_chat_weight = df_chat[df_chat['Covered'] == 'Y']['Weight'].sum()
    # print('covered_chat_weight = %f' % covered_chat_weight)
    covered_chat = list(df_chat['Covered']).count('Y')
    passed_chat = list(df_chat['Results']).count('Passed')
    error_chat = list(df_chat['Results']).count('Error')
    failed_chat = list(df_chat['Results']).count('Failed')

    total_nf = df_nf['1'].count()
    covered_nf = list(df_nf['Covered']).count('Y')
    passed_nf = list(df_nf['Results']).count('Passed')
    error_nf = list(df_nf['Results']).count('Error')
    failed_nf = list(df_nf['Results']).count('Failed')

    total_crm = df_crm['1'].count()
    covered_crm = list(df_crm['Covered']).count('Y')
    passed_crm = list(df_crm['Results']).count('Passed')
    error_crm = list(df_crm['Results']).count('Error')
    failed_crm = list(df_crm['Results']).count('Failed')

    # data_rate = {'Module': ['ESS員工自助', '太陽助理', '聊天', '最新動態', '設定', 'CRM'],
    #              'Coverage Rate': [covered_ess / total_ess, covered_assist / total_assist, covered_chat_weight / total_chat_weight,
    #                                covered_nf / total_nf, covered_setting / total_setting, covered_crm / total_crm],
    #              'Passed Rate': [safe_div(passed_ess, (passed_ess + error_ess + failed_ess)),
    #                              safe_div(passed_assist, (passed_assist + error_assist + failed_assist)),
    #                              safe_div(passed_chat, (passed_chat + error_chat + failed_chat)),
    #                              safe_div(passed_nf, (passed_nf + error_nf + failed_nf)),
    #                              safe_div(passed_setting, (passed_setting + error_setting + failed_setting)),
    #                              safe_div(passed_crm, (passed_crm + error_crm + failed_crm))]}
    data_rate = {'Module': ['ESS員工自助', '太陽助理', '聊天', '最新動態', 'CRM'],
                 'Coverage Rate': [covered_ess / total_ess, covered_assist / total_assist,
                                   covered_chat_weight / total_chat_weight,
                                   covered_nf / total_nf, covered_crm / total_crm],
                 'Passed Rate': [safe_div(passed_ess, (passed_ess + error_ess + failed_ess)),
                                 safe_div(passed_assist, (passed_assist + error_assist + failed_assist)),
                                 safe_div(passed_chat, (passed_chat + error_chat + failed_chat)),
                                 safe_div(passed_nf, (passed_nf + error_nf + failed_nf)),
                                 safe_div(passed_crm, (passed_crm + error_crm + failed_crm))]}
    #  'Error Rate': [safe_div(error_ess, (passed_ess+error_ess+failed_ess)), safe_div(error_assist, (passed_assist+error_assist+failed_assist)), safe_div(error_chat, (passed_chat+error_chat+failed_chat)), safe_div(error_nf, (passed_nf+error_nf+failed_nf)),
    # safe_div(error_setting, (passed_setting+error_setting+failed_setting)), safe_div(error_crm, (passed_crm+error_crm+failed_crm))],
    #  'Failed Rate': [safe_div(failed_ess, (passed_ess+error_ess+failed_ess)), safe_div(failed_assist, (passed_assist+error_assist+failed_assist)), safe_div(failed_chat, (passed_chat+error_chat+failed_chat)), safe_div(failed_nf, (passed_nf+error_nf+failed_nf)),
    #  safe_div(failed_setting, (passed_setting+error_setting+failed_setting)), safe_div(failed_crm, (passed_crm+error_crm+failed_crm))]
    pd.DataFrame(data_rate).to_csv(r'allure-report/html/data/rate_data.csv', index=False)
    transjson('allure-report/html/data/rate_data.json', 'allure-report/html/data/rate_data.csv')


# @pytest.mark.caldata
def zip_reconstruct(testrunid):
    # 前置 1， 替换繁中侧边栏对应的js
    behi_path = 'TestFiles/behaviors/index.js'
    pkg_path = 'TestFiles/packages/index.js'
    rep_behi_path = 'allure-report/html/plugins/behaviors/index.js'
    rep_pkg_path = 'allure-report/html/plugins/packages/index.js'
    shutil.copy(behi_path, rep_behi_path)
    shutil.copy(pkg_path, rep_pkg_path)
    # 前置 2， 替换html下的index.html 和 css文件
    shutil.copy('TestFiles/html/index.html', 'allure-report/html/index.html')
    shutil.copy('TestFiles/html/styles.css', 'allure-report/html/styles.css')
    # 复制 git 代码提交信息,并将 csv 转成 json
    # transjson('allure-report/html/data/gitinfo.json','TestFiles/gitinfo.csv')
    shutil.copy('TestFiles/gitinfo.json','allure-report/html/data/gitinfo.json')
    # 前置 3，copy整个 plugins/forms文件夹
    if os.path.exists('allure-report/html/plugins/forms'):
        shutil.rmtree('allure-report/html/plugins/forms')
    shutil.copytree('TestFiles/plugins/forms', 'allure-report/html/plugins/forms')

    # 遍历jenkins job文件下的文件夹，获取最大文件夹的名字
    # 修改为传递 build number 的方式获得文件夹名 areo @ 20200312
    filename = str(testrunid)
    job_path = "/Users/cf/.jenkins/jobs/Android-SP-QA-Neptune-Run-Auto/builds"
    # files = os.listdir(job_path)
    # files = sorted(files, key=lambda x: os.path.getctime(os.path.join(job_path, x)))
    # # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
    # # os.path.getmtime() 函数是获取文件最后修改时间
    # # os.path.getctime() 函数是获取文件最后创建时间
    # for file in files:
    #     if os.path.isdir(job_path + "/" + file):
    #         filename = file
    # 删除builds文件夹下的alluire report的zip文件
    file_new = job_path + "/" + filename + "/archive/allure-report.zip"
    if os.path.isfile(file_new):
        print("delete")
        os.remove(file_new)
    # 重构allure-report.zip
    zipf = zipfile.ZipFile(file_new, 'w', zipfile.ZIP_DEFLATED)
    start_dir = 'allure-report'
    for dir_path, dir_names, file_names in os.walk(start_dir):
        f_path = dir_path.replace(start_dir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
        f_path = f_path and f_path + os.sep or ''  # 实现当前文件夹以及包含的所有文件的压缩
        for filename in file_names:
            zipf.write(os.path.join(dir_path, filename), f_path + filename)
    zipf.close()


# 删除超过3天的截图
def del_ss():
    ss_path = 'ScreenShot/'
    files = os.listdir(ss_path)
    crruent_time = datetime.datetime.now()
    for file in files:
        file_suffix = os.path.splitext(file)[1]
        if file_suffix == '.png':
            create_time = datetime.datetime.fromtimestamp(os.path.getctime(ss_path + file))
            gap_day = (crruent_time-create_time).days
            if gap_day > 3:        # 删除大于3天的截图
                os.remove(ss_path + file)
                print(file)

# file:csv to json
def transjson(jsonpath, csvpath):
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


def safe_div(x, y):
    if y == 0:
        return 0
    return x / y

# 读取 testrun id
def read_id():
    filepath = '/Users/cf/.jenkins/workspace/Android-SP-QA-Neptune-Run-Auto/testrunid.csv'
    # filepath = 'TestFiles/testrunid.csv'
    df = pd.DataFrame(pd.read_csv(filepath, encoding='utf-8'))
    return df['testrun_id'][0]
