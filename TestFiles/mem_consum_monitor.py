import pymysql
import requests
import json
from TestFiles import git_handle

# bc地址
# BC_URL = 'https://hook.bearychat.com/=bwD9B/incoming/2d3ea8776cc6bf0a2d5f08c2b5e40ebc'  # 推送测试入口
BC_URL = 'https://hook.bearychat.com/=bwD9B/incoming/08476883bd3078de7fa08aa5c04b2bf9'  # 推送到 SP-Android

# 打开数据库连接
DB = pymysql.connect(host='106.75.22.108',
                     port=30061,
                     user='neptune',
                     password='L.hJMU3Px@GaL@aR',
                     database='Neptune',
                     charset='utf8')

# 默认pkg
PKG = 'com.suncity.sunpeople.qa'

# 默认platform
PLATFORM = 'Android'


# 处理建议
def get_handel_info(status, ratio):
    if status == 0:
        # return f"当前均值比对历史均值向上波动 {ratio}%, 内存消耗正常"
        return f"当前均值比对历史均值向上波动 {ratio}%"
    elif status == 1:
        # return f"当前均值比对历史均值向上波动 {ratio}%，请关注并进行优化处理"
        return f"当前均值比对历史均值向上波动 {ratio}%"
    elif status == 2:
        # return f"当前均值比对历史均值向上波动 {ratio}%，请 Dev 及时处理"
        return f"当前均值比对历史均值向上波动 {ratio}%"
    else:
        # return f"当前均值比对历史均值下降 {ratio}%，内存消耗正常"
        return f"当前均值比对历史均值下降 {ratio}%"


def notify_bc(url, flow_data):

    headers = {"Content-Type": "application/json"}
    issue_gate = 'http://cityfruit-doc.i-mocca.com/web/#/27?page_id=732'
    payload = flow_data + f"\n[传送门：我有建议提给质量自动化]({issue_gate})"
    requests.post(url, headers=headers, data=json.dumps({"text": payload}))
    return


