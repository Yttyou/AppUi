import requests
import json
import time
import base64
import pandas as pd
import pymysql
import sys
import yaml
import os, logging
from Common import logger


from Common.produce_id_dict import product_dict, Neptune_tab_id, Neptune_bug_sev
from Common.path_config import testfiles_path, caps_path
from Common.mysql_config import *
from TestFiles import git_handle
from Common.read_Iphone_config import ReadIphoneConfig


class WriteToMysql:
    def __init__(self):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset
        self.db = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                  passwd=self.passwd, db=self.database, charset=self.charset)
        self.cursor = self.db.cursor()

    def ExcQuery(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def ExcUpdate(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print("数据库更新成功!")
        except:
            print("数据库更新失败!")
            print(sys.exc_info())

    def ExcUpdateMany(self, sql,val):
        try:
            self.cursor.executemany(sql,val)
            self.db.commit()
            print("数据库更新成功!")
        except:
            print("数据库更新失败!")
            print(sys.exc_info())


    def __del__(self):
        self.db.close()
        print("数据库已关闭!")


class Commit_Bug_ZenTaoAPI(object):

    def __init__(self):
        # 正式环境地址
        # self.url = "http://cf-issue.i-mocca.com"
        # self.login_url = "http://cf-issue.i-mocca.com/user-login.json"
        # self.add_bug_url = "http://cf-issue.i-mocca.com/bug-create-{}.json".format(
        #     str(product_dict['SP']))
        # self.logout_url = "http://cf-issue.i-mocca.com/user-logout.json"

        # 测试环境地址
        self.url = "http://zentao.prosuntech.com"
        self.login_url = "http://zentao.prosuntech.com/user-login.json"
        self.add_bug_url = "http://zentao.prosuntech.com/bug-create-{}.json".format(
            str(product_dict['NeptunePlatform']))
        self.logout_url = "http://zentao.prosuntech.com/user-logout.json"


        self.login_headers = {'Content-Type': "application/x-www-form-urlencoded"}
        self.add_bug_headers = {'Content-Type': "application/x-www-form-urlencoded; charset=utf-8"}
        self.data = {"account": zentao_user, "password": zentao_passwd}
        self.session = requests.session()

    def login(self):
        response = self.session.post(self.login_url, headers=self.login_headers, data=self.data)
        if json.loads(response.content.decode('unicode_escape'))['status'] == "success":
            return True
        raise Exception("禪道登錄失敗!!!")

    def logout(self):
        response = self.session.post(self.logout_url, headers=self.login_headers, data=self.data)
        print(response.content.decode('unicode_escape'))
        if json.loads(response.content.decode('unicode_escape'))['status'] == "success":
            return True
        raise Exception("禪道登出失敗!!!")

    def img_to_base(self, img_path):
        with open(img_path, "rb") as f:
            data0 = f.read()
            return str(base64.b64encode(data0), 'utf-8')

    def add_bug_tozentao(self, bug_detail):
        """
        :param bug_detail:
        :return:  buglink-bug地址，duplicateFlag-判断BUG是否重复，xbugID-重复BUGid
        """
        # 提交BUG至禪道
        self.login()
        response = self.session.post(self.add_bug_url, headers=self.add_bug_headers, data=bug_detail)
        print("bug提交後返回數據:", response.content.decode("unicode_escape"))
        response_msg = json.loads(response.content.decode("unicode_escape"))
        xbugID = ""
        if not response_msg.get("error_code"):
            duplicateFlag = "N"                    # N：代表bug新提交
            bugID = str(response_msg.get("bugID",None))

        if response_msg.get("error_code") == 303:
            duplicateFlag = "Y"                     # Y：代表bug已经存在，状态为"未关闭"
            bugID = str(response_msg["rebugId"])

        if response_msg.get("error_code") == 304:
            duplicateFlag = "D"                     # D：代表bug已经存在，状态为"已关闭"
            xbugID = str(response_msg["rebugId"])
            bugID = response_msg["bugID"]

        buglink = self.url + "/bug-view-{bugID}.html".format(bugID=bugID)
        self.logout()
        return [buglink, duplicateFlag, bugID, xbugID]

    # 通过apk包名判定分支
    def get_bug_openedBuild(self):
        # apk_name = ReadIphoneConfig.filename
        apk_name = ReadIphoneConfig().get_apk_name_path()[1]
        logging.info("APK 文件名称：｛｝".format(apk_name))
        if apk_name.find("pre_live") > 0 :
            openedBuild = 3         # 判定为pre_live分支包
        else:
            openedBuild = "trunk"   # 判定为主干包
        return openedBuild

    # bug提交
    def submit_bug(self, bug_title, case_step, par_severity, ownig_module, imgpath=None):
        BranchID = self.get_bug_openedBuild()
        t = time.asctime(time.localtime(time.time()))
        str_bug_detail = {
            # "product": product_dict['SP'],  # int   所属产品 * 必填
            "product": product_dict['TMC'],  # int   所属产品 * 必填
            "openedBuild": BranchID,  # int | trunk   影响版本 * 必填
            # "branch": "2",  # int    分支 / 平台
            "module": Neptune_tab_id[ownig_module],  # int    所属模块
            # "project": 22,  # int   所属项目
            "assignedTo": git_handle.get_commit_po_4_bug(),  # string 指派给
            # "deadline": "2019-12-12",  # date 截止日期    日期格式：YY - mm - dd，如：2019 - 01 - 01
            "type": "designdefect",
            # string   Bug类型   取值范围： | codeerror | interface | config | install | security | performance | standard | automation | designchange | newfeature | designdefect | trackthings | codeimprovement | others
            "os": "android",
            # string 操作系统 取值范围： | all | windows | win8 | win7 | vista | winxp | win2012 | win2008 | win2003 | win2000 | android | ios | wp8 | wp7 | symbian | linux | freebsd | osx | unix | others
            # "browser": "",
            # string    浏览器 取值范围： | all | ie | ie11 | ie10 | ie9 | ie8 | ie7 | ie6 | chrome | firefox | firefox4 | firefox3 | firefox2 | opera | oprea11 | oprea10 | opera9 | safari | maxthon | uc | other
            "color": "#0091FF",  # string  颜色格式：  # RGB，如：#3da7f5
            "severity": par_severity,  # int  严重程度    取值范围：1 | 2 | 3 | 4
            "pri": 3,  # int   优先级 取值范围：0 | 1 | 2 | 3 | 4
            # "mailto": "",  # string 抄送给 填写帐号，多个账号用','分隔。
            "keywords": "Neptune.AI",  # string   关键词
            "title": bug_title,  # string  Bug标题 * 必填
            "steps": case_step,  # string   重现步骤
        }
        add_bug_result = self.add_bug_tozentao(bug_detail=str_bug_detail)

        cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())             # 生成BUG的时间
        # df_bug_logged = {
        #     "DateTime": [cur_time],
        #     "Module": [ownig_module],
        #     "Severity": [par_severity],
        #     "Title": [bug_title],
        #     "Defect Link": [add_bug_result[0]],
        #     "Bug ID": [add_bug_result[2]],
        #     "Recur": [add_bug_result[1]],
        #     "xBug ID": [add_bug_result[3]],
        #     "img": [imgpath]
        # }
        #
        # # 提交數據寫入csv
        # csv_filepath = testfiles_path + "/bug_list.csv"
        # pd.DataFrame(df_bug_logged).to_csv(csv_filepath, index=False, mode='a', header=False)

        buglink = "<a href=" + add_bug_result[0] + " target='_blank'>點擊查看 Defect 詳情</a>"

        # 提交數據寫入數據庫
        write_to_mysql_msg = yaml.load(open(caps_path + "/bc_app_config.yaml"))

        pkg_msg = write_to_mysql_msg['appPackage']
        platform_msg = write_to_mysql_msg['platformName']
        testrun_id_msg = os.getenv('BUILD_NUMBER')
        bug_id_msg = str(add_bug_result[2])
        module_msg = ownig_module
        title_msg = bug_title
        severiity_msg = Neptune_bug_sev[str(par_severity)]
        url_msg = add_bug_result[0]
        recur_msg = add_bug_result[1]
        exst_closed_bug_msg = str(add_bug_result[2]) if add_bug_result[1] == "D" else ""
        create_time_msg = cur_time
        img_msg = self.img_to_base(imgpath) if imgpath else ''

        sql = 'INSERT INTO bug_detail(pkg, platform, testrun_id, bug_id, module, title, severity, url,recur, exst_closed_bug, create_time, img) ' \
              'VALUES ("%s", "%s", "%s", "%s", "%s", "%s","%s", "%s", "%s", "%s", "%s", "%s")' % \
              (pkg_msg, platform_msg, testrun_id_msg, bug_id_msg, module_msg, title_msg, severiity_msg, url_msg,
               recur_msg, exst_closed_bug_msg, create_time_msg, img_msg)
        WriteToMysql().ExcUpdate(sql=sql)
        logging.info("提交BUG成功！")
        return buglink
