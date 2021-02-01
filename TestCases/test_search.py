__author__ = 'developer'

# 【最新动态】模块用例          #作者:游同同    时间:2020/11/20
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
from TestCases import test_fan_list
from PageObjects.page_objects import append_data


@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("全部")
@allure.sub_suite("建立貼文")
@allure.feature("最新動態/全部/建立貼文")
@allure.story("建立貼文:相关功能")
@pytest.mark.usefixtures("startApp_withReset")
class TestCreatePost:

    # 頭像/暱稱/發布到的位置:群组列表                                              作者：游同同    时间：2020/3/31
    @allure.title("頭像/暱稱/發布到的位置:群组列表")  # 用例標題
    @allure.description("點擊【個人動態】出現群组列表")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_share_group_list(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "點擊【個人動態】出現群组列表"
        test_chat.temp_num += 1
        case_name = "test_share_group_list"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   點擊【個人動態】出現群组列表    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、點擊最新動態-全部tab")
        ntp.click_all_tab()
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()
        case_step = case_step + cbz.case_step("4、點擊：[個人動態]跳转按钮")
        ntp.click_personal_dynamic()
        case_step = case_step + cbz.case_step("檢查：")
        is_find = ntp.find_share_page_list()
        try:
            assert is_find == True
            case_step = case_step + cbz.case_step("檢查成功，展示'分享至'群組列表正常")
            logging.info("檢查成功，展示'分享至'群組列表正常")
        except:
            actual = "檢查失敗！展示'分享至'群組列表異常"
            expect = "能够跳转到'分享至'页面并展示群组列表"
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

    # 頭像/暱稱/發布到的位置:个人身份标签和贴文公开选项                                作者：游同同    时间：2020/3/31
    @allure.title("頭像/暱稱/發布到的位置:个人身份标签和贴文公开选项")  # 用例標題
    @allure.description("帖子编辑选择群组后出现个人身份标签和贴文公开选项")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_share_odentity_Option(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        test_chat.temp_num += 1
        case_name = "test_share_odentity_Option"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        title = "帖子编辑选择群组后出现个人身份标签和贴文公开选项"
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   頭像/暱稱/發布到的位置:个人身份标签和贴文公开选项    *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、点击最新动态-全部tab")
        ntp.click_all_tab()                                             # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                               # 點擊：[你在想什麼?]入口
        case_step = case_step + cbz.case_step("4、點擊：[個人動態]跳转按钮")
        ntp.click_personal_dynamic()                                    # 點擊：[個人動態]跳转按钮
        list_number = ntp.get_share_list_number()  # 分享可选群组个数
        if list_number >= 2:
            case_step = case_step + cbz.case_step("5、點擊第2個分享對象後點擊「完成」按鈕")
            ntp.click_random_Object()                               # 點擊2個分享對象後點擊「完成」按鈕
        case_step = case_step + cbz.case_step("檢查：")
        find_admin = ntp.find_set_post_admin_button()                   # 查找：建立贴文页面-【管理员身份】下拉按钮
        find_public_post = ntp.find_public_post_buttn()                 # 查找：建立贴文页面- [公開帖文]下拉列表
        try:
            assert find_admin == True and find_public_post == True
            case_step = case_step + cbz.case_step("检查成功，选择群组后个人身份标签和贴文公开选项展示正常")
            logging.info("检查成功，选择群组后个人身份标签和贴文公开选项展示正常")
        except:
            actual = "檢查失敗！選擇群組後展示个人身份标签和贴文公开选项展示異常"
            expect = "选择群组后出现【个人身份】和【贴文公开】选项"
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

    # 分享的內容                                                                 作者：游同同    时间：2020/3/31
    @allure.title("分享的內容")  # 用例標題
    @allure.description("編輯多種組合字符能夠發布成功")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_share_content(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "分享的內容：編輯多種組合字符能夠發布成功"
        test_chat.temp_num += 1
        case_name = "test_share_content"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   分享的內容：編輯多種組合字符能夠發布成功    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、點擊最新動態-全部tab")
        ntp.click_all_tab()                                             # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                               # 點擊：[你在想什麼?]入口
        post_text = CD.post_send_texts + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                       # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：「發布」按鈕")
        ntp.click_post_publish_button()                                # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查：")
        send_post_text = ntp.get_all_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布'{}'帖子成功".format(post_text))
            logging.info("檢查成功，發布'{}'帖子成功".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'帖子異常".format(post_text)
            expect = "发帖能成功"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 分享的內容:群组和公开贴文                                                    作者：游同同    时间：2020/4/1
    @allure.title("分享的內容:群组和公开贴文")  # 用例標題
    @allure.description("編輯多種組合字符发布到群组能夠成功")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_share_content_group(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "分享的內容（至群组-公开）：編輯多種組合字符发布到群组能夠成功"
        test_chat.temp_num += 1
        case_name = "test_share_content_group"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   分享的內容:群组和公开贴文    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、點擊最新動態-全部tab")
        ntp.click_all_tab()                                              # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                                # 點擊：[你在想什麼?]入口
        post_text = CD.post_send_texts + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                         # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：[個人動態]跳转按钮")
        ntp.click_personal_dynamic()                                    # 點擊：[個人動態]跳转按钮
        list_number = ntp.get_share_list_number()  # 分享可选群组个数
        if list_number >= 2:
            random_index = ntp.random_int_one(list_number-1)
            case_step = case_step + cbz.case_step("6、點擊第{}個分享群組對象後點擊「完成」按鈕".format(random_index))
            ntp.click_random_index_Object(random_index)                 # 隨機點擊一個群組對象後點擊「完成」按鈕
        case_step = case_step + cbz.case_step("7、點擊：「發布」按鈕")
        ntp.click_post_publish_button()                                  # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("8、检查：")
        send_post_text = ntp.get_all_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布文本'{}'至公開帖子成功".format(post_text))
            logging.info("檢查成功，發布文本'{}'至公開帖子成功".format(post_text))
        except:
            actual = "檢查失敗！發布文本'{}'至公開帖子異常".format(post_text)
            expect = "发帖公开帖子能成功"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 分享的內容:群组和私密贴文                                                    作者：游同同    时间：2020/4/1
    @allure.title("分享的內容:群组和私密贴文")  # 用例標題
    @allure.description("編輯多種組合字符发布到私密群组能夠成功")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_share_content_group_private(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "分享的內容（至群组-私密）：編輯多種組合字符发布到群组能夠成功"
        test_chat.temp_num += 1
        case_name = "test_share_content_group_private"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   分享的內容:群组和私密贴文    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、點擊最新動態-全部tab")
        ntp.click_all_tab()                                                 # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                                   # 點擊：[你在想什麼?]入口
        post_text = CD.post_send_texts + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                            # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：[個人動態]跳转按钮")
        ntp.click_personal_dynamic()                                        # 點擊：[個人動態]跳转按钮
        list_number = ntp.get_share_list_number()                           # 分享可选群组个数
        if list_number >= 2:
            random_index = ntp.random_int_one(list_number - 1)
            case_step = case_step + cbz.case_step("6、點擊第{}個分享群組對象後點擊「完成」按鈕".format(random_index))
            ntp.click_random_index_Object(random_index)                     # 隨機點擊一個群組對象後點擊「完成」按鈕
        case_step = case_step + cbz.case_step("7、[公開帖文]下拉列表-[私密貼文]選項")
        ntp.click_public_post_buttn()                               # [公開帖文]下拉列表-[私密貼文]選項
        case_step = case_step + cbz.case_step("8、點擊：「發布」按鈕")
        ntp.click_post_publish_button()                             # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查：")
        send_post_text = ntp.get_all_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布文本'{}'至私密帖子成功".format(post_text))
            logging.info("檢查成功，發布文本'{}'至私密帖子成功".format(post_text))
        except:
            actual = "檢查失敗！發布文本'{}'至私密帖子異常".format(post_text)
            expect = "发帖私密帖子能成功"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 添加元素:提交投票                                                          作者：游同同    时间：2020/4/1
    @allure.title("添加元素:提交投票（添加选项功能）")  # 用例標題
    @allure.description("添加元素:提交投票添加选项功能")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_share_label_vote_add_Option(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "添加元素:提交投票添加选项功能"
        test_chat.temp_num += 1
        case_name = "test_share_label_vote_add_Option"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   添加元素:提交投票添加选项功能    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、點擊最新動態-全部tab")
        ntp.click_all_tab()                                             # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                               # 點擊：[你在想什麼?]入口
        case_step = case_step + cbz.case_step("4、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                           # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("5、點擊：[提交投票]选项")
        ntp.click_submit_vote()                                     # 點擊：[提交投票]选项
        case_step = case_step + cbz.case_step("6、 點擊：[提交投票]-[添加選項]按鈕")
        ntp.click_submit_vote_add_Option()                          # 點擊：[提交投票]-[添加選項]按鈕
        case_step = case_step + cbz.case_step("檢查：（選項3）")
        find_Option3 = ntp.find_add_Option3()
        try:
            assert find_Option3 == True
            case_step = case_step + cbz.case_step("檢查成功，添加「選項3」成功")
            logging.info("檢查成功，添加「選項3」成功")
        except:
            actual = "檢查失敗！查找「選項3」異常"
            expect = "创建「選項3」能成功"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("7、點擊：[提交投票]-[添加選項]按鈕")
            ntp.click_submit_vote_add_Option()              # 點擊：[提交投票]-[添加選項]按鈕
            case_step = case_step + cbz.case_step("檢查：（選項4）")
            find_Option4 = ntp.find_add_Option4()
            try:
                assert find_Option4 == True
                case_step = case_step + cbz.case_step("檢查成功，添加「選項4」成功")
                logging.info("檢查成功，添加「選項4」成功")
            except:
                actual = "檢查失敗！查找「選項4」異常"
                expect = "创建「選項4」能成功"
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

    # 添加元素:提交投票-时间选项                                                   作者：游同同    时间：2020/4/1
    @allure.title("添加元素:提交投票（时间选项）")  # 用例標題
    @allure.description("添加元素:提交投票时间选项展示是否正常")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_share_label_vote_voting_time(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "添加元素:提交投票时间选项展示是否正常"
        test_chat.temp_num += 1
        case_name = "test_share_label_vote_voting_time"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   添加元素:提交投票时间选项展示是否正常    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、點擊最新動態-全部tab")
        ntp.click_all_tab()                                             # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                               # 點擊：[你在想什麼?]入口
        case_step = case_step + cbz.case_step("4、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("5、點擊：[提交投票]选项")
        ntp.click_submit_vote()                                          # 點擊：[提交投票]选项
        case_step = case_step + cbz.case_step("6、點擊：[投票結束時間]選項")
        ntp.click_vote_end_time()                                    # 點擊：[投票結束時間]選項
        case_step = case_step + cbz.case_step("檢查：")
        time_Option_number = ntp.get_setting_time_Option_number()    # 獲取投票設置結束時間選項個數
        try:
            assert time_Option_number == 6
            case_step = case_step + cbz.case_step("檢查成功，設置投票結束時間共有6個選項")
            logging.info("檢查成功，設置投票結束時間共有6個選項")
        except:
            actual = "檢查失敗！設置投票結束時間目前共有{}個選項".format(time_Option_number)
            expect = "设置投票时间应该有6个选项"
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

    # 添加元素:提交投票-设置3天有效期                                              作者：游同同    时间：2020/4/1
    @allure.title("添加元素:提交投票（设置3天有效期）")  # 用例標題
    @allure.description("添加元素:提交投票设置3天有效期")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_share_label_vote_setting_three_day(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "添加元素:提交投票设置3天有效期"
        test_chat.temp_num += 1
        case_name = "test_share_label_vote_setting_three_day"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   添加元素:提交投票-设置3天有效期    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、點擊最新動態-全部tab")
        ntp.click_all_tab()                                                 # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                                   # 點擊：[你在想什麼?]入口
        case_step = case_step + cbz.case_step("4、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                   # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("5、點擊：[提交投票]选项")
        ntp.click_submit_vote()                                             # 點擊：[提交投票]选项
        case_step = case_step + cbz.case_step("6、點擊：[投票結束時間]選項")
        ntp.click_vote_end_time()                                           # 點擊：[投票結束時間]選項
        case_step = case_step + cbz.case_step("7、點擊：「3天」時間選項")
        ntp.click_list_time_days(1)                                 # 點擊：「3天」時間選項
        case_step = case_step + cbz.case_step("8、點擊2次[添加選項]按鈕")
        ntp.click_submit_vote_add_Option()                          # 點擊2次[添加選項]按鈕
        time.sleep(1)
        ntp.click_submit_vote_add_Option()
        title = CD.vote_title + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("9、輸入投票標題")
        ntp.input_vote_title(0, title)                              # 輸入投票標題
        text = CD.vote_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("10、輸入投票內容'{}'".format(text))
        time.sleep(1)
        ntp.input_vote_title(1, text)                               # 輸入投票內容
        case_step = case_step + cbz.case_step("11、輸入投票選項A、B、C、D")
        ntp.input_vote_title(2, "A")
        ntp.input_vote_title(3, "B")
        ntp.input_vote_title(4, "C")
        ntp.input_vote_title(5, "D")
        case_step = case_step + cbz.case_step("12、點擊：提交投票-「可多選」開關icon")
        ntp.click_multiple_choice_off()                             # 點擊：提交投票-「可多選」開關icon
        case_step = case_step + cbz.case_step("13、點擊：分享「群組」跳轉按鈕")
        case_step = case_step + "<br/>點擊：分享「群組」跳轉按鈕"
        ntp.click_share_group()                                     # 點擊：分享「群組」跳轉按鈕
        list_number = ntp.get_share_list_number()                   # 分享可选群组个数
        random_number = ntp.random_int(list_number-1)
        logging.info("可分享群组个数为：{}".format(list_number))
        case_step = case_step + cbz.case_step("14、點擊第{}個群組".format(random_number+1))
        ntp.click_random_Object_one(random_number)                  # 隨機點擊一個群組
        case_step = case_step + cbz.case_step("15、點擊：「發帖」按鈕")
        ntp.click_publish_button()                                  # 點擊：「發帖」按鈕
        case_step = case_step + cbz.case_step("检查：(投票标题)")
        vote_title = ntp.get_vote_title_text()
        try:
            assert vote_title == title
            case_step = case_step + cbz.case_step("检查成功，投票标题展示正确")
            logging.info("检查成功，投票标题展示正确")
        except:
            actual = "检查失败！编辑的投票标题为'{}'，实际展示的标题为'{}'".format(title,vote_title)
            expect = "投票标题应该为'{}'".format(title)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("检查：(投票内容)")
            vote_text = ntp.get_post_vote_text()
            try:
                assert vote_text == text
                case_step = case_step + cbz.case_step("檢查成功，投票內容展示正确")
                logging.info("檢查成功，投票內容展示正确")
            except:
                actual = "检查失败！编辑的投票內容为'{}'，实际展示的內容为'{}'".format(text, vote_text)
                expect = "投票内容应该为'{}'".format(text)
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                       "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("检查：(投票選項)")
                vote_Option_text = ntp.get_post_vote_Option_text()
                try:
                    assert vote_Option_text == "A"
                    case_step = case_step + cbz.case_step("檢查成功，投票選項展示正确")
                    logging.info("檢查成功，投票選項展示正确")
                except:
                    actual = "檢查失敗！編輯第一個選項內容為'{}'，實際為'{}'".format("A", vote_Option_text)
                    expect = "投票第一個選項应该为'{}'".format("A")
                    video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ntp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                           "最新動態")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
                else:
                    case_step = case_step + cbz.case_step("投票有效期检查：")
                    vote_end_time = ntp.get_vote_end_time()  # 投票截止时间
                    day_n_time = ntp.get_n_end_time(3)  # 3天后日期
                    try:
                        assert vote_end_time == day_n_time
                        case_step = case_step + cbz.case_step("检查成功，设置投票有效期至{0}，实际展示有效期为{1}".format(day_n_time, vote_end_time))
                        logging.info("检查成功，设置投票有效期至{0}，实际展示有效期为{1}".format(day_n_time, vote_end_time))
                    except:
                        actual = "检查失败！3天后时间为{0}，实际展示有效期至{1}".format(day_n_time, vote_end_time)
                        expect = "3天后时间应该为{0}".format(day_n_time)
                        video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                        case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                        ntp.screenshot(actual)
                        with allure.step(actual):
                            # 调用禅道api，报BUG单
                            bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                               "最新動態")  # 传入BUG标题，BUG复现步骤
                            with allure.step(bug_link):
                                raise

    # 添加元素:提交投票-设置永久有效期                                              作者：游同同    时间：2020/4/1
    @allure.title("添加元素:提交投票（设置永久有效期）")  # 用例標題
    @allure.description("添加元素:提交投票设置永久有效期")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_share_label_vote_setting_lasting(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "添加元素:提交投票设置永久有效期"
        test_chat.temp_num += 1
        case_name = "test_share_label_vote_setting_lasting"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   添加元素:提交投票-设置永久有效期    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、點擊最新動態-全部tab")
        ntp.click_all_tab()                                             # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                               # 點擊：[你在想什麼?]入口
        case_step = case_step + cbz.case_step("4、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                               # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("5、點擊：[提交投票]选项")
        ntp.click_submit_vote()                                         # 點擊：[提交投票]选项
        case_step = case_step + cbz.case_step("6、點擊：[投票結束時間]選項")
        ntp.click_vote_end_time()                                     # 點擊：[投票結束時間]選項
        case_step = case_step + cbz.case_step("7、點擊：「永久」時間選項")
        ntp.click_list_time_days(-1)                                  # 點擊：「永久」時間選項
        case_step = case_step + cbz.case_step("8、點擊[添加選項]按鈕")
        ntp.click_submit_vote_add_Option()                            # 點擊[添加選項]按鈕
        title = CD.vote_title + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("9、輸入投票標題'{}'".format(title))
        ntp.input_vote_title(0, title)                               # 輸入投票標題
        text = CD.vote_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("10、輸入投票內容'{}'".format(text))
        time.sleep(1)
        ntp.input_vote_title(1, text)                                # 輸入投票內容
        case_step = case_step + cbz.case_step("11、輸入投票選項A、B、C")
        ntp.input_vote_title(2, "A")
        ntp.input_vote_title(3, "B")
        ntp.input_vote_title(4, "C")
        case_step = case_step + cbz.case_step("12、點擊：提交投票-「可多選」開關icon")
        ntp.click_multiple_choice_off()                               # 點擊：提交投票-「可多選」開關icon
        case_step = case_step + cbz.case_step("13、點擊：分享「群組」跳轉按鈕")
        ntp.click_share_group()                                       # 點擊：分享「群組」跳轉按鈕
        list_number = ntp.get_share_list_number()                     # 分享可选群组个数
        random_number = ntp.random_int(list_number-1)
        logging.info("可分享群组个数为：{}".format(list_number))
        case_step = case_step + cbz.case_step("14、點擊第{}個群組".format(random_number + 1))
        ntp.click_random_Object_one(random_number)                    # 隨機點擊一個群組
        case_step = case_step + cbz.case_step("15、點擊：「發帖」按鈕")
        ntp.click_publish_button()                                    # 點擊：「發帖」按鈕
        case_step = case_step + cbz.case_step("检查①：(投票标题)")
        vote_title = ntp.get_vote_title_text()
        try:
            assert vote_title == title
            case_step = case_step + cbz.case_step("检查成功，投票标题展示正确")
            logging.info("检查成功，投票标题展示正确")
        except:
            actual = "检查失败！编辑的投票标题为'{}'，实际展示的标题为'{}'".format(title, vote_title)
            expect = "投票标题应该为'{}'".format(title)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("检查②：(投票内容)")
            vote_text = ntp.get_post_vote_text()
            try:
                assert vote_text == text
                case_step = case_step + cbz.case_step("檢查成功，投票內容展示正确")
                logging.info("檢查成功，投票內容展示正确")
            except:
                actual = "检查失败！编辑的投票內容为'{}'，实际展示的內容为'{}'".format(text, vote_text)
                expect = "投票內容应该为'{}'".format(text)
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                       "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("检查③：(投票選項)")
                vote_Option_text = ntp.get_post_vote_Option_text()
                try:
                    assert vote_Option_text == "A"
                    case_step = case_step + cbz.case_step("檢查成功，投票選項展示正确")
                    logging.info("檢查成功，投票選項展示正确")
                except:
                    actual = "檢查失敗！編輯第一個選項內容為'{}'，實際為'{}'".format("A", vote_Option_text)
                    expect = "第一個選項內容应该為'{}'".format("A")
                    video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ntp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                           "最新動態")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
                else:
                    case_step = case_step + cbz.case_step("检查④：投票有效期")
                    vote_end_time = ntp.get_vote_end_time()  # 投票截止时间
                    try:
                        assert vote_end_time == '永久'
                        case_step = case_step + cbz.case_step("检查成功，设置投票有效期為'永久'，实际展示有效期为'{}'".format(vote_end_time))
                        logging.info("检查成功，设置投票有效期為'永久'，实际展示有效期为'{}'".format(vote_end_time))
                    except:
                        actual = "检查失败！设置投票有效期為'永久'，實際為'{}'".format(vote_end_time)
                        expect = "投票有效期应该為'永久'"
                        video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                        case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                        ntp.screenshot(actual)
                        with allure.step(actual):
                            # 调用禅道api，报BUG单
                            bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],"最新動態")  # 传入BUG标题，BUG复现步骤
                            with allure.step(bug_link):
                                raise

    # 拍照:圖片                                                                 作者：游同同    时间：2020/4/1
    @allure.title("拍照:圖片")  # 用例標題
    @allure.description("拍照:拍攝照片能夠發送成功")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_share_label_photo_and_text(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "拍照:拍攝照片能夠發送成功"
        test_chat.temp_num += 1
        case_name = "test_share_label_photo_and_text"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   拍照:圖片    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、点击最新动态-全部tab")
        ntp.click_all_tab()                                             # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                               # 點擊：[你在想什麼?]入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                        # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                               # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：【拍照】选项")
        ntp.click_action_photo()                                        # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("7、點擊：快門icon")
        ntp.click_personal_tab_shutter_button()                         # 點擊：快門icon
        case_step = case_step + cbz.case_step("8、點擊：拍照頁面-「傳送」按鈕")
        ntp.click_personal_tab_send_button()                            # 點擊：拍照頁面-「傳送」按鈕
        case_step = case_step + cbz.case_step("9、點擊：「發帖」按鈕")
        ntp.click_publish_button()                                      # 點擊：「發帖」按鈕
        case_step = case_step + cbz.case_step("检查：")
        send_post_text = ntp.get_all_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布'{}'照片到個人動態成功".format(post_text))
            logging.info("檢查成功，發布'{}'照片到個人動態成功".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'照片到個人動態異常".format(post_text)
            expect = "發布照片到個人動態能夠成功"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.process_send_failure()              # 处理发送图片失败，退出回到首页

    # 拍照:視頻                                                                  作者：游同同    时间：2020/4/1
    @pytest.mark.debug
    @allure.title("拍照:視頻")  # 用例標題
    @allure.description("拍照:拍攝視頻能夠發送成功")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_share_label_video_and_text(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "拍照:拍攝視頻能夠發送成功"
        test_chat.temp_num += 1
        case_name = "test_share_label_video_and_text"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   拍照:視頻    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、点击最新动态-全部tab")
        ntp.click_all_tab()                                             # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                               # 點擊：[你在想什麼?]入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                        # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                               # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：【拍照】选项")
        ntp.click_action_photo()                                        # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("7、長按：拍攝視頻4s")
        ntp.long_tap_personal_tab_shutter_button()                      # 長按：拍攝視頻4s
        case_step = case_step + cbz.case_step("8、點擊：拍照頁面-「傳送」按鈕")
        ntp.click_personal_tab_send_button()                            # 點擊：拍照頁面-「傳送」按鈕
        case_step = case_step + cbz.case_step("9、點擊：「發帖」按鈕")
        ntp.click_publish_button()                                      # 點擊：「發帖」按鈕
        case_step = case_step + cbz.case_step("检查：")
        send_post_text = ntp.get_all_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布'{}'視頻到個人動態成功".format(post_text))
            logging.info("檢查成功，發布'{}'視頻到個人動態成功".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'視頻到個人動態異常".format(post_text)
            expect = "發布視頻到個人動態能夠成功"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.process_send_failure()  # 处理发送图片失败，退出回到首页

    @pytest.mark.demotest
    # 拍照:图片+視頻                                                             作者：游同同    时间：2020/4/1
    @allure.title("拍照:文本+图片+視頻")  # 用例標題
    @allure.description("拍照:文本+拍攝图片+視頻能夠發送成功")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_share_label_video__and_photo_and_text(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "拍照:文本+拍攝图片+視頻能夠發送成功"
        test_chat.temp_num += 1
        case_name = "test_share_label_video__and_photo_and_text"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   拍照:图片+視頻    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、点击最新动态-全部tab")
        ntp.click_all_tab()                                             # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                               # 點擊：[你在想什麼?]入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                        # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：[個人動態]跳转按钮")
        ntp.click_personal_dynamic()                                    # 點擊：[個人動態]跳转按钮
        list_number = ntp.get_share_list_number()                       # 分享可选群组个数
        if list_number >= 2:
            random_index = ntp.random_int_one(list_number-1)
            case_step = case_step + cbz.case_step("6、點擊第{}個分享群組對象後點擊「完成」按鈕".format(random_index))
            ntp.click_random_index_Object(random_index)             # 隨機點擊一個群組對象後點擊「完成」按鈕
            case_step = case_step + cbz.case_step("7、點擊：建立贴文页面- [公開帖文]下拉列表-[私密貼文]選項")
            ntp.click_public_post_buttn()                           # 點擊：建立贴文页面- [公開帖文]下拉列表-[私密貼文]選項
        case_step = case_step + cbz.case_step("8、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                           # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("9、點擊：【拍照】选项")
        ntp.click_action_photo()                                    # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("10、點擊：快門icon")
        ntp.click_personal_tab_shutter_button()                     # 點擊：快門icon
        case_step = case_step + cbz.case_step("11、點擊：拍照頁面-「傳送」按鈕")
        ntp.click_personal_tab_send_button()                        # 點擊：拍照頁面-「傳送」按鈕
        case_step = case_step + cbz.case_step("12、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                           # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("13、點擊：【拍照】选项")
        ntp.click_action_photo()                                    # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("14、長按：拍攝視頻4s")
        ntp.long_tap_personal_tab_shutter_button()                  # 長按：拍攝視頻4s
        case_step = case_step + cbz.case_step("15、點擊：拍照頁面-「傳送」按鈕")
        ntp.click_personal_tab_send_button()                        # 點擊：拍照頁面-「傳送」按鈕
        case_step = case_step + cbz.case_step("16、點擊：「發帖」按鈕")
        ntp.click_publish_button()                                  # 點擊：「發帖」按鈕
        case_step = case_step + cbz.case_step("检查：")
        send_post_text = ntp.get_all_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布'{}'+照片+视频到群组成功".format(post_text))
            logging.info("檢查成功，發布'{}'+照片+视频到群组成功".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'+照片+视频到群组異常".format(post_text)
            expect = "發布+照片+视频到群組能夠成功"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.process_send_failure()  # 处理发送图片失败，退出回到首页

    # 添加元素:標註人名                                                           作者：游同同    时间：2020/3/30
    @allure.title("添加元素:標註人名")  # 用例標題
    @allure.description("添加元素:標註人名")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_share_label_person(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "添加元素:標註人名"
        test_chat.temp_num += 1
        case_name = "test_share_label_person"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   添加元素:標註人名    *********")
        ntp.click_newdynamic()                                  # 點擊：【最新动态】
        ntp.click_nf_personal_tab()                             # 點擊：【個人】tab
        trace_count = ntp.get_personal_trace_count()            # 获取個人tab追踪中数量
        if trace_count <= 2:
            ntp.click_personal_trace()                              # 點擊：個人tab「追踪中」
            ntp.click_trace_more_icon()                             # 點擊：「追蹤更多」跳轉
            ntp.click_trace_more_personal_tab()                     # 點擊：'追蹤更多'頁面-「個人」tab
            index = ntp.get_list_one_personal_track_index()         # 第一个【追蹤】按钮索引
            user_name = ntp.get_list_one_personal_track_name(index)    # 獲取第一個可追蹤的用戶名並點擊「追蹤」按鈕
            time.sleep(1)
            ntp.return_button()  # 點擊:返回按鈕
            ntp.return_button()
        else:
            ntp.click_personal_trace()                              # 點擊：個人tab「追踪中」
            ntp.delete_personal_trace_user()                        # 删除多余的追踪个人或群组，分别保留2个
            ntp.return_button()
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、点击最新动态-全部tab")
        ntp.click_all_tab()                                                 # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                                   # 點擊：[你在想什麼?]入口
        case_step = case_step + cbz.case_step("4、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                               # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("5、點擊：【标注人名】选项")
        ntp.click_callout_name()                                        # 點擊：【标注人名】选项
        list_one_name = ntp.get_callout_name_page_list_name()           # 獲取列表第一個用戶暱稱
        case_step = case_step + cbz.case_step("6、點擊：'标注人名'頁面-列表第一個用戶")
        ntp.click_callout_name_page_list_name()                         # 點擊：'标注人名'頁面-列表第一個用戶
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("7、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                        # 輸入文本
        case_step = case_step + cbz.case_step("8、點擊：「發布」按鈕")
        ntp.click_post_publish_button()                                 # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查①：")
        send_post_text = ntp.get_all_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布'{}'到個人動態成功".format(post_text))
            logging.info("檢查成功，發布'{}'到個人動態成功".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'到個人動態異常".format(post_text)
            expect = "發布'{}'到個人動態能够成功".format(post_text)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("检查②：(標註用戶暱稱)")
            get_name = ntp.get_post_user_name()  # 獲取帖子的展示用戶暱稱
            try:
                assert list_one_name.find(get_name) != -1
                case_step = case_step + cbz.case_step("檢查成功，帖子展示用戶名稱中包含標註人名'{}'".format(list_one_name))
                logging.info("檢查成功，帖子展示用戶名稱中包含標註人名'{}'".format(list_one_name))
            except:
                actual = "檢查失敗！帖子展示用戶名稱中沒有包含標註人名'{}'".format(list_one_name)
                expect = "發布的帖子應該有展示標註的人名'{}'".format(list_one_name)
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                       "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise

    # 添加元素:相片/影片                                                          作者：游同同    时间：2020/3/30
    @allure.title("添加元素:相片/影片")  # 用例標題
    @allure.description("添加元素:相片/影片")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_share_photo_video(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "添加元素:相片/影片"
        test_chat.temp_num += 1
        case_name = "test_share_photo_video"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  添加元素:相片/影片    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、点击最新动态-全部tab")
        ntp.click_all_tab()                                                 # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                                   # 點擊：[你在想什麼?]入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                            # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                   # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：【相片/影片】选项")
        ntp.click_movie_photo()                                             # 點擊：【相片/影片】选项
        case_step = case_step + cbz.case_step("7、選擇9張圖片")
        ntp.click_douber_photo_send_button(9)                           # 選擇9張圖片
        case_step = case_step + cbz.case_step("8、點擊：點擊「傳送」按鈕")
        ntp.click_photo_send_button()                                   # 點擊：點擊「傳送」按鈕
        case_step = case_step + cbz.case_step("9、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                           # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查：")
        send_post_text = ntp.get_all_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布'{}'照片到個人動態成功".format(post_text))
            logging.info("檢查成功，發布'{}'照片到個人動態成功".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'和照片到個人動態異常".format(post_text)
            expect = "發布照片到個人動態能夠成功"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 添加元素:相片/影片(刪除照片後點發布)                                          作者：游同同    时间：2020/3/30
    @allure.title("添加元素:相片/影片(刪除照片後點發布) ")  # 用例標題
    @allure.description("發布動態:添加照片後刪除再發送彈出toast")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_tab_send_cancel_photo(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "添加照片後刪除再發送彈出toast"
        test_chat.temp_num += 1
        case_name = "test_all_tab_send_cancel_photo"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  添加照片後刪除再發送彈出toast    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、点击最新动态-全部tab")
        ntp.click_all_tab()                                                 # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                                   # 點擊：[你在想什麼?]入口
        case_step = case_step + cbz.case_step("4、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                   # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("5、點擊：【相片/影片】选项")
        ntp.click_movie_photo()                                             # 點擊：【相片/影片】选项
        case_step = case_step + cbz.case_step("6、選擇1張圖片")
        ntp.click_douber_photo_send_button(1)                               # 選擇1張圖片
        case_step = case_step + cbz.case_step("7、點擊：點擊「傳送」按鈕")
        ntp.click_photo_send_button()                                       # 點擊：點擊「傳送」按鈕
        case_step = case_step + cbz.case_step("8、點擊：照片刪除按鈕")
        ntp.click_photo_delete_button()                                    # 點擊：照片刪除按鈕
        case_step = case_step + cbz.case_step("9、點擊：「發布」按鈕")
        ntp.click_post_publish_button_no()                                 # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("檢查：")
        is_send_toast = ntp.find_send_text_void_tost()
        try:
            assert is_send_toast == True
            case_step = case_step + cbz.case_step("檢查成功，有彈出'內容不能為空'tost")
            logging.info("檢查成功，有彈出'內容不能為空'tost")
        except:
            actual = "檢查失敗！沒有彈出'內容不能為空'tost"
            expect = "需要彈出toast提示"
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
            ntp.is_click_return_quit_draft()

    # 添加图片超过9张时弹出toast                                                  作者：游同同    时间：2020/3/30
    @allure.title("添加元素:相片/影片(超过9张)")  # 用例標題
    @allure.description("添加元素:相片/影片(超过9张)弹出toast提示")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_tab_share_excess_toast(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "添加元素:相片/影片(超过9张)弹出toast提示"
        test_chat.temp_num += 1
        case_name = "test_all_tab_share_excess_toast"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  添加元素:相片/影片(超过9张)弹出toast提示    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、点击最新动态-全部tab")
        ntp.click_all_tab()                                                 # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                                   # 點擊：[你在想什麼?]入口
        case_step = case_step + cbz.case_step("4、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                   # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("5、點擊：【相片/影片】选项")
        ntp.click_movie_photo()                                             # 點擊：【相片/影片】选项
        case_step = case_step + cbz.case_step("6、選擇10張圖片")
        ntp.click_douber_photo_send_button(10)                             # 選擇10張圖片
        case_step = case_step + cbz.case_step("檢查：")
        find_toast = ntp.find_fuck_photo_sum_tost()
        try:
            assert find_toast == True
            case_step = case_step + cbz.case_step("檢查成功，選擇第10張圖片時有彈出toast提示")
            logging.info("檢查成功，選擇第10張圖片時有彈出toast提示")
        except:
            actual = "檢查失敗！選擇第10張圖片時沒有彈出'最多只能選擇9張'toast"
            expect = "需要彈出toast提示"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.click_photo_page_cancel_button()
            ntp.return_button()

    # 添加元素:相片/影片(隨機選中一張發送)                                           作者：游同同    时间：2020/3/30
    @allure.title("發布動態:添加元素-相片/影片")  # 用例標題
    @allure.description("發布動態:隨機選中一張照片發送")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_tab_send_random_photo(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "發布動態:隨機選中一張照片發送"
        test_chat.temp_num += 1
        case_name = "test_all_tab_send_random_photo"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  添加元素:相片/影片(隨機選中一張發送)    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、点击最新动态-全部tab")
        ntp.click_all_tab()                                         # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                           # 點擊：[你在想什麼?]入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本")
        ntp.input_post_inptu_box_text(post_text)                    # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                           # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：【相片/影片】选项")
        ntp.click_movie_photo()                                     # 點擊：【相片/影片】选项
        sum_photo = ntp.get_photo_sum()                             # 獲取當前頁面照片數量
        index = ntp.random_int(sum_photo-1)
        case_step = case_step + cbz.case_step("7、選擇第{}張圖片".format(index + 1))
        ntp.click_index_photo(index)                                # 點擊其中一張圖片
        case_step = case_step + cbz.case_step("8、點擊：點擊「傳送」按鈕")
        ntp.click_photo_send_button()                               # 點擊：點擊「傳送」按鈕
        case_step = case_step + cbz.case_step("9、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                        # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查：")
        send_post_text = ntp.get_all_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布'{}'照片到個人動態成功".format(post_text))
            logging.info("檢查成功，發布'{}'照片到個人動態成功".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'照片到個人動態異常".format(post_text)
            expect = "發布照片到個人動態能夠成功"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.process_send_failure()  # 处理发送图片失败，退出回到首页

    # 存為草稿                                                                   作者：游同同    时间：2020/3/30
    @allure.title("存為草稿")  # 用例標題
    @allure.description("編輯帖子退出時挽留操作-存為草稿功能")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_tab_post_save_draft(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "編輯帖子退出時挽留操作-存為草稿功能"
        test_chat.temp_num += 1
        case_name = "test_all_tab_post_save_draft"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  編輯帖子退出時挽留操作-存為草稿功能     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、点击最新动态-全部tab")
        ntp.click_all_tab()                                                     # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                                       # 點擊：[你在想什麼?]入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                                 # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                        # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：【标注人名】选项")
        ntp.click_callout_name()                                                 # 點擊：【标注人名】选项
        list_one_name = ntp.get_callout_name_page_list_name()  # 獲取列表第一個用戶暱稱
        case_step = case_step + cbz.case_step("7、點擊：'标注人名'頁面-列表第一個用戶")
        ntp.click_callout_name_page_list_name()                                  # 點擊：'标注人名'頁面-列表第一個用戶
        case_step = case_step + cbz.case_step("8、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                        # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("9、點擊：【拍照】选项")
        ntp.click_action_photo()                                                 # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("10、長按：拍攝視頻4s")
        ntp.long_tap_personal_tab_shutter_button()                               # 長按：拍攝視頻4s
        case_step = case_step + cbz.case_step("11、點擊：拍照頁面-「傳送」按鈕")
        ntp.click_personal_tab_send_button()                                     # 點擊：拍照頁面-「傳送」按鈕
        case_step = case_step + cbz.case_step("12、點擊：返回")
        ntp.return_button()                                              # 點擊：返回
        if_find = ntp.find_save_draft_button()                           # 查找：[存為草稿]按鈕
        case_step = case_step + cbz.case_step("检查①：")
        try:
            assert if_find == True
            case_step = case_step + cbz.case_step("檢查成功，返回時有彈出[存為草稿]按鈕")
            logging.info("檢查成功，返回時有彈出[存為草稿]按鈕")
        except:
            actual = "檢查失敗！點擊返回退出編輯時沒有彈出[存為草稿]按鈕"
            expect = "編寫文本時退出需要彈出[存為草稿]按鈕"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("13、點擊：[存為草稿]按鈕")
            ntp.click_save_draft_button()                               # 點擊：[存為草稿]按鈕
            case_step = case_step + cbz.case_step("14、點擊：'你在想什麼?'發帖入口")
            ntp.click_publish_dynamic()                                  # 點擊：'你在想什麼?'發帖入口
            case_step = case_step + cbz.case_step("检查②：")
            get_text = ntp.get_post_inptu_box_text()
            try:
                assert get_text == post_text
                case_step = case_step + cbz.case_step("檢查成功，[存為草稿]功能正常")
                logging.info("檢查成功，[存為草稿]功能正常")
            except:
                actual = "檢查失敗，[存為草稿]功能異常，上次操作文本為'{}'，實際文本為'{}'".format(post_text,get_text)
                expect = "再次回到編輯帖子時有保存上次的操作文本'{}'".format(post_text)
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("15、點擊：「發布」按鈕")
                ntp.click_post_photo_publish_button()             # 點擊：「發布」按鈕
                case_step = case_step + cbz.case_step("检查：")
                case_step = case_step + "<br/>检查："
                find_toast = ntp.find_toast_send_success()
                try:
                    assert find_toast == True
                    case_step = case_step + cbz.case_step("檢查成功，發布帖子成功有獲取到'發布成功'toast提示")
                    logging.info("檢查成功，發布帖子成功有獲取到'發布成功'toast提示")
                except:
                    actual = "檢查失敗！未獲取到'發布成功'toast提示"
                    expect = "發布成功並有展示'發布成功'toast提示"
                    video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ntp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                           "最新動態")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise

    # 放棄發布                                                                   作者：游同同    时间：2020/3/30
    @allure.title("放棄發布")  # 用例標題
    @allure.description("編輯帖子退出時挽留操作-放棄發布功能")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_tab_abandon_post(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "編輯帖子退出時挽留操作-放棄發布功能"
        test_chat.temp_num += 1
        case_name = "test_all_tab_abandon_post"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  編輯帖子退出時挽留操作-放棄發布功能     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、點擊最新動態-全部tab")
        ntp.click_all_tab()                                             # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                               # 點擊：[你在想什麼?]入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                    # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：返回")
        ntp.return_button()                                         # 點擊：返回
        if_find = ntp.find_abandon_post_button()                      # 查找：[放棄發布]按鈕
        case_step = case_step + cbz.case_step("检查①：")
        try:
            assert if_find == True
            case_step = case_step + cbz.case_step("檢查成功，返回時有彈出[放棄發布]按鈕")
            logging.info("檢查成功，返回時有彈出[放棄發布]按鈕")
        except:
            actual = "檢查失敗！點擊返回退出編輯時沒有彈出[放棄發布]按鈕示"
            expect = "退出帖子编辑时有弹出[放棄發布]按钮"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("6、點擊：[放棄發布]按鈕")
            ntp.click_abandon_post_button()                       # 點擊：[放棄發布]按鈕
            case_step = case_step + cbz.case_step("7、點擊：'你在想什麼?'發帖入口")
            ntp.click_publish_dynamic()                         # 點擊：'你在想什麼?'發帖入口
            case_step = case_step + cbz.case_step("检查②：")
            get_text = ntp.get_post_inptu_box_text()
            try:
                assert get_text == '請輸入想要分享的內容'
                case_step = case_step + cbz.case_step("檢查成功，[放棄發布]功能正常")
                logging.info("檢查成功，[放棄發布]功能正常")
            except:
                actual = "檢查失敗，[放棄發布]功能異常，上次操作文本為'{}'，實際文本為'{}'".format(post_text,get_text)
                expect = "保留上次编辑记录，文本应该为'{}'".format(post_text)
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

    # 發布                                                                       作者：游同同    时间：2020/3/30
    @allure.title("發布")  # 用例標題
    @allure.description("編輯帖子發布功能")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_tab_send_photo_post(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "編輯帖子發布功能"
        test_chat.temp_num += 1
        case_name = "test_all_tab_send_photo_post"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  編輯帖子發布功能     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、点击最新动态-全部tab")
        ntp.click_all_tab()                                                 # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：[你在想什麼?]入口")
        ntp.click_all_tab_post_entrance()                                   # 點擊：[你在想什麼?]入口
        case_step = case_step + cbz.case_step("4、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                   # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("5、點擊：【拍照】选项")
        ntp.click_action_photo()                                            # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("6、長按：拍攝視頻4s")
        ntp.long_tap_personal_tab_shutter_button()                          # 長按：拍攝視頻4s
        case_step = case_step + cbz.case_step("7、點擊：拍照頁面-「傳送」按鈕")
        ntp.click_personal_tab_send_button()                                # 點擊：拍照頁面-「傳送」按鈕
        case_step = case_step + cbz.case_step("8、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                    # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("9、點擊：【标注人名】选项")
        ntp.click_callout_name()                                            # 點擊：【标注人名】选项
        list_one_name = ntp.get_callout_name_page_list_name()               # 獲取列表第一個用戶暱稱
        case_step = case_step + cbz.case_step("10、點擊：'标注人名'頁面-列表第一個用戶")
        ntp.click_callout_name_page_list_name()                             # 點擊：'标注人名'頁面-列表第一個用戶
        case_step = case_step + cbz.case_step("11、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                           # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("12、點擊：【相片/影片】选项")
        ntp.click_movie_photo()                                     # 點擊：【相片/影片】选项
        sum_photo = ntp.get_photo_sum()  # 獲取當前頁面照片數量
        index = ntp.random_int(sum_photo-1)
        case_step = case_step + cbz.case_step("13、選擇第{}張圖片".format(index+1))
        ntp.click_index_photo(index)                                # 點擊其中一張圖片
        case_step = case_step + cbz.case_step("14、點擊：點擊「傳送」按鈕")
        ntp.click_photo_send_button()                               # 點擊：點擊「傳送」按鈕
        case_step = case_step + cbz.case_step("15、點擊：[個人動態]跳转按钮")
        ntp.click_personal_dynamic()                               # 點擊：[個人動態]跳转按钮
        list_number = ntp.get_share_list_number()                      # 分享可选群组个数
        if list_number >= 2:
            case_step = case_step + cbz.case_step("16、點擊第2個分享對象後點擊「完成」按鈕")
            case_step = case_step + "<br/>點擊第2個分享對象後點擊「完成」按鈕"
            ntp.click_random_Object()                              # 點擊2個分享對象後點擊「完成」按鈕
        case_step = case_step + cbz.case_step("17、點擊：建立贴文页面- [公開帖文]下拉列表-[私密貼文]選項")
        ntp.click_public_post_buttn()                                 # 點擊：建立贴文页面- [公開帖文]下拉列表-[私密貼文]選項
        case_step = case_step + cbz.case_step("18、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                       # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查：")
        find_toast = ntp.find_toast_send_success()
        try:
            assert find_toast == True
            case_step = case_step + cbz.case_step("檢查成功，發布帖子成功有獲取到'發布成功'toast提示")
            logging.info("檢查成功，發布帖子成功有獲取到'發布成功'toast提示")
        except:
            actual = "檢查失敗！發布失敗未獲取到'發布成功'toast提示"
            expect = "發布成功並彈出'發布成功'toast提示"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

@pytest.mark.nf
@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("全部")
@allure.sub_suite("貼文列表")
@allure.feature("最新動態/全部/貼文列表")
@allure.story("貼文列表:相关功能验证")
@pytest.mark.usefixtures("startApp_withReset")
class TestComment:  # 貼文列表

    # 頭像/暱稱/分享到的位置                                           作者：游同同    时间：2020/4/2
    @allure.title("頭像/暱稱/分享到的位置")  # 用例標題
    @allure.description("貼文列表:頭像/暱稱/分享到的位置,点击帖子用戶头像跳转至对应主页")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_share_post_position_homepage(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "貼文列表:頭像/暱稱/分享到的位置"
        test_chat.temp_num += 1
        case_name = "test_all_share_post_position_homepage"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  貼文列表:頭像/暱稱/分享到的位置    *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                      # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                         # 點擊：[全部]tab
        one_user_name = ntp.get_all_tab_user_name()                 # 获取【全部】tab下第一个帖子用戶昵称
        case_step = case_step + cbz.case_step("3、點擊：第一個帖子用戶頭像")
        ntp.click_all_tab_post_user_avatar()                        # 點擊：第一個帖子用戶頭像
        homepage_name = ntp.get_group_or_user_homepage_name()       # 獲取主頁用戶暱稱
        case_step = case_step + cbz.case_step("检查：")
        try:
            assert one_user_name.find(homepage_name) >= 0
            case_step = case_step + cbz.case_step("檢查成功，點擊用戶'{}'头像跳轉主頁正常'".format(one_user_name))
            logging.info("檢查成功，點擊用戶'{}'头像跳轉主頁正常'".format(one_user_name))
        except:
            actual = "檢查失敗！點擊用戶'{}'，實際跳轉主頁為'{}'".format(one_user_name,homepage_name)
            expect = "應該跳轉到對應的用戶主頁"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                   "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.return_button()

    # 發布時間                                                       作者：游同同    时间：2020/4/2
    @allure.title("發布時間")  # 用例標題
    @allure.description("發布時間與當前系統時間小於1分鐘")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_share_time(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "發布時間"
        test_chat.temp_num += 1
        case_name = "test_all_share_time"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  發布時間    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                          # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                             # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("3、點擊：'你在想什麼?'發帖入口")
        ntp.click_publish_dynamic()                                     # 點擊：'你在想什麼?'發帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                        # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                       # 點擊：「發布」按鈕
        share_time = int(ntp.get_system_time().split(':')[-1])      # 獲取當前系統時間-分
        case_step = case_step + cbz.case_step("检查：")
        release_time = ntp.get_release_time()                       # 獲取發帖成功後文案展示時間-分
        try:
            assert release_time - share_time <= 1
            case_step = case_step + cbz.case_step("檢查成功，發布時間正常")
            logging.info("檢查成功，發布時間正常")
        except:
            actual = "檢查失敗！發帖展示時間超過實際發布時間1分鐘"
            expect = "發布時間需在1分鐘沒有效"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 發布的內容:文字                                                 作者：游同同    时间：2020/4/2
    @allure.title("發布的內容:文字")  # 用例標題
    @allure.description("發布的內容:文字校验")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_all_share_data_content(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "發布的內容:文字"
        test_chat.temp_num += 1
        case_name = "test_all_share_data_content"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  發布的內容:文字    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                          # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                             # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("3、點擊：'你在想什麼?'發帖入口")
        ntp.click_publish_dynamic()                                      # 點擊：'你在想什麼?'發帖入口
        inptu_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(inptu_text))
        ntp.input_post_inptu_box_text(inptu_text)                    # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                       # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查：")
        post_text = ntp.get_all_tab_post_text()
        try:
            assert post_text == inptu_text
            case_step = case_step + cbz.case_step("檢查成功，發布'{}'到個人動態成功".format(post_text))
            logging.info("檢查成功，發布'{}'到個人動態成功".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'到個人動態異常".format(inptu_text)
            expect = "發布帖子到個人成功"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 發布的內容:投票                                                 作者：游同同    时间：2020/4/2
    @allure.title("發布的內容:投票")  # 用例標題
    @allure.description("發布的內容:投票内容一致性")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_all_share_vote_content(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "發布的內容:投票"
        test_chat.temp_num += 1
        case_name = "test_all_share_vote_content"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  發布的內容:投票    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                                  # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                                     # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("3、點擊：'你在想什麼?'發帖入口")
        ntp.click_publish_dynamic()                                             # 點擊：'你在想什麼?'發帖入口
        case_step = case_step + cbz.case_step("4、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                      # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("5、點擊：[提交投票]选项")
        ntp.click_submit_vote()                                                # 點擊：[提交投票]选项
        case_step = case_step + cbz.case_step("6、點擊：[投票結束時間]選項")
        ntp.click_vote_end_time()                                              # 點擊：[投票結束時間]選項
        case_step = case_step + cbz.case_step("7、點擊：「3天」時間選項")
        ntp.click_list_time_days(1)                                            # 點擊：「3天」時間選項
        title = CD.vote_title + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("8、輸入投票標題'{}'".format(title))
        ntp.input_vote_title(0,title)                                    # 輸入投票標題
        text = CD.vote_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("9、輸入投票內容'{}'".format(text))
        time.sleep(1)
        ntp.input_vote_title(1,text)                                     # 輸入投票內容
        case_step = case_step + cbz.case_step("10、輸入投票選項A、B")
        ntp.input_vote_title(2,"A")
        ntp.input_vote_title(3,"B")
        case_step = case_step + cbz.case_step("11、點擊：分享「群組」跳轉按鈕")
        ntp.click_share_group()                                          # 點擊：分享「群組」跳轉按鈕
        list_number = ntp.get_share_list_number()                        # 分享可选群组个数
        random_number = ntp.random_int(list_number-1)
        logging.info("可分享群组个数为：{}".format(list_number))
        case_step = case_step + cbz.case_step("12、點擊第{}個群組".format(random_number+1))
        ntp.click_random_Object_one(random_number)                       # 隨機點擊一個群組
        case_step = case_step + cbz.case_step("13、點擊：「發帖」按鈕")
        ntp.click_publish_button()                                       # 點擊：「發帖」按鈕
        case_step = case_step + cbz.case_step("14、點擊：[全部]tab")
        ntp.click_all_tab()                                              # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("检查①：(投票标题)")
        vote_title = ntp.get_vote_title_text()
        try:
            assert vote_title == title
            case_step = case_step + cbz.case_step("检查成功，投票标题展示正确")
            logging.info("检查成功，投票标题展示正确")
        except:
            actual = "检查失败！编辑的投票标题为'{}'，实际展示的标题为'{}'".format(title,vote_title)
            expect = "發布成功的投票標題應該為'{}'".format(title)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("检查②：(投票内容)")
            vote_text = ntp.get_post_vote_text()
            try:
                assert vote_text == text
                case_step = case_step + cbz.case_step("檢查成功，投票內容展示正确")
                logging.info("檢查成功，投票內容展示正确")
            except:
                actual = "检查失败！编辑的投票內容为'{}'，实际展示的內容为'{}'".format(text, vote_text)
                expect = "發布成功的投票內容應該為'{}'".format(text)
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1],
                                                       "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("检查③：(投票選項)")
                vote_Option_text = ntp.get_post_vote_Option_text()
                try:
                    assert vote_Option_text == "A"
                    case_step = case_step + cbz.case_step("檢查成功，投票選項展示正确")
                    logging.info("檢查成功，投票選項展示正确")
                except:
                    actual = "檢查失敗！編輯第一個選項為'{}'，實際為'{}'".format("A", vote_Option_text)
                    expect = "發布成功的投票第一個選項應該為'{}'".format("A")
                    video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ntp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1],
                                                           "最新動態")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise

    # 點讚                                                           作者：游同同    时间：2020/4/2
    @allure.title("點讚")  # 用例標題
    @allure.description("點讚，对自己发布的帖子点赞")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_post_like(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "點讚"
        test_chat.temp_num += 1
        case_name = "test_all_post_like"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  點讚    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                              # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                                 # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("3、點擊：'你在想什麼?'發帖入口")
        ntp.click_publish_dynamic()                                          # 點擊：'你在想什麼?'發帖入口
        inptu_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(inptu_text))
        ntp.input_post_inptu_box_text(inptu_text)                            # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                                # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("6、點擊：全部tab中-帖子文本")
        ntp.click_all_tab_post_text()                                        # 點擊：全部tab中-帖子文本
        like_number = ntp.get_post_detail_like_count_icon()                  # 获取文本：帖子详情页点击次数
        case_step = case_step + cbz.case_step("7、點擊：返回")
        ntp.return_button()
        case_step = case_step + cbz.case_step("8、點擊：給第一個帖子點讚")
        ntp.click_group_tab_list_like_icon()                                # 點擊：給第一個帖子點讚
        case_step = case_step + cbz.case_step("9、點擊：全部tab中-帖子文本")
        ntp.click_all_tab_post_text()                                       # 點擊：全部tab中-帖子文本
        like_Rear_number = ntp.get_post_detail_like_count_icon()            # 點讚後帖子的點讚數
        case_step = case_step + cbz.case_step("检查：")
        try:
            assert like_Rear_number - like_number == 1
            case_step = case_step + cbz.case_step("檢查成功，點讚前共有{}個讚，點讚後共有{}個讚".format(like_number, like_Rear_number))
            logging.info("檢查成功，點讚前共有{}個讚，點讚後共有{}個讚".format(like_number, like_Rear_number))
        except:
            actual = "檢查失敗！點讚前共有{}個讚，點讚後共有{}個讚".format(like_number, like_Rear_number)
            expect = "點讚增加次數應該與實際點讚次數相匹配"
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

    # 幾人點讚/幾個評論/幾次分享:留言                                    作者：游同同    时间：2020/4/2
    @allure.title("幾人點讚/幾個評論/幾次分享:留言")  # 用例標題
    @allure.description("幾人點讚/幾個評論/幾次分享:校驗 “x個留言”是否增加至 “x+3 個留言”")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_post_comments_number(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "幾人點讚/幾個評論/幾次分享:留言"
        test_chat.temp_num += 1
        case_name = "test_post_comments_number"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  幾人點讚/幾個評論/幾次分享:留言     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                              # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                                 # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("3、點擊：'你在想什麼?'發帖入口")
        ntp.click_publish_dynamic()                                         # 點擊：'你在想什麼?'發帖入口
        inptu_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(inptu_text))
        ntp.input_post_inptu_box_text(inptu_text)                          # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                                # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("6、點擊：全部tab中-帖子文本")
        ntp.click_all_tab_post_text()                                       # 點擊：全部tab中-帖子文本
        comments_before_number = ntp.get_post_comment_number_icon()         # 留言前獲取留言次數
        case_step = case_step + cbz.case_step("7、连续3次留言")
        ntp.double_send_messag_text(3,CD.send_message_reply)                # 连续3次留言
        comments_Rear_number = ntp.get_post_comment_number_icon()           # 留言後獲取留言次數
        case_step = case_step + cbz.case_step("檢查：")
        try:
            assert comments_Rear_number - comments_before_number == 3
            case_step = case_step + cbz.case_step("檢查成功，評論次數：留言前'{}'，評論後'{}'".format(comments_before_number,comments_Rear_number))
            logging.info("檢查成功，評論次數：留言前'{}'，評論後'{}'".format(comments_before_number,comments_Rear_number))
        except:
            actual = "檢查失敗！評論次數：留言前'{}'，評論3次後'{}'".format(comments_before_number,comments_Rear_number)
            expect = "留言增加次數應該增加3"
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

    # 幾人點讚/幾個評論/幾次分享:分享                                     作者：游同同    时间：2020/4/2
    @allure.title("幾人點讚/幾個評論/幾次分享:分享")  # 用例標題
    @allure.description("幾人點讚/幾個評論/幾次分享:分享2次，计数是否加2")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_post_share_number(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "幾人點讚/幾個評論/幾次分享:分享"
        test_chat.temp_num += 1
        case_name = "test_post_share_number"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  幾人點讚/幾個評論/幾次分享:分享     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                          # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                             # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("3、點擊：'你在想什麼?'發帖入口")
        ntp.click_publish_dynamic()                                     # 點擊：'你在想什麼?'發帖入口
        inptu_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(inptu_text))
        ntp.input_post_inptu_box_text(inptu_text)                    # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                       # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("6、點擊：全部tab中-帖子文本")
        ntp.click_all_tab_post_text()                               # 點擊：全部tab中-帖子文本
        comments_before_number = ntp.get_post_share_number_icon()   # 分享前獲取分享次數
        case_step = case_step + cbz.case_step("7、點擊： 帖子詳情-分享icon")
        ntp.click_post_page_share_icon()                            # 點擊： 帖子詳情-分享icon
        case_step = case_step + cbz.case_step("8、選擇'分享至sunpeople'并选择第一个对象")
        ntp.click_list_share_sp()                                   # 選擇'分享至sunpeople'
        ntp.click_share_user()                                      # 選中第一个對象分
        case_step = case_step + cbz.case_step("9、點擊： 帖子詳情-分享icon")
        ntp.click_post_page_share_icon()                            # 點擊： 帖子詳情-分享icon
        case_step = case_step + cbz.case_step("10、選擇‘分享’")
        ntp.click_list_share_button()                               # 选择【分享】
        case_step = case_step + cbz.case_step("11、不輸入文本，直接分享")
        ntp.click_share_button()                                    # 不輸入文本，直接點擊分享
        comments_Rear_number = ntp.get_post_share_number_icon()     # 分享后獲取分享次數
        case_step = case_step + cbz.case_step("检查：")
        try:
            assert comments_Rear_number - comments_before_number == 2
            case_step = case_step + cbz.case_step("检查成功，分享两次后计数加2")
            logging.info("检查成功，分享两次后计数加2")
        except:
            actual = "检查失败！分享前计数为'{}'，两次分享后计数为'{}'".format(comments_before_number,
                                                                               comments_Rear_number)
            expect = "被分享的帖子应该增加3次分享计数"
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

    # 評論:點擊留言計數跳轉  testID:8509
    @allure.title("評論:點擊留言計數跳轉")                                                   #用例標題
    @allure.description("評論:查看動態列表中的動態留言，是否成功跳轉至留言詳情頁。")            #用例描述
    @allure.severity(bsc.C[0])                                                      #用例嚴重程度
    def test_click_message_count(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "評論:點擊留言計數跳轉"
        test_chat.temp_num += 1
        case_name = "test_click_message_count"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   評論:点击留言计数跳转  testID:8509 *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                              # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                                 # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("3、點擊第一個動態消息下留言icon")
        ntp.click_one_message_count()                                   # 点击第一个动态消息下“X个留言”
        case_step = case_step + cbz.case_step("检查：")
        try:
            assert ntp.is_find_message_input() == True  # 檢查:True--找到留言输入文本框
            case_step = case_step + cbz.case_step("檢查成功.點擊留言icon後有跳轉至詳情頁")
            logging.info("檢查成功.點擊留言icon後有跳轉至詳情頁")
        except:
            actual = "檢查失敗!!!點擊留言icon後沒有跳轉至詳情頁"
            expect = "點擊留言icon應該跳轉至詳情頁"
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

    # 評論:評論     testID:8501
    @allure.title("評論:評論")
    @allure.description("評論:動態列表中，進行評論操作")
    @allure.severity(bsc.B[0])
    def test_leave_comment(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "評論:動態進行評論"
        test_chat.temp_num += 1
        case_name = "test_leave_comment"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   評論:留言评论     testID:8501 *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                           # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                             # 點擊：[全部]tab
        before_message_time = ntp.get_message_time()                    # 获取第一个动态留言次数
        logging.info("留言前评论个数为:{}".format(before_message_time))
        case_step = case_step + cbz.case_step("3、獲取留言前评论个数为:{}；然後點擊第一個動態中留言icon".format(before_message_time))
        ntp.click_one_message_count()                                    # 点击第一个动态，留言计数
        case_step = case_step + cbz.case_step("4、輸入文本'{}'，點擊發布".format(CD.send_message))
        ntp.send_messag_text(CD.send_message)                           # 输入文本，发布
        case_step = case_step + cbz.case_step("5、點擊返回按鈕")
        ntp.click_message_details_retun_button()                    # 返回上一页面（全部tab）
        later_message_time = ntp.get_message_time()                 # 获取留言完成后留言次数（即第一个动态）
        logging.info("留言后评论个数为:{}".format(later_message_time))
        case_step = case_step + cbz.case_step("6、獲取留言後評論個數變為:{}；並進行檢查".format(later_message_time))
        times = later_message_time - before_message_time            # 檢查:留言后次数-留言前次数 = 1
        logging.info("评论前后个数差为:{}".format(times))
        case_step = case_step + cbz.case_step("檢查：")
        try:
            assert times == 1
            case_step = case_step + cbz.case_step("檢查成功。留言前後評論個數差為1")
            logging.info("檢查成功。留言前後評論個數差為1")
        except:
            actual = "檢查失敗！！留言前後評論個數差為:{}".format(times)
            expect = "留言一次計數加1"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 評論:點讚     testID:8501
    @allure.title("評論:點讚")
    @allure.description("評論:動態列表中，對動態進行點讚操作")
    @allure.severity(bsc.B[0])
    def test_leave_like(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "評論:點讚-動態進行點讚"
        test_chat.temp_num += 1
        case_name = "test_leave_like"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********   評論:点赞     testID:8501 *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                                  # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                                     # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("3、點擊：跳轉帖子詳情頁（暱稱欄）")
        ntp.click_post_user_name()                                          # 點擊：跳轉帖子詳情頁（暱稱欄）
        before_like_time = ntp.get_post_detail_like_count_icon_number()     # 获取第一个动态点赞次数（点赞前）
        logging.info("点赞前赞个数为:{}".format(before_like_time))
        case_step = case_step + cbz.case_step("4、（第一個動態）獲取點擊個數為:{}，並進行點讚操作".format(before_like_time))
        ntp.click_like_button()                                              # 点击【点赞】icon
        later_like_time = ntp.get_post_detail_like_count_icon_number()       # 获取第一个动态点赞次数:点赞后次数
        logging.info("点赞后赞个数为:{}".format(later_like_time))
        case_step = case_step + cbz.case_step("5、點讚（第一個動態）後獲取點讚次數為:{}".format(later_like_time))
        like = abs(later_like_time - before_like_time)                # 檢查:abs(点赞后次数-点赞前次数) = 1     abs--取绝对值
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

    # 評論:二級評論   testID:8499
    @allure.title("評論:二級評論")
    @allure.description("評論:動態詳情頁，對留言進行評論")
    @allure.severity(bsc.C[0])
    def test_comment_reply(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "評論:動態進行點讚"
        test_chat.temp_num += 1
        case_name = "test_comment_reply"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********       評論:回复评论   testID:8499 *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                              # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                                 # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("3、點擊第一個動態留言計數icon")
        ntp.click_one_message_count()                                       # 点击第一个动态留言计数
        case_step = case_step + cbz.case_step("4、輸入文本‘{}’，進行留言".format(CD.send_message_data))
        ntp.send_messag_text(CD.send_message_data)  # 進行留言产生一个数据
        reply_one = ntp.get_message_details_time()  # 获取留言计数
        logging.info("回复评论前评论次数:{}".format(reply_one))
        case_step = case_step + cbz.case_step("5、獲取評論前留言個數為:{},再輸入文本‘{}’留言評論".format(reply_one, CD.send_message_reply))
        ntp.send_comment_reply(CD.send_message_reply)  # 给第一个留言回复
        time.sleep(1)  # 等待1s刷新时间，再次获取留言计数
        reply_two = ntp.get_message_time()  # 回复评论后次数
        logging.info("回复评论后评论次数:{}".format(reply_two))
        case_step = case_step + cbz.case_step("6、對留言進行回復後，評論計數個數為:{}".format(reply_two))
        reply = reply_two - reply_one  # 檢查:留言回复后计数-留言回复前计数 = 1
        logging.info("对留言回复前后差为:{}".format(reply))
        case_step = case_step + cbz.case_step("檢查：")
        try:
            assert reply == 1
            case_step = case_step + cbz.case_step("檢查成功。留言成功")
            logging.info("檢查成功。留言成功")
        except:
            actual = "留言失敗！回復評論失敗或回復評論後沒有計數！"
            expect = "對留言進行評論後計數加1"
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

@pytest.mark.nf
@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("全部")
@allure.sub_suite("貼文列表")
@allure.feature("最新動態/全部/貼文列表")
@allure.story("分享:模块相关功能")
@pytest.mark.usefixtures("startApp_withReset")
class TestShare:  # 貼文列表

    # 分享到最新動態（含文本）
    @allure.title("分享到最新動態:含文本")
    @allure.description("分享時輸入文本內容進行到個人動態")
    @allure.severity(bsc.B[0])
    def test_share_text_personal_updates(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "asd最新動態/全部/貼文列表-分享:分享（有文本）至個人動態"
        test_chat.temp_num += 1
        case_name = "test_share_text_personal_updates"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info('********    分享-分享（有文本）至個人動態   testID:8540 *********')
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                          # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                             # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("3、點擊第一個可分享動態分享icon")
        ntp.click_one_share_icon()                                      # 点击第一个可分享动态分享icon
        case_step = case_step + cbz.case_step("4、選擇‘分享’")
        ntp.click_list_share_button()                                   # 选择【分享】
        case_step = case_step + cbz.case_step("5、輸入文本‘{}’，點擊分享".format(CD.share_text))
        ntp.input_text_share(CD.share_text)                             # 輸入文本，點擊分享
        case_step = case_step + cbz.case_step("檢查：")
        try:  # “分享”檢查:彈出分享成功toast提示
            assert ntp.get_share_toast() == True
            case_step = case_step + cbz.case_step("‘分享’檢查成功。有彈出toast提示")
            logging.info("‘分享’檢查成功。有彈出toast提示")
        except:
            actual = "'分享'檢查失敗！！沒有彈出分享成功toast提示"
            expect = "分享成功並彈出toast提示"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 分享到最新動態（文本为空）
    @allure.title("分享到最新動態:文本为空")
    @allure.description("分享時不輸入內容直接分享到個人動態")
    @allure.severity(bsc.C[0])
    def test_share_personal_updates(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "最新動態/全部/貼文列表-分享:分享（輸入內容為空）至個人動態"
        test_chat.temp_num += 1
        case_name = "test_share_personal_updates"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info('********    分享:分享到最新動態（文本为空） *********')
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                          # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                             # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("3、點擊第一個可分享動態分享icon")
        ntp.click_one_share_icon()                                  # 点击第一个可分享动态分享icon
        case_step = case_step + cbz.case_step("4、選擇‘分享’")
        ntp.click_list_share_button()                               # 选择【分享】
        case_step = case_step + cbz.case_step("5、不輸入文本，直接分享")
        ntp.click_share_button()                                    # 不輸入文本，直接點擊分享
        ntp.screenshot("分享（輸入內容為空）至個人動態，點擊分享後立刻截圖")
        case_step = case_step + cbz.case_step("檢查:")
        find_toast = ntp.get_share_toast()
        try:                                                        # “分享”檢查:彈出分享成功toast提示
            assert find_toast == True
            case_step = case_step + cbz.case_step("‘分享’檢查成功。有彈出toast提示")
            logging.info("‘分享’檢查成功。有彈出toast提示")
        except:
            actual = "'分享'檢查失敗！！沒有彈出分享成功toast提示"
            expect = "分享成功並彈出toast提示"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 分享-分享至sunpeople   testID:8540
    @allure.title("分享到sunpeople chat")
    @allure.description("分享到sunpeople chat")
    @allure.severity(bsc.B[0])
    def test_share_sunpeple(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "最新動態/全部/貼文列表-分享:‘分享至sunpeople’"
        test_chat.temp_num += 1
        case_name = "test_share_sunpeple"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info('********    分享:分享到sunpeople chat   *********')
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                              # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                                 # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("3、點擊第一個可分享動態分享icon")
        ntp.click_one_share_icon()                                          # 点击第一个可分享动态分享icon
        case_step = case_step + cbz.case_step("4、選擇‘分享至sunpeople’")
        ntp.click_list_share_sp()                                           # 選擇“分享至sunpeople"
        case_step = case_step + cbz.case_step("5、選中第一個對象分享")
        ntp.click_share_user()                                               # 選中第一惡對象分享
        ntp.screenshot("选择分享对象后，立刻截图")
        case_step = case_step + cbz.case_step("檢查：")
        find_toast = ntp.get_share_toast()
        try:  # “分享至sunpeople”檢查:彈出分享成功toast提示
            assert find_toast == True
            case_step = case_step + cbz.case_step("‘分享至sunpeople’檢查成功。有彈出toast提示")
            logging.info("‘分享至sunpeople’檢查成功。有彈出toast提示")
        except:
            actual = "'分享至sunpeople'檢查失敗！！沒有彈出分享成功toast提示"
            expect = "分享成功並彈出toast提示"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 分享計數詳情頁
    @allure.title("分享計數詳情頁")
    @allure.description("分享-分享計數詳情頁,展示分享者列表")
    @allure.severity(bsc.C[0])
    def test_share_count(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "最新動態/全部/貼文列表-分享:分享計數詳情頁"
        test_chat.temp_num += 1
        case_name = "test_share_count"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info('******** 分享:分享計數詳情頁  *********')
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                          # 點擊：[最新動態]tab
        case_step = case_step + cbz.case_step("2、點擊：[全部]tab")
        ntp.click_all_tab()                                             # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("3、點擊：跳轉帖子詳情頁（暱稱欄）")
        ntp.click_post_user_name()                                       # 點擊：跳轉帖子詳情頁（暱稱欄）
        case_step = case_step + cbz.case_step("4、點擊： 帖子詳情-分享icon")
        ntp.click_post_page_share_icon()                                 # 點擊： 帖子詳情-分享icon
        case_step = case_step + cbz.case_step("5、選擇'分享至sunpeople'")
        ntp.click_list_share_sp()                                         # 選擇'分享至sunpeople'
        ntp.click_share_user()                                           # 選中第一惡對象分
        share_number = ntp.get_share_time()  # 獲取分享計數的次數
        case_step = case_step + cbz.case_step("6、獲取分享次數:{},然後點擊分享計數".format(share_number))
        ntp.click_share_time()                                           # 點擊分享計數
        user_number = ntp.get_actual_share_time()                        # 分享帖子頁:獲取用戶總數
        case_step = case_step + cbz.case_step("6、分享帖子頁獲取用戶數為:{},然後進行檢查:".format(user_number))
        try:
            assert share_number == user_number
            case_step = case_step + cbz.case_step("6、檢查成功，展示分享計數詳情頁正常")
            logging.info("檢查成功，展示分享計數詳情頁正常")
        except:
            actual = "檢查失敗！！展示分享計數詳情頁錯誤"
            expect = "展示分享計數詳情正常"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.return_button_one()

    # 個人tab-對自己發的帖子進行分享
    @allure.title("個人tab-對自己發的帖子進行分享")
    @allure.description("分享-個人tab-對自己發的帖子進行分享")
    @allure.severity(bsc.C[0])
    def test_personal_tab_share(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "最新動態/全部/貼文列表-分享:個人tab-對自己發的帖子進行分享"
        test_chat.temp_num += 1
        case_name = "test_personal_tab_share"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info('********      分享:個人tab-對自己發的帖子進行分享 *********')
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                           # 首页点击最新动态
        case_step = case_step + cbz.case_step("2、點擊【個人】tab")
        ntp.click_personal_tab()                                          # 點擊【個人】tab
        case_step = case_step + cbz.case_step("3、滑屏操作至分享icon可見")
        ntp.swipe_personal_tab()                                          # 滑屏
        case_step = case_step + cbz.case_step("4、點擊第一個可分享icon")
        ntp.click_persomal_tab_share_icon()                              # 點擊第一個分享icon
        case_step = case_step + cbz.case_step("5、點擊列表中的中【分享】")
        ntp.click_list_share_button()                               # 點擊列表中的中【分享】
        case_step = case_step + cbz.case_step("6、輸入文本‘{}’，點擊分享".format(CD.share_personal_text))
        ntp.input_text_share(CD.share_text)                         # 輸入文本，點擊分享
        ntp.screenshot("'個人頁分享自己帖子'点击分享后立即截图")
        case_step = case_step + cbz.case_step("檢查：")
        find_toast = ntp.get_share_toast()
        try:  # “分享”檢查:彈出分享成功toast提示
            assert find_toast == True
            case_step = case_step + cbz.case_step("‘個人頁分享自己帖子’檢查成功。有彈出toast提示")
            logging.info("‘個人頁分享自己帖子’檢查成功。有彈出toast提示")
        except:
            actual = "'個人頁分享自己帖子'檢查失敗！！沒有彈出分享成功toast提示"
            expect = "分享帖子成功並有彈出toast提示"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

@pytest.mark.nf
@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("全部")
@allure.sub_suite("拍照")
@allure.feature("最新動態/全部/拍照")
@allure.story("拍照:相关功能")
@pytest.mark.usefixtures("startApp_withReset")
class TestAllTabPhoto:

    # 重做:拍照                                                         作者：游同同    时间：2020/3/31
    @allure.title("重做:拍照 ")  # 用例標題
    @allure.description("拍照後能夠重新拍照")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_tab_redo_photo(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "重做:拍照-拍照後能夠重新拍照"
        test_chat.temp_num += 1
        case_name = "test_all_tab_redo_photo"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  重做:拍照-拍照後能夠重新拍照     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                           # 首页点击最新动态
        case_step = case_step + cbz.case_step("2、點擊【全部】teb")
        ntp.click_all_tab()                                               # 点击全部tab
        case_step = case_step + cbz.case_step("3、點擊：【拍照】选项")
        ntp.click_all_tab_photo_icon()                               # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("4、點擊：快門icon")
        ntp.click_personal_tab_shutter_button()                      # 點擊：快門icon
        case_step = case_step + cbz.case_step("5、點擊：[重做]按鈕")
        ntp.click_personal_tab_media_cancel()                        # 點擊：[重做]按鈕
        case_step = case_step + cbz.case_step("檢查：")
        find_shutter_button = ntp.find_personal_tab_shutter_button()
        try:
            assert find_shutter_button == True
            case_step = case_step + cbz.case_step("檢查成功，點擊「重做」按鈕後回到拍照界面")
            logging.info("檢查成功，點擊「重做」按鈕後回到拍照界面")
        except:
            actual = "檢查失敗！點擊「重做」按鈕後回到拍照界面發生異常"
            expect = "點擊「重做」後可以回到拍攝界面"
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

    # 重做:拍摄                                                         作者：游同同    时间：2020/3/31
    @allure.title("重做:拍摄 ")  # 用例標題
    @allure.description("拍摄後能夠重新拍照")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_tab_redo_photograph(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "重做:拍摄後能夠重新拍照"
        test_chat.temp_num += 1
        case_name = "test_all_tab_redo_photograph"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  重做:拍摄後能夠重新拍照     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                           # 首页点击最新动态
        case_step = case_step + cbz.case_step("2、點擊【全部】teb")
        ntp.click_all_tab()                                              # 点击全部tab
        case_step = case_step + cbz.case_step("3、點擊：【拍照】选项")
        ntp.click_all_tab_photo_icon()                                  # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("4、長按：拍攝視頻4s")
        ntp.long_tap_personal_tab_shutter_button()                  # 長按：拍攝視頻4s
        case_step = case_step + cbz.case_step("5、點擊：[重做]按鈕")
        ntp.click_personal_tab_media_cancel()                       # 點擊：[重做]按鈕
        case_step = case_step + cbz.case_step("檢查：")
        find_shutter_button = ntp.find_personal_tab_shutter_button()
        try:
            assert find_shutter_button == True
            case_step = case_step + cbz.case_step("檢查成功，點擊「重做」按鈕後回到拍照界面")
            logging.info("檢查成功，點擊「重做」按鈕後回到拍照界面")
        except:
            actual = "檢查失敗！點擊「重做」按鈕後回到拍照界面發生異常"
            expect = "點擊重做後可以繼續拍攝"
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

    # 重做:拍摄上滑取消                                                   作者：游同同    时间：2020/3/31
    @allure.title("重做:拍摄上滑取消 ")  # 用例標題
    @allure.description("拍摄上滑取消後能夠重新拍照")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_tab_photograph_slide(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "重做:拍摄上滑取消後能夠重新拍照"
        test_chat.temp_num += 1
        case_name = "test_all_tab_photograph_slide"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  重做:拍摄上滑取消後能夠重新拍摄     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                          # 首页点击最新动态
        case_step = case_step + cbz.case_step("2、點擊【全部】teb")
        ntp.click_all_tab()                                             # 点击全部tab
        case_step = case_step + cbz.case_step("3、點擊：【拍照】选项")
        ntp.click_all_tab_photo_icon()                          # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("4、長按拍摄视频4s后并上滑取消")
        ntp.long_tap_slide()                                    # 長按拍摄视频4s后并上滑取消
        case_step = case_step + cbz.case_step("檢查：")
        find_shutter_button = ntp.find_personal_tab_shutter_button()
        try:
            assert find_shutter_button == True
            case_step = case_step + cbz.case_step("檢查成功，拍摄视频4s后上滑取消後能停留在拍照界面")
            logging.info("檢查成功，拍摄视频4s后上滑取消後能停留在拍照界面")
        except:
            actual = "檢查失敗！拍摄视频4s后上滑取消後能停留在拍照界面异常"
            expect = "取消操作正常且回到拍攝界面"
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

    # 傳送:發布                                                         作者：游同同    时间：2020/3/25
    @allure.title("傳送:發布")  # 用例標題
    @allure.description("編輯帖子發布功能")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_tab_send_photo(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "編輯帖子發布功能"
        test_chat.temp_num += 1
        case_name = "test_all_tab_send_photo"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  編輯帖子發布功能     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                          # 首页点击最新动态
        case_step = case_step + cbz.case_step("2、點擊【全部】teb")
        ntp.click_all_tab()                                             # 点击全部tab
        case_step = case_step + cbz.case_step("3、點擊：'你在想什麼?'發帖入口")
        ntp.click_publish_dynamic()                                     # 點擊：'你在想什麼?'發帖入口
        case_step = case_step + cbz.case_step("4、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                               # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("5、點擊：【拍照】选项")
        ntp.click_action_photo()                                    # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("6、長按：拍攝視頻4s")
        ntp.long_tap_personal_tab_shutter_button()                  # 長按：拍攝視頻4s
        case_step = case_step + cbz.case_step("7、點擊：拍照頁面-「傳送」按鈕")
        ntp.click_personal_tab_send_button()                        # 點擊：拍照頁面-「傳送」按鈕
        case_step = case_step + cbz.case_step("8、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                           # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("9、點擊：【标注人名】选项")
        ntp.click_callout_name()                                    # 點擊：【标注人名】选项
        list_one_name = ntp.get_callout_name_page_list_name()  # 獲取列表第一個用戶暱稱
        case_step = case_step + cbz.case_step("10、點擊：'标注人名'頁面-列表第一個用戶")
        ntp.click_callout_name_page_list_name()                     # 點擊：'标注人名'頁面-列表第一個用戶
        case_step = case_step + cbz.case_step("11、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                           # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("12、點擊：【相片/影片】选项")
        ntp.click_movie_photo()                                     # 點擊：【相片/影片】选项
        sum_photo = ntp.get_photo_sum()  # 獲取當前頁面照片數量
        index = ntp.random_int(sum_photo-1)
        case_step = case_step + cbz.case_step("13、選擇第{}張圖片".format(index+1))
        ntp.click_index_photo(index)                                # 點擊其中一張圖片
        case_step = case_step + cbz.case_step("14、點擊：點擊「傳送」按鈕")
        ntp.click_photo_send_button()                               # 點擊：點擊「傳送」按鈕
        case_step = case_step + cbz.case_step("15、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                       # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查：")
        ntp.screenshot("发布完成后立马截图")
        find_toast = ntp.find_toast_send_success()
        try:
            assert find_toast == True
            case_step = case_step + cbz.case_step("檢查成功，發布帖子成功有獲取到'發布成功'toast提示")
            logging.info("檢查成功，發布帖子成功有獲取到'發布成功'toast提示")
        except:
            actual = "檢查失敗！發布失敗未獲取到'發布成功'toast提示"
            expect = "發布成功並有彈出toast提示"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 傳送:建立貼文發布                                                   作者：游同同    时间：2020/3/25
    @allure.title("傳送:建立貼文發布")  # 用例標題
    @allure.description("編輯包含拍照、文本、公開貼文發送成功")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_tab_pthot_and_text_send_post(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "編輯包含拍照、文本、公開貼文發送成功"
        test_chat.temp_num += 1
        case_name = "test_all_tab_pthot_and_text_send_post"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  編輯包含拍照、文本、公開貼文發送成功     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                                  # 首页点击最新动态
        case_step = case_step + cbz.case_step("2、點擊【全部】teb")
        ntp.click_all_tab()                                                     # 点击全部tab
        case_step = case_step + cbz.case_step("3、點擊：'你在想什麼?'發帖入口")
        ntp.click_publish_dynamic()                                             # 點擊：'你在想什麼?'發帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、<br/>輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                    # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                           # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：【拍照】选项")
        ntp.click_action_photo()                                    # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("7、點擊：快門icon")
        ntp.click_personal_tab_shutter_button()                     # 點擊：快門icon
        case_step = case_step + cbz.case_step("8、點擊：拍照頁面-「傳送」按鈕")
        ntp.click_personal_tab_send_button()                        # 點擊：拍照頁面-「傳送」按鈕
        case_step = case_step + cbz.case_step("9、點擊：[個人動態]跳转按钮")
        ntp.click_personal_dynamic()                                # 點擊：[個人動態]跳转按钮
        list_number = ntp.get_share_list_number()                       # 分享可选群组个数
        if list_number >= 2:
            case_step = case_step + cbz.case_step("10、點擊第2個分享對象後點擊「完成」按鈕")
            ntp.click_random_Object()                              # 點擊2個分享對象後點擊「完成」按鈕
        case_step = case_step + cbz.case_step("11、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                       # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查：")
        find_toast = ntp.find_toast_send_success()
        try:
            assert find_toast == True
            case_step = case_step + cbz.case_step("檢查成功，發布帖子成功有獲取到'發布成功'toast提示")
            logging.info("檢查成功，發布帖子成功有獲取到'發布成功'toast提示")
        except:
            actual = "檢查失敗！發布失敗未獲取到'發布成功'toast提示"
            expect = "發布成功並有彈出toast提示"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 傳送:存為草稿                                                       作者：游同同    时间：2020/3/25
    @allure.title("傳送:存為草稿")  # 用例標題
    @allure.description("編輯帖子退出時挽留操作-存為草稿功能")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_tab_photo_save_draft(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "編輯帖子退出時挽留操作-存為草稿功能"
        test_chat.temp_num += 1
        case_name = "test_all_tab_photo_save_draf"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  編輯帖子退出時挽留操作-存為草稿功能     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                              # 首页点击最新动态
        case_step = case_step + cbz.case_step("2、點擊【全部】teb")
        ntp.click_all_tab()                                                 # 点击全部tab
        case_step = case_step + cbz.case_step("3、點擊：'你在想什麼?'發帖入口")
        ntp.click_publish_dynamic()                                         # 點擊：'你在想什麼?'發帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、<br/>輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                             # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                   # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：【拍照】选项")
        ntp.click_action_photo()                                    # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("7、長按：拍攝視頻4s")
        ntp.long_tap_personal_tab_shutter_button()                  # 長按：拍攝視頻4s
        case_step = case_step + cbz.case_step("8、點擊：拍照頁面-「傳送」按鈕")
        ntp.click_personal_tab_send_button()                        # 點擊：拍照頁面-「傳送」按鈕
        case_step = case_step + cbz.case_step("9、點擊：返回")
        ntp.return_button()                                         # 點擊：返回
        if_find = ntp.find_save_draft_button()                      # 查找：[存為草稿]按鈕
        case_step = case_step + cbz.case_step("检查①：")
        try:
            assert if_find == True
            case_step = case_step + cbz.case_step("檢查成功，返回時有彈出[存為草稿]按鈕")
            logging.info("檢查成功，返回時有彈出[存為草稿]按鈕")
        except:
            actual = "檢查失敗！點擊返回退出編輯時沒有彈出[存為草稿]按鈕"
            expect = "編輯貼文時退出有彈出[存為草稿]按鈕"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("10、點擊：[存為草稿]按鈕")
            ntp.click_save_draft_button()                       # 點擊：[存為草稿]按鈕
            case_step = case_step + cbz.case_step("11、點擊：'你在想什麼?'發帖入口")
            ntp.click_publish_dynamic()                         # 點擊：'你在想什麼?'發帖入口
            case_step = case_step + cbz.case_step("检查：")
            get_text = ntp.get_post_inptu_box_text()
            try:
                assert get_text == post_text
                case_step = case_step + cbz.case_step("檢查成功，[存為草稿]功能正常")
                logging.info("檢查成功，[存為草稿]功能正常")
            except:
                actual = "檢查失敗，[存為草稿]功能異常，上次操作文本為'{}'，實際文本為'{}'".format(post_text,get_text)
                expect = "再次進入發帖編輯時有保存上次記錄"
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("12、點擊：「發布」按鈕")
                ntp.click_post_photo_publish_button()                   # 點擊：「發布」按鈕
                case_step = case_step + cbz.case_step("检查：")
                find_toast = ntp.find_toast_send_success()
                try:
                    assert find_toast == True
                    case_step = case_step + cbz.case_step("檢查成功，發布帖子成功有獲取到'發布成功'toast提示")
                    logging.info("檢查成功，發布帖子成功有獲取到'發布成功'toast提示")
                except:
                    actual = "檢查失敗！發布失敗未獲取到'發布成功'toast提示"
                    expect = "發布成功並有彈出toast提示"
                    video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ntp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                           "最新動態")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise

    # 傳送:放棄發布                                                       作者：游同同    时间：2020/3/25
    @allure.title("傳送:放棄發布")  # 用例標題
    @allure.description("編輯帖子退出時挽留操作-放棄發布功能")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_all_tab_abandon_photo(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "編輯帖子退出時挽留操作-放棄發布功能"
        test_chat.temp_num += 1
        case_name = "test_all_tab_abandon_photo"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  編輯帖子退出時挽留操作-放棄發布功能     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                                  # 首页点击最新动态
        case_step = case_step + cbz.case_step("2、點擊【全部】teb")
        ntp.click_all_tab()                                                     # 点击全部tab
        case_step = case_step + cbz.case_step("3、點擊：'你在想什麼?'發帖入口")
        ntp.click_publish_dynamic()                                             # 點擊：'你在想什麼?'發帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、<br/>輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                                # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                       # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：【拍照】选项")
        ntp.click_action_photo()                                                 # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("7、長按：拍攝視頻4s")
        ntp.long_tap_personal_tab_shutter_button()                               # 長按：拍攝視頻4s
        case_step = case_step + cbz.case_step("8、點擊：拍照頁面-「傳送」按鈕")
        ntp.click_personal_tab_send_button()                                    # 點擊：拍照頁面-「傳送」按鈕
        case_step = case_step + cbz.case_step("9、點擊：返回")
        ntp.return_button()                                         # 點擊：返回
        if_find = ntp.find_abandon_post_button()                      # 查找：[放棄發布]按鈕
        case_step = case_step + cbz.case_step("检查①：")
        try:
            assert if_find == True
            case_step = case_step + cbz.case_step("檢查成功，返回時有彈出[放棄發布]按鈕")
            logging.info("檢查成功，返回時有彈出[放棄發布]按鈕")
        except:
            actual = "檢查失敗！點擊返回退出編輯時沒有彈出[放棄發布]按鈕"
            expect = "退出編輯貼文時有彈出[放棄發布]按鈕"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("10、點擊：[放棄發布]按鈕")
            ntp.click_abandon_post_button()                                  # 點擊：[放棄發布]按鈕
            case_step = case_step + cbz.case_step("11、點擊：'你在想什麼?'發帖入口")
            ntp.click_publish_dynamic()                                      # 點擊：'你在想什麼?'發帖入口
            case_step = case_step + cbz.case_step("检查②：")
            get_text = ntp.get_post_inptu_box_text()
            try:
                assert get_text == '請輸入想要分享的內容'
                case_step = case_step + cbz.case_step("檢查成功，[放棄發布]功能正常")
                logging.info("檢查成功，[放棄發布]功能正常")
            except:
                actual = "檢查失敗，[放棄發布]功能異常，上次操作文本為'{}'，實際文本為'{}'".format(post_text,get_text)
                expect = "[放棄發布]按鈕不會保留上次記憶操作"
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

@pytest.mark.nf
@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("搜索")
@allure.sub_suite("貼文")
@allure.feature("最新動態/搜索/貼文")
@allure.story("貼文:模块相关功能")
@pytest.mark.usefixtures("startApp_withReset")
class TestStearchPost:

    # 查看全部                                                                  作者：游同同    时间：2020/3/30
    @allure.title("查看全部")
    @allure.description("贴文-查看全部")
    @allure.severity(bsc.C[0])
    def test_search_all(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "最新動態/搜索/分類:查看全部"
        test_chat.temp_num += 1
        case_name = "test_search_all"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********       貼文:查看全部      *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                           # 点击【最新动态】
        case_step = case_step + cbz.case_step("2、點擊[搜索]tab")
        ntp.click_search_button()                                       # 点击【搜索】
        case_step = case_step + cbz.case_step("3、點擊輸入框並輸入‘{}’，搜索".format(CD.search_test))
        ntp.input_search_text(CD.search_test)                   # 点击搜索输入框，输入文本，点击键盘搜索按钮
        case_step = case_step + cbz.case_step("檢查：")
        is_find = ntp.is_find_view()
        try:
            assert is_find == True
            case_step = case_step + cbz.case_step("檢查成功。搜索‘{}’有結果".format(CD.search_test))
            logging.info("檢查成功。搜索‘{}’有結果".format(CD.search_test))
        except:
            actual = "檢查失敗！搜索‘{}’沒有結果".format(CD.search_test)
            expect = "搜索有對應的結果"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.click_cancel_button()

    # 貼文:3個貼文                                                              作者：游同同    时间：2020/3/30
    @allure.title("3個貼文")
    @allure.description("搜索關鍵字，篩選貼文類型")
    @allure.severity(bsc.C[0])
    def test_search_post(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "最新動態/搜索/分類:貼文"
        test_chat.temp_num += 1
        case_name = "test_search_post"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********    搜索展示-3個貼文    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                           # 点击【最新动态】
        case_step = case_step + cbz.case_step("2、點擊[搜索]tab")
        ntp.click_search_button()                                        # 点击【搜索】
        case_step = case_step + cbz.case_step("3、點擊輸入框並輸入‘{}’，搜索".format(CD.search_test))
        ntp.input_search_text(CD.search_test)                       # 点击搜索输入框，输入文本，点击键盘搜索按钮
        case_step = case_step + cbz.case_step("檢查①：")
        is_find_user = ntp.is_find_user_all_button()
        is_find_post = ntp.is_find_post_all_button()
        try:
            assert is_find_user == True or is_find_post == True # “查看全部”按钮判断-有
            case_step = case_step + cbz.case_step("檢查成功。未筛选时展示了全部结果")
            logging.info("檢查成功。未筛选时展示了全部结果")
        except:
            actual = "檢查失敗！！未篩選時展示全部類型異常"
            expect = "未筛选时展示全部结果"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("4、點擊[貼文]")
            ntp.click_poat_button()                                 # 点击【贴文】
            case_step = case_step + cbz.case_step("檢查②：")
            is_find = ntp.is_find_post_all_button()
            try:
                assert is_find == False  # “查看全部”按钮判断-无
                case_step = case_step + cbz.case_step("檢查成功。点击【贴文】后筛选成功")
                logging.info("檢查成功。点击【贴文】后筛选成功")
            except:
                actual = "檢查失敗！！點擊貼文後篩選結果錯誤"
                expect = "篩選「貼文」功能正常"
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                       "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("5、再次點擊貼文")
                ntp.click_poat_button()                          # 再次点击【贴文】
                case_step = case_step + cbz.case_step("檢查③：")
                is_find_user = ntp.is_find_user_all_button()
                is_find_post = ntp.is_find_post_all_button()
                try:
                    assert is_find_user == True or is_find_post == True  # “查看全部”按钮判断-有
                    case_step = case_step + cbz.case_step("檢查成功。取消【贴文】筛选后展示全部结果")
                    logging.info("檢查成功。取消【贴文】筛选后展示全部结果")
                except:
                    actual = "檢查失敗！！取消【貼文】篩選後展示結果類型錯誤"
                    expect = "取消【贴文】筛选后展示全部结果"
                    video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ntp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step,
                                                           bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
        finally:
            ntp.click_cancel_button()

@pytest.mark.nf
@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("搜索")
@allure.sub_suite("群組-公開群組")
@allure.feature("最新動態/搜索/群組-公開群組")
@allure.story("群組-公開群組:相关功能验证")
@pytest.mark.usefixtures("startApp_withReset")
class TestStearchGroup:

    # 查看全部                                                          作者：游同同    时间：2020/3/30
    @allure.title("查看全部")
    @allure.description("搜索關鍵字，篩選群組類型")
    @allure.severity(bsc.C[0])
    def test_search_group(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "最新動態/搜索/分類:群組筛选功能"
        test_chat.temp_num += 1
        case_name = "test_search_group"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  查看全部:搜索展示-群组  *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                             # 点击【最新动态】
        case_step = case_step + cbz.case_step("2、點擊[搜索]")
        ntp.click_search_button()                                         # 点击【搜索】
        case_step = case_step + cbz.case_step("3、點擊輸入框並輸入‘{}’，搜索".format(CD.search_test))
        ntp.input_search_text(CD.search_test)                           # 点击搜索输入框，输入文本，点击键盘搜索按钮
        case_step = case_step + cbz.case_step("檢查①：")
        find_view = ntp.is_find_view()
        try:
            assert find_view == True  # “查看全部”按钮判断-有
            case_step = case_step + cbz.case_step("檢查成功。未筛选时展示了全部结果")
            logging.info("檢查成功。未筛选时展示了全部结果")
        except:
            actual = "檢查失敗！！未篩選時展示了全部類型錯誤"
            expect = "未筛选时展示全部结果"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("4、點擊【群組】")
            ntp.click_group_button()                                    # 点击【群组】
            case_step = case_step + cbz.case_step("檢查②：")
            find_view = ntp.is_find_view()
            find_public = ntp.is_find_public_group_button()
            logging.info("find_viewd的值為{}".format(find_view))
            logging.info("find_public的值為{}".format(find_public))
            try:  # "查看全部"不存在&&【公共群组】存在
                assert find_view == False and find_public == True
                case_step = case_step + cbz.case_step("檢查成功。点击【群组】后筛选成功")
                logging.info("檢查成功。点击【群组】后筛选成功")
            except:
                actual = "檢查失敗！點擊【群組】篩選後展示類型錯誤"
                expect = "点击【群组】后筛选功能正常"
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                       "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("5、再次點擊【群組】")
                ntp.click_group_button()                                # 再次点击【群组】
                case_step = case_step + cbz.case_step("檢查③：")
                find_view = ntp.is_find_view()
                try:
                    assert find_view == True  # “查看全部”按钮判断-有
                    case_step = case_step + cbz.case_step("檢查成功。取消【群组】筛选后展示全部结果")
                    logging.info("檢查成功。取消【群组】筛选后展示全部结果")
                except:
                    actual = "檢查失敗！！取消【群組】篩選後展示類型錯誤"
                    expect = "取消【群组】筛选后展示全部结果"
                    video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ntp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step,
                                                           bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
            finally:
                ntp.click_cancel_button()


@pytest.mark.nf
@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("搜索")
@allure.sub_suite("用戶")
@allure.feature("最新動態/搜索/用戶")
@allure.story("查看全部")
@pytest.mark.usefixtures("startApp_withReset")
class TestStearchUser:

    # 搜索展示-用戶                                                       作者：游同同    时间：2020/3/31
    @allure.title("查看全部")
    @allure.description("搜索關鍵字，篩選用戶類型")
    @allure.severity(bsc.C[0])
    def test_search_user(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "最新動態/搜索/分類:用戶"
        test_chat.temp_num += 1
        case_name = "test_search_user"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********       搜索展示-用戶     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                           # 点击【最新动态】
        case_step = case_step + cbz.case_step("2、點擊[搜索]tab")
        ntp.click_search_button()                                   # 点击【搜索】
        case_step = case_step + cbz.case_step("3、點擊輸入框並輸入‘{}’，搜索".format(CD.search_user_test))
        ntp.input_search_text(CD.search_user_test)                  # 点击搜索输入框，输入文本，点击键盘搜索按钮
        case_step = case_step + cbz.case_step("檢查①：")
        is_find = ntp.is_find_view()
        try:
            assert is_find == True  # “查看全部”按钮判断-有
            case_step = case_step + cbz.case_step("檢查成功。未筛选时展示了全部结果")
            logging.info("檢查成功。未筛选时展示了全部结果")
        except:
            actual = "檢查失敗！！為篩選時展示全部結果錯誤"
            expect = "未筛选时展示全部结果"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("4、點擊【用戶】按鈕")
            ntp.click_user_button()                                     # 点击【用戶】按钮
            case_step = case_step + cbz.case_step("檢查②：") # 檢查【追踪】按钮存在&&“查看全部”不存在
            find_track = ntp.is_find_track()
            find_view = ntp.is_find_view()
            try:
                assert find_track == True and find_view == False
                case_step = case_step + cbz.case_step("檢查成功。点击【用戶】后筛选成功")
                logging.info("檢查成功。点击【用戶】后筛选成功")
            except:
                actual = "檢查失败！！点击【用戶】后筛选错误"
                expect = "【用戶】后筛选功能正常"
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                       "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("5、再次點擊【用戶】")
                ntp.click_user_button()                             # 再次点击【用戶】按钮
                case_step = case_step + cbz.case_step("檢查③：")
                try:
                    assert ntp.is_find_view() == True  # “查看全部”按钮判断-有
                    case_step = case_step + cbz.case_step("檢查成功。取消【用戶】筛选后展示全部结果")
                    logging.info(" 檢查成功。取消【用戶】筛选后展示全部结果")
                except:
                    actual = "斷層失敗！點擊【用戶】取消篩選後展示類型錯誤"
                    expect = "取消【用戶】筛选后展示全部结果"
                    video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ntp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                           "最新動態")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
            finally:
                 ntp.click_cancel_button()

@pytest.mark.yyy
@pytest.mark.nf
@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("搜索")
@allure.sub_suite("分類")
@allure.feature("最新動態/搜索/分類")
@allure.story("分類：相关功能检测")
@pytest.mark.usefixtures("startApp_withReset")
class TestStearchSort:

    # 貼文:點讚                                                       作者：游同同    时间：2020/3/31
    @allure.title("貼文:點讚")
    @allure.description("貼文:對搜索的貼文搜索進行點讚")
    @allure.severity(bsc.C[0])
    def test_search_post_like(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "貼文:對搜索的貼文搜索進行點讚"
        test_chat.temp_num += 1
        case_name = "test_search_post_like"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     貼文:點讚    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                          # 点击【最新动态】
        case_step = case_step + cbz.case_step("2、點擊[搜索]tab")
        ntp.click_search_button()                                       # 点击【搜索】
        case_step = case_step + cbz.case_step("3、點擊輸入框並輸入‘{}’，搜索".format(CD.search_test))
        ntp.input_search_text(CD.search_test)                       # 点击搜索输入框，输入文本，点击键盘搜索按钮
        case_step = case_step + cbz.case_step("4、點擊[貼文]")
        ntp.click_poat_button()                                     # 点击【贴文】
        case_step = case_step + cbz.case_step("5、點擊：跳轉帖子詳情頁（暱稱欄）")
        ntp.click_post_user_name()                                  # 點擊：跳轉帖子詳情頁（暱稱欄）
        before_like_number = ntp.get_post_detail_like_count_icon_number()  # 获取第一个动态点赞次数（点赞前）
        case_step = case_step + cbz.case_step("6、給第一個帖子點讚")
        ntp.click_group_tab_list_like_icon()                        # 給第一個帖子點讚
        case_step = case_step + cbz.case_step("檢查：")
        rear_like_number = ntp.get_post_detail_like_count_icon_number()  # 點讚後讚數
        like_bumber = abs(rear_like_number - before_like_number)
        try:
            assert like_bumber == 1       # 點讚前後差1
            case_step = case_step + cbz.case_step("檢查成功，點讚前後點讚次數差值為1")
            logging.info("檢查成功，點讚前後點讚次數差值為1")
        except:
            actual = "檢查失敗！點讚前後記錄帖子讚次數差值為{}".format(like_bumber)
            expect = "點讚前後點讚次數差值為1"
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

    # 貼文:分享                                                       作者：游同同    时间：2020/3/31
    @allure.title("貼文:分享（对象文本帖）")
    @allure.description("貼文:對搜索的文本貼文搜索進行分享")
    @allure.severity(bsc.C[0])
    def test_search_post_share_text(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "貼文:對搜索的文本貼文搜索進行分享"
        test_chat.temp_num += 1
        case_name = "test_search_post_share_text"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     貼文:分享    *********")
        case_Preposition = "创建一个包含文本为'test'的群组帖子"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                             # 点击【最新动态】
        case_step = case_step + cbz.case_step("2、點擊【全部】teb")
        ntp.click_all_tab()                                                # 点击全部tab
        case_step = case_step + cbz.case_step("3、點擊：'你在想什麼?'發帖入口")
        ntp.click_publish_dynamic()                                         # 點擊：'你在想什麼?'發帖入口
        inptu_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(inptu_text))
        ntp.input_post_inptu_box_text(inptu_text)                            # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                             # 點擊：「發布」按鈕
        time.sleep(3)
        case_step = case_step + cbz.case_step("6、點擊[搜索]tab")
        ntp.click_search_button()                                          # 点击【搜索】
        case_step = case_step + cbz.case_step("7、點擊輸入框並輸入‘{}’，搜索".format(inptu_text))
        ntp.input_search_text(inptu_text)                                 # 点击搜索输入框，输入文本，点击键盘搜索按钮
        case_step = case_step + cbz.case_step("8、點擊[貼文]")
        ntp.click_poat_button()                                     # 点击【贴文】
        comments_before_number = ntp.get_post_share_number_icon()  # 分享前獲取分享次數
        case_step = case_step + cbz.case_step("9、點擊：「分享」-分享")
        ntp.click_group_tab_post_share_icon()                      # 點擊：「分享」-分享
        comments_Rear_number = ntp.get_post_share_number_icon()    # 分享后獲取分享次數
        case_step = case_step + cbz.case_step("检查：")
        try:
            assert comments_Rear_number - comments_before_number == 1
            case_step = case_step + cbz.case_step("检查成功，分享两次后计数加1")
            logging.info("检查成功，分享两次后计数加1")
        except:
            actual = "检查失败！分享前计数为'{}'，两次分享后计数为'{}'".format(comments_before_number,
                                                           comments_Rear_number)
            expect = "分享两次后计数加1"
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

    # 貼文:評論                                                       作者：游同同    时间：2020/3/31
    @allure.title("貼文:評論")
    @allure.description("貼文:對搜索的貼文搜索進行評論")
    @allure.severity(bsc.C[0])
    def test_search_post_comment(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "貼文:對搜索的貼文搜索進行評論"
        test_chat.temp_num += 1
        case_name = "test_search_post_comment"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     貼文:評論    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                          # 点击【最新动态】
        case_step = case_step + cbz.case_step("2、點擊[搜索]tab")
        ntp.click_search_button()                                       # 点击【搜索】
        case_step = case_step + cbz.case_step("3、點擊輸入框並輸入‘{}’，搜索".format(CD.search_test))
        ntp.input_search_text(CD.search_test)                           # 点击搜索输入框，输入文本，点击键盘搜索按钮
        case_step = case_step + cbz.case_step("4、點擊[貼文]")
        ntp.click_poat_button()                                         # 点击【贴文】
        case_step = case_step + cbz.case_step("5、點擊：帖子留言icon")
        ntp.click_post_comment_icon()                                   # 點擊：帖子留言icon
        comments_before_number = ntp.get_post_comment_number_icon()     # 留言前獲取留言次數
        logging.info("當前帖子留言次數為{}".format(comments_before_number))
        case_step = case_step + cbz.case_step("6、連續3次留言")
        ntp.comment_double(3,CD.send_message_data)                      # 連續3次留言
        time.sleep(1)
        comments_Rear_number = ntp.get_post_comment_number_icon()       # 留言後獲取留言次數
        logging.info("留言{}次後獲取留言次數'{}'".format(3,comments_Rear_number))
        case_step = case_step + cbz.case_step("檢查：")
        try:
            assert comments_Rear_number - comments_before_number == 3
            case_step = case_step + cbz.case_step("檢查成功，評論次數：留言前'{}'，評論後'{}'".format(comments_before_number,comments_Rear_number))
            logging.info("檢查成功，評論次數：留言前'{}'，評論後'{}'".format(comments_before_number,comments_Rear_number))
        except:
            actual = "檢查失敗！評論次數：留言前'{}'，評論3次後'{}'".format(comments_before_number,comments_Rear_number)
            expect = "評論3次後計數加3"
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

    # 群組:追蹤                                                       作者：游同同    时间：2020/3/31
    @allure.title("群組:追蹤")
    @allure.description("群組:對搜索的群組搜索進行追蹤")
    @allure.severity(bsc.C[0])
    def test_search_group_track(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "群組:對搜索的群組搜索進行追蹤"
        test_chat.temp_num += 1
        case_name = "test_search_group_track"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     群組:追蹤    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                              # 点击【最新动态】
        case_step = case_step + cbz.case_step("2、點擊[搜索]tab")
        ntp.click_search_button()                                           # 点击【搜索】
        case_step = case_step + cbz.case_step("3、點擊輸入框並輸入‘{}’，搜索".format(CD.search_test))
        ntp.input_search_text(CD.search_test)                               # 点击搜索输入框，输入文本，点击键盘搜索按钮
        case_step = case_step + cbz.case_step("4、點擊[群组]")
        ntp.click_group_button()                                     # 点击【群组】
        track_index = ntp.get_search_group_track_button_index()      # 獲取第一個可追蹤的群組索引
        logging.info("track_index的类型为{}，值为'{}'".format(type(track_index),track_index))
        case_step = case_step + cbz.case_step("5、點擊第{}個群組的「追蹤」按鈕".format(track_index+1))
        ntp.click_index_search_group_track_button(track_index)       # 點擊指定「追蹤」按鈕
        case_step = case_step + cbz.case_step("檢查①：")
        index_track_text = ntp.get_search_group_track_button(track_index)
        try:
            assert index_track_text == '追蹤中'
            case_step = case_step + cbz.case_step("檢查成功，點擊列表中第{}個群組追蹤按鈕後，'追蹤'變為'追蹤中'".format(track_index+1))
            logging.info("檢查成功，點擊列表中第{}個群組追蹤按鈕後，'追蹤'變為'追蹤中'".format(track_index+1))
        except:
            actual = "檢查失敗！點擊列表中第{}個群組追蹤按鈕後，'按鈕文案變為'{}'".format(track_index+1,index_track_text)
            expect = "點擊「追蹤」後按鈕文本應變為'追蹤中'"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("6、點擊第{}個群組名稱".format(track_index+1))
            ntp.click_index_search_group_name_list(track_index)  # 點擊指定剛追蹤的群組名稱
            case_step = case_step + cbz.case_step("7、點擊：群組中更多icon-「取消追蹤」按鈕")
            ntp.click_personal_home_trace_group_cancel()         # 點擊：群組中更多icon-「取消追蹤」按鈕
            case_step = case_step + cbz.case_step("8、點擊：返回")
            ntp.return_button()                                  # 點擊：返回
            case_step = case_step + cbz.case_step("檢查：")
            cancel_track_text = ntp.get_search_group_track_button(track_index)
            try:
                assert cancel_track_text == '追蹤'
                case_step = case_step + cbz.case_step("檢查成功，在群組詳情頁取消追蹤後，列表中展示群組'可追蹤'文案正常")
                logging.info("檢查成功，在群組詳情頁取消追蹤後，列表中展示群組'可追蹤'文案正常")
            except:
                actual = "檢查失敗！在群組詳情頁取消追蹤後，回到搜索列表中展示群組按鈕文案實際為'{}',功能異常或文案沒有刷新".format(cancel_track_text)
                expect = "在群組詳情頁取消追蹤後，列表中展示群組'可追蹤'文案"
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

    # 用戶:追蹤                                                       作者：游同同    时间：2020/3/31
    @allure.title("用戶:追蹤")
    @allure.description("用戶:對搜索的用戶搜索進行追蹤")
    @allure.severity(bsc.C[0])
    def test_search_user_track(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "用戶:對搜索的群組搜索進行追蹤"
        test_chat.temp_num += 1
        case_name = "test_search_user_track"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     用戶:追蹤    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                          # 点击【最新动态】
        case_step = case_step + cbz.case_step("2、點擊[搜索]tab")
        ntp.click_search_button()                                       # 点击【搜索】
        case_step = case_step + cbz.case_step("3、點擊輸入框並輸入‘{}’，搜索".format(CD.search_user_test))
        ntp.input_search_text(CD.search_user_test)                       # 点击搜索输入框，输入文本，点击键盘搜索按钮
        case_step = case_step + cbz.case_step("4、點擊[用戶]")
        ntp.click_user_button()                                          # 点击【用戶】
        user_index = ntp.get_search_user_track_button_index()            # 獲取索引(用戶)：搜索'用戶'第一個可追蹤的索引
        case_step = case_step + cbz.case_step("5、點擊第{}個用戶的「追蹤」按鈕".format(user_index + 1))
        ntp.click_index_search_user_track_button(user_index)        # 點擊(用戶)：根據索引點擊指定的「追蹤」按鈕
        case_step = case_step + cbz.case_step("檢查①：")
        user_index_track_text = ntp.get_search_user_track_button(user_index)
        try:
            assert user_index_track_text == '追蹤中'
            case_step = case_step + cbz.case_step("檢查成功，點擊列表中第{}個用戶追蹤按鈕後，'追蹤'變為'追蹤中'".format(user_index + 1))
            logging.info("檢查成功，點擊列表中第{}個用戶追蹤按鈕後，'追蹤'變為'追蹤中'".format(user_index + 1))
        except:
            actual = "檢查失敗！點擊列表中第{}個用戶追蹤按鈕後，'按鈕文案變為'{}'".format(user_index + 1, user_index_track_text)
            expect = "對應的按鈕文案'追蹤'變為'追蹤中'"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("6、點擊第{}個用戶名稱".format(user_index+1))
            ntp.click_index_search_user_name_list(user_index)                   # 點擊指定剛追蹤的群組名稱
            case_step = case_step + cbz.case_step("7、點擊：用戶主頁「追蹤中」-「確認取消」")
            ntp.click_personal_home_page_trace()                            # 點擊：用戶主頁「追蹤中」-「確認取消」
            case_step = case_step + cbz.case_step("8、點擊：返回")
            ntp.return_button()                                            # 點擊：返回
            case_step = case_step + cbz.case_step("檢查②：")
            cancel_track_text = ntp.get_search_user_track_button(user_index)
            try:
                assert cancel_track_text == '追蹤'
                case_step = case_step + cbz.case_step("檢查成功，在用戶主頁取消追蹤後，列表中展示群組'可追蹤'文案正常")
                logging.info("檢查成功，在用戶主頁取消追蹤後，列表中展示群組'可追蹤'文案正常")
            except:
                actual = "檢查失敗！在用戶主頁取消追蹤後，回到搜索列表中展示用戶按鈕文案實際為'{}',功能異常或文案沒有刷新".format(cancel_track_text)
                expect = "在用戶主頁取消追蹤後，列表中展示群組'可追蹤'文案正常"
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


@pytest.mark.nf
@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("群組")
@allure.sub_suite("建立群組")
@allure.feature("最新動態/群組/建立群組")
@allure.story("建立群組:页面相关功能")
@pytest.mark.usefixtures("startApp_withReset")
class TestFoundGroup:

    # 名稱                                                          作者：游同同    时间：2020/3/26
    @allure.title("名稱")  # 用例標題
    @allure.description("名稱:验证创建后的群组是否存在")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_found_group_name(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "名稱:验证创建后的群组是否存在"
        test_chat.temp_num += 1
        case_name = "test_found_group_name"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     建立群組-名稱    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                               # 點擊：[群組] tab
        case_step = case_step + cbz.case_step("3、點擊：[建立群組]按鈕")
        ntp.click_create_group_button()                                     # 點擊：[建立群組]按鈕
        letter1 = ntp.random_english_letter()
        letter2 = ntp.random_english_letter()
        letter3 = ntp.random_english_letter()
        group_name = CD.create_group_text + letter1 + letter2 + letter3 + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入群組名稱'{}'".format(group_name))
        ntp.input_create_group_name_input(group_name)                       # 輸入群組名稱
        case_step = case_step + cbz.case_step("5、點擊：[建立群組]完成按鈕")
        ntp.click_create_group_done_button()                                # 點擊：[建立群組]完成按鈕
        case_step = case_step + cbz.case_step("6、點擊：[查看全部] 按鈕")
        ntp.click_group_tab_view_all()                                      # 點擊：[查看全部] 按鈕
        find_group = ntp.find_create_group_name(group_name)
        case_step = case_step + cbz.case_step("檢查：")
        try:
            assert find_group == True
            case_step = case_step + cbz.case_step("檢查成功，'你的群組'中有找到先創建的群組-{}".format(group_name))
            logging.info("檢查成功，'你的群組'中有找到先創建的群組-{}".format(group_name))
        except:
            actual = "檢查失敗！'你的群組'中沒有找到先創建的群組-{}".format(group_name)
            expect = "'你的群組'中有找到先創建的群組-{}".format(group_name)
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

    # 隱私設定:公開                                                  作者：游同同    时间：2020/3/27
    @allure.title("隱私設定:公開")  # 用例標題
    @allure.description("隱私設定:創建公開群組後能夠被搜索到")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_found_group_set_public(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "隱私設定:創建公開群組後能夠被搜索到"
        test_chat.temp_num += 1
        case_name = "test_found_group_set_public"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     隱私設定:公開    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                               # 點擊：[群組] tab
        case_step = case_step + cbz.case_step("3、點擊：[建立群組]按鈕")
        ntp.click_create_group_button()                                     # 點擊：[建立群組]按鈕
        letter1 = ntp.random_english_letter()
        letter2 = ntp.random_english_letter()
        letter3 = ntp.random_english_letter()
        group_name = CD.create_group_text + letter1 + letter2 + letter3 + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入群組名稱'{}'".format(group_name))
        ntp.input_create_group_name_input(group_name)                       # 輸入群組名稱
        case_step = case_step + cbz.case_step("5、點擊：[建立群組]完成按鈕")
        ntp.click_create_group_done_button()                                # 點擊：[建立群組]完成按鈕
        case_step = case_step + cbz.case_step("6、點擊：[探索群組]按鈕")
        ntp.click_explore_group_button()                                    # 點擊：[探索群組]按鈕
        case_step = case_step + cbz.case_step("检查①：")
        is_find = ntp.find_track_more_grouplist()
        try:
            assert is_find == True
            case_step = case_step + cbz.case_step("检查成功，未输入关键词筛选有列出群组列表")
            logging.info("检查成功，未输入关键词筛选有列出群组列表")
        except:
            actual = "检查失败！未输入关键词筛选时群组列表展示异常"
            expect = "未输入关键词筛选有列出群组列表"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                   "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("7、輸入群組名'test{0}{1}{2}'後觸發搜索".format(letter1,letter2,letter3))
            ntp.input_track_more_search_box(letter1,letter2,letter3)          # 輸入群組名後觸發搜索
            case_step = case_step + cbz.case_step("檢查②：(搜索結果)")
            is_find_search = ntp.is_track_more_search_grouplist()
            try:
                assert is_find_search == True
                case_step = case_step + cbz.case_step("檢查成功，有搜索到結果")
                logging.info("檢查成功，有搜索到結果")
            except:
                actual = "檢查失敗！輸入文本'{}'搜索無結果".format(group_name)
                expect = "有搜索到結果"
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                       "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                find_result = ntp.find_track_more_search_grouplist(group_name)
                case_step = case_step + cbz.case_step("檢查③：(文本內容)")
                try:
                    assert find_result == True
                    case_step = case_step + cbz.case_step("檢查成功，文本內容展示正確")
                    logging.info("檢查成功，文本內容展示正確")
                except:
                    actual = "檢查失敗！輸入文本'{}'在搜索结果中查找不到对象".format(group_name)
                    expect = "文本內容展示正確"
                    video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ntp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                           "最新動態")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
            finally:
                 ntp.return_button()

    # 隱私設定:私密                                                 作者：游同同    时间：2020/3/27
    @allure.title("隱私設定:私密")  # 用例標題
    @allure.description("隱私設定:創建私密群組後不能夠被搜索到")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_found_group_set_private(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "隱私設定:創建私密群組後不能夠被搜索到"
        test_chat.temp_num += 1
        case_name = "test_found_group_set_private"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     隱私設定:私密    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                           # 點擊：[群組] tab
        case_step = case_step + cbz.case_step("3、點擊：[建立群組]按鈕")
        ntp.click_create_group_button()                                 # 點擊：[建立群組]按鈕
        letter1 = ntp.random_english_letter()
        letter2 = ntp.random_english_letter()
        letter3 = ntp.random_english_letter()
        group_name = CD.create_group_text + letter1 + letter2 + letter3 + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入群組名稱'{}'".format(group_name))
        ntp.input_create_group_name_input(group_name)                       # 輸入群組名稱
        case_step = case_step + cbz.case_step("5、點擊：'建立群組'頁面-[私密]單選按鈕")
        ntp.click_create_group_private_icon()                               # 點擊：'建立群組'頁面-[私密]單選按鈕
        case_step = case_step + cbz.case_step("6、點擊：[建立群組]完成按鈕")
        ntp.click_create_group_done_button()                                 # 點擊：[建立群組]完成按鈕
        case_step = case_step + cbz.case_step("7、點擊：[探索群組]按鈕")
        ntp.click_explore_group_button()                                    # 點擊：[探索群組]按鈕
        case_step = case_step + cbz.case_step("輸入群組名'test{0}{1}{2}'後觸發搜索".format(letter1, letter2, letter3))
        ntp.input_track_more_search_box(letter1, letter2, letter3)          # 輸入群組名後觸發搜索
        find_result = ntp.find_track_more_search_grouplist(group_name)
        case_step = case_step + cbz.case_step("檢查:")
        try:
            assert find_result == False
            case_step = case_step + cbz.case_step('檢查成功，未搜索到私密群組"{}"'.format(group_name))
            logging.info('檢查成功，未搜索到私密群組"{}"'.format(group_name))
        except:
            actual = "檢查失敗！輸入文本'{}'在搜索结果沒有展示私密群組".format(group_name)
            expect = '未搜索到私密群組"{}"'.format(group_name)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                   "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
             ntp.return_button()

    # 成員                                                        作者：游同同    时间：2020/3/27
    @allure.title("成員")  # 用例標題
    @allure.description("驗證成功創建群組後成員人數是否與創建時相匹配")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_found_group_add_member(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "驗證成功創建群組後成員人數是否與創建時相匹配"
        test_chat.temp_num += 1
        case_name = "test_found_group_add_member"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     成員:創建成員    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                               # 點擊：[群組] tab
        case_step = case_step + cbz.case_step("3、點擊：[建立群組]按鈕")
        ntp.click_create_group_button()                                     # 點擊：[建立群組]按鈕
        letter1 = ntp.random_english_letter()
        letter2 = ntp.random_english_letter()
        letter3 = ntp.random_english_letter()
        group_name = CD.create_group_text + letter1 + letter2 + letter3 + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入群組名稱'{}'".format(group_name))
        ntp.input_create_group_name_input(group_name)                         # 輸入群組名稱
        case_step = case_step + cbz.case_step("5、點擊：'建立群組'頁面-[新增成員]")
        ntp.click_create_group_add_member_icon()                            # 點擊：'建立群組'頁面-[新增成員]
        member_number = 2
        case_step = case_step + cbz.case_step("6、[新增成員]頁面選中{}個人員".format(member_number))
        ntp.click_double_add_member_list(member_number)                     # [新增成員]頁面選中多個人員
        case_step = case_step + cbz.case_step("7、點擊：[建立群組]完成按鈕")
        ntp.click_create_group_done_button()                                # 點擊：[建立群組]完成按鈕
        case_step = case_step + cbz.case_step("8、點擊：[查看全部] 按鈕")
        ntp.click_group_tab_view_all()                                      # 點擊：[查看全部] 按鈕
        case_step = case_step + cbz.case_step("9、點擊指定群組'{}'".format(group_name))
        ntp.find_click_group(group_name)                                     # 點擊指定群組
        case_step = case_step + cbz.case_step("檢查：")
        member_count = ntp.get_group_home_group_count()                     # 獲取文本：群組主頁展示成員個數
        try:
            assert member_number + 1 == member_count
            case_step = case_step + cbz.case_step("檢查成功，創建群組時添加{}個成員，群組主頁展示成員個數為{}".format(member_number,member_count))
            logging.info("檢查成功，創建群組時添加{}個成員，群組主頁展示成員個數為{}".format(member_number,member_count))
        except:
            actual = "檢查失敗!創建群組時添加{}個成員，群組主頁展示成員個數為{}".format(member_number,member_count)
            expect = '群組主頁展示成員數=添加成員數+1'
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                   "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.return_button()


@pytest.mark.nf
@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("群組")
@allure.sub_suite("探索群組")
@allure.feature("最新動態/群組/探索群組")
@allure.story("探索群組:页面相关功能")
@pytest.mark.usefixtures("startApp_withReset")
class TestSearchGroup:

    # 篩選                                                         作者：游同同    时间：2020/3/19
    @allure.title("篩選")  # 用例標題
    @allure.description("篩選:通過字母導航快速定位")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_search_group_filter(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "探索群組-篩選:通過字母導航快速定位"
        test_chat.temp_num += 1
        case_name = "test_search_group_filter"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     探索群組-篩選    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                     # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                      # 點擊：[群組] tab
        case_step = case_step + cbz.case_step("3、點擊：[探索群組]按鈕")
        ntp.click_explore_group_button()                           # 點擊：[探索群組]按鈕
        case_step = case_step + cbz.case_step("4、點擊：'追蹤更多'頁面-[導航欄]-M或N")
        ntp.click_track_more_navigate_M()                          # 點擊："追蹤更多"頁面-[導航欄]-W或N
        get_head = ntp.get_list_head_title()  # 獲取群組列表中群組首字母第一個
        case_step = case_step + cbz.case_step("5、當前屏幕群組列表中群組第一個首字母為{},並檢查：".format(get_head))
        try:
            assert get_head == 'M' or get_head == 'N' or get_head == 'P'
            case_step = case_step + cbz.case_step("檢查成功，字母導航欄快速篩選功能正常")
            logging.info("檢查成功，字母導航欄快速篩選功能正常")
        except:
            actual = "檢查失敗！點擊字母導航欄-W，定位到的通訊位置為{}".format(get_head)
            expect = '字母導航欄快速篩選功能正常'
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],"最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.return_button()

    # 搜索                                                        作者：游同同    时间：2020/3/19
    @allure.title("搜索")  # 用例標題
    @allure.description("搜索:出現符合搜索條件的群組列表")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_search_group_search(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "搜索:出現符合搜索條件的群組列表"
        test_chat.temp_num += 1
        case_name = "test_search_group_search"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     探索群組-搜索    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                     # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                      # 點擊：[群組] tab
        case_step = case_step + cbz.case_step("3、點擊：[建立群組]按鈕")
        ntp.click_create_group_button()                            # 點擊：[建立群組]按鈕
        letter1 = ntp.random_english_letter()
        letter2 = ntp.random_english_letter()
        letter3 = ntp.random_english_letter()
        group_name = CD.create_group_text + letter1 + letter2 + letter3 + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入群組名稱'{}'".format(group_name))
        ntp.input_create_group_name_input(group_name)               # 輸入群組名稱
        case_step = case_step + cbz.case_step("5、點擊：[建立群組]完成按鈕")
        ntp.click_create_group_done_button()                       # 點擊：[建立群組]完成按鈕
        case_step = case_step + cbz.case_step("6、點擊：[探索群組]按鈕")
        ntp.click_explore_group_button()                           # 點擊：[探索群組]按鈕
        case_step = case_step + cbz.case_step("检查①：")
        is_find = ntp.find_track_more_grouplist()
        try:
            assert is_find == True
            case_step = case_step + cbz.case_step("检查成功，未输入关键词筛选有列出群组列表")
            logging.info("检查成功，未输入关键词筛选有列出群组列表")
        except:
            actual = "检查失败！未输入关键词筛选时群组列表展示异常"
            expect = '未输入关键词筛选有列出群组列表'
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                   "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("輸入群組名'test{0}{1}{2}'後觸發搜索".format(letter1, letter2, letter3))
            ntp.input_track_more_search_box(letter1, letter2, letter3)    # 輸入群組名後觸發搜索
            case_step = case_step + cbz.case_step('檢查②：(搜索結果)')
            is_find_search = ntp.is_track_more_search_grouplist()
            try:
                assert is_find_search == True
                case_step = case_step + cbz.case_step('檢查成功，有搜索到結果')
                logging.info("檢查成功，有搜索到結果")
            except:
                actual = "檢查失敗！輸入文本'{}'搜索無結果".format(group_name)
                expect = '有搜索到結果'
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                       "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                find_result = ntp.find_track_more_search_grouplist(group_name)
                case_step = case_step + cbz.case_step('檢查③：(文本內容)')
                try:
                    assert find_result == True
                    case_step = case_step + cbz.case_step('檢查成功，有搜索到結果')
                    logging.info("檢查成功，有搜索到結果")
                except:
                    actual = "檢查失敗！輸入文本'{}'在搜索结果中查找不到对象".format(group_name)
                    expect = '搜索結果能找到對象'
                    video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ntp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                           "最新動態")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
            finally:
                 ntp.return_button()

    # 個人                                                        作者：游同同    时间：2020/3/19
    @allure.title("個人")  # 用例標題
    @allure.description("個人:可追踪功能检查")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_search_group_personal(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "個人:可追踪功能检查"
        test_chat.temp_num += 1
        case_name = "test_search_group_personal"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     探索群組-個人    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                     # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                      # 點擊：[群組] tab
        case_step = case_step + cbz.case_step("3、點擊：[探索群組]按鈕")
        ntp.click_explore_group_button()                           # 點擊：[探索群組]按鈕
        case_step = case_step + cbz.case_step("4、點擊：'追蹤更多'頁面-[個人]tab")
        ntp.click_track_more_personal_tab()                        # 點擊：'追蹤更多'頁面-[個人]tab
        index = ntp.get_list_one_track_index()
        user_name = ntp.get_list_one_track_name(index)  # 獲取文本：個人tab中第一個"追蹤"的用戶名稱並點擊「追蹤」按鈕
        case_step = case_step + cbz.case_step("5、獲取文本：個人tab中第一個可'追蹤'的用戶名为：{}；稱並點擊「追蹤」按鈕".format(user_name))
        case_step = case_step + cbz.case_step("6、點擊:返回")
        ntp.return_button()                                        # 點擊:返回
        case_step = case_step + cbz.case_step("7、點擊：【個人】tab")
        ntp.click_personal_tab()                                   # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("8、點擊：個人tab「追踪中」")
        ntp.click_personal_trace()                                 # 點擊：個人tab「追踪中」
        case_step = case_step + cbz.case_step("檢查：")
        is_find_trace_user = ntp.is_personal_trace_list_user(user_name)     # 查找用戶是否在追踪列表中
        try:
            assert is_find_trace_user == True
            case_step = case_step + cbz.case_step("檢查成功，追蹤中的用戶被展示在'追蹤中'tab中")
            logging.info("檢查成功，追蹤中的用戶被展示在'追蹤中'tab中")
        except:
            actual = "檢查失敗！追蹤中的用戶'{}'沒有出現在個人tab-追蹤中的列表中".format(user_name)
            expect = "追蹤中的用戶被展示在'追蹤中'tab中"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                   "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("9、點擊查找到的用戶'{}'".format(user_name))
            ntp.click_find_user(user_name)                          # 點擊查找到的用戶
            case_step = case_step + cbz.case_step("10、點擊：用戶主頁[追踪中]按鈕")
            ntp.click_personal_home_page_trace()                     # 點擊：用戶主頁[追踪中]按鈕
            case_step = case_step + cbz.case_step("11、連續2次返回")
            ntp.return_button()
            ntp.return_button()
            case_step = case_step + cbz.case_step("12、點擊：[群組] tab")
            ntp.click_group_tab()                                    # 點擊：[群組] tab
            case_step = case_step + cbz.case_step("13、點擊：[探索群組]按鈕")
            ntp.click_explore_group_button()                         # 點擊：[探索群組]按鈕
            case_step = case_step + cbz.case_step("14、點擊：'追蹤更多'頁面-[個人]tab")
            ntp.click_track_more_personal_tab()                     # 點擊：'追蹤更多'頁面-[個人]tab
            case_step = case_step + cbz.case_step("檢查：")
            button_name = ntp.get_list_one_track_button_name(index)
            try:
                assert button_name == "追蹤"
                case_step = case_step + cbz.case_step("檢查成功，取消'{}'追蹤後按鈕文案變為'追蹤'".format(user_name))
                logging.info("檢查成功，取消'{}'追蹤後按鈕文案變為'追蹤'".format(user_name))
            except:
                actual = "檢查失敗！取消追蹤後按鈕文案變為'{}'".format(button_name)
                expect = "追蹤中的用戶被展示在'追蹤中'tab中"
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                       "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            finally:
                ntp.return_button()
        finally:
            ntp.return_button()

    # 群組-非群組中成員                                             作者：游同同    时间：2020/3/19
    @allure.title("群組:非群組中成員")  # 用例標題
    @allure.description("群組（非群組中成員）:可追踪功能检查")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_search_group_group_not_member(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "群組（非群組中成員）:可追踪功能检查"
        test_chat.temp_num += 1
        case_name = "test_search_group_group_not_member"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     探索群組-群組:非群組中成員   *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                     # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                      # 點擊：[群組] tab
        case_step = case_step + cbz.case_step("3、點擊：[探索群組]按鈕")
        ntp.click_explore_group_button()                           # 點擊：[探索群組]按鈕
        index = ntp.get_list_one_group_track_index()               # 第一个【追蹤】按钮索引
        group_name = ntp.get_list_one_group_track_name(index)      # 獲取第一個可追蹤的群組名稱並點擊「追蹤」按鈕
        case_step = case_step + cbz.case_step("4、獲取第一個可追蹤的群組名稱為'{}'，並點擊「追蹤」按鈕".format(group_name))
        case_step = case_step + cbz.case_step("5、點擊:返回")
        ntp.return_button()                                     # 點擊:返回
        case_step = case_step + cbz.case_step("6、點擊：【個人】tab")
        ntp.click_personal_tab()                                # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("7、點擊：個人tab「追踪中」")
        ntp.click_personal_trace()                              # 點擊：個人tab「追踪中」
        case_step = case_step + cbz.case_step("檢查①：")
        find_droup = ntp.find_track_group_list_all(group_name)
        try:
            assert find_droup == True
            case_step = case_step + cbz.case_step("检查成功，群组中有展示被追踪的群组'{}'".format(group_name))
            logging.info("检查成功，群组中有展示被追踪的群组'{}'".format(group_name))
        except:
            actual = "检查失败！追踪中的群组中没有找到''".format(group_name)
            expect = "群组中有展示被追踪的群组'{}'".format(group_name)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                   "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("8、點擊查找到的群组'{}'".format(group_name))
            ntp.click_find_user(group_name)                     # 點擊查找到的群组
            case_step = case_step + cbz.case_step("9、點擊：群組中更多icon-「取消追蹤」按鈕")
            ntp.click_personal_home_trace_group_cancel()        # 點擊：群組中更多icon-「取消追蹤」按鈕
            case_step = case_step + cbz.case_step("10、點擊2次返回")
            ntp.return_button()
            ntp.return_button()
            case_step = case_step + cbz.case_step("11、點擊：[群組] tab")
            ntp.click_group_tab()                           # 點擊：[群組] tab
            case_step = case_step + cbz.case_step("12、點擊：[探索群組]按鈕")
            ntp.click_explore_group_button()                # 點擊：[探索群組]按鈕
            case_step = case_step + cbz.case_step("檢查②：")
            track_button_text = ntp.get_list_group_one_track_button_name(index)
            try:
                assert track_button_text == "追蹤"
                case_step = case_step + cbz.case_step("檢查成功，取消'{}'追蹤後按鈕文案變為'追蹤'".format(group_name))
                logging.info("檢查成功，取消'{}'追蹤後按鈕文案變為'追蹤'".format(group_name))
            except:
                actual = "檢查失敗！取消追蹤後按鈕文案變為'{}'".format(track_button_text)
                expect = "取消'{}'追蹤後按鈕文案變為'追蹤'".format(group_name)
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                       "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            finally:
                ntp.return_button()
        finally:
            ntp.return_button()

    # 群組-群組中成員                                               作者：游同同    时间：2020/3/19
    @allure.title("群組:群組中成員")  # 用例標題
    @allure.description("群組（群組中成員）:不可追踪功能检查，可退出")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_search_group_group_member(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "群組（群組中成員）:不可追踪功能检查"
        test_chat.temp_num += 1
        case_name = "test_search_group_group_member"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     探索群組-群組:群組中成員不可追踪   *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                          # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                           # 點擊：[群組] tab
        case_step = case_step + cbz.case_step("3、點擊：[建立群組]按鈕")
        ntp.click_create_group_button()                            # 點擊：[建立群組]按鈕
        letter1 = ntp.random_english_letter()
        letter2 = ntp.random_english_letter()
        letter3 = ntp.random_english_letter()
        group_name = CD.create_group_text + letter1 + letter2 + letter3 + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入群組名稱'{}'".format(group_name))
        ntp.input_create_group_name_input(group_name)              # 輸入群組名稱
        case_step = case_step + cbz.case_step("5、點擊：[建立群組]完成按鈕")
        ntp.click_create_group_done_button()                       # 點擊：[建立群組]完成按鈕
        case_step = case_step + cbz.case_step("6、點擊：[探索群組]按鈕")
        ntp.click_explore_group_button()                           # 點擊：[探索群組]按鈕
        case_step = case_step + cbz.case_step("7、輸入群組名'test{0}{1}{2}'後觸發搜索".format(letter1, letter2, letter3))
        ntp.input_track_more_search_box(letter1, letter2, letter3)  # 輸入群組名後觸發搜索
        case_step = case_step + cbz.case_step("8、點擊：'追蹤更多'頁面群組tab-「追蹤」按鈕")
        ntp.click_track_more_track_button()                         # 點擊："追蹤更多"頁面群組tab-「追蹤」按鈕
        case_step = case_step + cbz.case_step("檢查：")
        find_quit = ntp.find_quit_group_button()
        try:
            assert find_quit == True
            case_step = case_step + cbz.case_step("檢查成功，有彈出'退出群組'提示彈框")
            logging.info("檢查成功，有彈出'退出群組'提示彈框")
        except:
            actual = "檢查失敗！彈出'退出群組'提示彈框異常"
            expect = "有彈出'退出群組'提示彈框"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                   "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.click_quit_group_button()  # 點擊：退出群组弹框-【確定退出】按钮
            ntp.return_button()

@pytest.mark.nf
@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("群組")
@allure.sub_suite("你的群組")
@allure.feature("最新動態/群組/你的群組")
@allure.story("你的群組:模块相关功能")
@pytest.mark.usefixtures("startApp_withReset")
class TestNfYourGroup:

    # 群組                                                            作者：游同同    时间：2020/3/23
    @allure.title("群組")  # 用例標題
    @allure.description("點擊群組頭像或暱稱機內對應群組")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_search_group_title_jump(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "點擊群組頭像或暱稱機內對應群組"
        test_chat.temp_num += 1
        case_name = "test_search_group_title_jump"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     群組:群組頭像、名稱    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                              # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                                # 點擊：[群組] tab
        case_step = case_step + cbz.case_step("3、點擊：[建立群組]按鈕")
        ntp.click_create_group_button()                                     # 點擊：[建立群組]按鈕
        letter1 = ntp.random_english_letter()
        letter2 = ntp.random_english_letter()
        letter3 = ntp.random_english_letter()
        group_name = CD.create_group_text + letter1 + letter2 + letter3 + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入群組名稱'{}'".format(group_name))
        ntp.input_create_group_name_input(group_name)                            # 輸入群組名稱
        case_step = case_step + cbz.case_step("5、點擊：[建立群組]完成按鈕")
        ntp.click_create_group_done_button()                                # 點擊：[建立群組]完成按鈕
        case_step = case_step + cbz.case_step("6、點擊：[查看全部] 按鈕")
        ntp.click_group_tab_view_all()                              # 點擊：[查看全部] 按鈕
        case_step = case_step + cbz.case_step("7、查找對應群組並點擊")
        ntp.find_click_group(group_name)                            # 查找對應群組並點擊
        case_step = case_step + cbz.case_step("檢查：")
        get_group_name = ntp.get_group_page_group_title_name()
        try:
            assert get_group_name == group_name
            case_step = case_step + cbz.case_step("檢查成功，跳轉對應的群組正確")
            logging.info("檢查成功，跳轉對應的群組正確")
        except:
            actual = "檢查失敗！點擊群組名'{0}'，實際跳轉到'{1}'".format(group_name,get_group_name)
            expect = "跳轉對應的群組正確"
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

    # 查看全部:成員                                                   作者：游同同    时间：2020/3/23
    @allure.title("查看全部:成员")  # 用例標題
    @allure.description("查看全部:管理員人數+成員數是否正確")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_your_group_member(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "查看全部:管理員人數+成員數是否正確"
        test_chat.temp_num += 1
        case_name = "test_your_group_member"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  查看全部:管理員人數+成員數     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                  # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                   # 點擊：[群組] tab
        case_step = case_step + cbz.case_step("3、點擊：[查看全部] 按鈕")
        ntp.click_group_tab_view_all()                           # 點擊：[查看全部] 按鈕
        case_step = case_step + cbz.case_step("4、點擊：'你的群組'頁面列表中第一個群組")
        ntp.click_your_group_page_list()                         # 點擊："你的群組"頁面列表中第一個群組
        cont_group = ntp.get_group_home_group_count()            # 獲取文本：群組主頁展示成員個數
        case_step = case_step + cbz.case_step("5、點擊：群組主頁-成員頭像")
        ntp.click_group_home_member_avatar()                     # 點擊：群組主頁-成員頭像
        case_step = case_step + cbz.case_step("检查：")
        group_list_number = ntp.get_group_member_list()          # 獲取列數：'成員和粉絲'頁面用戶數
        try:
            assert group_list_number == cont_group
            case_step = case_step + cbz.case_step("檢查成功，{}位成员展示功能正常".format(cont_group))
            logging.info("檢查成功，{}位成员展示功能正常".format(cont_group))
        except:
            actual = "檢查失敗！群组主頁展示成員總數為{}，成員頁面列表實際有{}個成员".format(cont_group,group_list_number)
            expect = "{}位成员展示功能正常".format(cont_group)
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

    # 查看全部:追蹤中                                                   作者：游同同    时间：2020/3/23
    @allure.title("查看全部:追蹤中")  # 用例標題
    @allure.description("查看全部:追蹤中功能是否正常")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_your_group_track(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "查看全部:追蹤中功能是否正常"
        test_chat.temp_num += 1
        case_name = "test_your_group_track"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  查看全部:追蹤中     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                          # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                           # 點擊：[群組] tab
        case_step = case_step + cbz.case_step("3、點擊：[探索群組]按鈕")
        ntp.click_explore_group_button()                           # 點擊：[探索群組]按鈕
        index = ntp.get_list_one_group_track_index()               # 第一个【追蹤】按钮索引
        group_name = ntp.get_list_one_group_track_name(index)      # 獲取第一個可追蹤的群組名稱並點擊「追蹤」按鈕
        case_step = case_step + cbz.case_step("4、獲取第一個可追蹤的群組名稱為'{}'，並點擊「追蹤」按鈕".format(group_name))
        case_step = case_step + cbz.case_step("5、點擊:返回")
        ntp.return_button()                                        # 點擊:返回
        case_step = case_step + cbz.case_step("6、點擊：[查看全部] 按鈕")
        ntp.click_group_tab_view_all()                             # 點擊：[查看全部] 按鈕
        case_step = case_step + cbz.case_step("7、點擊：'你的群组'页面-【追踪中】tab")
        ntp.click_your_group_following_tab()                       # 點擊：'你的群组'页面-【追踪中】tab
        list_index = ntp.get_following_tab_group_index(group_name)  # 获取目标群组的索引
        case_step = case_step + cbz.case_step("检查：")
        try:
            assert list_index != -1
            case_step = case_step + cbz.case_step("检查成功，群组名为'{}'有出现在【追踪中】tab中".format(group_name))
            logging.info("检查成功，群组名为'{}'有出现在【追踪中】tab中".format(group_name))
        except:
            actual = "检查失败！群组名为'{}'没有出现在【追踪中】tab中".format(group_name)
            expect = "群组名为'{}'有出现在【追踪中】tab中".format(group_name)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.click_following_tab_list_following_button(list_index)     # 取消追踪
            ntp.return_button()

    # 查看全部:其他                                                   作者：游同同    时间：2020/3/23
    @allure.title("查看全部:其他")  # 用例標題
    @allure.description("查看全部:其他tab展示没有追踪的用戶或群组")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_your_group_other(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "查看全部:其他tab展示没有追踪的用戶或群组"
        test_chat.temp_num += 1
        case_name = "test_your_group_other"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  查看全部:其他      *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                     # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                      # 點擊：[群組] tab
        case_step = case_step + cbz.case_step("3、點擊：[查看全部] 按鈕")
        ntp.click_group_tab_view_all()                             # 點擊：[查看全部] 按鈕
        ntp.click_your_group_page_other_tab()                      # 點擊："你的群组"页面-【其他】tab
        list_one_name = ntp.get_other_tab_user_list()              # 獲取文本： "你的群组"页面-【其他】tab 第一個用戶暱稱
        ntp.click_other_tab_track_button()                         # 點擊："你的群组"页面-【其他】tab - [追踪]按钮
        case_step = case_step + cbz.case_step("4、點擊：'你的群组'页面-【追踪中】tab")
        ntp.click_your_group_following_tab()                        # 點擊：'你的群组'页面-【追踪中】tab
        list_index = ntp.get_following_tab_group_index(list_one_name)  # 获取目标群组的索引
        logging.info("目标群组的索引为'{}'".format(list_index))
        case_step = case_step + cbz.case_step("检查：")
        try:
            assert list_index != -1
            case_step = case_step + cbz.case_step("检查成功，對象为'{}'有出现在【追踪中】tab中".format(list_one_name))
            logging.info("检查成功，對象为'{}'有出现在【追踪中】tab中".format(list_one_name))
        except:
            actual = "检查失败！對象名为'{}'没有出现在【追踪中】tab中".format(list_one_name)
            expect = "對象为'{}'有出现在【追踪中】tab中".format(list_one_name)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.click_following_tab_list_following_button(list_index)
            ntp.return_button()


@pytest.mark.nf
@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("群組")
@allure.sub_suite("群組帖子")
@allure.feature("最新動態/群組/群組帖子")
@allure.story("群組帖子:页面相关功能")
@pytest.mark.usefixtures("startApp_withReset")
class TestGroupPost:

    # 頭像/暱稱/分享到的位置                                              作者：游同同    时间：2020/3/23
    @allure.title("頭像/暱稱/分享到的位置")  # 用例標題
    @allure.description("點擊「群組」tab中帖子用戶跳轉至首頁")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_group_post_user_homepage(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "點擊「群組」tab中帖子用戶跳轉至首頁"
        test_chat.temp_num += 1
        case_name = "test_group_post_user_homepage"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  群組帖子：頭像/暱稱/分享到的位置     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                     # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                      # 點擊：[群組] tab
        one_post_user_name = ntp.get_group_page_one_post_user_name()    # 獲取第一個帖子的群組或用戶暱稱
        case_step = case_step + cbz.case_step("3、點擊：第一個帖子用戶暱稱")
        ntp.click_group_page_one_post_user_name()                  # 點擊：第一個帖子用戶暱稱
        case_step = case_step + cbz.case_step("檢查：")
        is_jump_home = ntp.is_jump_home_page()                     # 判斷是否跳轉
        try:
            assert is_jump_home == True
            case_step = case_step + cbz.case_step("檢查成功，點擊用戶名'{}'跳轉主頁成功".format(one_post_user_name))
            logging.info("檢查成功，點擊用戶名'{}'跳轉主頁成功".format(one_post_user_name))
            ntp.return_button()          # 跳轉成功則點擊返回
        except:
            actual = "檢查失敗！點擊帖子用戶名'{}'跳轉主頁失敗".format(one_post_user_name)
            expect = "點擊用戶名'{}'跳轉主頁成功".format(one_post_user_name)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 管理員身份/個人                                                    作者：游同同    时间：2020/3/23
    @allure.title("管理員身份/個人")  # 用例標題
    @allure.description("公開群組身份發送帖子，可在群组tab中找到帖子")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_group_post_group_can_share(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "公開群組身份發送帖子，可分享"
        test_chat.temp_num += 1
        case_name = "test_group_post_group_can_share"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********    管理員身份/個人     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【最新動態】")
        ntp.click_newdynamic()                                     # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊最新動態-全部tab")
        ntp.click_all_tab()                                        # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：'你在想什麼?'發帖入口")
        ntp.click_publish_dynamic()                                # 點擊：'你在想什麼?'發帖入口
        input_text = CD.post_fend_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(input_text))
        ntp.inptu_publish_input(input_text)                        # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：[個人動態]跳转按钮")
        ntp.click_personal_dynamic()                                # 點擊：[個人動態]跳转按钮
        list_number = ntp.get_share_list_number()                       # 分享可选群组个数
        if list_number >= 2:
            case_step = case_step + cbz.case_step("6、點擊第2個分享對象後點擊「完成」按鈕")
            ntp.click_random_Object()                              # 點擊2個分享對象後點擊「完成」按鈕
        case_step = case_step + cbz.case_step("7、點擊：「發帖」按鈕")
        ntp.click_publish_button()                                 # 點擊：「發帖」按鈕
        ntp.wait_fend_post_loading_icon()                          # 等待【加载中...】提示消失
        case_step = case_step + cbz.case_step("8、點擊：[群組] tab")
        ntp.click_group_tab()                                      # 點擊：[群組] tab
        get_one_post_text = ntp.get_group_tab_one_post_text()      # 获取文本：群组tab中第一个贴子的文本
        case_step = case_step + cbz.case_step("检查①：")
        try:
            assert get_one_post_text == input_text
            case_step = case_step + cbz.case_step("检查成功,发送的群组贴有在群组teb中找到")
            logging.info("检查成功,发送的群组贴有在群组teb中找到")
        except:
            actual = "检查失败！发送文本'{}'群组贴文后在群组tab中没有找到对应贴子".format(input_text)
            expect = "发送的群组贴有在群组teb中找到"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("9、点击：群组tab中第一个贴子的文本")
            ntp.click_group_tab_one_post_text()             # 点击：群组tab中第一个贴子的文本
            find_share_icon = ntp.find_group_tab_post_share_icon()
            case_step = case_step + cbz.case_step("检查②：")
            try:
                assert find_share_icon == True
                case_step = case_step + cbz.case_step("檢查成功，該公開貼文可以被分享")
                logging.info("檢查成功，該公開貼文可以被分享")
            except:
                actual = "檢查失敗！該公開貼文不可被分享"
                expect = "該公開貼文可以被分享"
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

    # 公開/私密                                                          作者：游同同    时间：2020/3/24
    @allure.title("公開/私密")  # 用例標題
    @allure.description("以管理員身份發送一條私密貼文不可分享")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_group_public_post_no_share(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "公開/私密：以管理員身份發送一條私密貼文不可分享"
        test_chat.temp_num += 1
        case_name = "test_group_public_post_no_share"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********    公開/私密     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                              # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊最新動態-全部tab")
        ntp.click_all_tab()                                                 # 点击最新动态-全部tab
        case_step = case_step + cbz.case_step("3、點擊：'你在想什麼?'發帖入口")
        ntp.click_publish_dynamic()                                         # 點擊：'你在想什麼?'發帖入口
        input_text = CD.post_fend_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(input_text))
        ntp.inptu_publish_input(input_text)                                 # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：[個人動態]跳转按钮")
        ntp.click_personal_dynamic()                                        # 點擊：[個人動態]跳转按钮
        list_number = ntp.get_share_list_number()                      # 分享可选群组个数
        if list_number >= 2:
            case_step = case_step + cbz.case_step("6、點擊第2個分享對象後點擊「完成」按鈕")
            ntp.click_random_Object()                              # 點擊2個分享對象後點擊「完成」按鈕
        case_step = case_step + cbz.case_step("7、點擊：建立贴文页面-【管理员身份】下拉按钮")
        ntp.click_set_post_admin_button()                             # 點擊：建立贴文页面-【管理员身份】下拉按钮
        case_step = case_step + cbz.case_step("8、點擊：下拉列表選項「個人身份」")
        ntp.click_set_post_page_admin_list_one()                      # 點擊：下拉列表選項「個人身份」
        case_step = case_step + cbz.case_step("9、點擊：建立贴文页面- [公開帖文]下拉列表-[私密貼文]選項")
        ntp.click_public_post_buttn()                                 # 點擊：建立贴文页面- [公開帖文]下拉列表-[私密貼文]選項
        case_step = case_step + cbz.case_step("10、點擊：「發帖」按鈕")
        ntp.click_publish_button()                                # 點擊：「發帖」按鈕
        ntp.wait_fend_post_loading_icon()                         # 等待【加载中...】提示消失
        case_step = case_step + cbz.case_step("11、點擊：[群組] tab")
        ntp.click_group_tab()                                      # 點擊：[群組] tab
        get_one_post_text = ntp.get_group_tab_one_post_text()      # 获取文本：群组tab中第一个贴子的文本
        case_step = case_step + cbz.case_step("检查①：")
        try:
            assert get_one_post_text == input_text
            case_step = case_step + cbz.case_step("检查成功,发送的群组贴子有在群组teb中找到")
            logging.info("检查成功,发送的群组贴子有在群组teb中找到")
        except:
            actual = "检查失败！发送文本'{}'群组個人私密贴文后在群组tab中没有找到对应贴子".format(input_text)
            expect = "发送的群组贴子有在群组teb中找到"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("12、点击：群组tab中第一个贴子的文本")
            ntp.click_group_tab_one_post_text()                         # 点击：群组tab中第一个贴子的文本
            find_share_icon = ntp.find_group_tab_post_share_icon()
            case_step = case_step + cbz.case_step("检查②：")
            try:
                assert find_share_icon == False
                case_step = case_step + cbz.case_step("檢查成功，該私密貼文不可被分享")
                logging.info("檢查成功，該私密貼文不可被分享")
            except:
                actual = "檢查失敗！該私密貼文可以被分享"
                expect = "該私密貼文不可被分享"
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

    # 幾人點讚/幾個評論/幾次分享:點讚                                       作者：游同同    时间：2020/3/24
    @allure.title("幾人點讚/幾個評論/幾次分享:點讚")  # 用例標題
    @allure.description("對帖子進行點讚後，點讚次數變化1")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_group_post_like(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "對帖子進行點讚後，點讚次數變化1"
        test_chat.temp_num += 1
        case_name = "test_group_post_like"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********    幾人點讚/幾個評論/幾次分享:點讚     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                     # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                      # 點擊：[群組] tab
        case_step = case_step + cbz.case_step("3、點擊：跳轉帖子詳情頁（暱稱欄）")
        ntp.click_post_user_name()                                 # 點擊：跳轉帖子詳情頁（暱稱欄）
        before_like_number = ntp.get_post_detail_like_count_icon_number()  # 获取第一个动态点赞次数（点赞前）
        case_step = case_step + cbz.case_step("4、給第一個帖子點讚")
        ntp.click_group_tab_list_like_icon()                        # 給第一個帖子點讚
        case_step = case_step + cbz.case_step("檢查：")
        rear_like_number = ntp.get_post_detail_like_count_icon_number()  # 點讚後讚數
        like_bumber = abs(rear_like_number - before_like_number)
        try:
            assert like_bumber == 1       # 點讚前後差1
            case_step = case_step + cbz.case_step("檢查成功，點讚前後點讚次數差值為1")
            logging.info("檢查成功，點讚前後點讚次數差值為1")
        except:
            actual = "檢查失敗！點讚前後記錄帖子讚次數差值為{}".format(like_bumber)
            expect = "點讚前後點讚次數差值為1"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 幾人點讚/幾個評論/幾次分享:留言                                       作者：游同同    时间：2020/3/24
    @allure.title("幾人點讚/幾個評論/幾次分享:留言")  # 用例標題
    @allure.description("對帖子進行留言前後次數變化")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_group_post_comment(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "對帖子進行留言前後次數變化"
        test_chat.temp_num += 1
        case_name = "test_group_post_comment"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********    幾人點讚/幾個評論/幾次分享:留言     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                     # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                      # 點擊：[群組] tab
        ntp.action_group_tab_post_like_icon()                      # 處理帖子點讚icon可見
        case_step = case_step + cbz.case_step("3、點擊：列表帖子留言icon")
        ntp.click_group_tab_post_leave_icon()                      # 點擊：列表帖子留言icon
        comments_before_number = ntp.get_post_comment_number_icon() # 留言前獲取留言次數
        case_step = case_step + cbz.case_step("4、連續2次留言")
        ntp.comment_double(2,CD.send_message)                       # 連續2次留言
        comments_Rear_number = ntp.get_post_comment_number_icon()  # 留言後獲取留言次數
        case_step = case_step + cbz.case_step("檢查：")
        try:
            assert comments_Rear_number - comments_before_number == 2
            case_step = case_step + cbz.case_step("檢查成功，評論次數：留言前'{}'，評論後'{}'".format(comments_before_number, comments_Rear_number))
            logging.info("檢查成功，評論次數：留言前'{}'，評論後'{}'".format(comments_before_number, comments_Rear_number))
        except:
            actual = "檢查失敗！評論次數：留言前'{}'，評論3次後'{}'".format(comments_before_number,
                                                                              comments_Rear_number)
            expect = "评论前后次数显示相差2"
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

    # 幾人點讚/幾個評論/幾次分享:分享                                       作者：游同同    时间：2020/3/24
    @allure.title("幾人點讚/幾個評論/幾次分享:分享")  # 用例標題
    @allure.description("對帖子進行分享前後次數變化")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_group_post_commentsss(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "對帖子進行分享前後次數變化"
        test_chat.temp_num += 1
        case_name = "test_group_post_commentsss"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********    幾人點讚/幾個評論/幾次分享:分享     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                     # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()                                      # 點擊：[群組] tab
        ntp.action_group_tab_post_share_icon()                      # 處理帖子點讚icon可見
        comments_before_number = ntp.get_post_share_number_icon()  # 分享前獲取分享次數
        case_step = case_step + cbz.case_step("3、點擊：「分享」-分享")
        ntp.click_group_tab_post_share_icon()                      # 點擊：「分享」-分享
        comments_Rear_number = ntp.get_post_share_number_icon()    # 分享后獲取分享次數
        case_step = case_step + cbz.case_step("检查：")
        try:
            assert comments_Rear_number - comments_before_number == 1
            case_step = case_step + cbz.case_step("检查成功，分享两次后计数加1")
            logging.info("检查成功，分享两次后计数加1")
        except:
            actual = "检查失败！分享前计数为'{}'，两次分享后计数为'{}'".format(comments_before_number,
                                                                               comments_Rear_number)
            expect = "分享两次后计数加1"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise


@pytest.mark.nf
@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("個人")
@allure.sub_suite("")
@allure.feature("最新動態/個人")
@allure.story("個人:相关功能")
@pytest.mark.usefixtures("startApp_withReset")
class TestPersonalTab:

    # 暱稱                                                             作者：游同同    时间：2020/3/27
    @allure.title("暱稱")  # 用例標題
    @allure.description("暱稱:最终的昵称是否展示正确")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_user_name(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        ctp = CTP(startApp_withReset)
        title = "暱稱:最终的昵称是否展示正确"
        test_chat.temp_num += 1
        case_name = "test_personal_user_name"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     暱稱:最终的昵称是否展示正确    *********")
        ctp.click_chat_tab()                                    # 點擊【聊天】
        ctp.click_address_book_tab()                            # 點擊【通訊錄】tab
        random_number = ctp.random_int(7)
        user_name = ctp.get_book_list_user_name(random_number)     # 獲取隨機用戶的暱稱
        ctp.click_book_list_user_name(random_number)
        ctp.click_book_user_data_site_name_label()                 # 點擊：設定昵稱和標簽
        name_label = CD.user_name + ctp.random_str_share_china()
        ctp.input_book_user_data_site_name_label_input(name_label)  # 輸入：暱稱文本，並點擊「完成」
        ctp.return_button()
        case_Preposition = "进入通讯录给一个用户设定昵称'{}'".format(name_label)      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                           # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、点击【搜索】")
        ntp.click_search_button()                               # 点击【搜索】
        case_step = case_step + cbz.case_step("3、點擊輸入框並輸入‘{}’，搜索".format(name_label))
        ntp.input_search_text(name_label)                       # 点击搜索输入框，输入文本，点击键盘搜索按钮
        if ntp.get_search_user_track_button_text() == '追蹤中':
            case_step = case_step + cbz.case_step("4、搜索用戶'{}'已经是追踪状态，點擊【返回】".format(name_label))
            logging.info("搜索用戶'{}'已经是追踪状态，點擊【返回】".format(name_label))
            ntp.return_button()                                 # 點擊【返回】
        else:
            case_step = case_step + cbz.case_step("5、點擊：搜索-用戶「追蹤」按鈕")
            ntp.click_search_user_track_button()                # 點擊：搜索-用戶「追蹤」按鈕
            case_step = case_step + cbz.case_step("6、返回")
            ctp.return_button()
        case_step = case_step + cbz.case_step("7、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                             # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("8、點擊:個人tab[追蹤中]")
        ntp.click_personal_trace_tab()                          # 點擊:個人tab[追蹤中]
        case_step = case_step + cbz.case_step("檢查：")
        find_user = ntp.find_track_user(user_name)
        try:
            assert find_user == True
            case_step = case_step + cbz.case_step("檢查成功，追蹤中列表有找到'{}'".format(user_name))
            logging.info("檢查成功，追蹤中列表有找到'{}'".format(user_name))
        except:
            actual = "檢查失敗！追蹤中列表沒有找到'{}'".format(user_name)
            expect = "追蹤中列表有找到'{}'".format(user_name)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            index = ntp.find_personal_trace_user_name_index(user_name)
            ntp.click_personal_trace_user_name_index(index)                 # 取消追蹤
            ntp.wait_qroup_loading_icon()

    # 粉絲人數                                                          作者：游同同    时间：2020/3/27
    @allure.title("粉絲人數")  # 用例標題
    @allure.description("粉絲人數:展示粉絲人數是否與實際一致")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_tab_fens(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        ctp = CTP(startApp_withReset)
        title = "粉絲人數:展示粉絲人數是否與實際一致"
        test_chat.temp_num += 1
        case_name = "test_personal_tab_fens"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     個人:粉絲人數    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                      # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                             # 點擊：【個人】tab
        fans_count = ntp.get_personal_fans_count()              # 獲取個人tab展示粉絲總數
        case_step = case_step + cbz.case_step("3、點擊[粉丝人數")
        ntp.click_personal_fans()                               # 點擊[粉丝人數]
        case_step = case_step + cbz.case_step("檢查：")
        list_user = ntp.get_fan_list_count()                    # 列表中粉絲數
        try:
            assert  list_user == fans_count
            case_step = case_step + cbz.case_step("檢查成功，個人主頁統計粉絲數與實際粉絲數相符合")
            logging.info("檢查成功，個人主頁統計粉絲數與實際粉絲數相符合")
        except:
            actual = "檢查失敗！個人主頁展示粉絲數為{}，粉絲列表中實際有{}個粉絲".format(fans_count,list_user)
            expect = "個人主頁統計粉絲數與實際粉絲數相符合"
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

    # 追蹤中                                                            作者：游同同    时间：2020/3/27

    @allure.title("追蹤中")  # 用例標題
    @allure.description("追蹤中:先用戶的追蹤或取消統計人數有對應的增減")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_tab_track(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        ctp = CTP(startApp_withReset)
        title = "追蹤中:先用戶的追蹤或取消統計人數有對應的增減"
        test_chat.temp_num += 1
        case_name = "test_personal_tab_track"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     個人:追蹤中    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                  # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                             # 點擊：【個人】tab
        trace_count = ntp.get_personal_trace_count()            # 获取個人tab追踪中数量
        case_step = case_step + cbz.case_step("3、(追蹤人數{})點擊：個人tab「追踪中」".format(trace_count))
        ntp.click_personal_trace()                              # 點擊：個人tab「追踪中」
        case_step = case_step + cbz.case_step("4、點擊：「追蹤更多」跳轉")
        ntp.click_trace_more_icon()                             # 點擊：「追蹤更多」跳轉
        case_step = case_step + cbz.case_step("5、點擊：'追蹤更多'頁面-「個人」tab")
        ntp.click_trace_more_personal_tab()                     # 點擊：'追蹤更多'頁面-「個人」tab
        index = ntp.get_list_one_personal_track_index()         # 第一个【追蹤】按钮索引
        logging.info(index)
        case_step = case_step + cbz.case_step("6、獲取第一個可追蹤的用戶名並點擊「追蹤」按鈕")
        user_name = ntp.get_list_one_personal_track_name(index)    # 獲取第一個可追蹤的用戶名並點擊「追蹤」按鈕
        time.sleep(1)
        case_step = case_step + cbz.case_step("7、續兩次返回")
        ntp.return_button()                                     # 點擊:返回按鈕
        ntp.return_button()                                     # 點擊:返回按鈕
        time.sleep(2)
        case_step = case_step + cbz.case_step("8、下拉屏幕刷新")
        ntp.swipe_screen(0.5,0.3,0.5,0.7)                       # 下拉刷新
        time.sleep(1)
        trace_rear_count = ntp.get_personal_trace_count()       # 获取個人tab追踪中数量
        case_step = case_step + cbz.case_step("檢查：")
        try:
            assert trace_count + 1 == trace_rear_count
            case_step = case_step + cbz.case_step("檢查成功，追蹤一個用戶後追蹤中的數量有加1")
            logging.info("檢查成功，追蹤一個用戶後追蹤中的數量有加1")
        except:
            actual = "檢查失敗！追蹤前展示個數為{}，追蹤一個用戶後展示個數為{}".format(trace_count,trace_rear_count)
            expect = "追蹤一個用戶後追蹤中的數量有加1"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise


@pytest.mark.nf
@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("個人")
@allure.sub_suite("發帖")
@allure.feature("最新動態/個人/發帖")
@allure.story("發帖:相关功能")
@pytest.mark.usefixtures("startApp_withReset")
class TestPersonalSendPost:

    # 發布動態:頭像/暱稱/發布到的位置                                       作者：游同同    时间：2020/3/27
    @allure.title("發布動態:頭像/暱稱/發布到的位置")  # 用例標題
    @allure.description("發布一個群組動態不會展示在個人tab中")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_personal_tab_personal_post(self, startApp_withReset):
        ntp = NTP(startApp_withReset)
        ctp = CTP(startApp_withReset)
        title = "發布一個群組動態不會展示在個人tab中"
        test_chat.temp_num += 1
        case_name = "test_personal_tab_personal_post"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     發布動態:頭像/暱稱/發布到的位置    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                           # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                     # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                         # 點擊：個人tab[在想些什麼?]发帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                   # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：「發布」按鈕")
        ntp.click_post_publish_button()                            # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查①：(個人tab中有無發布的個人帖子)")
        send_post_text = ntp.get_personal_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，個人tab中有展示發布'{}'帖子".format(post_text))
            logging.info("檢查成功，個人tab中有展示發布'{}'帖子".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'到個人動態異常".format(post_text)
            expect = "個人tab中有展示發布'{}'帖子".format(post_text)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("6、點擊：[群組] tab")
            ntp.click_group_tab()                           # 點擊：[群組] tab
            case_step = case_step + cbz.case_step("检查②：(群組tab中有無發布的個人帖子)")
            one_post = ntp.get_group_tab_one_post_text()
            try:
                assert one_post != post_text
                case_step = case_step + cbz.case_step("檢查成功，群組tab中沒有找到個人帖子")
                logging.info("檢查成功，群組tab中沒有找到個人帖子")
            except:
                actual = "檢查失敗！群組tab中有找到發布的個人帖子'{}'".format(post_text)
                expect = "群組tab中不会展示個人帖子"
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1],
                                                       "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise

    # 發布動態:添加元素-標註人                                             作者：游同同    时间：2020/3/24
    @allure.title("發布動態:添加元素-標註人名")  # 用例標題
    @allure.description("發布動態:添加元素-標註人名搜索功能")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_tab_send_group_moving(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "發布動態:添加元素-標註人名搜索功能"
        test_chat.temp_num += 1
        case_name = "test_personal_tab_send_group_moving"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  發布動態:添加元素-標註人名搜索功能     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                           # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                      # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                          # 點擊：個人tab[在想些什麼?]发帖入口
        case_step = case_step + cbz.case_step("4、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                               # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("5、點擊：【标注人名】选项")
        ntp.click_callout_name()                                         # 點擊：【标注人名】选项
        list_one_name = ntp.get_callout_name_page_list_name()           # 獲取列表第一個用戶暱稱
        case_step = case_step + cbz.case_step("6、點擊：'标注人名'頁面-列表第一個用戶")
        ntp.click_callout_name_page_list_name()                     # 點擊：'标注人名'頁面-列表第一個用戶
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("7、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                     # 輸入文本
        case_step = case_step + cbz.case_step("8、點擊：「發布」按鈕")
        ntp.click_post_publish_button()                             # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查①：")
        send_post_text = ntp.get_personal_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布'{}'到個人動態成功".format(post_text))
            logging.info("檢查成功，發布'{}'到個人動態成功".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'到個人動態異常".format(post_text)
            expect = "發布'{}'到個人動態成功".format(post_text)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("检查②：(標註用戶暱稱)")
            get_name = ntp.get_post_user_name()         # 獲取帖子的展示用戶暱稱
            try:
                assert list_one_name.find(get_name) != -1
                case_step = case_step + cbz.case_step("檢查成功，帖子展示用戶名稱中包含標註人名'{}'".format(list_one_name))
                logging.info("檢查成功，帖子展示用戶名稱中包含標註人名'{}'".format(list_one_name))
            except:
                actual = "檢查失敗！帖子展示用戶名稱中沒有包含標註人名'{}'".format(list_one_name)
                expect = "帖子展示用戶名稱中包含標註人名'{}'".format(list_one_name)
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise

    # 發布動態:添加元素-相片/影片(選擇9張圖片)                                作者：游同同    时间：2020/3/24
    @allure.title("發布動態:添加元素-相片/影片")  # 用例標題
    @allure.description("發布動態:發送9張圖片")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_tab_send_double_photo(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "發布動態:發送9張圖片"
        test_chat.temp_num += 1
        case_name = "test_personal_tab_send_double_photo"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  發布動態:發送9張圖片    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                              # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                         # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                              # 點擊：個人tab[在想些什麼?]发帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                             # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                    # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：【相片/影片】选项")
        ntp.click_movie_photo()                                              # 點擊：【相片/影片】选项
        case_step = case_step + cbz.case_step("7、選擇9張圖片")
        ntp.click_douber_photo_send_button(9)                                 # 選擇9張圖片
        case_step = case_step + cbz.case_step("8、點擊：點擊「傳送」按鈕")
        ntp.click_photo_send_button()                                     # 點擊：點擊「傳送」按鈕
        case_step = case_step + cbz.case_step("9、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                             # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查：")
        send_post_text = ntp.get_personal_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布'{}'照片到個人動態成功".format(post_text))
            logging.info("檢查成功，發布'{}'照片到個人動態成功".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'照片到個人動態異常".format(post_text)
            expect = "發布'{}'照片到個人動態成功".format(post_text)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 發布動態:添加元素-相片/影片(刪除照片後點發布)                             作者：游同同    时间：2020/3/24
    @allure.title("發布動態:添加元素-相片/影片")  # 用例標題
    @allure.description("發布動態:添加照片後刪除再發送彈出toast")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_tab_send_cancel_photo(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "發布動態:添加照片後刪除再發送彈出toast"
        test_chat.temp_num += 1
        case_name = "test_personal_tab_send_cancel_photo"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  發布動態:添加照片後刪除再發送彈出toast    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                          # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                     # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                          # 點擊：個人tab[在想些什麼?]发帖入口
        case_step = case_step + cbz.case_step("4、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                               # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("5、點擊：【相片/影片】选项")
        ntp.click_movie_photo()                                    # 點擊：【相片/影片】选项
        case_step = case_step + cbz.case_step("6、選擇1張圖片")
        ntp.click_douber_photo_send_button(1)                      # 選擇1張圖片
        case_step = case_step + cbz.case_step("7、點擊：點擊「傳送」按鈕")
        ntp.click_photo_send_button()                              # 點擊：點擊「傳送」按鈕
        case_step = case_step + cbz.case_step("8、點擊：照片刪除按鈕")
        ntp.click_photo_delete_button()                            # 點擊：照片刪除按鈕
        case_step = case_step + cbz.case_step("9、點擊：「發布」按鈕")
        ntp.click_post_publish_button_no()                            # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("檢查：")
        is_send_toast = ntp.find_send_text_void_tost()
        try:
            assert is_send_toast == True
            case_step = case_step + cbz.case_step("檢查成功，有彈出'內容不能為空'tost")
            logging.info("檢查成功，有彈出'內容不能為空'tost")
        except:
            actual = "檢查失敗！沒有彈出'內容不能為空'tost"
            expect = "有彈出'內容不能為空'tost"
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
            ntp.is_click_return_quit_draft()

    # 發布動態:添加元素-相片/影片(超過9張圖片))                                 作者：游同同    时间：2020/3/24
    @allure.title("發布動態:添加元素-相片/影片")  # 用例標題
    @allure.description("發布動態:操過9張圖片時給toast提示")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_tab_send_beyond_photo_toast(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "發布動態:操過9張圖片時給toast提示"
        test_chat.temp_num += 1
        case_name = "test_personal_tab_send_beyond_photo_toast"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********    發布動態:操過9張圖片時給toast提示    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                                  # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                             # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                                  # 點擊：個人tab[在想些什麼?]发帖入口
        case_step = case_step + cbz.case_step("4、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                       # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("5、點擊：【相片/影片】选项")
        ntp.click_movie_photo()                                                 # 點擊：【相片/影片】选项
        case_step = case_step + cbz.case_step("6、選擇10張圖片並點擊傳送按鈕")
        ntp.click_douber_photo_send_button(10)                                 # 選擇10張圖片並點擊傳送按鈕
        case_step = case_step + cbz.case_step("檢查：")
        find_toast = ntp.find_fuck_photo_sum_tost()
        try:
            assert find_toast == True
            case_step = case_step + cbz.case_step("檢查成功，選擇第10張圖片時有彈出toast提示")
            logging.info("檢查成功，選擇第10張圖片時有彈出toast提示")
        except:
            actual = "檢查失敗！選擇第10張圖片時沒有彈出'最多只能選擇9張'toast"
            expect = "選擇第10張圖片時有彈出toast提示"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.click_photo_page_cancel_button()
            ntp.return_button()

    # 發布動態:添加元素-相片/影片(隨機選中一張發送)                               作者：游同同    时间：2020/3/24
    @allure.title("發布動態:添加元素-相片/影片")  # 用例標題
    @allure.description("發布動態:隨機選中一張照片發送")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_tab_send_random_photo(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "發布動態:隨機選中一張照片發送"
        test_chat.temp_num += 1
        case_name = "test_personal_tab_send_random_photo"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  發布動態:隨機選中一張照片發送    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                                      # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                                 # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                                     # 點擊：個人tab[在想些什麼?]发帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        ase_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                                   # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                           # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：【相片/影片】选项")
        ntp.click_movie_photo()                                                    # 點擊：【相片/影片】选项
        sum_photo = ntp.get_photo_sum()  # 獲取當前頁面照片數量
        index = ntp.random_int(sum_photo-1)
        case_step = case_step + cbz.case_step("7、選擇第{}張圖片".format(index+1))
        ntp.click_index_photo(index)                                               # 點擊其中一張圖片
        case_step = case_step + cbz.case_step("8、點擊：點擊「傳送」按鈕")
        ntp.click_photo_send_button()                              # 點擊：點擊「傳送」按鈕
        case_step = case_step + cbz.case_step("9、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                       # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查：")
        send_post_text = ntp.get_personal_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布'{}'照片到個人動態成功".format(post_text))
            logging.info("檢查成功，發布'{}'照片到個人動態成功".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'照片到個人動態異常".format(post_text)
            expect = "發布'{}'照片到個人動態成功".format(post_text)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.process_send_failure()              # 处理发送图片失败，退出回到首页

    # 拍照:重做                                                             作者：游同同    时间：2020/3/24
    @allure.title("拍照:重做")  # 用例標題
    @allure.description("拍照:重做能夠重新拍照")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_tab_afresh_photo(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "拍照:重做能夠重新拍照"
        test_chat.temp_num += 1
        case_name = "test_personal_tab_afresh_photo"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  拍照:重做能夠重新拍照    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                          # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                     # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                         # 點擊：個人tab[在想些什麼?]发帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                        # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                               # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：【拍照】选项")
        ntp.click_action_photo()                                    # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("7、點擊：快門icon")
        ntp.click_personal_tab_shutter_button()                     # 點擊：快門icon
        case_step = case_step + cbz.case_step("8、點擊：[重做]按鈕")
        ntp.click_personal_tab_media_cancel()                       # 點擊：[重做]按鈕
        case_step = case_step + cbz.case_step("檢查：")
        find_shutter_button = ntp.find_personal_tab_shutter_button()
        try:
            assert find_shutter_button == True
            case_step = case_step + cbz.case_step("檢查成功，點擊「重做」按鈕後回到拍照界面")
            logging.info("檢查成功，點擊「重做」按鈕後回到拍照界面")
        except:
            actual = "檢查失敗！點擊「重做」按鈕後回到拍照界面發生異常"
            expect = "點擊「重做」按鈕後回到拍照界面"
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

    # 拍照:傳送                                                              作者：游同同    时间：2020/3/24
    @allure.title("拍照:傳送")  # 用例標題
    @allure.description("拍照:多種編輯類型混合發送")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_tab_combination_send(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "拍照:多種編輯類型混合發送"
        test_chat.temp_num += 1
        case_name = "test_personal_tab_combination_send"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  拍照:多種編輯類型混合發送    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                          # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                     # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                         # 點擊：個人tab[在想些什麼?]发帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                    # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                           # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：【拍照】选项")
        ntp.click_action_photo()                                    # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("7、點擊：快門icon")
        ntp.click_personal_tab_shutter_button()                     # 點擊：快門icon
        case_step = case_step + cbz.case_step("8、點擊：拍照頁面-「傳送」按鈕")
        ntp.click_personal_tab_send_button()                        # 點擊：拍照頁面-「傳送」按鈕
        case_step = case_step + cbz.case_step("9、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                           # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("10、點擊：【相片/影片】选项")
        ntp.click_movie_photo()                                     # 點擊：【相片/影片】选项
        sum_photo = ntp.get_photo_sum()  # 獲取當前頁面照片數量
        index = ntp.random_int(sum_photo-1)
        case_step = case_step + cbz.case_step("11、選擇第{}張圖片".format(index+1))
        ntp.click_index_photo(index)                                # 點擊其中一張圖片
        case_step = case_step + cbz.case_step("12、點擊：點擊「傳送」按鈕")
        ntp.click_photo_send_button()                              # 點擊：點擊「傳送」按鈕
        case_step = case_step + cbz.case_step("13、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                       # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查：")
        send_post_text = ntp.get_personal_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布'{}'照片到個人動態成功".format(post_text))
            logging.info("檢查成功，發布'{}'照片到個人動態成功".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'照片到個人動態異常".format(post_text)
            expect = "發布'{}'照片到個人動態成功".format(post_text)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.process_send_failure()              # 处理发送图片失败，退出回到首页

    # 拍照:拍攝+拍照                                                          作者：游同同    时间：2020/3/24
    @allure.title("拍照:拍攝+拍照")  # 用例標題
    @allure.description("拍照:同時發送視頻和圖片")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_tab_afresh_photo(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "拍照:同時發送視頻和圖片"
        test_chat.temp_num += 1
        case_name = "test_personal_tab_afresh_photo"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  拍照:同時發送視頻和圖片    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                          # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                     # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                         # 點擊：個人tab[在想些什麼?]发帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                        # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：【拍照】选项")
        ntp.click_action_photo()                                         # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("7、點擊：快門icon")
        ntp.click_personal_tab_shutter_button()                          # 點擊：快門icon
        case_step = case_step + cbz.case_step("8、點擊：拍照頁面-「傳送」按鈕")
        ntp.click_personal_tab_send_button()                            # 點擊：拍照頁面-「傳送」按鈕
        case_step = case_step + cbz.case_step("9、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                               # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("10、點擊：【拍照】选项")
        ntp.click_action_photo()                                        # 點擊：【拍照】选项
        case_step = case_step + cbz.case_step("11、長按：拍攝視頻4s")
        ntp.long_tap_personal_tab_shutter_button()                      # 長按：拍攝視頻4s
        case_step = case_step + cbz.case_step("12、點擊：拍照頁面-「傳送」按鈕")
        ntp.click_personal_tab_send_button()                        # 點擊：拍照頁面-「傳送」按鈕
        case_step = case_step + cbz.case_step("13、點擊：「發布」按鈕")
        ntp.click_post_photo_publish_button()                       # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查：")
        send_post_text = ntp.get_personal_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布'{}'照片到個人動態成功".format(post_text))
            logging.info("檢查成功，發布'{}'照片到個人動態成功".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'照片到個人動態異常".format(post_text)
            expect = "發布'{}'照片到個人動態成功".format(post_text)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.process_send_failure()              # 处理发送图片失败，退出回到首页

    # 投票转为发帖                                                         作者：游同同    时间：2020/5/22
    @allure.title("投票转为发帖:文本有保留")  # 用例標題
    @allure.description("投票转为发帖:编辑发帖时添加投票然后又变更为发帖，保留编辑发帖操作")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_tab_vote_change_post(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "投票转为发帖:编辑发帖时添加投票然后又变更为发帖，没有保留编辑发帖操作"
        test_chat.temp_num += 1
        case_name = "test_personal_tab_vote_change_post"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  投票转为发帖:文本有保留    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                          # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                     # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                         # 點擊：個人tab[在想些什麼?]发帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                        # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：[提交投票]选项")
        ntp.click_submit_vote()                                          # 點擊：[提交投票]选项
        case_step = case_step + cbz.case_step("5、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("6、點擊：【建立帖文】选项")
        ntp.click_vote_page_set_post()                                   # 點擊：【建立帖文】选项
        input_text = ntp.get_publish_input_text()
        case_step = case_step + cbz.case_step("检查：")
        try:
            assert input_text == post_text
            case_step = case_step + cbz.case_step("检查成功，回到编辑帖子模式有保留上次操作")
            logging.info("检查成功，回到编辑帖子模式有保留上次操作")
        except:
            actual = "檢查失敗！保留上次编辑文本'{}'发生异常".format(post_text)
            expect = "回到编辑帖子模式有保留上次操作"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ntp.click_publish_button()

    # 发帖@功能                                                         作者：游同同    时间：2020/5/28
    @allure.title("发帖@功能:@联系人或群组")  # 用例標題
    @allure.description("发帖@功能:建立贴文页面输入'@'后有弹出聯繫人列表")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_tab_post_at(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "发帖@功能:建立贴文页面输入'@'后弹出聯繫人列表異常"
        test_chat.temp_num += 1
        case_name = "test_personal_tab_post_at"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  发帖@功能:輸入@後出現聯繫人列表    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                          # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                     # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                         # 點擊：個人tab[在想些什麼?]发帖入口
        case_step = case_step + cbz.case_step("4、輸入文本'@'")
        ntp.input_post_inptu_box_text('@@')                              # 輸入文本
        ntp.delete_one_char()                                           # 删除一个字符
        case_step = case_step + cbz.case_step("5、點擊：@聯繫人列表第一行")
        ntp.click_set_post_at_list()                                    # 點擊：@聯繫人列表第一行
        case_step = case_step + cbz.case_step("檢查①：")
        text = ntp.get_at_contact_name()
        try:
            assert len(text) >= 2      # 文本長度大於2
            case_step = case_step + cbz.case_step("检查成功，@選中用戶功能正常")
            logging.info("检查成功，@選中用戶功能正常")
        except:
            actual = "檢查失敗！選擇@列表聯繫人功能異常"
            expect = "@選中用戶功能正常"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("6、點擊：「發帖」按鈕")
            ntp.click_publish_button()                                  # 點擊：「發帖」按鈕
            case_step = case_step + cbz.case_step("检查：")
            send_post_text = ntp.get_personal_tab_post_text()
            try:
                assert send_post_text == text
                case_step = case_step + cbz.case_step("檢查成功，@聯繫人後發貼成功")
                logging.info("檢查成功，@聯繫人後發貼成功")
            except:
                actual = "檢查失敗！@聯繫人後發帖異常"
                expect = "@聯繫人後發貼能成功"
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise

@pytest.mark.nf
@pytest.mark.all
@allure.parent_suite("最新動態")
@allure.suite("個人")
@allure.sub_suite("個人發布的帖子")
@allure.feature("最新動態/個人/個人發布的帖子")
@allure.story("個人發布的帖子:相关功能")
@pytest.mark.usefixtures("startApp_withReset")
class TestPersonalPost:

    # 發布時間                                                             作者：游同同    时间：2020/3/20
    @allure.title("發布時間")  # 用例標題
    @allure.description("發布時間:发送成功帖子的时间为当前系统时间")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_post_time(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "發布時間:发送成功帖子的时间为当前系统时间"
        test_chat.temp_num += 1
        case_name = "test_personal_post_time"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********     個人發布的帖子-發布時間    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                     # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                    # 點擊：個人tab[在想些什麼?]发帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                   # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：「發布」按鈕")
        ntp.click_post_publish_button()                            # 點擊：「發布」按鈕
        share_time = int(ntp.get_system_time().split(':')[-1])     # 獲取當前系統時間-分
        case_step = case_step + cbz.case_step("检查：")
        release_time = ntp.get_release_time()                      # 獲取發帖成功後文案展示時間-分
        try:
            assert release_time - share_time <= 1
            case_step = case_step + cbz.case_step("檢查成功，發布時間正常")
            logging.info("檢查成功，發布時間正常")
        except:
            actual = "檢查失敗！發帖時間為{},成功後展示時間為{}，超過1分鐘".format(share_time,release_time)
            expect = "發布時間正常"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 發布的內容:文字                                                      作者：游同同    时间：2020/3/20
    @allure.title("發布的內容:文字")  # 用例標題
    @allure.description("發布的內容:文字校验")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_share_data_content(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "發布的內容:文字"
        test_chat.temp_num += 1
        case_name = "test_share_data_content"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  發布的內容:文字    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                            # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                      # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                           # 點擊：個人tab[在想些什麼?]发帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                           # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：「發布」按鈕")
        ntp.click_post_publish_button()                                   # 點擊：「發布」按鈕
        case_step = case_step + cbz.case_step("检查：")
        send_post_text = ntp.get_personal_tab_post_text()
        try:
            assert send_post_text == post_text
            case_step = case_step + cbz.case_step("檢查成功，發布'{}'到個人動態成功".format(post_text))
            logging.info("檢查成功，發布'{}'到個人動態成功".format(post_text))
        except:
            actual = "檢查失敗！發布'{}'到個人動態異常".format(post_text)
            expect = "發布'{}'到個人動態成功".format(post_text)
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 發布的內容:投票                                                      作者：游同同    时间：2020/3/20
    @allure.title("發布的內容:投票")  # 用例標題
    @allure.description("發布的內容:投票内容一致性")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_share_vote_content(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "發布的內容:投票"
        test_chat.temp_num += 1
        case_name = "test_share_vote_content"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  發布的內容:投票    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                              # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                         # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                              # 點擊：個人tab[在想些什麼?]发帖入口
        case_step = case_step + cbz.case_step("4、點擊：【添加更多元素】icon")
        ntp.click_add_more_element_icon()                                   # 點擊：【添加更多元素】icon
        case_step = case_step + cbz.case_step("5、點擊：[提交投票]选项")
        ntp.click_submit_vote()                                          # 點擊：[提交投票]选项
        case_step = case_step + cbz.case_step("6、點擊：[投票結束時間]選項")
        ntp.click_vote_end_time()                                       # 點擊：[投票結束時間]選項
        case_step = case_step + cbz.case_step("7、點擊：「3天」時間選項")
        ntp.click_list_time_days(1)                                     # 點擊：「3天」時間選項
        title = CD.vote_title + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("8、輸入投票標題'{}'".format(title))
        ntp.input_vote_title(0,title)                                    # 輸入投票標題
        text = CD.vote_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("9、輸入投票內容'{}'".format(text))
        time.sleep(1)
        ntp.input_vote_title(1,text)                                     # 輸入投票內容
        case_step = case_step + cbz.case_step("10、輸入投票選項A、B")
        ntp.input_vote_title(2,"A")
        ntp.input_vote_title(3,"B")
        case_step = case_step + cbz.case_step("11、點擊：分享「群組」跳轉按鈕")
        ntp.click_share_group()                                          # 點擊：分享「群組」跳轉按鈕
        list_number = ntp.get_share_list_number()                        # 分享可选群组个数
        random_number = ntp.random_int(list_number-1)
        logging.info("可分享群组个数为：{}".format(list_number))
        case_step = case_step + cbz.case_step("12、點擊第{}個群組".format(random_number+1))
        ntp.click_random_Object_one(random_number)                       # 隨機點擊一個群組
        case_step = case_step + cbz.case_step("13、點擊：「發帖」按鈕")
        ntp.click_publish_button()                                       # 點擊：「發帖」按鈕
        case_step = case_step + cbz.case_step("14、點擊：[全部]tab")
        ntp.click_all_tab()                                              # 點擊：[全部]tab
        case_step = case_step + cbz.case_step("检查①：(投票标题)")
        vote_title = ntp.get_vote_title_text()
        try:
            assert vote_title == title
            case_step = case_step + cbz.case_step("检查成功，投票标题展示正确")
            logging.info("检查成功，投票标题展示正确")
        except:
            actual = "检查失败！编辑的投票标题为'{}'，实际展示的标题为'{}'".format(title,vote_title)
            expect = "投票标题展示正确"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("检查②：(投票内容)")
            vote_text = ntp.get_post_vote_text()
            try:
                assert vote_text == text
                case_step = case_step + cbz.case_step("檢查成功，投票內容展示正确")
                logging.info("檢查成功，投票內容展示正确")
            except:
                actual = "检查失败！编辑的投票內容为'{}'，实际展示的內容为'{}'".format(text, vote_text)
                expect = "投票內容展示正确"
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                       "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("检查③：(投票選項)")
                vote_Option_text = ntp.get_post_vote_Option_text()
                try:
                    assert vote_Option_text == "A"
                    case_step = case_step + cbz.case_step("檢查成功，投票選項展示正确")
                    logging.info("檢查成功，投票選項展示正确")
                except:
                    actual = "檢查失敗！編輯第一個選項內容為'{}'，實際為'{}'".format("A", vote_Option_text)
                    expect = "投票選項展示正确"
                    video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ntp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                           "最新動態")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
                else:
                    case_step = case_step + cbz.case_step("检查④：投票有效期")
                    vote_end_time = ntp.get_vote_end_time()  # 投票截止时间
                    day_n_time = ntp.get_n_end_time(3)  # 3天后日期
                    try:
                        assert vote_end_time == day_n_time
                        case_step = case_step + cbz.case_step("检查④：检查成功，设置投票有效期至{0}，实际展示有效期为{1}".format(day_n_time, vote_end_time))
                        logging.info("检查成功，设置投票有效期至{0}，实际展示有效期为{1}".format(day_n_time, vote_end_time))
                    except:
                        actual = "檢查失敗！編輯第一個選項內容為'{}'，實際為'{}'".format("A", vote_Option_text)
                        expect = "设置投票有效期至{0}，期望展示有效期为{1}".format(day_n_time, vote_end_time)
                        video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                        case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                        ntp.screenshot(actual)
                        with allure.step(actual):
                            # 调用禅道api，报BUG单
                            bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],
                                                               "最新動態")  # 传入BUG标题，BUG复现步骤
                            with allure.step(bug_link):
                                raise

    # 點讚                                                                作者：游同同    时间：2020/3/20
    @allure.title("點讚")  # 用例標題
    @allure.description("點讚，对自己发布的帖子点赞")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_post_like(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "點讚，对自己发布的帖子点赞"
        test_chat.temp_num += 1
        case_name = "test_post_like"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  點讚    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                              # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                         # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                             # 點擊：個人tab[在想些什麼?]发帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                           # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：「發布」按鈕")
        ntp.click_post_publish_button()                            # 點擊：「發布」按鈕
        time.sleep(2)
        ntp.swipe_screen(0.5,0.9,0.5,0.7)
        case_step = case_step + cbz.case_step("6、點擊：跳轉帖子詳情頁（暱稱欄）")
        ntp.click_post_user_name()                                 # 點擊：跳轉帖子詳情頁（暱稱欄）
        before_like_number = ntp.get_post_detail_like_count_icon_number()  # 获取第一个动态点赞次数（点赞前）
        logging.info("點讚前帖子的點讚數為：'{}'".format(before_like_number))
        case_step = case_step + cbz.case_step("7、點擊：返回按鈕")
        ntp.return_button()
        case_step = case_step + cbz.case_step("8、點擊：帖子點讚icon")
        ntp.click_post_like_icon()                                  # 點擊：帖子點讚icon
        case_step = case_step + cbz.case_step("9、點擊：跳轉帖子詳情頁（暱稱欄）")
        ntp.click_post_user_name()                                  # 點擊：跳轉帖子詳情頁（暱稱欄）
        like_Rear_number = ntp.get_post_detail_like_count_icon_number()  # 获取第一个动态点赞次数（点赞后）
        logging.info("點讚后帖子的點讚數為：'{}'".format(like_Rear_number))
        case_step = case_step + cbz.case_step("檢查：")
        try:
            assert like_Rear_number - before_like_number ==1
            case_step = case_step + cbz.case_step("檢查成功，點讚前後讚數差值為1")
            logging.info("檢查成功，點讚前後讚數差值為1")
        except:
            actual = "檢查失敗！帖子點讚前讚數為{}，點讚後讚數為{}".format(before_like_number,like_Rear_number)
            expect = "點讚前後讚數差值為1"
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

    # 幾人點讚/幾個評論/幾次分享:留言                                         作者：游同同    时间：2020/3/20
    @allure.title("幾人點讚/幾個評論/幾次分享:留言")  # 用例標題
    @allure.description("幾人點讚/幾個評論/幾次分享:校驗 “x個留言”是否增加至 “x+3 個留言”")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_post_comments_number(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "幾人點讚/幾個評論/幾次分享:留言"
        test_chat.temp_num += 1
        case_name = "test_post_comments_number"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  幾人點讚/幾個評論/幾次分享:留言     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                              # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                         # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                             # 點擊：個人tab[在想些什麼?]发帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                            # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：「發布」按鈕")
        ntp.click_post_publish_button()                            # 點擊：「發布」按鈕
        time.sleep(2)
        ntp.swipe_screen(0.5,0.9,0.5,0.7)
        case_step = case_step + cbz.case_step("6、點擊：帖子留言icon")
        ntp.click_post_comment_icon()                              # 點擊：帖子留言icon
        comments_before_number = ntp.get_post_comment_number_icon()     # 留言前獲取留言次數
        logging.info("當前帖子留言次數為{}".format(comments_before_number))
        case_step = case_step + cbz.case_step("7、連續3次留言")
        ntp.comment_double(3,CD.send_message_data)                 # 連續3次留言
        time.sleep(1)
        comments_Rear_number = ntp.get_post_comment_number_icon()  # 留言後獲取留言次數
        logging.info("留言{}次後獲取留言次數'{}'".format(3,comments_Rear_number))
        case_step = case_step + cbz.case_step("檢查：")
        try:
            assert comments_Rear_number - comments_before_number == 3
            case_step = case_step + cbz.case_step("檢查成功，評論次數：留言前'{}'，評論後'{}'".format(comments_before_number,comments_Rear_number))
            logging.info("檢查成功，評論次數：留言前'{}'，評論後'{}'".format(comments_before_number,comments_Rear_number))
        except:
            actual = "檢查失敗！評論次數：留言前'{}'，評論3次後'{}'".format(comments_before_number,comments_Rear_number)
            expect = "點讚前後讚數差值為3"
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

    # 幾人點讚/幾個評論/幾次分享:分享                                         作者：游同同    时间：2020/3/20
    @allure.title("幾人點讚/幾個評論/幾次分享:分享")  # 用例標題
    @allure.description("幾人點讚/幾個評論/幾次分享:校驗 “x個留言”是否增加至 “x+3 個留言”")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_post_share_number(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "幾人點讚/幾個評論/幾次分享:分享"
        test_chat.temp_num += 1
        case_name = "test_post_share_number"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  幾人點讚/幾個評論/幾次分享:分享     *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                          # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                      # 點擊：【個人】tab
        case_step = case_step + cbz.case_step("3、點擊：個人tab[在想些什麼?]发帖入口")
        ntp.click_personal_post_entrance_icon()                          # 點擊：個人tab[在想些什麼?]发帖入口
        post_text = CD.personal_post_text + ntp.random_str_share_china()
        case_step = case_step + cbz.case_step("4、輸入文本'{}'".format(post_text))
        ntp.input_post_inptu_box_text(post_text)                        # 輸入文本
        case_step = case_step + cbz.case_step("5、點擊：「發布」按鈕")
        ntp.click_post_publish_button()                            # 點擊：「發布」按鈕
        time.sleep(2)
        ntp.swipe_screen(0.5,0.9,0.5,0.7)
        case_step = case_step + cbz.case_step("6、進入帖子詳情頁")
        ntp.click_personal_tab_post_text()                         # 進入帖子詳情頁
        comments_before_number = ntp.get_post_share_number_icon()     # 分享前獲取分享次數
        logging.info("分享前计数为：'{}'".format(comments_before_number))
        case_step = case_step + cbz.case_step("7、點擊：帖子分享icon")
        ntp.click_post_share_icon()                                 # 點擊：帖子分享icon
        case_step = case_step + cbz.case_step("8、分享到「分享」")
        ntp.click_post_share_to_share()                             # 分享到「分享」
        case_step = case_step + cbz.case_step("9、點擊：帖子分享icon")
        ntp.click_post_share_icon()                                 # 點擊：帖子分享icon
        case_step = case_step + cbz.case_step("10、分享到[分享至sp]")
        ntp.click_post_share_to_sp()                                # 分享到[分享至sp]
        comments_Rear_number = ntp.get_post_share_number_icon()     # 分享后獲取分享次數
        logging.info("分享后计数为：'{}'".format(comments_Rear_number))
        case_step = case_step + cbz.case_step("检查：")
        try:
            assert comments_Rear_number - comments_before_number == 2
            case_step = case_step + cbz.case_step("检查成功，分享两次后计数加2")
            logging.info("检查成功，分享两次后计数加2")
        except:
            actual = "检查失败！分享前计数为'{}'，两次分享后计数为'{}'".format(comments_before_number,
                                                                               comments_Rear_number)
            expect = "分享两次后计数加2"
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

    # 分享:分享到最新動態                                                   作者：游同同    时间：2020/3/20
    @allure.title("分享:分享到最新動態")  # 用例標題
    @allure.description("分享至群組功能是否正常")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_post_share_to_group(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "個人tab中隨機分享帖子分享至群組功能是否正常"
        test_chat.temp_num += 1
        case_name = "test_post_share_to_group"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list,test_fan_list.per_num,module,case_name,title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  分享:分享到最新動態    *********")
        case_Preposition = "无"      # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()                                          # 點擊：【最新动态】
        case_step = case_step + cbz.case_step("2、點擊：【個人】tab")
        ntp.click_nf_personal_tab()                                     # 點擊：【個人】tab
        swipe_number = ntp.random_int_one(4)
        case_step = case_step + cbz.case_step("3、隨機向上滑屏{}次".format(swipe_number))
        ntp.random_swipe(swipe_number)                           # 隨機向上滑屏
        case_step = case_step + cbz.case_step("4、點擊帖子分享icon")
        ntp.click_personal_post_share_icon()                     # 點擊帖子分享icon
        case_step = case_step + cbz.case_step("5、點擊：分享icon-下拉選項「分享」")
        ntp.click_personal_post_share_to_share()                 # 點擊：分享icon-下拉選項「分享」
        case_step = case_step + cbz.case_step("6、點擊：'分享動態'頁面-分享至跳轉选项群组并点击【完成】按钮")
        ntp.click_share_nf_Jump_icon()                           # 點擊：'分享動態'頁面-分享至跳轉选项群组并点击【完成】按钮
        case_step = case_step + cbz.case_step("7、输入分享文本'{}'".format(CD.share_post_text))
        ntp.input_share_nf_input(CD.share_post_text)             # 输入分享文本
        case_step = case_step + cbz.case_step("8、點擊：'分享動態'頁面-「分享」按鈕")
        ntp.click_share_to_done()                                # 點擊：'分享動態'頁面-「分享」按鈕
        case_step = case_step + cbz.case_step("檢查：")
        find_toast = ntp.get_share_toast()
        try:
            assert find_toast == True
            case_step = case_step + cbz.case_step("檢查成功，分享後有彈出分享成功的toast")
            logging.info("檢查成功，分享後有彈出分享成功的toast")
        except:
            actual = "檢查失敗！分享後沒有彈出分享成功toast"
            expect = "需要弹出toast提示"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise


@pytest.mark.all
@pytest.mark.demotest
@allure.feature("回归测试救命清单/NF/验证帖子头像能否正常展示")
@allure.story("发送消息")
@pytest.mark.usefixtures("startApp_withReset")
class TestNfPostTxt:

    # 发送消息:NF中预览消息
    @allure.title("NF:验证帖子头像能否正常展示")  # 用例標題
    @allure.description("nf模块各tab展示数据是否正常")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_post_Avatar_show(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "NF:验证帖子头像能否正常展示"
        test_chat.temp_num += 1
        case_name = "test_post_share_number"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list, test_fan_list.per_num, module, case_name, title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  NF:验证帖子头像能否正常展示     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、點擊：[群組] tab")
        ntp.click_group_tab()
        case_step = case_step + cbz.case_step("检查①：群组tab中数据展示")
        group_data = ntp.find_all_tab_user_name()
        try:
            assert group_data == True
            case_step = case_step + cbz.case_step("檢查成功，群组tab数据展示正常")
            logging.info("檢查成功，群组tab数据展示正常")
        except:
            actual = "檢查成功，群组tab数据展示有异常！"
            expect = "群组tab数据展示正常"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("3、點擊：[通知] tab")
            ntp.click_notice_tab()
            case_step = case_step + cbz.case_step("检查②：[通知] tab数据展示")
            find_notice = ntp.find_notice_list_message()
            try:
                assert find_notice == True
                case_step = case_step + cbz.case_step("檢查成功，通知tab数据展示正常")
                logging.info("檢查成功，通知tab数据展示正常")
            except:
                actual = "檢查成功，通知tab数据展示有异常！"
                expect = "通知tab数据展示正常"
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("4、點擊：[个人] tab")
                ntp.click_nf_personal_tab()
                case_step = case_step + cbz.case_step("检查③：[个人] tab数据展示")
                find_user_data  = ntp.find_user_homepage_name()
                try:
                    assert find_user_data == True
                    case_step = case_step + cbz.case_step("檢查成功，个人tab数据展示正常")
                    logging.info("檢查成功，个人tab数据展示正常")
                except:
                    actual = "檢查成功，个人tab数据展示有异常！"
                    expect = "个人tab数据展示正常"
                    video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ntp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise

    @pytest.mark.hhh
    # 发送消息:NF中预览图片、视频
    @allure.title("NF:验证帖子图片、视频能否正常展示")  # 用例標題
    @allure.description("nf群组、个人中图片、视频展示正常")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_post_photo_video(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        title = "NF:验证帖子头像能否正常展示"
        test_chat.temp_num += 1
        case_name = "test_post_share_number"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(test_chat.temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        test_fan_list.per_num += 1
        module = 'NF'
        per_list = append_data(per_list, test_fan_list.per_num, module, case_name, title)
        test_fan_list.data_lsit.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ntp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ntp.return_home()  # 用例前置--返回首页
        logging.info("*********  nf群组、个人中图片、视频展示正常     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊：【最新动态】")
        ntp.click_newdynamic()
        case_step = case_step + cbz.case_step("2、全部tab")
        ntp.click_all_tab()
        case_step = case_step + cbz.case_step("3、点击拍摄icon发送一张照片帖子")
        ntp.click_personal_tab_photo_icon()
        ntp.click_personal_tab_shutter_button()         # 点击快门
        ntp.click_personal_tab_send_button()            # 点击【传送】
        ntp.click_post_photo_publish_button()           # 点击发布
        case_step = case_step + cbz.case_step("4、点击全部tab中列表帖子中图片")
        ntp.click_all_tab_post_photo()
        case_step = case_step + cbz.case_step("检查①：全部tab中放大帖子中的图片功能")
        find_download = ntp.find_photo_download()
        try:
            assert find_download == True
            case_step = case_step + cbz.case_step("檢查成功，全部tab中帖子图片放大功能正常")
            logging.info("檢查成功，全部tab中帖子图片放大功能正常")
        except:
            actual = "檢查成功，全部tab中帖子图片放大功能有异常！"
            expect = "全部tab中帖子图片放大功能正常"
            video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ntp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            # 检查个人tab中的图片放大
            case_step = case_step + cbz.case_step("5、返回")
            ntp.return_button()
            case_step = case_step + cbz.case_step("6、點擊：[个人] tab")
            ntp.click_nf_personal_tab()
            case_step = case_step + cbz.case_step("7、點擊：[个人] tab中的贴子中的图片")
            ntp.swipe_to_post_find()            # 滑屏处理至帖子可见
            ntp.click_all_tab_post_photo()      # 点击图片
            case_step = case_step + cbz.case_step("检查②：个人tab中放大帖子中的图片功能")
            find_download = ntp.find_photo_download()
            try:
                assert find_download == True
                case_step = case_step + cbz.case_step("檢查成功，个人tab中帖子图片放大功能正常")
                logging.info("檢查成功，个人tab中帖子图片放大功能正常")
            except:
                actual = "檢查成功，个人tab中帖子图片放大功能有异常！"
                expect = "个人tab中帖子图片放大功能正常"
                video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ntp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                # 检查全部tab中视频详情播放功能
                case_step = case_step + cbz.case_step("8、返回")
                ntp.return_button()
                time.sleep(1)
                case_step = case_step + cbz.case_step("9、全部tab")
                ntp.click_all_tab()
                case_step = case_step + cbz.case_step("10、点击拍摄icon发送一断视频帖子")
                ntp.click_personal_tab_photo_icon()
                ntp.long_tap_personal_tab_shutter_button()      # 长按快门4s
                ntp.click_personal_tab_send_button()            # 点击【传送】
                ntp.click_post_photo_publish_button()           # 点击发布
                case_step = case_step + cbz.case_step("11、点击全部tab中列表帖子中视频")
                ntp.click_all_tab_post_video()
                case_step = case_step + cbz.case_step("检查③：全部tab中视频详情播放功能")
                find_play = ntp.find_post_video_play_progress()
                try:
                    assert find_play == True
                    case_step = case_step + cbz.case_step("檢查成功，全部tab中帖子视频进入详情页播放正常")
                    logging.info("檢查成功，全部tab中帖子视频进入详情页播放正常")
                except:
                    actual = "檢查成功，全部tab中帖子中视频播放有异常！"
                    expect = "全部tab中帖子视频进入详情页播放正常"
                    video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ntp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "最新動態")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
                else:
                    # 检查个人tab中的帖子视频详情播放功能
                    case_step = case_step + cbz.case_step("12、返回")
                    ntp.return_button()
                    case_step = case_step + cbz.case_step("13、點擊：[个人] tab")
                    ntp.click_nf_personal_tab()
                    case_step = case_step + cbz.case_step("14、點擊：[个人] tab中的贴子中的视频")
                    ntp.swipe_to_post_find()            # 滑屏处理至帖子可见
                    ntp.click_all_tab_post_video()      # 点击视频
                    case_step = case_step + cbz.case_step("检查④：个人tab中视频详情播放功能")
                    find_play_1 = ntp.find_post_video_play_progress()
                    try:
                        assert find_play_1 == True
                        case_step = case_step + cbz.case_step("檢查成功，个人tab中帖子视频进入详情页播放正常")
                        logging.info("檢查成功，个人tab中帖子视频进入详情页播放正常")
                    except:
                        actual = "檢查成功，个人tab中帖子中视频播放有异常！"
                        expect = "个人tab中帖子视频进入详情页播放正常"
                        video_download_url = ntp.get_bug_video_url(android_video_path, video_name)
                        case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                        ntp.screenshot(actual)
                        with allure.step(actual):
                            # 调用禅道api，报BUG单
                            bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1],
                                                                 "最新動態")  # 传入BUG标题，BUG复现步骤
                            with allure.step(bug_link):
                                raise
        finally:
            ntp.return_button()

    @pytest.mark.ddd
    def test_app_subscript(self,startApp_withReset):
        ntp = NTP(startApp_withReset)
        case_step = ''  # BUG复现步骤
        list_data = ntp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        ntp.click_newdynamic()          # 點擊：【最新动态】
        ntp.click_notice_tab()          # 点击【通知】tab
        time.sleep(3)                   # 等待消息红点小消失
        ntp.click_chat_tab()            # 點擊【聊天】
        ntp.double_click_chat_tab()     # 双击【聊天tab】
        time.sleep(10)



        # ntp.adb_keycode(3)              # 按HOME键到手机桌面
        #
        #
        #
        #
        # # 处理至APP可见
        # ntp.Action_app_home_vis()
        # number = ntp.get_app_Subscript_bumber()
        # logging.info("获取的角标数：{}".format(number))
        # # ntp.click_home_app_name()
        # time.sleep(2)
        # ntp.click_home_app_name()
        # # ntp.start_ap_app()
        # case_step = case_step + cbz.case_step("2、點擊：【最新动态】")
        # ntp.click_newdynamic()
        # case_step = case_step + cbz.case_step("3、點擊：[个人] tab")
        # ntp.click_nf_personal_tab()
        # logging.info("仙游中去哪了。。。")