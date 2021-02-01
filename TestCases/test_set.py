import pytest
from PageObjects.newdynamic_tab_page import NewDynamicTabPage as NTP
from PageObjects.chat_tab_page import ChatTabPage as CTP
from PageObjects.setting_tab_page import SettingTabPage as STP
from TestDatas import COMMON_DATA as CD
import logging
import time
import allure
from Common.ZenTaoApiToMysql import Commit_Bug_ZenTaoAPI as ZenTaoBugApi
from Common import bug_severity_config as bsc
from Common import Case_bug_ZenTao as cbz


@pytest.mark.set
@allure.parent_suite("设定")
@allure.story("用户头像/更换用户头像")
@pytest.mark.usefixtures("startApp_withReset")
class TestSet:
    # 個人tab/點擊粉絲人數/粉絲列表
    @allure.title("用户头像/更换用户头像")  # 用例標題
    @allure.description("更换用户头像:校驗 '头像上传成功'的提示")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_change_user_image(self, startApp_withReset):
        stp = STP(startApp_withReset)
        title = "用户头像/更换用户头像"
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(stp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        stp.return_home()  # 用例前置--返回首页
        logging.info("*********  用户头像/更换用户头像     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        case_step = case_step + cbz.case_step("1、點擊【设定】")
        stp.click_set()  # 點擊：[设定]tab
        case_step = case_step + cbz.case_step("2、點擊：【用户图像】")
        stp.click_user_image()
        case_step = case_step + cbz.case_step("3、點擊：【拍照】")
        stp.click_taking_pictures(0)  # 點擊：[拍照]
        case_step = case_step + cbz.case_step("4、点击快门")
        stp.click_the_shutter()
        case_step = case_step + cbz.case_step("5、点击确定")
        stp.click_the_is_ok()
        case_step = case_step + cbz.case_step("6、点击完成")
        stp.click_the_finish()
        case_step = case_step + cbz.case_step("7、返回上傳頭像成功")
        ret = stp.find_send_text_photo_tost()
        try:
            assert ret == True  # 返回结果是否正确
            case_step = case_step + cbz.case_step("检查成功，能正常返回提示")
            logging.info("检查成功，能正常返回提示")
        except:
            actual = "檢查失敗！！未能正常返回提示"
            expect = "上传图像时返回提示不准确"
            case_step = case_step + cbz.case_result(actual, expect)  # 测试结果
            stp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "设定")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            stp.return_button()
            stp.return_button()
