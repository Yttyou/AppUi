from Common.ZenTaoApiToMysql import WriteToMysql, caps_path
from Common.get_to_pdf import GetPdf
from Common.path_config import allure_report_path, testfiles_path
import logging
import json
import yaml


def tuple_del_repeat(tuple_data):  # 元祖去重
    del_repeat_list = []
    for each in tuple_data:
        if each not in del_repeat_list:
            del_repeat_list.append(each)
    return del_repeat_list


def get_data(testrun_id):
    # --------获取前置条件信息----------------#
    write_to_mysql_msg = yaml.load(open(caps_path + "/bc_app_config.yaml"))
    pkg_msg = write_to_mysql_msg['appPackage']
    platform_msg = write_to_mysql_msg['platformName']
    # --------获取数据库中对应的BUG数据--------#
    bug_data = []
    sql_bug_detail = "SELECT module,title,url,severity FROM bug_detail WHERE testrun_id = '{}' and pkg = '{}' and platform = '{}' ORDER BY severity ASC;".format(
        testrun_id, pkg_msg, platform_msg)
    bug_list = WriteToMysql().ExcQuery(sql=sql_bug_detail)
    if not bug_list:
        return []
    # ---------处理成我们想要的数据列表（且去重）---------#
    bug_list_new = tuple_del_repeat(bug_list)  # bug去重，不影响排序
    for i in bug_list_new:
        bug_data.append(list(i))
    del_no_list = []  # 最终需要写入的数据列表
    for i in bug_data:
        if "" in i:
            continue
        del_no_list.append(i)
    for m, i in enumerate(del_no_list):
        i.insert(0, int(m) + 1)
        # i.pop(-2) #删除 URL
        if i[-1] == "S4-优化建议":
            i[-1] = '輕度Bug'
        if i[-1] == "S3-功能有瑕疵":
            i[-1] = '中度Bug'
        if i[-1] == "S2-功能有問題":
            i[-1] = '嚴重Bug'
        if i[-1] == "S1-功能不可用":
            i[-1] = '嚴重Bug'
    del_no_list.insert(0, ['序號', '模塊', '標題', '嚴重程度'])
    return del_no_list


def get_pdf_file():
    # 获取testrun_id
    testrun_idpath = allure_report_path + '/html/data/duration.json'
    with open(testrun_idpath, 'r') as load_r:
        load_list = json.load(load_r)
        testrun_id = load_list[0]['TestRun ID']
    write_to_mysql_msg = yaml.load(open(caps_path + "/bc_app_config.yaml"))
    pkg_msg = write_to_mysql_msg['appPackage']
    platform_msg = write_to_mysql_msg['platformName']
    pkg_list = (pkg_msg, platform_msg)
    if pkg_list == ('com.suncity.sunpeople.qa', 'Android'):
        filename = 'SP-Android-QA-#{}.pdf'.format(testrun_id)

    elif pkg_list == ('com.suncity.sunpeople.uat', 'Android'):
        filename = 'SP-Android-UAT-#{}.pdf'.format(testrun_id)

    elif pkg_list == ('com.suncity.sunpeople.qa', 'iOS'):
        filename = 'SP-iOS-QA-#{}.pdf'.format(testrun_id)

    elif pkg_list == ('com.suncity.sunpeople.uat', 'iOS'):
        filename = 'SP-iOS-UAT-#{}.pdf'.format(testrun_id)

    else:
        raise Exception("bc_app_config.yaml存在不正確的包名或設備名")

    filenames = testfiles_path + '/' + filename
    data = get_data(testrun_id)
    if len(data) <= 1:
        print("該testrun_id下無bug數據")
        return "PASS"
    try:
        GetPdf(filename=filenames, data=data)
        print("PDF写入成功！！！")
        return ["OK", filename]
    except:
        print("PDF写入失败！！！")
        return "Error"