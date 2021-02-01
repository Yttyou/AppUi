#通过禅道API接口，传入BUG单相应的参数

from Common import ZenTaoApiToMysql
import time, json
from TestFiles import git_handle
import requests

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
if __name__ == "__main__":
    print(git_handle.get_commit_dev('bjp_ftz'))
    # t = time.asctime(time.localtime(time.time()))
    # str_bug_detail = {
    #         "product": 24,  # int   所属产品 * 必填
    #         "openedBuild": 1,  # int | trunk   影响版本 * 必填
    #         # "branch": "2",  # int    分支 / 平台
    #         "module": 242,  # int    所属模块
    #         "project": 22,  # int   所属项目
    #         "assignedTo": "Neptune.AI",  # string 指派给
    #         # "deadline": "2019-12-12",  # date 截止日期    日期格式：YY - mm - dd，如：2019 - 01 - 01
    #         "type": "designdefect",
    #         # string   Bug类型   取值范围： | codeerror | interface | config | install | security | performance | standard | automation | designchange | newfeature | designdefect | trackthings | codeimprovement | others
    #         "os": "android",
    #         # string 操作系统 取值范围： | all | windows | win8 | win7 | vista | winxp | win2012 | win2008 | win2003 | win2000 | android | ios | wp8 | wp7 | symbian | linux | freebsd | osx | unix | others
    #         # "browser": "",
    #         # string    浏览器 取值范围： | all | ie | ie11 | ie10 | ie9 | ie8 | ie7 | ie6 | chrome | firefox | firefox4 | firefox3 | firefox2 | opera | oprea11 | oprea10 | opera9 | safari | maxthon | uc | other
    #         "color": "#0091FF",  # string  颜色格式：  # RGB，如：#3da7f5
    #         "severity": 2,  # int  严重程度    取值范围：1 | 2 | 3 | 4
    #         "pri": 3,  # int   优先级 取值范围：0 | 1 | 2 | 3 | 4
    #         # "mailto": "",  # string 抄送给 填写帐号，多个账号用','分隔。
    #         "keywords": "Neptune.AI",  # string   关键词
    #         "title": "Neptune Testing ",  # string  Bug标题 * 必填
    #         "steps": "Neptune Testing Scripts test"  # string   重现步骤
    #     }
    # bug = ZenTao.ZenTaoAPI()
    # bug.get_session()
    # bug.login()
    # print(bug.add_bug(str_bug_detail))
    # bug.logout()
    # print(ZenTaoBugApi.submit_bug("NeptuneScriptTest123","123","3","聊天"))
    # transjson('TestFiles/gitinfo.json', 'TestFiles/gitinfo.csv')
    transjson('TestFiles/roster.json', 'TestFiles/roster.csv')
    # headers = {"Content-Type": "application/json"}
    # BC_URL = 'https://hook.bearychat.com/=bwD9B/incoming/712c31e32db064f4c39dab549ac4a03e'
    # payload = "推送测试，请忽略"
    # requests.post(BC_URL, headers=headers, data=json.dumps({"text": payload}))
