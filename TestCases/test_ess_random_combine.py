__author__ = 'developer'

# 【員工自助】模块用例          #作者:金伟    时间:2020/04/08
import datetime
import os
import time
import pytest

from Common.path_config import base_path
from PageObjects.employee_tab_page import EmpTabPage as EMP
from PageObjects.accessIds_tab import *
import allure
import logging
import requests
import json
import random
from Common import bug_severity_config as bsc
from Common.ZenTaoApiToMysql import Commit_Bug_ZenTaoAPI as ZenTaoBugApi
from TestCases import test_chat

@allure.parent_suite("員工自助")
@allure.story("ESS員工自助:隨機接口自動化")
class TestEssRandomCombine:

    def send_request(self, *accessIds):
        url = "https://sp-api.i-mocca.com/adminpanel_api/api/rbac/add_role_access"
        headers = {"Cookie": "sunpeople_admin=AR6CNWVB1Osq7jXDwK1uOQ==",
                   "Content-Type": "application/json"}
        params = {"roleId": "=bw54g", "accessIds": str(",".join(accessIds))}
        logging.info("請求參數為:{}".format(str(params)))
        response = requests.post(url=url, params=params, headers=headers)
        msg = json.loads(response.text)
        time.sleep(2)
        logging.info("響應是:{}".format(msg))
        if msg.get("code") == "200" and msg.get('message') == "success":
            logging.info("接口請求成功")
            return [True, str(msg)]
        else:
            logging.error("接口請求失敗!!!!,原因:{}".format(msg))
            return [False, str(msg)]

    # 傳多個params參數
    def employee_request_test(self, startApp_withReset,case_name, *accessIds):
        emp = EMP(startApp_withReset)
        case_step = ''
        logging.info("********* 隨機接口自動化測試 *********")
        logging.info("參數列表為：{}".format(accessIds))
        suite_title_list = sorted(set((accessIds_title_dict[i] for i in accessIds)))  # 二級標題確定(去重)
        sub_title_list = sorted(set((accessIds_subtitle_dict[i] for i in accessIds)))  # 三級標題確定
        title = "員工自助/{}/{}".format("、".join(suite_title_list), "、".join(sub_title_list))
        test_chat.temp_num += 1
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        print("bug標題:{}".format(title))
        bug_title = "[Neptune.AI][{0}][{1}]接口測試失敗".format(emp.get_app_environment(), title)  # BUG标题
        logging.info("要檢查的二級標題元素已確定,依次為:{}".format("、".join(suite_title_list)))
        logging.info("要檢查的三級標題元素已確定,依次為:{}".format("、".join(sub_title_list)))
        msg_post = self.send_request(*accessIds)
        logging.info("響應為:{}".format(msg_post))
        if not msg_post[0]:
            with allure.step("隨機接口發送失敗,請求參數為:{},返回結果為:{}".format(accessIds, msg_post[1])):
                # 调用禅道api，报BUG单
                # 传入BUG标题，BUG复现步骤
                logging.error("隨機接口發送失敗,請求參數為:{},返回結果為:{}".format(accessIds, msg_post[1]))
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "ESS員工自助")
                with allure.step(bug_link):
                    raise Exception("接口請求失敗:{}".format(msg_post[1]))
        if msg_post[0]:
            case_step = ""
            logging.info("*********  點擊【員工自助】 *********")
            with allure.step("點擊【員工自助】"):
                time.sleep(1)
                case_step = case_step + "點擊【員工自助】"
                emp.click_employee_self_tab()
            with allure.step("檢查頁面是否只出現{}及{}:".format("、".join(suite_title_list), "、".join(sub_title_list))):
                case_step = case_step + "<br/>檢查頁面是否只出現{}及{}:".format("、".join(suite_title_list),
                                                                      "、".join(sub_title_list))

                emp.wait_loading_done()  # 加載文案
                get_suite_info_1 = [i.text for i in set(emp.get_employee_information_text())]  # 獲取【二級標題】
                time.sleep(0.5)
                get_sub_info_1 = [i.text.replace("\n", "").strip() for i in
                                  set(emp.get_attendance_calendar_text())]  # 獲取【三級標題】
                logging.info("員工自助頁面下拉前頁面元素為:第二模塊--{}；第三模塊--{}"
                             .format("、".join(get_suite_info_1), "、".join(get_sub_info_1)))

            get_suite_info_2, get_suite_info_3 = [], []
            get_sub_info_2, get_sub_info_3 = [], []
            if len(accessIds) > 2:
                time.sleep(1)
                with allure.step("向下滑屏一段距離"):
                    emp.swipe_screen(0.5, 0.1, 0.5, 0.8, model="頁面元素過多，先向下滑屏")
                    time.sleep(1)
                    get_suite_info_2 = [i.text for i in set(emp.get_employee_information_text())]  # 獲取【二級標題】
                    time.sleep(0.5)
                    get_sub_info_2 = [i.text.replace("\n", "").strip() for i in
                                      set(emp.get_attendance_calendar_text())]  # 獲取【三級標題】

                    logging.info("員工自助頁面向下滑屏後頁面元素為:第二模塊--{}；第三模塊--{}"
                                 .format("、".join(get_suite_info_2), "、".join(get_sub_info_2)))

                time.sleep(1)
                with allure.step("向上滑屏一段距離"):
                    emp.swipe_screen(0.5, 0.8, 0.5, 0.1, model="頁面元素過多，向上滑屏")
                    time.sleep(1)
                    get_suite_info_3 = [i.text for i in set(emp.get_employee_information_text())]  # 獲取【二級標題】
                    time.sleep(0.5)
                    get_sub_info_3 = [i.text.replace("\n", "").strip() for i in
                                      set(emp.get_attendance_calendar_text())]  # 獲取【三級標題】

                    logging.info("員工自助頁面向上滑屏後頁面元素為:第二模塊--{}；第三模塊--{}"
                                 .format("、".join(get_suite_info_3), "、".join(get_sub_info_3)))

            # 合併去重排序
            get_suite_info = sorted(set(get_suite_info_1 + get_suite_info_2 + get_suite_info_3))
            get_sub_info = sorted(set(get_sub_info_1 + get_sub_info_2 + get_sub_info_3))

            try:
                assert suite_title_list == get_suite_info and sub_title_list == get_sub_info
                logging.info("檢查成功,當前員工自助頁面只出現{}:{}".format(get_suite_info, get_sub_info))
                fail_state = "PASS"
            except:
                fail_state = "FAIL"
                case_step = case_step + "<br/>檢查失败！！當前員工自助頁面出現了{}:{}".format("、".join(get_suite_info),
                                                                             "、".join(get_sub_info))
                logging.exception("檢查失败！！當前員工自助頁面出現了{}:{}".format("、".join(get_suite_info), "、".join(get_sub_info)))
                emp.screenshot("檢查員工自助頁面元素捕獲异常")
                with allure.step("檢查失败！！當前員工自助頁面不是只出現員工資訊及考勤日曆"):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "ESS員工自助")  # 传入BUG标题，BUG复现步骤
            finally:
                emp.return_button_one()
                return fail_state

    def get_ess_random_main(self, startApp_withReset, case_name,combine_number=1, random_number=10):
        # combine_number :隨機組合個數    random_number : 隨機測試次數
        test_times = 0
        result_state = []
        while test_times < int(random_number):
            random_ids = random.sample(accessIds_list, int(combine_number))
            logging.info("第{}次進行測試的兩個參數為:{}".format(test_times, random_ids))
            result = self.employee_request_test(startApp_withReset, case_name,*random_ids)
            result_state.append(result)
            test_times = test_times + 1
            time.sleep(2)
        logging.info("10組隨機組合測試結果集:{}".format(result_state))
        if "FAIL" in result_state:
            raise Exception("10組隨機組合測試失敗")

    # =====================     測試用例    ==========================
    @pytest.mark.essrandom1
    @allure.title("隨機開啟 2 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_2(self, startApp_withReset):
        case_name = "test_ess_2"
        self.get_ess_random_main(startApp_withReset,case_name, combine_number=2)

    @pytest.mark.essrandom1
    @allure.title("隨機開啟 3 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_3(self, startApp_withReset):
        case_name = "test_ess_3"
        self.get_ess_random_main(startApp_withReset,case_name, combine_number=3)

    @pytest.mark.essrandom1
    @allure.title("隨機開啟 4 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_4(self, startApp_withReset):
        case_name = "test_ess_4"
        self.get_ess_random_main(startApp_withReset,case_name, combine_number=4)

    @pytest.mark.essrandom1
    @allure.title("隨機開啟 5 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_5(self, startApp_withReset):
        case_name = "test_ess_5"
        self.get_ess_random_main(startApp_withReset,case_name, combine_number=5)

    @pytest.mark.essrandom1
    @allure.title("隨機開啟 6 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_6(self, startApp_withReset):
        case_name = "test_ess_6"
        self.get_ess_random_main(startApp_withReset, case_name,combine_number=6)

    @pytest.mark.essrandom1
    @allure.title("隨機開啟 7 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_7(self, startApp_withReset):
        case_name = "test_ess_7"
        self.get_ess_random_main(startApp_withReset,case_name, combine_number=7)

    @pytest.mark.essrandom1
    @allure.title("隨機開啟 8 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_8(self, startApp_withReset):
        case_name = "test_ess_8"
        self.get_ess_random_main(startApp_withReset,case_name,combine_number=8)

    @pytest.mark.essrandom2
    @allure.title("隨機開啟 9 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_9(self, startApp_withReset):
        case_name = "test_ess_9"
        self.get_ess_random_main(startApp_withReset, case_name,combine_number=9)

    @pytest.mark.essrandom2
    @allure.title("隨機開啟 10 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_10(self, startApp_withReset):
        case_name = "test_ess_10"
        self.get_ess_random_main(startApp_withReset, case_name,combine_number=10)

    @pytest.mark.essrandom2
    @allure.title("隨機開啟 11 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_11(self, startApp_withReset):
        case_name = "test_ess_11"
        self.get_ess_random_main(startApp_withReset, case_name,combine_number=11)

    @pytest.mark.essrandom2
    @allure.title("隨機開啟 12 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_12(self, startApp_withReset):
        case_name = "test_ess_12"
        self.get_ess_random_main(startApp_withReset, case_name,combine_number=12)

    @pytest.mark.essrandom2
    @allure.title("隨機開啟 13 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_13(self, startApp_withReset):
        case_name = "test_ess_13"
        self.get_ess_random_main(startApp_withReset,case_name, combine_number=13)

    @pytest.mark.essrandom2
    @allure.title("隨機開啟 14 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_14(self, startApp_withReset):
        case_name = "test_ess_14"
        self.get_ess_random_main(startApp_withReset,case_name, combine_number=14)

    @pytest.mark.essrandom2
    @allure.title("隨機開啟 15 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_15(self, startApp_withReset):
        case_name = "test_ess_15"
        self.get_ess_random_main(startApp_withReset,case_name, combine_number=15)

    @pytest.mark.essrandom2
    @allure.title("隨機開啟 16 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_16(self, startApp_withReset):
        case_name = "test_ess_16"
        self.get_ess_random_main(startApp_withReset, case_name,combine_number=16)

    @pytest.mark.essrandom2
    @allure.title("隨機開啟 17 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_17(self, startApp_withReset):
        case_name = "test_ess_17"
        self.get_ess_random_main(startApp_withReset,case_name, combine_number=17)

    @pytest.mark.essrandom2
    @allure.title("隨機開啟 18 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_18(self, startApp_withReset):
        case_name = "test_ess_18"
        self.get_ess_random_main(startApp_withReset,case_name, combine_number=18)

    @pytest.mark.essrandom2
    @allure.title("隨機開啟 19 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_19(self, startApp_withReset):
        case_name = "test_ess_1"
        self.get_ess_random_main(startApp_withReset,case_name, combine_number=19)

    @pytest.mark.essrandom2
    @allure.title("隨機開啟 20 個卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_20(self, startApp_withReset):
        case_name="test_ess_20"
        self.get_ess_random_main(startApp_withReset, case_name,combine_number=20)

    @pytest.mark.essrandom2
    @allure.title("隨機開啟全部卡片權限")
    @allure.severity(bsc.B[0])
    def test_ess_21(self, startApp_withReset):
        case_name = "test_ess_21"
        self.get_ess_random_main(startApp_withReset, case_name,random_number=1, combine_number=21)