def get_flow_data():
    # 使用cursor()方法获取操作游标
    cursor = DB.cursor(cursor=pymysql.cursors.DictCursor)

    # 获取最大的testrun_id
    # sql_max_id = "select max(testrun_id) from mem_consum where platform =%s and pkg =%s ; "
    sql_max_id = "select max(CONVERT(testrun_id,SIGNED)) as testrun_id from mem_consum where platform =%s and pkg =%s ;"


    # 拼接并执行sql语句
    cursor.execute(sql_max_id, [PLATFORM, PKG])

    # 取到testrun_id查询结果
    max_test_id = cursor.fetchone()['testrun_id']
    # print('max_test_id', type(max_test_id))

    # 看是否需要推送报告
    sql_need_report = "select * from mem_consum \
                      where platform =%s and pkg =%s and testrun_id =%s and status = 'Y'; "
    cursor.execute(sql_need_report, [PLATFORM, PKG, max_test_id])
    need_report = cursor.fetchall()
    print(need_report)
    # 如果是None就退出
    if not need_report:
        return 'N/A'

    # 初始值
    c_max_total = 0
    c_max_native = 0
    c_max_dalvik = 0
    c_mean_total = 0
    c_mean_native = 0
    c_mean_dalvik = 0

    h_max_total = 0
    h_max_native = 0
    h_max_dalvik = 0
    h_mean_total = 0
    h_mean_native = 0
    h_mean_dalvik = 0

    # 当前消耗峰值：即为当期一轮监测数据中status=Y 的最大total, native, dalvik值
    sql_current_max = "select max(total) as maxtotal, max(native) as maxnative, max(dalvik) as maxdalvik from mem_consum " \
                      "where platform =%s and pkg =%s and testrun_id =%s and status = 'Y' ; "
    sql_current_avg = "select avg(total) as avgtotal, avg(native) as avgnative, avg(dalvik) as avgdalvik from mem_consum " \
                      "where platform =%s and pkg =%s and testrun_id =%s and status = 'Y' ; "

    cursor.execute(sql_current_max, [PLATFORM, PKG, max_test_id])
    max_total = cursor.fetchone()
    # print('current_max', max_total)

    # 避免查询结果是None
    if max_total['maxtotal']:
        c_max_total = max_total['maxtotal']
    if max_total['maxnative']:
        c_max_native = max_total['maxnative']
    if max_total['maxdalvik']:
        c_max_dalvik= max_total['maxdalvik']

    # 如果峰值是零，就不用再查询均值了
    if c_max_total != 0:
        cursor.execute(sql_current_avg, [PLATFORM, PKG, max_test_id])
        avg_total = cursor.fetchone()
        # print('current_avg', avg_total)
        c_mean_total = round(avg_total['avgtotal'])
        c_mean_native = round(avg_total['avgnative'])
        c_mean_dalvik = round(avg_total['avgdalvik'])
        # print(c_max_total)

    # 历史峰值
    sql_history_max = "select max(total) as maxtotal, max(native) as maxnative, max(dalvik) as maxdalvik from mem_consum " \
                      "where platform =%s and pkg =%s and testrun_id != %s and status = 'Y' ; "
    sql_history_avg = "select avg(total) as avgtotal, avg(native) as avgnative, avg(dalvik) as avgdalvik from mem_consum " \
                      "where platform =%s and pkg =%s and testrun_id != %s and status = 'Y' ; "

    cursor.execute(sql_history_max, [PLATFORM, PKG, max_test_id])
    max_total = cursor.fetchone()
    # print('history_max', max_total)

    # 避免查询结果是None
    if max_total['maxtotal']:
        h_max_total = max_total['maxtotal']
    if max_total['maxnative']:
        h_max_native = max_total['maxnative']
    if max_total['maxdalvik']:
        h_max_dalvik = max_total['maxdalvik']

    # 历史均值，先判断历史峰值，如果是零
    if h_max_total != 0:
        cursor.execute(sql_history_avg, [PLATFORM, PKG, max_test_id])
        avg_total = cursor.fetchone()
        # print('history_avg', avg_total)
        h_mean_total = round(avg_total['avgtotal'])
        h_mean_native = round(avg_total['avgnative'])
        h_mean_dalvik = round(avg_total['avgdalvik'])
        # print(h_max_total)

    # 获取提交信息
    sql_info = "select * from testrun_info where pkg =%s and platform =%s and testrun_id =%s; "
    cursor.execute(sql_info, [PKG, PLATFORM, max_test_id])
    infos = cursor.fetchall()

    text = "**`SP-Android-QA 包` `内存消耗`分析报告**"
    text_env = "\n 未获取到分支和测试环境信息"
    for info in infos:
        submitter = "提交人：" + f"`{git_handle.get_commit_dev(info['submitter'])}`"  # 提交人
        branch = "分支：" + f"`{info['branch']}`"  # 分支
        commit_info = "提交信息：" + f"`{info['commit_info']}`"  # 提交信息
        device = "设备型号：" + f"`{info['device']}`"  # 设备型号
        os_ver = "系統版本：" + f"`{info['os_ver']}`"  # 系統版本
        pkg_ver = "软件版本：" + f"`{info['pkg_ver']}`"  # 软件版本
        # 获取最后一个提交信息
        if info['submitter'] is None:
            text_env = "\n" + "-----" + "\n未获取到分支提交信息" + "\n" + device + " | " + os_ver + " | " + pkg_ver
        else:
            text_env = "\n" + "-----" + "\n" + submitter + " | " + branch + "\n" + commit_info + "\n" + device + " | " \
                    + os_ver + " | " + pkg_ver

    text = text + text_env
    text = text + "\n" + "-----" + "\n"
    text = text + "`Total:`" + " \n" + f" > 当前峰值：{c_max_total} kb | 历史峰值：{h_max_total} kb \n > 当前均值：{c_mean_total} kb | 历史均值：{h_mean_total} kb \n"
    text = text + "\n `Native:`" + " \n" + f" > 当前峰值：{c_max_native} kb | 历史峰值：{h_max_native} kb \n > 当前均值：{c_mean_native} kb | 历史均值：{h_mean_native} kb \n"
    text = text + "\n `Dalvik:`" + "\n" + f" > 当前峰值：{c_max_dalvik} kb | 历史峰值：{h_max_dalvik} kb \n > 当前均值：{c_mean_dalvik} kb | 历史均值：{h_mean_dalvik} kb \n"

    # ratio = round(100 * (c_max_total - h_mean_total) / h_mean_total, 2)
    ratio = round(100 * (c_mean_total - h_mean_total) / h_mean_total, 2)


    status = 3
    if ratio > 20:
        status = 2
    elif 10 < ratio <= 20:
        status = 1
    elif 0 < ratio <= 10:
        status = 0
    if ratio < 0:
        ratio = - ratio
    handle_info = get_handel_info(status, ratio)
    text = text + "\n" + "-----\n" + "分析评估：\n" + f" > {handle_info} \n \
        >> 10% 以内为正常\n \
        >> 10% ~ 20% 建议优化\n \
        >> 大于 20% 立刻处理\n \
        \n-----"
    # print(text)
    if status == 2:
        sql_update = "update mem_consum set status = 'N' where platform =%s and pkg =%s and testrun_id =%s ;"
        cursor.execute(sql_update, [PLATFORM, PKG, max_test_id])
        DB.commit()
    DB.close()
    return text


def run():
    # 内存监控推送
    mem_info = get_flow_data()
    # if mem_info != 'N/A':
    #     notify_bc(BC_URL, mem_info)

if __name__ == '__main__':
    run()






