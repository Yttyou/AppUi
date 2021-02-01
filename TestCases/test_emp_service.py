__author__ = 'developer'

# 【員工自助】模块用例          #作者:金伟    时间:2020/04/02
import datetime
import os
import time
import pytest

from Common.path_config import base_path
from PageObjects.employee_tab_page import EmpTabPage as EMP

from PageObjects.accessIds_tab import accessIds_subtitle_dict, accessIds_title_dict
import allure
import logging
import requests
import json

from Common import ZenTaoApiToMysql
from Common import bug_severity_config as bsc
from TestCases import test_chat


@allure.parent_suite("ESS員工自助")
@allure.story("考勤日曆/員工培訓/薪酬單據/評估表/電子船票")
class TestEmoployee_SF:

    def send_request(self, *accessIds):
        url = "https://sp-api.i-mocca.com/adminpanel_api/api/rbac/add_role_access"
        headers = {"Cookie": "sunpeople_admin=AR6CNWVB1Osq7jXDwK1uOQ==",
                   "Content-Type": "application/json"}
        params = {"roleId": "=bw54g", "accessIds": str(",".join(accessIds))}
        logging.info("請求參數為:{}".format(str(params)))
        response = requests.post(url=url, params=params, headers=headers)
        msg = json.loads(response.text)
        if msg.get("code") == "200" and msg.get('message') == "success":
            logging.info("接口請求成功")
            return (True, msg)
        else:
            logging.error("接口請求失敗!!!!,原因:{}".format(msg))
            return (False, msg)

    # 傳一個或多個params參數
    def employee_request_test(self, startApp_withReset,case_name, *accessIds):
        emp = EMP(startApp_withReset)
        case_step = ''
        logging.info("********* 接口自動化測試 *********")
        suite_title_list = sorted(set((accessIds_title_dict[i] for i in accessIds)))  # 二級標題確定(去重)
        sub_title_list = sorted(set((accessIds_subtitle_dict[i] for i in accessIds)))  # 三級標題確定
        title = "員工自助/{}/{}".format("、".join(suite_title_list), "、".join(sub_title_list))
        test_chat.temp_num += 1
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        bug_title = "[Neptune.AI][{0}][{1}]接口測試失敗".format(emp.get_app_environment(), title)  # BUG标题
        logging.info("要檢查的二級標題元素已確定,依次為:{}".format("、".join(suite_title_list)))
        logging.info("要檢查的三級標題元素已確定,依次為:{}".format("、".join(sub_title_list)))
        msg_post = self.send_request(*accessIds)
        logging.info("響應為:{}".format(msg_post))
        time.sleep(2)
        if not msg_post[0]:
            with allure.step("接口發送失敗,請求參數為:{},返回結果為:{}".format(accessIds, msg_post[1])):
                # 调用禅道api，报BUG单
                # 传入BUG标题，BUG复现步骤
                logging.error("隨機接口發送失敗,請求參數為:{},返回結果為:{}".format(accessIds, msg_post[1]))
                bug_link = ZenTaoApiToMysql.Commit_Bug_ZenTaoAPI().submit_bug(bug_title, case_step, bsc.B[1], "ESS員工自助")
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
                try:
                    get_suite_info = sorted([i.text for i in set(emp.get_employee_information_text())])  # 獲取【二級標題】
                except:
                    get_suite_info = []
                try:
                    get_sub_info = sorted(
                        [i.text.replace("\n", "").strip() for i in set(emp.get_attendance_calendar_text())])  # 獲取【三級標題】
                except:
                    get_sub_info = []
                try:
                    assert suite_title_list == get_suite_info and sub_title_list == get_sub_info
                    with allure.step("檢查成功,當前員工自助頁面只出現{}:{}".format(get_suite_info, get_sub_info)):
                        logging.info("檢查成功,當前員工自助頁面只出現{}:{}".format(get_suite_info, get_sub_info))

                except:
                    if get_suite_info == [] and get_sub_info == []:
                        case_step = case_step + "<br/>檢查失败！！當前員工自助頁面二級標題及三級標題都沒有出現"
                        logging.exception("檢查失败！！當前員工自助頁面二級標題及三級標題都沒有出現")

                    elif get_suite_info and get_sub_info:
                        case_step = case_step + "<br/>檢查失败！！當前員工自助頁面出現了{}:{}" \
                            .format("、".join(get_suite_info), "、".join(get_sub_info))
                        logging.exception("檢查失败！！當前員工自助頁面出現了{}:{}"
                                          .format("、".join(get_suite_info), "、".join(get_sub_info)))

                    elif get_sub_info == [] and get_suite_info:
                        case_step = case_step + "<br/>檢查失败！！當前員工自助頁面出現了二級標題為:{}，但未出現三級標題".format(
                            "、".join(get_suite_info))
                        logging.exception("檢查失败！！當前員工自助頁面出現了二級標題為:{}，但未出現三級標題"
                                          .format("、".join(get_suite_info)))

                    else:
                        case_step = case_step + "<br/>檢查失败！！當前員工自助頁面出現了三級標題為:{}，但未出現二級標題".format(
                            "、".join(get_sub_info))
                        logging.exception("檢查失败！！當前員工自助頁面出現了三級標題為:{}，但未出現二級標題"
                                          .format("、".join(get_sub_info)))

                    filepath = emp.screenshot("檢查員工自助頁面异常！！！")
                    with allure.step("檢查失败！！當前員工自助頁面不是只出現員工資訊及考勤日曆"):
                        # 调用禅道api，报BUG单
                        # bug_link = ZenTaoBugApi.submit_bug(bug_title, case_step, bsc.B[1], "ESS員工自助")  # 传入BUG标题，BUG复现步骤
                        bug_link = ZenTaoApiToMysql.Commit_Bug_ZenTaoAPI().submit_bug(bug_title, case_step, bsc.B[1],
                                                                                      "ESS員工自助", filepath)
                        with allure.step(bug_link):
                            raise
                finally:
                    emp.return_button_one()

    # ======================卡片8=========================
    @pytest.mark.fffkkk
    @allure.suite("員工資訊")
    @allure.sub_suite("")
    @allure.title("考勤日曆")
    @allure.description("員工資訊:考勤日曆")
    @allure.severity(bsc.B[0])
    def test_hr_attendance(self, startApp_withReset):
        case_name = "test_hr_attendanc"
        self.employee_request_test(startApp_withReset,case_name,"=bw54i")

    @pytest.mark.fffkkk
    @allure.suite("一般功能")
    @allure.sub_suite("")
    @allure.title("員工培訓")
    @allure.description("一般功能:員工培訓")
    @allure.severity(bsc.B[0])
    def test_hr_training(self, startApp_withReset):
        case_name = "test_hr_training"
        self.employee_request_test(startApp_withReset,case_name, "=bw54j")

    @allure.suite("員工資訊")
    @allure.sub_suite("")
    @allure.title("薪酬單據")
    @allure.description("員工資訊:薪酬單據")
    @allure.severity(bsc.B[0])
    def test_emp_payslip(self, startApp_withReset):
        case_name = "test_emp_payslip"
        self.employee_request_test(startApp_withReset,case_name, "=bw54k")

    @allure.suite("問卷調查")
    @allure.sub_suite("")
    @allure.title("評估表")
    @allure.description("問卷調查:評估表")
    @allure.severity(bsc.B[0])
    def test_hr_evaluation(self, startApp_withReset):
        case_name = "test_hr_evaluation"
        self.employee_request_test(startApp_withReset,case_name, "=bw53Y")

    @allure.suite("一般功能")
    @allure.sub_suite("")
    @allure.title("電子船票")
    @allure.description("一般功能:電子船票")
    @allure.severity(bsc.B[0])
    def test_hr_electronic_ticket(self, startApp_withReset):
        case_name = "test_hr_electronic_ticket"
        self.employee_request_test(startApp_withReset,case_name, "=bw53O")

    # ======================卡片9=====================================

    @allure.suite("員工資訊")
    @allure.sub_suite("")
    @allure.title("員工發展寶典")
    @allure.description("員工資訊:員工發展寶典")
    @allure.severity(bsc.B[0])
    def test_hr_training_developi(self, startApp_withReset):
        case_name = "test_hr_training_developi"
        self.employee_request_test(startApp_withReset,case_name, "=bw53M")

    @allure.suite("一般功能")
    @allure.sub_suite("")
    @allure.title("員工提名")
    @allure.description("一般功能:員工提名")
    @allure.severity(bsc.B[0])
    def test_hr_nomination(self, startApp_withReset):
        case_name = "test_hr_nomination"
        self.employee_request_test(startApp_withReset,case_name, "=bw53K")

    @allure.suite("問卷調查")
    @allure.sub_suite("")
    @allure.title("問卷調查")
    @allure.description("問卷調查:問卷調查")
    @allure.severity(bsc.B[0])
    def test_hr_survey(self, startApp_withReset):
        case_name = "test_hr_survey"
        self.employee_request_test(startApp_withReset,case_name,"=bw53J")

    @allure.suite("一般功能")
    @allure.sub_suite("")
    @allure.title("申請表")
    @allure.description("一般功能:申請表")
    @allure.severity(bsc.B[0])
    def test_hr_application_form(self, startApp_withReset):
        case_name = "test_hr_application_form"
        self.employee_request_test(startApp_withReset,case_name, "=bw53F")

    @allure.suite("一般功能")
    @allure.sub_suite("")
    @allure.title("百萬行")
    @allure.description("一般功能:百萬行")
    @allure.severity(bsc.B[0])
    def test_hr_enrollment_form(self, startApp_withReset):
        case_name = "test_hr_enrollment_form"
        self.employee_request_test(startApp_withReset,case_name, "=bw53E")

    # ===================卡片10=======================

    @allure.suite("問卷調查")
    @allure.sub_suite("")
    @allure.title("場面評核")
    @allure.description("問卷調查:場面評核")
    @allure.severity(bsc.B[0])
    def test_marketing_360(self, startApp_withReset):
        case_name = "test_marketing_360"
        self.employee_request_test(startApp_withReset,case_name, "=bw53C")

    @allure.suite("一般功能")
    @allure.sub_suite("")
    @allure.title("違規舉報")
    @allure.description("一般功能:違規舉報")
    @allure.severity(bsc.B[0])
    def test_violation_report(self, startApp_withReset):
        case_name = "test_violation_report"
        self.employee_request_test(startApp_withReset,case_name, "=bw53B")

    @allure.suite("問卷調查")
    @allure.sub_suite("")
    @allure.title("膳食調查")
    @allure.description("問卷調查:膳食調查")
    @allure.severity(bsc.B[0])
    def test_emp_meal(self, startApp_withReset):
        case_name = "test_emp_meal"
        self.employee_request_test(startApp_withReset,case_name, "=bw53A")

    @allure.suite("員工資訊")
    @allure.sub_suite("")
    @allure.title("員工優惠")
    @allure.description("員工資訊:員工優惠")
    @allure.severity(bsc.B[0])
    def test_emp_discount(self, startApp_withReset):
        case_name = "test_emp_discoun"
        self.employee_request_test(startApp_withReset,case_name, "=bw539")

    @allure.suite("一般功能")
    @allure.sub_suite("")
    @allure.title("公司電話")
    @allure.description("一般功能:公司電話")
    @allure.severity(bsc.B[0])
    def test_company_phone(self, startApp_withReset):
        case_name = "test_company_phone"
        self.employee_request_test(startApp_withReset, case_name,"=bw538")

    # ====================卡片11=====================

    @allure.suite("員工資訊")
    @allure.sub_suite("")
    @allure.title("員工手冊")
    @allure.description("員工資訊:員工手冊")
    @allure.severity(bsc.B[0])
    def test_emp_manual(self, startApp_withReset):
        case_name = "test_emp_manua"
        self.employee_request_test(startApp_withReset,case_name, "=bw537")

    @allure.suite("一般功能")
    @allure.sub_suite("")
    @allure.title("洗衣卡")
    @allure.description("一般功能:洗衣卡")
    @allure.severity(bsc.B[0])
    def test_laundry_card(self, startApp_withReset):
        case_name ="test_laundry_card"
        self.employee_request_test(startApp_withReset,case_name, "=bw536")

    @allure.suite("一般功能")
    @allure.sub_suite("")
    @allure.title("諮詢服務")
    @allure.description("一般功能:諮詢服務")
    @allure.severity(bsc.B[0])
    def test_consulting_service(self, startApp_withReset):
        case_name = "test_consulting_service"
        self.employee_request_test(startApp_withReset,case_name, "=bw535")

    @allure.suite("問卷調查")
    @allure.sub_suite("")
    @allure.title("360績評")
    @allure.description("問卷調查:360績評")
    @allure.severity(bsc.B[0])
    def test_evaluation_360(self, startApp_withReset):
        case_name = "test_evaluation_360"
        self.employee_request_test(startApp_withReset,case_name, "=bw534")

    @allure.suite("員工資訊")
    @allure.sub_suite("")
    @allure.title("員工守則")
    @allure.description("員工資訊:員工守則")
    @allure.severity(bsc.B[0])
    def test_emp_rules(self, startApp_withReset):
        case_name = "test_emp_rules"
        self.employee_request_test(startApp_withReset,case_name, "=bw533")

    @allure.suite("員工資訊")
    @allure.sub_suite("")
    @allure.title("個人信息")
    @allure.description("員工資訊:個人信息")
    @allure.severity(bsc.B[0])
    def test_emp_hrprofile(self, startApp_withReset):
        case_name = "test_emp_hrprofile"
        self.employee_request_test(startApp_withReset,case_name,"=bw54h")
