import datetime
import os

import pytest

from Common.path_config import base_path
from PageObjects.newdynamic_tab_page import NewDynamicTabPage as NTP
from PageObjects.chat_tab_page import ChatTabPage as CTP
from TestCases import test_chat
from TestDatas import COMMON_DATA as CD
import logging
import time
import allure
from Common.ZenTaoApiToMysql import Commit_Bug_ZenTaoAPI as ZenTaoBugApi
from Common import bug_severity_config as bsc
from Common import Case_bug_ZenTao as cbz
from TestDatas.COMMON_DATA import vote_title_str, vote_content_str
from PageObjects.page_objects import append_data

per_num = 0
data_lsit = []
data_dict={}
@pytest.mark.all
@pytest.mark.fan
@allure.parent_suite("最新动态")
@allure.story("個人tab/點擊粉絲人數/粉絲列表")
@pytest.mark.usefixtures("startApp_withReset")
class TestFanList:

    # 個人tab/點擊粉絲人數/粉絲列表
    @allure.title("個人tab/點擊粉絲人數/粉絲列表")  # 用例標題
    @allure.description("搜索粉丝名:校驗 搜索结果显示是否正确")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_post_fan_message(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "個人tab/點擊粉絲人數/粉絲列表/搜索粉丝名"
        test_chat.temp_num += 1
        case_name = "test_post_fan_message"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num,data_lsit,data_dict
        per_num+=1
        module = 'NF'
        per_list = append_data(per_list,per_num,module,case_name,title)
        data_lsit.append(per_list)

        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  個人tab/點擊粉絲人數/粉絲列表/搜索粉丝名     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()  # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：【个人】tab")
        ntp.click_personal_tab()  # 点击：[个人]tab
        case_step = case_step + cbz.case_step("3、點擊：【粉丝人数】")
        ntp.click_personal_fans()  # 點擊：[个人粉丝]
        user_name1 = ntp.get_first_track_name(0)  # 获取第一个粉丝名称
        case_step = case_step + cbz.case_step("5、输入搜索内容进行搜索")
        ntp.input_search_fan_username(user_name1)  # 输入搜索内容进行搜索
        user_name2 = ntp.get_first_track_name(0)  # 获取搜索后第一个粉丝名称
        try:
            assert user_name1 == user_name2  # 搜索结果是否正确
            case_step = case_step + cbz.case_step("检查成功，能正常搜索粉丝名")
            logging.info("检查成功，能正常搜索粉丝名")
        except:
            actual = "檢查失敗！！未能正常搜索显示粉丝名"
            expect = "搜索时不能搜索出粉丝名"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("6 点击粉丝用户昵称进入个人主页")
            ntp.user_name_to_jump()  # 点击搜索出来的用户名进行跳转
            ntp.swipe_personal_search_message()  # 滑屏到第一个留言icon可见为止
            count_number_1 = ntp.get_message_count_icon()  # 获取留言次数
            logging.info("當前帖子留言次數為{}".format(count_number_1))
            case_step = case_step + cbz.case_step("7、点击留言icon，进行留言")
            ntp.search_click_first_message_icon()  # 点击留言icon，进行留言
            ntp.comment_double(1, CD.send_message_data)  # 留言
            time.sleep(1)
            count_number_2 = ntp.get_message_count_icon()  # 留言後獲取留言次數
            logging.info("留言{}次後獲取留言次數'{}'".format(3, count_number_2))
            case_step = case_step + cbz.case_step("檢查：")
            try:
                assert count_number_2 - count_number_1 == 1
                case_step = case_step + cbz.case_step(
                    "檢查成功，評論次數：留言前'{}'，評論後'{}'".format(count_number_1, count_number_2))
                logging.info("檢查成功，評論次數：留言前'{}'，評論後'{}'".format(count_number_1, count_number_2))
            except:
                actual = "檢查失敗！評論次數：留言前'{}'，評論後'{}'".format(count_number_1, count_number_2)
                expect = "留言前後留言數差值為1"
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            finally:
                ntp.return_button()
                ntp.return_button()
                ntp.return_button()

    # 個人tab/點擊粉絲人數/粉絲列表
    @allure.title("個人tab/點擊粉絲人數/粉絲列表")  # 用例標題
    @allure.description("搜索粉丝名:校驗 分享结果显示是否正确")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_post_fan_share(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "個人tab/點擊粉絲人數/粉絲列表/搜索粉丝名"
        test_chat.temp_num += 1
        case_name = "test_post_fan_share"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit
        per_num += 1
        module = 'NF'
        per_list = append_data(per_list,per_num,module,case_name,title)
        data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  個人tab/點擊粉絲人數/粉絲列表/搜索粉丝名     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()  # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：【个人】tab")
        ntp.click_personal_tab()  # 点击：[个人]tab
        case_step = case_step + cbz.case_step("3、點擊：【粉丝人数】")
        ntp.click_personal_fans()  # 點擊：[个人粉丝]
        user_name1 = ntp.get_first_track_name(0)  # 获取第一个粉丝名称
        case_step = case_step + cbz.case_step("5、输入搜索内容进行搜索")
        ntp.input_search_fan_username(user_name1)  # 输入搜索内容进行搜索
        case_step = case_step + cbz.case_step("6 点击粉丝用户昵称进入个人主页")
        ntp.user_name_to_jump()  # 点击搜索出来的用户名进行跳转
        ntp.swipe_personal_search_share()  # 滑屏到第一个分享icon可见为止
        count_number_1 = ntp.get_share_count_icon()  # 获取分享次数
        logging.info("當前帖子分享次數為{}".format(count_number_1))
        case_step = case_step + cbz.case_step("7、点击分享icon，进行分享")
        ntp.search_click_first_share_icon()  # 点击分享icon，进行分享
        case_step = case_step + cbz.case_step("8、分享到「分享」")
        ntp.click_post_share_to_share()  # 分享到「分享」
        ntp.swipe_personal_search_share2()  # 下拉刷新
        case_step = case_step + cbz.case_step("9、點擊：帖子分享icon")
        ntp.search_click_first_share_icon()  # 點擊：帖子分享icon
        case_step = case_step + cbz.case_step("10、分享到[分享至sp]")
        ntp.click_post_share_to_sp()  # 分享到[分享至sp]
        ntp.swipe_personal_search_share2()  # 下拉刷新
        count_number_2 = ntp.get_share_count_icon()  # 分享后獲取分享次數
        logging.info("分享后计数为：'{}'".format(count_number_2))
        case_step = case_step + cbz.case_step("檢查：")
        try:
            assert count_number_2 - count_number_1 == 2
            case_step = case_step + cbz.case_step(
                "檢查成功，分享次數：分享前'{}'，分享后後'{}'".format(count_number_1, count_number_2))
            logging.info("檢查成功，分享次數：分享前'{}'，分享后後'{}'".format(count_number_1, count_number_2))
        except:
            actual = "檢查失敗！分享次數：分享前'{}'，分享后後'{}'".format(count_number_1, count_number_2)
            expect = "分享前後分享次數差值為2"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.return_button()
            ntp.return_button()
            ntp.return_button()

    # 個人tab/點擊粉絲人數/粉絲列表
    @allure.title("個人tab/點擊粉絲人數/粉絲列表")  # 用例標題
    @allure.description("搜索粉丝名:校驗 分享结果显示是否正确")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_post_fan_like(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "個人tab/點擊粉絲人數/粉絲列表/搜索粉丝名"
        test_chat.temp_num += 1
        case_name = "test_post_fan_like"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit
        per_num += 1
        module = 'NF'
        per_list = append_data(per_list,per_num,module,case_name,title)
        data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  個人tab/點擊粉絲人數/粉絲列表/搜索粉丝名     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()  # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：【个人】tab")
        ntp.click_personal_tab()  # 点击：[个人]tab
        case_step = case_step + cbz.case_step("3、點擊：【粉丝人数】")
        ntp.click_personal_fans()  # 點擊：[个人粉丝]
        user_name1 = ntp.get_first_track_name(0)  # 获取第一个粉丝名称
        case_step = case_step + cbz.case_step("5、输入搜索内容进行搜索")
        ntp.input_search_fan_username(user_name1)  # 输入搜索内容进行搜索
        case_step = case_step + cbz.case_step("6 点击粉丝用户昵称进入个人主页")
        ntp.user_name_to_jump()  # 点击搜索出来的用户名进行跳转
        ntp.swipe_personal_search_share()  # 滑屏到第一个分享icon可见为止
        before_like_time = ntp.get_post_detail_like_count_icon_number()  # 获取第一个动态点赞次数（点赞前）
        logging.info("点赞前赞个数为:{}".format(before_like_time))
        case_step = case_step + cbz.case_step("7、（第一個動態）獲取點擊個數為:{}，並進行點讚操作".format(before_like_time))
        ntp.click_like_button()  # 点击【点赞】icon
        later_like_time = ntp.get_post_detail_like_count_icon_number()  # 获取第一个动态点赞次数:点赞后次数
        logging.info("点赞后赞个数为:{}".format(later_like_time))
        case_step = case_step + cbz.case_step("5、點讚（第一個動態）後獲取點讚次數為:{}".format(later_like_time))
        like = abs(later_like_time - before_like_time)  # 檢查:abs(点赞后次数-点赞前次数) = 1     abs--取绝对值
        logging.info("点赞前后赞数相差为:{}".format(like))
        case_step = case_step + cbz.case_step("檢查：")
        try:
            assert like == 1
            case_step = case_step + cbz.case_step("檢查成功。點擊後與點讚前差值為1")
            logging.info("檢查成功。點擊後與點讚前差值為1")
        except:
            actual = "檢查失敗！！點讚後與點讚前差值不等於1,實際結果差值為:{}".format(like)
            expect = "點讚前後差值為1"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.return_button()
            ntp.return_button()

    # 個人tab/點擊粉絲人數/粉絲列表
    @allure.title("個人tab/點擊粉絲人數/追踪列表")  # 用例標題
    @allure.description("搜索群组名:校驗 搜索结果显示是否正确")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_post_group_message(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "個人tab/點擊粉絲人數/追踪列表/搜索群组名"
        test_chat.temp_num += 1
        case_name = "test_post_group_message"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit
        per_num += 1
        module = 'NF'
        per_list = append_data(per_list,per_num,module,case_name,title)
        data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  個人tab/點擊粉絲人數/追踪列表/搜索群组名     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()  # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：【个人】tab")
        ntp.click_personal_tab()  # 点击：[个人]tab
        case_step = case_step + cbz.case_step("3、點擊：【追踪中】")
        ntp.click_personal_trace_tab()  # 點擊：[追踪中]
        case_step = case_step + cbz.case_step("4 点击群组昵称进入群组主页")
        ntp.group_name_to_jump()  # 点击搜索出来的用户名进行跳转
        ntp.swipe_personal_search_message()  # 滑屏到第一个留言icon可见为止
        count_number_1 = ntp.get_message_count_icon()  # 获取留言次数
        logging.info("當前帖子留言次數為{}".format(count_number_1))
        case_step = case_step + cbz.case_step("5、点击留言icon，进行留言")
        ntp.search_click_first_message_icon()  # 点击留言icon，进行留言
        ntp.comment_double(1, CD.send_message_data)  # 留言
        time.sleep(1)
        count_number_2 = ntp.get_message_count_icon()  # 留言後獲取留言次數
        logging.info("留言{}次後獲取留言次數'{}'".format(3, count_number_2))
        case_step = case_step + cbz.case_step("檢查：")
        try:
            assert count_number_2 - count_number_1 == 1
            case_step = case_step + cbz.case_step(
                "檢查成功，評論次數：留言前'{}'，評論後'{}'".format(count_number_1, count_number_2))
            logging.info("檢查成功，評論次數：留言前'{}'，評論後'{}'".format(count_number_1, count_number_2))
        except:
            actual = "檢查失敗！評論次數：留言前'{}'，評論後'{}'".format(count_number_1, count_number_2)
            expect = "留言前後留言數差值為1"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.return_button()
            ntp.return_button()
            ntp.return_button()

    @allure.title("個人tab/點擊粉絲人數/追踪列表")  # 用例標題
    @allure.description("搜索群组名:校驗 点赞次数显示是否正确")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_post_group_like(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "個人tab/點擊粉絲人數/追踪列表/搜索群组名"
        test_chat.temp_num += 1
        case_name = "test_post_group_like"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit
        per_num += 1
        module = 'NF'
        per_list = append_data(per_list,per_num,module,case_name,title)
        data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  個人tab/點擊粉絲人數/追踪列表/搜索群组名     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()  # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：【个人】tab")
        ntp.click_personal_tab()  # 点击：[个人]tab
        case_step = case_step + cbz.case_step("3、點擊：【追踪中】")
        ntp.click_personal_trace_tab()  # 點擊：[追踪中]
        case_step = case_step + cbz.case_step("4 点击群组用户昵称进入个人主页")
        ntp.group_name_to_jump()  # 点击搜索出来的群组名进行跳转
        ntp.swipe_personal_search_share()  # 滑屏到第一个分享icon可见为止
        before_like_time = ntp.get_post_detail_like_count_icon_number()  # 获取第一个动态点赞次数（点赞前）
        logging.info("点赞前赞个数为:{}".format(before_like_time))
        case_step = case_step + cbz.case_step("5、（第一個動態）獲取點擊個數為:{}，並進行點讚操作".format(before_like_time))
        ntp.click_like_button()  # 点击【点赞】icon
        later_like_time = ntp.get_post_detail_like_count_icon_number()  # 获取第一个动态点赞次数:点赞后次数
        logging.info("点赞后赞个数为:{}".format(later_like_time))
        # case_step = case_step + cbz.case_step("點讚（第一個動態）後獲取點讚次數為:{}".format(later_like_time))
        like = abs(later_like_time - before_like_time)  # 檢查:abs(点赞后次数-点赞前次数) = 1     abs--取绝对值
        logging.info("点赞前后赞数相差为:{}".format(like))
        case_step = case_step + cbz.case_step("檢查：")
        try:
            assert like == 1
            case_step = case_step + cbz.case_step("檢查成功。點擊後與點讚前差值為1")
            logging.info("檢查成功。點擊後與點讚前差值為1")
        except:
            actual = "檢查失敗！！點讚後與點讚前差值不等於1,實際結果差值為:{}".format(like)
            expect = "點讚前後差值為1"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.return_button()
            ntp.return_button()

    @allure.title("全部tab/你在想什么/添加更多元素")  # 用例標題
    @allure.description("择一个群组并发布:校驗 提交投票按钮消失")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_tab_one_group(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "全部tab/你在想什么/添加更多元素/择一个群组并发布"
        test_chat.temp_num += 1
        case_name = "test_all_tab_one_group"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit
        per_num += 1
        module = 'NF'
        per_list = append_data(per_list,per_num,module,case_name,title)
        data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  全部tab/你在想什么/添加更多元素/择一个群组并发布     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()  # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：【全部】tab")
        ntp.click_all_tab()  # 点击：[全部]tab
        case_step = case_step + cbz.case_step("4、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()
        case_step = case_step + cbz.case_step("6、點擊：【提交投票】icon")
        ntp.click_submit_to_vote_icon()
        title = CD.vote_title + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("7、點擊：【投票标题】输入内容")
        ntp.input_vote_title(0, title)
        text = CD.vote_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("8、點擊：【投票内容】输入内容")
        time.sleep(1)
        ntp.input_vote_title(1, text)
        case_step = case_step + cbz.case_step("9、輸入投票選項A、B")
        ntp.input_vote_title(2, "A")
        ntp.input_vote_title(3, "B")
        case_step = case_step + cbz.case_step("10、點擊：【投票结束时间】")
        ntp.click_vote_end_time()
        case_step = case_step + cbz.case_step("11、选择：【投票结束时间】")
        ntp.choose_days(1)
        case_step = case_step + cbz.case_step("12、點擊：【群组】")
        ntp.click_share_group()
        list_number = ntp.get_share_list_number()  # 分享可选群组个数
        random_number = ntp.random_int(list_number - 1)
        logging.info("可分享群组个数为：{}".format(list_number))
        ntp.click_random_Object_one(random_number)
        case_step = case_step + cbz.case_step("13、點擊：「發帖」按鈕")
        ntp.click_publish_button()
        case_step = case_step + cbz.case_step("14、點擊：[全部]tab")
        ntp.click_all_tab()  # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("15：點擊：投票单选")
        ntp.click_one_select(0)
        case_step = case_step + cbz.case_step("16：查找：提交投票")
        ret = ntp.find_vote_button()
        try:
            assert ret == False
            case_step = case_step + cbz.case_step("检查成功，投票按钮消失")
            logging.info("检查成功，投票按钮消失")
        except:
            actual = "检查失败！投票按钮没有消失"
            expect = "投票按钮消失"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.return_button()


    @allure.title("全部tab/你在想什么/添加更多元素")  # 用例標題
    @allure.description("择一个群组并发布:校驗 提交投票按钮消失")  # 用例描述
    @allure.severity(bsc.C[0])
    @pytest.mark.demo1
    def test_all_tab_more_group(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "全部tab/你在想什么/添加更多元素/择一个群组并发布"
        test_chat.temp_num += 1
        case_name = "test_all_tab_more_group"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit
        per_num += 1
        module = 'NF'
        per_list = append_data(per_list,per_num,module,case_name,title)
        data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  全部tab/你在想什么/添加更多元素/择一个群组并发布     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()  # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：【全部】tab")
        ntp.click_all_tab()  # 点击：[全部]tab
        case_step = case_step + cbz.case_step("4、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()
        case_step = case_step + cbz.case_step("6、點擊：【提交投票】icon")
        ntp.click_submit_to_vote_icon()
        title = CD.vote_title + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("7、點擊：【投票标题】输入内容")
        ntp.input_vote_title(0, title)
        text = CD.vote_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("8、點擊：【投票内容】输入内容")
        time.sleep(1)
        ntp.input_vote_title(1, text)
        case_step = case_step + cbz.case_step("9、輸入投票選項A、B")
        ntp.input_vote_title(2, "A")
        ntp.input_vote_title(3, "B")
        case_step = case_step + cbz.case_step("10、點擊:【可多选】")
        ntp.can_more_select()
        case_step = case_step + cbz.case_step("11、點擊：【投票结束时间】")
        ntp.click_vote_end_time()
        case_step = case_step + cbz.case_step("12、选择：【投票结束时间】")
        ntp.choose_days(1)
        case_step = case_step + cbz.case_step("13、點擊：【群组】")
        ntp.click_share_group()
        list_number = ntp.get_share_list_number()  # 分享可选群组个数
        random_number = ntp.random_int(list_number - 1)
        logging.info("可分享群组个数为：{}".format(list_number))
        ntp.click_random_Object_one(random_number)
        case_step = case_step + cbz.case_step("14、點擊：「發帖」按鈕")
        ntp.click_publish_button()
        case_step = case_step + cbz.case_step("15、點擊：[全部]tab")
        ntp.click_all_tab()  # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("16：點擊：投票单选")
        ntp.select_more_select(0)
        ntp.select_more_select(1)
        case_step = case_step + cbz.case_step("17：點擊：提交投票")
        ntp.push_vote_more()
        case_step = case_step + cbz.case_step("18：查找：提交投票")
        ret = ntp.find_vote_button()
        try:
            assert ret == False
            case_step = case_step + cbz.case_step("检查成功，投票按钮消失")
            logging.info("检查成功，投票按钮消失")
        except:
            actual = "检查失败！投票按钮没有消失"
            expect = "投票按钮消失"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.return_button()

    @allure.title("群组tab/查看全部")  # 用例標題
    @allure.description("择一个群组:校驗搜索第一个待邀请成员名是否对得上")  # 用例描述
    @allure.severity(bsc.C[0])
    @pytest.mark.fkfkfk
    def test_newdynastic_to_group(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "群组tab/查看全部"
        test_chat.temp_num += 1
        case_name = "test_newdynastic_to_group"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit
        per_num += 1
        module = 'NF'
        per_list = append_data(per_list,per_num,module,case_name,title)
        data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  群组tab/查看全部/择一个群组     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()  # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊【群组tab】")
        ntp.click_group_tab()
        case_step = case_step + cbz.case_step("3、點擊【查看全部】")
        ntp.click_group_tab_view_all()
        case_step = case_step + cbz.case_step("4、點擊【第一个成员】")
        ntp.click_your_group_page_list()
        case_step = case_step + cbz.case_step("5、點擊【邀请】")
        ntp.click_invitation()
        case_step = case_step + cbz.case_step("6、获取第一个用户名")
        member_name1 = ntp.get_first_member_name(0)#获取第一个用户名
        ntp.input_search_fan_username(member_name1)  # 输入搜索内容进行搜索
        member_name2 = ntp.get_first_member_name(0)#获取搜索后第一个用户名
        try:
            assert member_name1 == member_name2  # 搜索结果是否正确
            case_step = case_step + cbz.case_step("检查成功，能正常搜索用户名")
            logging.info("检查成功，能正常搜索用户名")
        except:
            actual = "檢查失敗！！未能正常搜索显示用户名"
            expect = "搜索时不能搜索出用户名"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("7 点击搜索出来的成员")
            ntp.click_search_one_member()
            case_step = case_step + cbz.case_step("8 点击完成")
            ntp.click_finish()
            ret = ntp.find_toast_invitation_success()#获取toast提示
            try:
                assert ret==True
                case_step = case_step + cbz.case_step("检查成功，toast提示正确")
                logging.info("检查成功，toast提示正确")
            except:
                actual = "檢查失敗！！toast提示不正确"
                expect = "点击完成时，toast提示不正确"
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            finally:
                ntp.return_button()
                ntp.return_button()
