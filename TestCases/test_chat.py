"""   【聊天】模块相关用例   """
import datetime
import os

import pytest
from PageObjects.chat_tab_page import ChatTabPage as CTP
from TestDatas import COMMON_DATA as CD
import logging
import time
import allure
from Common.ZenTaoApiToMysql import Commit_Bug_ZenTaoAPI as ZenTaoBugApi
from Common import bug_severity_config as bsc
from Common import Case_bug_ZenTao as cbz
from Common.path_config import base_path
from PageObjects.page_objects import append_data

temp_num = 0
data_lsit2 = []
per_num = 0


@pytest.mark.chat
@allure.feature("聊天/訊息/搜索")
@allure.story("分類")
@pytest.mark.all
@pytest.mark.usefixtures("startApp_withReset")
class TestSort:  # -----【讯息】tab相关用例-------

    # 讯息-独立讯息搜索关键词    testID:7472
    @allure.title("獨立訊息")  # 用例標題
    @allure.description("訊息-搜索功能，獨立訊息分類。")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_message_search_independet(self, startApp_withReset):
        global temp_num
        temp_num += 1
        case_name = "test_message_search_independet"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ctp = CTP(startApp_withReset)
        title = "聊天/訊息/搜索/分類-獨立訊息"
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********讯息-独立讯息搜索关键词    testID:7472 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        Module = "搜索"
        video_name = "SP-NF-"+ Module + "-" + list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()
        case_step = case_step + cbz.case_step("3、點擊搜索欄，輸入文本‘{}’,並觸發搜索".format(CD.message_search_text))
        ctp.click_message_search_input(CD.message_search_text)
        case_step = case_step + cbz.case_step("检查①：是否有搜索結果:")
        number = ctp.search_message_number()
        try:  # 檢查:独立讯息统计搜索结果总数不为0
            assert number != 0  # 搜索结果个数不为0
            case_step = case_step + cbz.case_step("檢查成功，关键字搜索到结果")
            logging.info("檢查成功，关键字搜索到结果")
        except:
            actual = "檢查失败！关键字搜索无结果！"
            expect = "关键字搜索结果正确"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        # 檢查:消息列表中包含收拾关键词
        else:
            case_step = case_step + cbz.case_step("检查②：是否包含關鍵詞")
            try:
                text = ctp.get_message_tab_one_text()
                assert text.find(CD.message_search_text) != -1  # -1 索引为负数表示找不到
                case_step = case_step + cbz.case_step("檢查成功，消息列表中包含搜索关键词{}".format(CD.message_search_text))
                logging.info("檢查成功，消息列表中包含搜索关键词{}".format(CD.message_search_text))
            except:
                actual = "檢查失败！！消息列表中没有包含搜索关键词{}".format(CD.message_search_text)
                expect = "消息列表中包含搜索关键词"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("4、點擊搜索結果跳轉下拉列表")
                ctp.click_drop_down_list_button()  # 點擊搜索結果跳轉下拉列表
                case_step = case_step + cbz.case_step("检查③：是否有跳轉對應聊天窗口")
                # 用戶頭像元素ID發生改變@jinwei
                is_message = ctp.is_message_find(CD.message_search_text)
                try:
                    assert is_message == True
                    case_step = case_step + cbz.case_step("檢查成功，跳转聊天窗口中有包含搜索关键词{}".format(CD.message_search_text))
                    logging.info("檢查成功，跳转聊天窗口中有包含搜索关键词{}".format(CD.message_search_text))
                    ctp.get_bug_video_url(android_video_path, video_name)
                except:
                    actual = "檢查失败！！跳转聊天窗口中沒有包含搜索关键词{}".format(CD.message_search_text)
                    expect = "跳转聊天窗口中包含搜索关键词"
                    video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ctp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
                finally:
                    ctp.return_button()
        finally:
            ctp.return_button()

    # 讯息-群组类别搜索关键词    testID:7472
    @allure.title("群組類別")  # 用例標題
    @allure.description("訊息-搜索功能，群組類別分類。")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_message_search_group(self, startApp_withReset):
        global temp_num
        temp_num += 1
        case_name = "test_message_search_group"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ctp = CTP(startApp_withReset)
        title = "聊天/訊息/搜索/分類-群組類別"
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********讯息-群组类别搜索关键词    testID:7472 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()
        case_step = case_step + cbz.case_step("3、點擊搜索欄，輸入文本‘{}’,並觸發搜索".format(CD.message_search_text))
        ctp.click_message_search_input(CD.message_search_text)
        case_step = case_step + cbz.case_step("4、點擊【群組類別】")
        ctp.click_group_category_tab()
        # 檢查:群组类别统计搜索结果总数不为0
        case_step = case_step + cbz.case_step("检查①：是否有搜索出結果")
        number = ctp.search_message_group_number()
        try:
            assert number != 0  # 搜索结果个数不为0
            case_step = case_step + cbz.case_step("檢查成功:关键字搜索-群组类别有结果")
            logging.info("檢查成功:关键字搜索-群组类别有结果")
        except:
            actual = "檢查失敗！！關鍵字搜索-全職類沒有結果"
            expect = "關鍵字搜索-全職類結果正确"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        case_step = case_step + cbz.case_step("5、點擊群組類別中第一行數據下拉列表")
        ctp.click_message_group_one()  # 点击群组类别中第一行数据下拉列表
        time.sleep(5)
        # 会出现三中情况，聊天记录、通讯录、聊天室
        if ctp.find_group_tab_one_list() == True or ctp.find_pus_button() == False:  # 判断为“聊天记录”类型
            text = ctp.get_group_one_text()  # 获取第一行记录文本内容
            case_step = case_step + cbz.case_step("检查②：是否有搜索出結果")
            try:
                assert text.find(CD.message_search_text) != -1
                logging.info("檢查成功:聊天记录页列表文本包含{}".format(CD.message_search_text))
                case_step = case_step + cbz.case_step("檢查成功:聊天记录页列表文本包含{}".format(CD.message_search_text))
            except:
                actual = "檢查失敗！！聊天記錄頁文本中沒有包含‘{}’".format(CD.message_search_text)
                expect = "聊天記錄頁文本中包含‘{}’".format(CD.message_search_text)
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            case_step = case_step + cbz.case_step("6、點擊群組類別-聊天記錄列第一行進入聊天窗口")
            ctp.click_group_one()  # 点击群组类别-聊天记录列第一行进入聊天窗口
            case_step = case_step + cbz.case_step("检查③：跳轉聊天窗口中有包含搜索關鍵詞")
            is_message = ctp.is_message_find(CD.message_search_text)
            try:
                assert is_message == True
                case_step = case_step + cbz.case_step("檢查成功，跳轉聊天窗口中有包含搜索關鍵詞‘{}’".format(CD.message_search_text))
                logging.info("檢查成功，跳转聊天窗口中有包含搜索关键词{}".format(CD.message_search_text))
            except:
                actual = "檢查失敗！！跳轉聊天窗口中沒有包含搜索關鍵詞‘{}’".format(CD.message_search_text)
                expect = "跳轉聊天窗口中沒有包含搜索關鍵詞‘{}’".format(CD.message_search_text)
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            finally:
                ctp.return_button_one()
                ctp.return_button_one()
                # @jinwei 此處後退兩步不能回到主頁面，加一步
                time.sleep(1)
        elif ctp.find_pus_button() == True or ctp.find_group_tab_one_list() == False:  # 点击为“通讯录”类型
            logging.info("檢查成功，跳转通讯录成功！！")
            case_step = case_step + cbz.case_step("6、跳轉為通訊錄，並點擊【取消】按鈕")
            ctp.click_pus_button()  # 点击提示弹框中的【取消】按钮
            logging.info("点击【取消】按钮")
            case_step = case_step + cbz.case_step("检查②：聊天室名是否包含‘{}’".format(CD.message_search_text))
            text = CD.message_search_text.lower()
            title = ctp.get_center_title()
            try:
                assert title.find(text) != -1
                case_step = case_step + cbz.case_step("檢查成功，跳轉通訊錄-聊天窗口，聊天室名包含‘{}’".format(CD.message_search_text))
                logging.info("檢查成功，跳转通讯录-聊天窗口，聊天室名包含-{}".format(CD.message_search_text))
            except:
                actual = "檢查失敗！！跳轉通訊錄-聊天窗口，聊天室名沒有包含‘{}’".format(CD.message_search_text)
                expect = "跳轉通訊錄-聊天窗口，聊天室名包含‘{}’".format(CD.message_search_text)
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            finally:
                ctp.return_button_one()
        else:  # 点击为“聊天室”类型
            title = ctp.get_chatroom_title()
            case_step = case_step + cbz.case_step("检查②：聊天室名是否包含‘{}’".format(CD.message_search_text))
            try:
                assert title.find(CD.message_search_text.lower()) != -1
                case_step = case_step + cbz.case_step("檢查成功。搜索群組跳轉聊天室，聊天室名稱包含‘{}’".format(CD.message_search_text))
                logging.info("檢查成功，搜索群組跳轉聊天室，聊天室名包含-{}".format(CD.message_search_text))
            except:
                actual = "搜索群組-檢查失敗！！搜索群組跳轉聊天室，聊天室名稱沒有包含‘{}’".format(CD.message_search_text)
                expect = "搜索群組跳轉聊天室，聊天室名稱包含‘{}’".format(CD.message_search_text)
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            finally:
                ctp.return_button_one()


@pytest.mark.chat
@allure.feature("聊天/訊息/新增")
@allure.story("新增對話")
@pytest.mark.all
@pytest.mark.usefixtures("startApp_withReset")
class TestAddConversation:

    # 新增对话-选择人员跳转聊天窗口 testID:7466
    @allure.title("新增對話:人員列表")  # 用例標題
    @allure.description("訊息-新增對話選擇對用的聯繫人。")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_new_conversation_jump(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/訊息/新增-新增對話"
        global temp_num
        temp_num += 1
        case_name = "test_new_conversation_jump"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********新增对话-选择人员跳转聊天窗口    testID:7466 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()
        case_step = case_step + cbz.case_step("3、點擊[新建對話]")
        ctp.enter_personal_chat_page()  # 点击创建-新建对话
        uesr_name = ctp.get_new_message_one_name()  # 获取新增对话页第一个用户的昵称
        case_step = case_step + cbz.case_step("4、獲取第一個用戶的暱稱；‘{}’,並點擊第一個用戶".format(uesr_name))
        ctp.click_new_message_list_one()  # 新增对话页中点击第一个用户，跳转
        chat_title = ctp.get_personal_chat_title()  # 获取个页聊天窗口title
        case_step = case_step + cbz.case_step("检查①：是否跳转为对应用户聊天窗口")
        try:
            assert uesr_name == chat_title
            case_step = case_step + cbz.case_step("檢查成功。（跳转对应用户聊天窗口）")
            logging.info("檢查成功。（跳转对应用户聊天窗口）")
        except:
            actual = "檢查失敗！！（跳转对应用户聊天窗口失敗）"
            expect = "跳转到对应用户聊天窗口"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()

    # #新增对话-未上线用户拨打弹框提示   testID:7466
    # @allure.title("新增對話:未上線人員彈框提示")  # 用例標題
    # @allure.description("訊息-新增對話選擇未上線的用戶時，檢查是否有彈出彈框提示。")  # 用例描述
    # @allure.severity(bsc.C[0])
    # def test_user_call_alert(self,startApp_withReset):
    #     ####   [Neptune.AI][QA][5/5][聊天-訊息-新增對話]自动化检测到功能异常
    #     ctp = CTP(startApp_withReset)
    #     title = "聊天/訊息/新增-新增對話"
    #     bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(),title)     #BUG标题
    #     case_step = ''                                                                                      #BUG复现步骤
    #     ctp.return_home()            #用例前置--返回首页
    #     logging.info("*********新增对话-选择未上線人員彈撥打彈框提示    testID:7466 *********")
    #     with allure.step("點擊【聊天】，使用賬號:{}，密碼:{}".format(CD.user,CD.passwd)):
    #         case_step = case_step + "點擊【聊天】，使用賬號:{}，密碼:{}".format(CD.user,CD.passwd)
    #         ctp.click_chat_tab()                                                #点击【聊天】tab
    #     with allure.step("點擊【訊息】tab"):
    #         case_step = case_step + "<br/>點擊【訊息】tab"
    #         ctp.click_message_tab()                                             #点击【讯息】tab
    #     with allure.step("點擊創建-【新建對話】"):
    #         case_step = case_step + "<br/>點擊創建-【新建對話】"
    #         ctp.click_create_new_message()                                      #点击创建-新建对话
    #     with allure.step("[新增對話]頁面:默認點擊第一個頭像為灰色用戶（未上線）"):
    #         case_step = case_step + "<br/>[新增對話]頁面:默認點擊第一個頭像為灰色用戶（未上線）"
    #         ctp.click_offline_user()                                            #点击头像为灰色用户（未上线）
    #         user_name = ctp.find_user_name()                                     #獲取點擊用戶的用戶名
    #     with allure.step("點擊灰色用戶對象的用戶暱稱為:{}".format(user_name)):
    #         case_step = case_step + "<br/>點擊灰色用戶對象的用戶暱稱為:{}".format(user_name)
    #         is_dial = ctp.is_dial_box()
    #         try:
    #             assert is_dial == True
    #             logging.info("檢查成功，弹出拨打提示弹框")
    #             allure.attach("檢查成功。有彈出撥打提示框")
    #         except:
    #             case_step = case_step + "<br/>檢查失敗！！沒有彈出撥打提示彈框"
    #             logging.exception("檢查失败！！没有弹出拨打提示弹框")
    #             ctp.screenshot("檢查失败！！没有弹出拨打提示弹框")
    #             with allure.step("檢查失敗！！沒有彈出撥打提示彈框"):
    #                 #调用禅道api，报BUG单
    #                 bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1],"聊天")  # 传入BUG标题，BUG复现步骤
    #                 with allure.step(bug_link):
    #                     raise
    #         else:
    #             with allure.step("點擊彈框中的【點擊撥打】"):
    #                 case_step = case_step + "<br/>點擊彈框中的【點擊撥打】"
    #                 ctp.click_dial()                                                #提示弹框中点击拨打按钮
    #                 logging.info("点击提示弹框中的【拨打】按钮")
    #             with allure.step("檢查結果:"):
    #                 case_step = case_step + "<br/>檢查結果:"
    #                 is_list = ctp.is_dial_box_list()
    #                 try:
    #                     assert is_list == True
    #                     with allure.step("檢查成功。點擊撥打有彈出下拉列表"):
    #                         logging.info("檢查成功，点击拨打有弹出下拉列表")
    #                 except:
    #                     case_step = case_step + "<br/>檢查失敗！！點擊撥打按鈕沒有彈出下拉選項"
    #                     logging.exception("檢查失败！！点击拨打按钮没有弹出下拉选项")
    #                     ctp.screenshot("檢查失败！！点击拨打按钮没有弹出下拉选项")
    #                     with allure.step("檢查失敗！！點擊撥打按鈕沒有彈出下拉選項"):
    #                         # 调用禅道api，报BUG单
    #                         bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step,bsc.C[1],"聊天")  # 传入BUG标题，BUG复现步骤
    #                         with allure.step(bug_link):
    #                             raise
    #         finally:
    #             ctp.return_button_one()
    #             ctp.return_button_one()


    # 新增对话-字母導航 BUG
    # @allure.title("新增對話:字母導航")  # 用例標題
    # @allure.description("訊息-新增對話頁面人員列表字母導航。")  # 用例描述
    # @allure.severity(bsc.B[0])
    # def test_new_indexsidebar(self, startApp_withReset):
    #     ctp = CTP(startApp_withReset)
    #     title = "聊天/訊息/新增/新增對話：字母導航"
    #     bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
    #     case_step = ''  # BUG复现步骤
    #     ctp.return_home()  # 用例前置--返回首页
    #     logging.info("*********新增对话-字母導航    testID:7466 *********")
    #     case_Preposition = "无"  # 前置条件
    #     case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
    #         case_step = case_step + "點擊【聊天】"
    #         ctp.click_chat_tab()                                     # 点击【聊天】tab
    #     with allure.step("點擊【訊息】"):
    #         case_step = case_step + "<br/>點擊【訊息】"
    #         ctp.click_message_tab()                                 # 点击【讯息】tab
    #     with allure.step("點擊[新建對話]"):
    #         case_step = case_step + "<br/>點擊[新建對話]"
    #         ctp.enter_personal_chat_page()                          # 点击创建-新建对话
    #     with allure.step("點擊：「新增對話」頁面字母導航欄-W"):
    #         case_step = case_step + "<br/>點擊：「新增對話」頁面字母導航欄-W"
    #         ctp.click_create_new_message_letter_W()                     #點擊：「新增對話」頁面字母導航欄-W
    #         user_title = ctp.get_create_new_message_letter_text()
    #     with allure.step("检查："):
    #         case_step = case_step + "<br/>检查："
    #         try:                                                           #检查：当前页面最上方展示W 开头用户
    #             assert user_title == 'W'
    #             with allure.step("檢查成功，點擊字母快速導航欄W，定位成功"):
    #                 logging.info("檢查成功，點擊字母快速導航欄W，定位成功")
    #         except:
    #             case_step = case_step + "<br/>檢查失敗！點擊字母快速導航欄W，定位失敗"
    #             logging.exception("檢查失敗！點擊字母快速導航欄W，定位失敗")
    #             ctp.screenshot("檢查失敗！點擊字母快速導航欄W，定位失敗")
    #             with allure.step("檢查失敗！點擊字母快速導航欄W，定位失敗"):
    #                 # 调用禅道api，报BUG单
    #                 bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step,bsc.C[1],"聊天")  # 传入BUG标题，BUG复现步骤
    #                 with allure.step(bug_link):
    #                     raise
    #         finally:
    #             ctp.return_button_one()


@pytest.mark.chat
@allure.feature("聊天/訊息/新增")
@allure.story("新增群組")
@pytest.mark.all
@pytest.mark.usefixtures("startApp_withReset")
class TestNewGroup:

    # 新增群组，添加群组主题       testID:7477
    @allure.title("新增群組:群主題及圖標")  # 用例標題
    @allure.description("訊息-新增群組群組命名有效輸入字符長度")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_add_group(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/訊息/新增-新增群組：群主題及圖標"
        global temp_num
        temp_num += 1
        case_name = "test_add_group"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 新增群組:群主題及圖標       testID:7477 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、點擊創建icon-新建群組")
        ctp.click_create_channel()  # 点击创建-新建群组
        theme_itme = ctp.get_count_input_number()  # 获取默认长度（未输入文本前）
        logging.info("未输入主题前，可输入字符长度为:{}".format(theme_itme))
        case_step = case_step + cbz.case_step("檢查①：獲取默認可輸入文本長度是否为26")
        try:
            assert theme_itme == 26
            case_step = case_step + cbz.case_step("檢查成功。默认输入字符长度为26")
            logging.info("檢查成功。默认输入字符长度为26")
        except:
            actual = "檢查失敗！！實際獲取到的字符長度為:{}".format(theme_itme)
            expect = "獲取到的字符長度為26"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            input_text_lenth = ctp.get_input_count_text_length(CD.create_group_name)  # 获取输入文本的字符长度
            case_step = case_step + cbz.case_step(
                "4、輸入文本‘{}’，所佔用字符長度為:{}".format(CD.create_group_name, input_text_lenth))
            ctp.input_count_text(CD.create_group_name)
            theme_itme_to = ctp.get_count_input_number()  # 获取文本:输入文本后还可输入文本长度
            # 檢查:可输入字符长度-输入文本长度 = 输入文本后还可输入文本长度
            case_step = case_step + cbz.case_step("檢查②：獲取輸入文本後還可以輸入文本長度是否為:{}".format(theme_itme_to))
            try:
                assert theme_itme - input_text_lenth == theme_itme_to
                case_step = case_step + cbz.case_step(
                    "檢查成功。輸入‘{}’後還可以輸入{}個字符".format(CD.create_group_name, theme_itme_to))
                logging.info("檢查成功。输入‘{}’后还可输入{}个字符".format(CD.create_group_name, theme_itme_to))
            except:
                actual = "檢查失敗！！輸入‘{}’後還可以輸入{}個字符".format(CD.create_group_name, theme_itme_to)
                expect = "輸入‘{}’後還可以輸入{}個字符".format(CD.create_group_name, theme_itme_to)
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
        finally:
            ctp.return_button_one()

    # 新增图片-拍照     testID:7476
    @allure.title("新增群組:添加群組頭像")  # 用例標題
    @allure.description("訊息-新增群組群時添加群組頭像-拍照方式")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_add_photo_take_photo(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/訊息/新增-新增群組:添加群組頭像-拍照"
        global temp_num
        temp_num += 1
        case_name = "test_add_photo_take_photo"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********添加群组图片-拍照     testID:7476 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、點擊創建icon-新增群組")
        ctp.click_create_channel()  # 点击创建-新建群组
        case_step = case_step + cbz.case_step("4、點擊新增相片icon")
        ctp.click_add_photo()  # 点击【新增相片】icon(未上传图像前)
        case_step = case_step + cbz.case_step("5、點擊下拉列表以外部分")
        ctp.click_touch_outside()  # 点击下拉列表以外部分
        case_step = case_step + cbz.case_step("检查①：列表是否消失")
        is_list = ctp.is_add_photo_list()
        try:
            assert is_list == False  # 檢查:点击下拉列表以外，列表隐藏
            case_step = case_step + cbz.case_step("檢查成功。点击新增相片下拉列表以外的部分，列表消失")
            logging.info("檢查成功。点击新增相片下拉列表以外的部分，列表消失")
        except:
            actual = "檢查失敗！！點擊新增相片下拉列表以外的部分，列表沒有消失"
            expect = "點擊新增相片下拉列表以外的部分，列表消失"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("6、點擊【新增相片】icon")
            ctp.click_add_photo()  # 点击【新增相片】icon
            case_step = case_step + cbz.case_step("7、新增相片-下拉列表中-【拍照】-按快門")
            ctp.click_take_photo_button()  # 新增相片-下拉列表中-【拍照】-按快门
            case_step = case_step + cbz.case_step("8、確定頁-【重試】-【拍照】-確定-完成")
            ctp.click_retry()  # 确定页-【重试】-拍照-确定-完成
            time.sleep(3)  # 头像数据加载
            case_step = case_step + cbz.case_step("9、點擊新增相片icon")
            ctp.click_add_photo_to()  # 点击【新增相片】icon(上传图片后)
            case_step = case_step + cbz.case_step("检查②：添加群組頭像是否成功")
            is_photo = ctp.is_find_delete_photo()
            try:
                assert is_photo == True  # 通过验证列表中是否有[删除图片]选项来判断是否添加头像成功
                case_step = case_step + cbz.case_step("檢查成功。添加群组头像成功")
                logging.info("檢查成功。添加群组头像成功")
            except:
                actual = "檢查失敗！！添加群組頭像失敗"
                expect = "添加群組頭像成功"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
        finally:
            ctp.return_button_one()

    # 新增群組-添加聯繫人     testID:7511
    @allure.title("新增群組:添加聯繫人")  # 用例標題
    @allure.description("訊息-新增群組群時添加群組頭像-拍照方式")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_create_group(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/訊息/新增-新增群組:創建群組-添加聯繫人"
        global temp_num
        temp_num += 1
        case_name = "test_create_group"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********创建群组-添加联络人     testID:7511 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、點擊創建-新增群組")
        ctp.click_create_channel()  # 点击创建-新建群组
        case_step = case_step + cbz.case_step("4、點擊新增相片icon")
        ctp.click_add_photo()  # 点击【新增相片】icon(未上传图像前)
        case_step = case_step + cbz.case_step("5、確定頁-重試-拍照-確定-完成")
        ctp.click_take_photo_button()  # 新增相片-下拉列表中-【拍照】-按快门
        ctp.click_retry()  # 确定页-【重试】-拍照-确定-完成
        time.sleep(3)  # 头像数据加载
        case_step = case_step + cbz.case_step("6、輸入文本‘{}’".format(CD.create_group_name))
        ctp.input_count_text(CD.create_group_name)  # 输入文本
        case_step = case_step + cbz.case_step("7、點擊下一步")
        ctp.click_next_step_button()  # 点击【下一步】
        case_step = case_step + cbz.case_step("8、點擊＋號icon")
        ctp.click_add_people_icon()  # 点击+号icon
        case_step = case_step + cbz.case_step("9、勾選{}名聯繫人並點擊創建".format(CD.create_group_user_times))
        ctp.check_uesr_done(CD.create_group_user_times)  # 勾选多名联系人并点击创建
        case_step = case_step + cbz.case_step("检查①：是否成功獲取到創建成功toast提示")
        is_toast = ctp.get_create_success_toast()
        try:
            assert is_toast == True
            case_step = case_step + cbz.case_step("檢查成功:获取到创建群组成功toast")
            logging.info("檢查成功:获取到创建群组成功toast")
        except:
            actual = "檢查失敗！！沒有獲取到創建成功toast提示"
            expect = "获取到创建群组成功toast"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()

    # 新增群組:是否設有管理員
    @allure.title("新增群組:是否設有管理員")  # 用例標題
    @allure.description("新增群组时默认设置群组有管理员")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_default_count_admin_switch(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/訊息/新增-新增群組:是否設有管理員"
        global temp_num
        temp_num += 1
        case_name = "test_default_count_admin_switch"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 新增群組:是否設有管理員     testID:7511 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()
        case_step = case_step + cbz.case_step("3、點擊創建-新增群組")
        ctp.click_create_channel()  # 点击创建-新建群组
        case_step = case_step + cbz.case_step("检查①：【新增群组】页面是否显示'設有群組管理員'開關'")
        is_switch = ctp.is_site_admin_switch()
        try:  # 检查：【設有群組管理員】开关打开   checked == true
            assert is_switch == True
            case_step = case_step + cbz.case_step("检查成功。【新增群组】页面有显示'設有群組管理員'開關")
            logging.info("检查成功。【新增群组】页面有显示'設有群組管理員'開關")
        except:
            actual = "檢查失敗！「新增群組」頁面默認展示錯誤"
            expect = "新增群組」頁面默認展示正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("4、输入群名稱‘{}’".format(CD.create_group_name))
            ctp.input_count_text(CD.create_group_name)  # 输入群名稱
            case_step = case_step + cbz.case_step("5、點擊下一步")
            ctp.click_next_step_button()  # 点击【下一步】
            case_step = case_step + cbz.case_step("6、點擊＋號icon")
            ctp.click_add_people_icon()  # 点击+号icon
            case_step = case_step + cbz.case_step("7、勾選{}名聯繫人並點擊創建".format(CD.create_group_user_times))
            ctp.check_uesr_done(CD.create_group_user_times)  # 勾选多名联系人并点击创建
            case_step = case_step + cbz.case_step("8、點擊：群聊天中-右上角頭像icon")
            ctp.click_droup_chat_avatar()  # 點擊：群聊天中-右上角頭像icon
            case_step = case_step + cbz.case_step("检查②：[群組資訊」頁中「設有群組管理員」是否為打開狀態")
            is_admin_switch = ctp.is_droup_page_site_admin_switch()
            try:  # 檢查：「設有群組管理員」開關狀態
                assert is_admin_switch == True
                case_step = case_step + cbz.case_step("檢查成功。[群組資訊」頁中「設有群組管理員」為打開狀態")
                logging.info("檢查成功。[群組資訊」頁中「設有群組管理員」為打開狀態")
            except:
                actual = "檢查失敗！[群組資訊」頁中「設有群組管理員」為關閉狀態"
                expect = "[群組資訊」頁中「設有群組管理員」為打開狀態"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            finally:
                ctp.return_button_one()

    # 新增群組:是否允許成員自動退出群組
    @allure.title("新增群組:是否允許成員自動退出群組")  # 用例標題
    @allure.description("新增群组时默认设置允許成員自動退出群組")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_default_count_leave_group(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/訊息/新增-新增群組:是否允許成員自動退出群組"
        global temp_num
        temp_num += 1
        case_name = "test_default_count_leave_group"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 新增群組:是否允許成員自動退出群組     testID:7511 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()
        case_step = case_step + cbz.case_step("3、點擊創建-新增群組")
        ctp.click_create_channel()  #
        case_step = case_step + cbz.case_step("检查①：是否允許成員自動退出群組】开关打开'")
        is_group = ctp.is_leave_group()
        try:  # 检查：【是否允許成員自動退出群組】开关打开   checked == true
            assert is_group == True
            case_step = case_step + cbz.case_step("新增群组】页面有显示'是否允許成員自動退出群組'默认状态为打开")
            logging.info("检查成功。【新增群组】页面有显示'是否允許成員自動退出群組'默认状态为打开")
        except:
            actual = "檢查失敗！「新增群組」頁面'是否允許成員自動退出群組'默認状态錯誤"
            expect = "[新增群组】页面有显示'是否允許成員自動退出群組'默认状态为打开"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("4、输入群名稱‘{}’".format(CD.create_group_name))
            ctp.input_count_text(CD.create_group_name)  # 输入群名稱
            case_step = case_step + cbz.case_step("5、點擊下一步")
            ctp.click_next_step_button()  # 点击【下一步】
            case_step = case_step + cbz.case_step("6、點擊＋號icon")
            ctp.click_add_people_icon()  # 点击+号icon
            case_step = case_step + cbz.case_step("7、勾選{}名聯繫人並點擊創建".format(CD.create_group_user_times))
            ctp.check_uesr_done(CD.create_group_user_times)  # 勾选多名联系人并点击创建
            case_step = case_step + cbz.case_step("8、點擊：群聊天中-右上角頭像icon")
            ctp.click_droup_chat_avatar()  # 點擊：群聊天中-右上角頭像icon
            case_step = case_step + cbz.case_step("检查②：[群組資訊」頁中「'是否允許成員自動退出群組員'是否為打開狀態")
            is_switch = ctp.is_droup_page_leave_group()
            try:  # 檢查：「是否允許成員自動退出群組」開關狀態
                assert is_switch == True
                case_step = case_step + cbz.case_step("檢查成功。[群組資訊」頁中「'是否允許成員自動退出群組員'為打開狀態")
                logging.info("檢查成功。[群組資訊」頁中「'是否允許成員自動退出群組員'為打開狀態")
            except:
                actual = "檢查失敗！[群組資訊」頁中'是否允許成員自動退出群組員'為關閉狀態"
                expect = "[群組資訊」頁中「'是否允許成員自動退出群組員'為打開狀態"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            finally:
                ctp.return_button_one()


@pytest.mark.chat
@allure.feature("聊天/訊息/聊天/個人")
@allure.story("列表左滑各操作項功能是否正常")
@pytest.mark.all
@pytest.mark.usefixtures("startApp_withReset")
class TestArchiveList:

    # 列表左滑:存檔  testID:7615
    @allure.title("列表左滑:存檔")  # 用例標題
    @allure.description("訊息-列表左滑-存檔操作")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_archive(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/訊息/聊天:列表左滑-存檔"
        global temp_num
        temp_num += 1
        case_name = "test_archive"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********  列表左滑:存檔     testID:7615 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        before_time = ctp.get_chat_record_time()  # 獲取封存聊天記錄個數
        case_step = case_step + cbz.case_step("3、獲取聊天記錄數為:{}，左滑動第一個聊天記錄".format(before_time))
        ctp.swipe_left_list_one()  # 訊息頁中左滑動第一個聊天記錄
        case_step = case_step + cbz.case_step("4、點擊【存檔】icon")
        ctp.click_left_archive_icon()  # 點擊【存檔】icon
        rear_time = ctp.get_chat_record_time()  # 再次獲取封存的聊天記錄個數
        case_step = case_step + cbz.case_step("检查①：點擊【封存】後，封存計數是否加1")
        try:
            assert rear_time - before_time == 1  # 檢查:封存操作後 - 封存操作前 = 1
            case_step = case_step + cbz.case_step("封存檢查成功:點擊【封存】後，封存計數加1")
            logging.info("封存檢查成功:點擊【封存】後，封存計數加1")
        except:
            actual = "檢查失敗:點擊封存後實際增加個數為:{}".format(rear_time - before_time)
            expect = "點擊【封存】後，封存計數加1"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("5、點擊封存聊天記錄icon")
            ctp.click_chat_record()  # 點擊封存聊天記錄icon
            chat_one = ctp.find_dialogue_list_one_name()  # 獲取封存對話頁第一行聊天記錄暱稱
            case_step = case_step + cbz.case_step("6、獲取封存對話頁第一行聊天記錄暱稱為:{}，左滑第一個聊天記錄".format(chat_one))
            ctp.swipe_dialogue_list_one()  # 封存對話頁對左滑第一個聊天記錄
            case_step = case_step + cbz.case_step("7、點擊【解除封存】")
            ctp.click_left_archive_icon()  # 點擊【解除封存】
            time.sleep(2)
            case_step = case_step + cbz.case_step("检查②：被解除封存的聊天記錄是否消失")
            is_find_archive = ctp.find_archive_chat(chat_one)
            try:
                logging.info("被解除對象為:{}".format(chat_one))
                assert is_find_archive == False  # 檢查:被取消個人/群暱稱在列表中消失
                case_step = case_step + cbz.case_step("檢查成功:被解除封存的聊天記錄消失")
                logging.info("檢查成功:被解除封存的聊天記錄消失")
            except:
                actual = "檢查失敗！解除封存失敗，目標沒有消失"
                expect = "被解除封存的聊天記錄消失"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
        finally:
            ctp.return_button_one()

    # 列表左滑:靜音設置
    @pytest.mark.voicebuttom
    @allure.title("列表左滑:靜音設置置")  # 用例標題
    @allure.description("訊息-列表左滑-靜音設置")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_mute_site(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/訊息/聊天:列表左滑-靜音設置"
        global temp_num
        temp_num += 1
        case_name = "test_mute_site"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********  列表左滑:靜音設置     testID:7615 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        if ctp.get_chat_record_time() == 0:  # 記錄個數大於0，則不需要創建數據
            case_step = case_step + cbz.case_step("3、訊息頁中左滑動第一個聊天記錄")
            ctp.swipe_left_list_one()  # 訊息頁中左滑動第一個聊天記錄
            case_step = case_step + cbz.case_step("4、點擊【存檔】icon")
            ctp.click_left_archive_icon()  # 點擊【存檔】icon
        case_step = case_step + cbz.case_step("5、點擊封存聊天記錄icon")
        ctp.click_chat_record()  # 點擊封存聊天記錄icon
        if ctp.find_mute_icon() == True:  # 判斷靜音icon是否存在:存在--左滑，按鈕文案為”取消靜音“；不存在，按鈕文案為”靜音“
            case_step = case_step + cbz.case_step("6、左滑:封存頁第一行")
            ctp.swipe_dialogue_list_one()  # 左滑:封存頁第一行
            case_step = case_step + cbz.case_step("检查①：靜音狀態下設置按鈕文案是否为取消靜音")
            status_text = ctp.find_status_text()
            try:
                assert status_text == "取消靜音"
                logging.info("檢查狀態成功，靜音狀態下設置按鈕文案為:{}".format(ctp.find_status_text()))
            except:
                actual = "檢查狀態失敗！靜音狀態下設置按鈕文案為:{}".format(status_text)
                expect = "靜音狀態下設置按鈕文案為取消靜音"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("7、點擊靜音設置按鈕，靜音icon消失")
                ctp.click_left_mute_icon()  # 點擊靜音設置按鈕，靜音icon消失
                time.sleep(8)  # 設置靜音响应时间
                case_step = case_step + cbz.case_step("检查②：取消靜音後，靜音icon是否消失")
                is_mute = ctp.find_mute_icon()
                try:
                    assert is_mute == False
                    case_step = case_step + cbz.case_step("檢查成功。取消靜音後，靜音icon消失")
                    logging.info("檢查成功。取消靜音後，靜音icon消失")
                except:
                    actual = "檢查失敗！點擊[取消靜音]後异常"
                    expect = "取消靜音後，靜音icon消失"
                    video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ctp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
            finally:
                ctp.return_button_one()
        else:
            case_step = case_step + cbz.case_step("6、左滑:封存頁第一行")
            ctp.swipe_dialogue_list_one()  # 左滑:封存頁第一行
            case_step = case_step + cbz.case_step("检查①：非靜音狀態下設置按鈕文案是否为靜音")
            is_status = ctp.find_status_text()
            try:
                assert is_status == "靜音"
                case_step = case_step + cbz.case_step("檢查狀態成功，非靜音狀態下設置按鈕文案為:{}".format(ctp.find_status_text()))
                logging.info("檢查狀態成功，非靜音狀態下設置按鈕文案為:{}".format(ctp.find_status_text()))
            except:
                actual = "檢查狀態失敗！非靜音狀態下設置按鈕文案為:{}".format(ctp.find_status_text())
                expect = "非靜音狀態下設置按鈕文案为靜音"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("7、點擊【靜音】按鈕")
                ctp.click_left_mute_icon()  # 點擊【靜音】按鈕
                time.sleep(8)  # 設置靜音响应时间
                case_step = case_step + cbz.case_step("检查②：設置靜音，是否出現靜音icon")
                is_mute = ctp.find_mute_icon()
                try:
                    assert is_mute == True
                    case_step = case_step + cbz.case_step("檢查成功。設置靜音，出現靜音icon")
                    logging.info("檢查成功。設置靜音，出現靜音icon")
                except:
                    actual = "檢查失敗！點擊[靜音]後异常"
                    expect = "設置靜音，出現靜音icon"
                    video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ctp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
            finally:
                ctp.return_button_one()

    # 列表左滑:標為未讀
    @allure.title("列表左滑:標為未讀")  # 用例標題
    @allure.description("訊息-列表左滑-[標為未讀]設置")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_unread_site(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/訊息/聊天:列表左滑-標為未讀"
        global temp_num
        temp_num += 1
        case_name = "test_unread_site"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********  列表左滑:標為未讀     testID:7615 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        if ctp.get_chat_record_time() == 0:  # 記錄個數大於0，則不需要創建數據
            case_step = case_step + cbz.case_step("3、訊息頁中左滑動第一個聊天記錄")
            ctp.swipe_left_list_one()  # 訊息頁中左滑動第一個聊天記錄
            case_step = case_step + cbz.case_step("4、點擊【存檔】icon")
            ctp.click_left_archive_icon()  # 點擊【存檔】icon
        case_step = case_step + cbz.case_step("5、點擊封存聊天記錄icon")
        ctp.click_chat_record()  # 點擊封存聊天記錄icon
        if ctp.find_msg_count_icon() == True:  # 判斷第一行是否有未讀圖標
            case_step = case_step + cbz.case_step("6、左滑，第一行")
            ctp.swipe_dialogue_list_one()  # 左滑，第一行
            case_step = case_step + cbz.case_step("检查①：未讀狀態下，設置按鈕文案是否為標為已讀")
            count_text = ctp.get_msg_count_icon_text()
            try:  # 有--未讀設置按鈕文案為“標為已讀”；
                assert count_text == "標為已讀"
                case_step = case_step + cbz.case_step("檢查狀態成功。未讀狀態下，設置按鈕文案為:{}".format(ctp.get_msg_count_icon_text()))
                logging.info("檢查狀態成功。未讀狀態下，設置按鈕文案為:{}".format(ctp.get_msg_count_icon_text()))

            except:
                actual = "檢查狀態失敗！未讀狀態下，設置按鈕文案為:{}".format(ctp.get_msg_count_icon_text())
                expect = "未讀狀態下，設置按鈕文案為標為已讀"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("7、左滑第一個聊天記錄")
                ctp.swipe_dialogue_list_one()  # 左滑第一個聊天記錄
                case_step = case_step + cbz.case_step("8、點擊設置按鈕")
                ctp.click_left_read_icon()  # 點擊設置按鈕，
                time.sleep(2)
                case_step = case_step + cbz.case_step("检查②：設置已讀後，未讀圖標消失")
                is_count = ctp.find_msg_count_icon()
                try:  # 檢查:未讀圖標消失
                    assert is_count == False
                    case_step = case_step + cbz.case_step("檢查成功。設置已讀後，未讀圖標消失")
                    logging.info("檢查成功。設置已讀後，未讀圖標消失")
                except:
                    actual = "檢查失敗！設置已讀後出現異常"
                    expect = "設置已讀後未讀圖標消失"
                    video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ctp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
            finally:
                ctp.return_button_one()
        else:
            case_step = case_step + cbz.case_step("6、左滑，第一行")
            ctp.swipe_dialogue_list_one()  # 左滑，第一行
            case_step = case_step + cbz.case_step("检查①：已讀狀態下，設置按鈕文案是否為標為未讀")
            is_count_text = ctp.get_msg_count_icon_text()
            try:  # 沒有未讀圖標 --設置按鈕文案為“標為未讀”
                assert is_count_text == "標為未讀"
                case_step = case_step + cbz.case_step("檢查狀態成功。已讀狀態下，設置按鈕文案為:{}".format(ctp.get_msg_count_icon_text()))
                logging.info("檢查狀態成功。已讀狀態下，設置按鈕文案為:{}".format(ctp.get_msg_count_icon_text()))
            except:
                actual = "檢查失敗！已讀狀態下，設置按鈕文案為:{}".format(ctp.get_msg_count_icon_text())
                expect = "已讀狀態下，設置按鈕文案為標為未讀"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                case_step = case_step + cbz.case_step("7、左滑第一個聊天記錄")
                ctp.swipe_dialogue_list_one()  # 左滑第一個聊天記錄
                case_step = case_step + cbz.case_step("8、點擊設置按鈕")
                ctp.click_left_read_icon()  # 點擊設置按鈕，
                time.sleep(2)
                case_step = case_step + cbz.case_step("检查②：已讀狀態設置未讀後，未讀圖標出現")
                is_text = ctp.find_msg_count_icon()
                try:  # 未讀圖標出現
                    assert is_text == True
                    case_step = case_step + cbz.case_step("檢查成功。已讀狀態設置未讀後，未讀圖標出現")
                    logging.info("檢查成功。已讀狀態設置未讀後，未讀圖標出現")
                except:
                    actual = "檢查失敗！已讀狀態下設置未讀後，出現異常！"
                    expect = "已讀狀態設置未讀後，未讀圖標出現"
                    video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ctp.screenshot(actual)
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
            finally:
                ctp.return_button_one()


# ---------------------------- 个人【聊天】 ---------------------------------
@pytest.mark.chat
@allure.feature("聊天/訊息/聊天/個人")
@allure.story("聊天:發送文本")
@pytest.mark.all
@pytest.mark.usefixtures("startApp_withReset")
class TestPersonalChat:

    # 个人【聊天】输入文本（中文、数字、英文、emoji表情、MD）
    @allure.title("聊天:可發送文本")  # 用例標題
    @allure.description("發送文本（中文、數字、英文、emoji表情、MD）")  # 用例描述
    @allure.severity(bsc.B[0])
    @pytest.mark.parametrize("data", CD.chat_data)
    def test_personal_chat_input_text(self, startApp_withReset, data):
        ctp = CTP(startApp_withReset)
        title = "个人【聊天】/訊息/聊天:發送文本（中文、數字、英文、emoji表情、MD）"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_input_text"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 个人【聊天】:發送文本（中文、數字、英文、emoji表情、MD）    testID:8431 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、點擊輸入框")
        ctp.click_chat_text_input()  # 點擊輸入框
        case_step = case_step + cbz.case_step("5、輸入文本，點擊傳送")
        ctp.message_input_text_click_send(data["text"])  # 輸入文本，點擊傳送
        case_step = case_step + cbz.case_step("6、獲取最新消息")
        new_message = ctp.get_chat_new_message_text()  # 獲取最新消息
        case_step = case_step + cbz.case_step("检查①：發送‘{}’文本是否成功".format(data["text"]))
        try:
            assert new_message.find(data["result"]) != -1  # 檢查:最新消息文本包含了輸入文本
            case_step = case_step + cbz.case_step("檢查成功")
            logging.info("檢查成功")
        except:
            actual = "檢查失敗！發送‘{}’文本出錯".format(data["text"])
            expect = "發送‘{}’文本成功".format(data["text"])
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 个人【聊天】:發送語音
    @allure.title("聊天:按住發語音")  # 用例標題
    @allure.description("聊天-按住發語音")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_personal_chat_send_voice(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "个人【聊天】/訊息/聊天:按住發語音"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_send_voice"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 个人【聊天】:按住發語音     testID:8418 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、點擊語音icon")
        ctp.click_voice_icon()
        while ctp.is_group_chat_authority() == True:
            ctp.allow_authorization(model_name="獲取允許權限")  # 获取允许权限
            time.sleep(1)
        logging.info("获取允许权限")
        case_step = case_step + cbz.case_step("5、長按【按住說話】3秒發送語音")
        ctp.long_press_voice_icon()  # 長按【按住說話】3秒發送語音
        case_step = case_step + cbz.case_step("检查①：發送語音是否成功")
        time_text = ctp.find_chat_new_voice_time()
        try:  # 檢查:聊天窗口中有語音
            assert time_text in [3, 4]  # 語音時間等於3秒
            case_step = case_step + cbz.case_step("檢查成功。發送語音成功")
            logging.info("檢查成功。發送語音成功")
        except:
            actual = "檢查失敗！發送語音失敗"
            expect = "檢查成功。發送語音成功"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button()

    # 个人【聊天】:發送語音-取消操作
    @allure.title("聊天:發送語音-取消操作")  # 用例標題
    @allure.description("聊天-發送語音-取消操作")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_personal_chat_send_voice_cancel(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "个人【聊天】/訊息/聊天:發送語音-取消操作"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_send_voice_cancel"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 个人【聊天】:發送語音-取消操作     testID:8418 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、點擊語音icon")
        ctp.click_voice_icon()  # 點擊語音icon
        while ctp.is_group_chat_authority() == True:
            ctp.allow_authorization(model_name="獲取允許權限")  # 获取允许权限
            time.sleep(1)
        logging.info("获取允许权限")
        case_step = case_step + cbz.case_step("5、按【按住說話】3秒後上滑取消發送")
        ctp.cancel_long_press_voice_icon()  # 長按【按住說話】4秒後上滑取消發送
        case_step = case_step + cbz.case_step("检查①：發送語音是否取消成功")
        is_voice_toast = ctp.get_cancel_voice_toast()
        try:
            assert is_voice_toast == True  # 檢查:有彈出“取消傳送”toast
            case_step = case_step + cbz.case_step("檢查成功。取消發送語音有彈出‘取消傳送’toast提示")
            logging.info("檢查成功。取消發送語音有彈出‘取消傳送’toast提示")
        except:
            actual = "檢查失敗！取消發送語音失敗"
            expect = "發送語音取消成功"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()

    # 个人【聊天】:可即時拍攝圖片、視頻發送
    @allure.title("聊天:可即時拍攝圖片、視頻發送")  # 用例標題
    @allure.description("聊天-可即時拍攝圖片、視頻發送")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_personal_chat_send_video(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "个人【聊天】/訊息/聊天:可即時拍攝圖片、視頻發送"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_send_video"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 个人【聊天】:可即時拍攝圖片、視頻發送     testID:9211 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、点击拍摄icon")
        ctp.click_chat_shoot_icon()  # 点击拍摄icon
        case_step = case_step + cbz.case_step("5、获取允许权限")
        while ctp.is_group_chat_authority() == True:
            ctp.allow_authorization(model_name="獲取允許權限")  # 获取允许权限
            time.sleep(1)
        logging.info("获取允许权限")
        case_step = case_step + cbz.case_step("6、點擊快門")
        ctp.click_chat_shutter_button()  # 點擊快門
        case_step = case_step + cbz.case_step("7、點擊傳送")
        ctp.click_chat_shoot_send_button()  # 點擊傳送
        case_step = case_step + cbz.case_step("检查①：拍照發送功能是否正常")
        system_time = ctp.get_system_time()
        new_time = ctp.get_chat_news_time()
        try:  # 檢查:最新生成文件時間=系統時間
            assert system_time == new_time
            case_step = case_step + cbz.case_step("檢查成功。拍攝圖片發送成功")
            logging.info("檢查成功。拍攝圖片發送成功")
        except:
            actual = "檢查失敗！拍攝圖片發送異常"
            expect = "拍攝圖片發送正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        time.sleep(1)
        case_step = case_step + cbz.case_step("8、点击拍摄icon")
        ctp.click_chat_shoot_icon()  # 点击拍摄icon
        case_step = case_step + cbz.case_step("9、长按快門拍摄视频")
        ctp.longpress_chat_shutter_button()  # 长按快門拍摄视频
        case_step = case_step + cbz.case_step("10、点击发送")
        ctp.click_chat_shoot_send_button()  # 点击发送
        case_step = case_step + cbz.case_step("检查②：發送視頻是否成功")
        is_new_video = ctp.find_chat_news_video()
        try:  # 检查:聊天窗口中找打视频播放icon
            assert is_new_video == True
            case_step = case_step + cbz.case_step("檢查成功。發送視頻成功")
            logging.info("檢查成功。發送視頻成功")
        except:
            actual = "檢查失敗！發送消息異常功"
            expect = "發送視頻成功"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()

    # 个人【聊天】:可發送圖片、視頻
    @allure.title("聊天:可發送圖片、視頻")  # 用例標題
    @allure.description("聊天:可發送圖片、視頻")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_personal_chat_send_images(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "个人【聊天】/訊息/聊天:可發送圖片、視頻"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_send_images"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 个人【聊天】: 可發送圖片、視頻     testID:9211 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、點擊圖片icon")
        ctp.click_chat_image_icon()  # 點擊圖片icon
        case_step = case_step + cbz.case_step("5、選多個圖片")
        ctp.click_chat_select_photo_tick(5)  # 勾選多個圖片
        case_step = case_step + cbz.case_step("6、點擊【完成】")
        ctp.click_chat_image_done()  # 點擊【完成】
        case_step = case_step + cbz.case_step("检查①：發送圖片是否成功")
        system_time = ctp.get_system_time()
        chat_news_time = ctp.get_chat_news_time()
        try:  # 檢查:最新生成文件時間=系統時間
            assert system_time == chat_news_time
            case_step = case_step + cbz.case_step("檢查成功。發送圖片成功")
            logging.info("檢查成功。發送圖片成功")
        except:
            actual = "檢查失敗！發送圖片檢查異常"
            expect = "發送圖片成功"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 个人【聊天】: 快速回到底部功能
    @pytest.mark.quick
    @allure.title("聊天:快速回到底部功能")  # 用例標題
    @allure.description("聊天:快速回到底部功能")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_personal_chat_backbottom_quickly(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "个人【聊天】/訊息/聊天: 快速回到底部功能"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_backbottom_quickly"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 个人【聊天】: 快速回到底部功能      *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、製造數據：發送多條消息")
        ctp.send_data_chat(15)  # 製造數據：發送多條消息
        case_step = case_step + cbz.case_step("5、滑屏：下滑聊天記錄")
        ctp.swipe_chat_recording()  # 滑屏：下滑聊天記錄
        case_step = case_step + cbz.case_step("检查①：快速回到底部button是否出現")
        is_back_button = ctp.is_chat_recording_back_button()
        try:  # 檢查：快速回到底部button出現
            assert is_back_button == True
            case_step = case_step + cbz.case_step("檢查成功。上滑聊天記錄，快速回到底部button出現")
            logging.info("檢查成功。上滑聊天記錄，快速回到底部button出現")

        except:
            actual = "檢查失敗。上滑聊天記錄-快速回到底部button沒有出現"
            expect = "上滑聊天記錄-快速回到底部button出現"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("6、回到底部button出現")
            ctp.click_chat_recording_back_button()  # 點擊：回到底部button出現
            case_step = case_step + cbz.case_step("检查②：回到最底部（回到底部button是否消失）")
            is_button = ctp.is_chat_recording_back_button()
            try:  # 檢查：回到最底部（回到底部button消失）
                assert is_button == False
                case_step = case_step + cbz.case_step("檢查成功。快速回到底部正常")
                logging.info("檢查成功。快速回到底部正常")
            except:
                actual = "檢查失敗！快速回到聊天底部異常"
                expect = "快速回到底部正常"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()


@pytest.mark.chat
@allure.feature("聊天/訊息/聊天/個人")
@allure.story("更多:個人資料頁面各功能")
@pytest.mark.all
@pytest.mark.usefixtures("startApp_withReset")
class TestPersonalChatMore:

    # 更多:可查看頭像、暱稱
    @allure.title("更多:可查看頭像、暱稱")  # 用例標題
    @allure.description("个人页面:可查看頭像、暱稱")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_personal_chat_page_user_name_avater(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:可查看頭像、暱稱"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_user_name_avater"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:可查看頭像、暱稱   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、點擊：右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("检查①：用户昵称展示是否成功")
        is_user_name = ctp.is_personal_chat_page_user_name()
        try:  # 检查用户昵称展示
            assert is_user_name == True
            case_step = case_step + cbz.case_step("檢查成功。用戶頭像展示成功")
            logging.info("檢查成功。用戶頭像展示成功")
        except:
            actual = "檢查失敗！用戶頭像展示異常"
            expect = "用戶頭像展示正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        # with allure.step("检查用户头像展示"):
        #     case_step = case_step + "<br/>检查用户头像展示"
        #     is_user_avatar = ctp.is_personal_chat_page_user_avatar()
        #     try:                                                         #检查用户头像展示
        #         assert is_user_avatar == True
        #         with allure.step("檢查成功。用戶頭像展示成功"):
        #             logging.info("檢查成功。用戶頭像展示成功")
        #     except:
        #         case_step = case_step + "<br/>檢查失敗！用戶頭像展示異常"
        #         logging.exception("檢查失敗！用戶頭像展示異常")
        #         ctp.screenshot("檢查失敗！用戶頭像展示異常")
        #         with allure.step("檢查失敗！用戶頭像展示異常"):
        #             # 调用禅道api，报BUG单
        #             bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
        #             with allure.step(bug_link):
        #                 raise
        finally:
            ctp.return_button_one()

    # 更多:可查看複製郵箱、傳送電郵
    @allure.title("更多:可查看複製郵箱、傳送電郵")  # 用例標題
    @allure.description("个人页面:可查看複製郵箱、傳送電郵")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_chat_page_email_copy(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:可查看複製郵箱、傳送電郵"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_email_copy"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:可查看複製郵箱、傳送電郵     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、點擊 新增對話，進入有郵箱的用戶個人資料頁面")
        # ctp.enter_personal_chat_email()                        # 新增對話，進入有郵箱的用戶個人資料頁面
        ctp.click_create_new_message()  # 点击+号-【新增对话】
        while ctp.is_new_message_one_low() == False:
            ctp.return_button_one()
            ctp.click_create_new_message()  # 点击+号-【新增对话】
            time.sleep(2)
        ctp.add_conversation_enter_user_is_email()  # 新增對話，進入有郵箱的用戶個人資料頁面
        case_step = case_step + cbz.case_step("4、點擊郵箱")
        ctp.click_book_user_data_email()  # 點擊郵箱
        case_step = case_step + cbz.case_step("5、選擇複製")
        ctp.click_email_list_copy()  # 選擇複製
        case_step = case_step + cbz.case_step("检查①：是否彈出toast提示'已經複製到剪切板")
        time.sleep(0.4)
        ctp.screenshot("点击【复制】后立刻截图")
        is_copy_toast = ctp.is_find_email_copy_toast()
        try:  # 檢查：彈出toast提示"已經複製到剪切板"
            assert is_copy_toast == True
            case_step = case_step + cbz.case_step("檢查成功。點擊複製後有彈出toast提示")
            logging.info("檢查成功。點擊複製後有彈出toast提示")
        except:
            actual = "檢查失敗！點擊複製後沒有彈出toast提示"
            expect = "點擊複製後彈出toast提示"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 更多:隸屬部門
    @allure.title("更多:隸屬部門")  # 用例標題
    @allure.description("个人页面:隸屬部門")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_chat_page_section(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:隸屬部門"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_section"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:隸屬部門     testID:9211 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、點擊：右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("检查①：查找對象是否显示正常")
        data_name = ctp.get_book_user_data_section_name()
        is_data_section = ctp.is_find_book_user_data_section()
        try:  # 檢查：查找對象
            assert is_data_section == True
            case_step = case_step + cbz.case_step("檢查成功。資料頁面有展示'隸屬部門'，對應的部門名稱為'{}'".format(data_name))
            logging.info("檢查成功。資料頁面有展示'隸屬部門'，對應的部門名稱為'{}'".format(data_name))
        except:
            actual = "檢查失敗！資料頁面沒有展示'隸屬部門'"
            expect = "資料頁面展示'隸屬部門'"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()

    # 更多:辦公室/場館
    @allure.title("更多:辦公室/場館")  # 用例標題
    @allure.description("个人页面:辦公室/場館")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_chat_page_office(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:辦公室/場館"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_office"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:辦公室/場館     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、點擊：右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("检查①：查找對象是否显示正常")
        data_name = ctp.get_book_user_data_office_name()
        is_data_office = ctp.is_find_book_user_data_office()
        try:  # 檢查：查找對象
            assert is_data_office == True
            case_step = case_step + cbz.case_step("檢查成功。資料頁面有展示'辦公室/場館',對應的辦公室名稱為'{}'".format(data_name))
            logging.info("檢查成功。資料頁面有展示'辦公室/場館',對應的辦公室名稱為'{}'".format(data_name))
        except:
            actual = "檢查失敗！資料頁面沒有展示'辦公室/場館'"
            expect = "資料頁面展示'辦公室/場館"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 更多:地區
    @allure.title("更多:地區")  # 用例標題
    @allure.description("个人页面:地區")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_chat_page_area(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:地區"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_area"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:地區     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、點擊：右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("检查①：查找對象是否显示正常")
        data_name = ctp.get_book_user_data_area_name()
        is_data_area = ctp.is_find_book_user_data_area()
        try:  # 檢查：查找對象
            assert is_data_area == True
            case_step = case_step + cbz.case_step("檢查成功。資料頁面有展示'地區',對應的地區為'{}'".format(data_name))
            logging.info("檢查成功。資料頁面有展示'地區',對應的地區為'{}'".format(data_name))
        except:
            actual = "檢查失敗！資料頁面沒有展示'地區'"
            expect = "資料頁面展示'地區'"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 更多:部門同事
    @allure.title("更多:部門同事")  # 用例標題
    @allure.description("个人页面:部門同事")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_chat_page_colleague(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:部門同事"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_colleague"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:部門同事     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、點擊：右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("检查①：資料頁面是否有展示'部門同事'")
        itme = ctp.get_book_user_data_colleague_itme()
        is_data_colleague = ctp.is_find_book_user_data_colleague()
        try:  # 檢查：
            assert is_data_colleague == True
            case_step = case_step + cbz.case_step("檢查成功。資料頁面有展示'部門同事',个数为'{}'".format(itme))
            logging.info("檢查成功。資料頁面有展示'部門同事',个数为'{}'".format(itme))
        except:
            actual = "檢查失敗！資料頁面沒有展示'部門同事'"
            expect = "資料頁面展示'部門同事'"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("5、點擊：部門同事")
            ctp.click_book_user_data_colleague_itme()  # 點擊：部門同事
            case_step = case_step + cbz.case_step("检查②：跳轉部門同事頁面是否正常")
            is_title = ctp.is_colleague_page_title()
            try:
                assert is_title == True
                case_step = case_step + cbz.case_step("檢查成功。跳轉部門同事頁面正常")
                logging.info("檢查成功。跳轉部門同事頁面正常")
            except:
                actual = "檢查失敗！跳轉部門同事頁面錯誤"
                expect = "部門同事頁面跳转正常"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            finally:
                ctp.return_button_one()
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 更多:設定暱稱
    @allure.title("更多:設定暱稱")  # 用例標題
    @allure.description("个人页面:設定暱稱")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_chat_page_name_label(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:設定暱稱"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_name_label"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:設定暱稱     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、點擊：右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("5、點擊：設定昵稱和標簽")
        ctp.click_book_user_data_site_name_label()  # 點擊：設定昵稱和標簽
        case_step = case_step + cbz.case_step("6、輸入：暱稱文本，並點擊「完成」")
        ctp.input_book_user_data_site_name_label_input(CD.name_label_data)  # 輸入：暱稱文本，並點擊「完成」
        case_step = case_step + cbz.case_step("7、再次點擊：設定昵稱和標簽")
        ctp.click_book_user_data_site_name_label()  # 再次點擊：設定昵稱和標簽
        label_name = ctp.get_name_label_input_text()
        case_step = case_step + cbz.case_step("检查①：輸入框中是否記錄上次輸入文本")
        try:  # 檢查：輸入框中記錄上次輸入文本
            assert label_name == CD.name_label_data
            case_step = case_step + cbz.case_step("檢查成功。設置暱稱為'{}'".format(label_name))
            logging.info("檢查成功。設置暱稱為'{}'".format(label_name))
        except:
            actual = "檢查失敗！設置暱稱功能出錯"
            expect = "設置暱稱功能正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()
            ctp.return_button_one()

    # 更多:標註訊息
    @allure.title("更多:標註訊息")  # 用例標題
    @allure.description("个人页面:標註訊息")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_chat_page_more_callout(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:標註訊息"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_more_callout"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:標註訊息     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、进入聊天窗口中，标注信")
        ctp.create_callout()  # 进入聊天窗口中，标注信息
        case_step = case_step + cbz.case_step("5、點擊：右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("6、點擊：「標註信息」")
        ctp.click_colleague_page_more_callout()  # 點擊：「標註信息」
        case_step = case_step + cbz.case_step("7、點擊：標註信息」頁面一行標註跳轉")
        ctp.click_more_callout_page_jump_icon()  # 點擊：「標註信息」頁面一行標註跳轉
        case_step = case_step + cbz.case_step("检查①：跳轉對應的聊天窗口界面是否正常")
        is_callout_star = ctp.is_more_callout_star()
        try:  # 檢查：跳轉對應的聊天窗口界面
            assert is_callout_star == True
            case_step = case_step + cbz.case_step("檢查成功。跳轉對應標註信息正常")
            logging.info("檢查成功。跳轉對應標註信息正常")
        except:
            actual = "檢查失敗！跳轉對應標註信息失敗，聊天界面沒有找到標註圖標"
            expect = "跳轉對應標註信息成功，聊天界面有標註圖標"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()
            ctp.return_button_one()

    # 更多:媒體，連結和文件--媒體
    @allure.title("更多:媒體，連結和文件--媒體")  # 用例標題
    @allure.description("个人页面:媒體，連結和文件--媒體")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_chat_page_more_rl_file_media(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:媒體，連結和文件--媒體"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_more_rl_file_media"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:媒體，連結和文件--媒體     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        # 发送：图片
        case_step = case_step + cbz.case_step("4、拍摄一张图片发送")
        ctp.click_chat_shoot_icon()  # 点击拍摄icon
        while ctp.is_group_chat_authority() == True:
            ctp.allow_authorization(model_name="獲取允許權限")  # 获取允许权限
            time.sleep(1)
        case_step = case_step + cbz.case_step("5、點擊快門")
        ctp.click_chat_shutter_button()
        case_step = case_step + cbz.case_step("6、点击发送")  # 點擊快門
        ctp.click_chat_shoot_send_button()  # 点击发送
        case_step = case_step + cbz.case_step("7、點擊右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("8、點擊：「所有媒體、連結和文件」")
        ctp.click_colleague_page_more_rl_file()  # 點擊：「所有媒體、連結和文件」
        case_step = case_step + cbz.case_step("检查①：媒體tab是否展示圖片和視頻")
        is_tab_list = ctp.is_more_rl_file_media_tab_list()
        try:  # 檢查：媒體tab是否展示圖片和視頻
            assert is_tab_list == True
            case_step = case_step + cbz.case_step("檢查成功。媒體tab中有展示圖片或視頻")
            logging.info("檢查成功。媒體tab中有展示圖片或視頻")
        except:
            actual = "檢查失敗！媒體tab中展示文件異常"
            expect = "媒體tab中展示文件正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()
            ctp.return_button_one()

    # 更多:媒體，連結和文件--連結
    @pytest.mark.href
    @allure.title("更多:媒體，連結和文件--連結")  # 用例標題
    @allure.description("个人页面:媒體，連結和文件--連結")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_chat_page_more_rl_file_connection(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:媒體，連結和文件--連結"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_more_rl_file_connection"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:媒體，連結和文件--連結     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        # 发送：连接
        case_step = case_step + cbz.case_step("4、发送连接")
        ctp.message_input_text_click_send("https://www.baidu.com/?tn=98010089_dg&ch=16/")
        case_step = case_step + cbz.case_step("5、點擊：右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("6、點擊：「所有媒體、連結和文件」")
        ctp.click_colleague_page_more_rl_file()  # 點擊：「所有媒體、連結和文件」
        case_step = case_step + cbz.case_step("6、點擊：「連接」tab")
        ctp.click_more_rl_link_tab()  # 點擊：「連接」tab
        case_step = case_step + cbz.case_step("检查①：列表中是否展示連接")
        is_tab_list = ctp.is_more_rl_file_link_tab_list()
        try:  # 檢查：列表中是否展示連接
            assert is_tab_list == True
            case_step = case_step + cbz.case_step("檢查成功。「連接」tab中有連接")
            logging.info("檢查成功。「連接」tab中有連接")
        except:
            actual = "檢查失敗！「連接」中展示連接異常"
            expect = "「連接」中展示連接正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 更多:共同群組
    @pytest.mark.qqq
    @allure.title("更多:共同群組")  # 用例標題
    @allure.description("个人页面:共同群組")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_chat_page_common_group(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:共同群組"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_common_group"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:共同群組     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、进入聊天窗口中，标注信")
        ctp.create_callout()  # 进入聊天窗口中，标注信息
        case_step = case_step + cbz.case_step("5、點擊：右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("6、點擊：邀请用户加入群组")
        ctp.invite_to_group_data()  # 邀请用户加入群组
        case_step = case_step + cbz.case_step("7、點擊：共同群組")
        ctp.click_chat_page_common_group_no()  # 點擊：共同群組
        is_data = ctp.is_chat_page_common_group_data()
        case_step = case_step + cbz.case_step("检查①：[共同群组]页面展示數據是否正常")
        try:  # 檢查：「共同群組」頁面有數據
            assert is_data == True
            case_step = case_step + cbz.case_step("檢查成功。[共同群组]页面展示數據正常")
            logging.info("檢查成功。[共同群组]页面展示數據正常")
        except:
            actual = "檢查失敗！「共同群組」頁面展示數據異常"
            expect = "「共同群組」頁面展示數據正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 更多:靜音
    @allure.title("更多:靜音")  # 用例標題
    @allure.description("个人页面:靜音")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_chat_page_mute_switch(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:靜音"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_mute_switch"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:靜音     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、进入聊天窗口中，标注信")
        ctp.create_callout()  # 进入聊天窗口中，标注信息
        case_step = case_step + cbz.case_step("5、點擊：右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("6、滑動：上滑屏幕至「靜音」設置項可見")
        ctp.swipe_personal_page()  # 滑動：上滑屏幕至「靜音」設置項可見
        before_status_text = ctp.get_personal_page_mute_switch_text()  # 设置前：开关状态
        case_step = case_step + cbz.case_step("7、點擊：「靜音」開關-改變狀態(設置前開關狀態為'{}')".format(before_status_text))
        ctp.click_personal_page_mute_switch()  # 點擊：「靜音」開關-改變狀態
        time.sleep(5)  # 等待设置时间
        rear_status_text = ctp.get_personal_page_mute_switch_text()  # 设置后：开关状态
        case_step = case_step + cbz.case_step("检查①：(點擊靜音開關後狀態是否為'{}')".format(rear_status_text))
        try:  # 檢查：设置前后状态不相同
            assert before_status_text != rear_status_text
            case_step = case_step + cbz.case_step("檢查成功。設置靜音功能正常")
            logging.info("檢查成功。設置靜音功能正常")
        except:
            actual = "檢查失敗！設置靜音功能異常"
            expect = "設置靜音功能正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 更多:聊天置頂
    @allure.title("更多:聊天置頂")  # 用例標題
    @allure.description("个人页面:聊天置頂")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_chat_page_chat_sticky(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:聊天置頂"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_chat_sticky"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:聊天置頂     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、进入聊天窗口中，标注信")
        ctp.create_callout()  # 进入聊天窗口中，标注信息
        case_step = case_step + cbz.case_step("5、點擊：右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("6、滑動：上滑屏幕至「聊天置頂」設置項可見")
        ctp.swipe_personal_page()  # 滑動：上滑屏幕至「聊天置頂」設置項可見
        before_sticky_text = ctp.get_personal_page_chat_sticky_text()  # 设置前：开关状态
        case_step = case_step + cbz.case_step("7、點擊：「聊天置頂」開關-改變狀態(設置前開關狀態為'{}')".format(before_sticky_text))
        ctp.click_personal_page_chat_sticky()  # 點擊：「聊天置頂」開關-改變狀態
        time.sleep(5)  # 等待设置时间
        rear_sticky_text = ctp.get_personal_page_chat_sticky_text()  # 设置后：开关状态
        case_step = case_step + cbz.case_step("检查①：(點擊聊天置頂開關後狀態為'{}')".format(rear_sticky_text))
        try:  # 檢查：设置前后状态不相同
            assert before_sticky_text != rear_sticky_text
            case_step = case_step + cbz.case_step("檢查成功。設置聊天置頂功能正常")
            logging.info("檢查成功。設置聊天置頂功能正常")
        except:
            actual = "檢查失敗！設置聊天置頂功能异常"
            expect = "設置聊天置頂功能正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 更多:查找聊天內容
    @allure.title("更多:查找聊天內容")  # 用例標題
    @allure.description("个人页面:查找聊天內容")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_personal_chat_page_find_search_result(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:查找聊天內容"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_find_search_result"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:查找聊天內容     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、點擊輸入框")
        ctp.click_chat_text_input()  # 點擊輸入框
        case_step = case_step + cbz.case_step("5、輸入文本，點擊傳送")
        ctp.message_input_text_click_send(CD.find_chat_text)  # 輸入文本，點擊傳送
        case_step = case_step + cbz.case_step("6、點擊：右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("7、滑動：上滑屏幕至「查找聊天內容」設置項可見")
        ctp.swipe_personal_page()  # 滑動：上滑屏幕至「查找聊天內容」項可見
        case_step = case_step + cbz.case_step("8、點擊：「查找聊天內容」")
        ctp.click_personal_page_find_chat_text()  # 點擊：「查找聊天內容」
        case_step = case_step + cbz.case_step("9、輸入文本：輸入文本觸發搜索")
        ctp.input_text_personal_page_find_search_input(CD.find_chat_text)  # 輸入文本：輸入文本觸發搜索
        time.sleep(1)
        is_search_result = ctp.is_personal_page_find_search_result()  # 有无搜索结果
        case_step = case_step + cbz.case_step("检查①：有无搜索結果")
        try:  # 檢查：有搜索結果，且搜索結果包含關鍵詞
            assert is_search_result == True
            case_step = case_step + cbz.case_step("檢查成功。輸入關鍵詞有搜索結果")
            logging.info("檢查成功。輸入關鍵詞有搜索結果")
        except:
            actual = "檢查失敗！輸入關鍵詞'{}'搜索無結果".format(CD.find_chat_text)
            expect = "輸入關鍵詞，有搜索結果"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            search_result_data = ctp.find_personal_page_find_search_result()
            case_step = case_step + cbz.case_step("检查②：搜索結果內容是否包含关键词")
            try:
                assert search_result_data == CD.find_chat_text
                case_step = case_step + cbz.case_step("檢查成功。內容文本中包含搜索關鍵詞'{}'".format(CD.find_chat_text))
                logging.info("檢查成功。內容文本中包含搜索關鍵詞'{}'".format(CD.find_chat_text))
            except:
                actual = "檢查失敗！搜索結果沒有包含搜索關鍵詞'{}'".format(CD.find_chat_text)
                expect = "內容文本中包含搜索關鍵詞"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 更多:傳送訊息
    @allure.title("更多:傳送訊息")  # 用例標題
    @allure.description("个人页面:傳送訊息")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_personal_chat_page_send_message(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:傳送訊息"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_send_message"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:傳送訊息     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、进入聊天窗口中，标注信")
        ctp.create_callout()  # 进入聊天窗口中，标注信息
        case_step = case_step + cbz.case_step("5、點擊：右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("6、滑屏后點擊：傳送訊息")
        ctp.click_book_user_data_sendmessag()  # 滑屏后點擊：傳送訊息
        case_step = case_step + cbz.case_step("檢查①：是否跳轉至聊天窗口")
        is_data_sendmessag = ctp.is_book_user_data_sendmessag_page()
        try:  # 檢查：跳轉至聊天窗口
            assert is_data_sendmessag == True
            case_step = case_step + cbz.case_step("檢查成功。跳轉聊天窗口成功")
            logging.info("檢查成功。跳轉聊天窗口成功")
        except:
            actual = "檢查失敗！跳轉聊天窗口異常"
            expect = "跳轉聊天窗口正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 更多:邀请群組
    @allure.title("更多:邀请群組")  # 用例標題
    @allure.description("个人页面:邀请群組")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_personal_chat_page_Invite_group(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "個人资料更多:邀请群組"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_page_Invite_group"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 個人资料更多:邀请群組     *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建個人聊天")
        ctp.enter_personal_chat()  # 創建個人聊天
        case_step = case_step + cbz.case_step("4、进入聊天窗口中，标注信")
        ctp.create_callout()  # 进入聊天窗口中，标注信息
        case_step = case_step + cbz.case_step("5、點擊：右上角個人icon")
        ctp.click_droup_chat_avatar()  # 點擊：右上角個人icon
        case_step = case_step + cbz.case_step("6、點擊：邀請群組")
        ctp.click_book_user_data_Invite_group()  # 點擊：邀請群組
        case_step = case_step + cbz.case_step("7、點擊：一個群組")
        ctp.click_Invite_group_page_one()  # 點擊：一個群組
        case_step = case_step + cbz.case_step("檢查①：邀請群組加入是否成功")
        is_invite = ctp.is_return_invite()
        try:  # 檢查：
            assert is_invite == True
            case_step = case_step + cbz.case_step("檢查成功。邀請群組加入成功")
            logging.info("檢查成功。邀請群組加入成功")
        except:
            actual = "檢查失敗！邀請加入群組失敗"
            expect = "邀請加入群組成功"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()


# ---------------------------- 群組【聊天】 ---------------------------------
@allure.feature("聊天/訊息/聊天/群組")
@pytest.mark.chat
@allure.story("群組聊天:發送文本")
@pytest.mark.all
@pytest.mark.usefixtures("startApp_withReset")
class TestGroupChat:

    # 群組【聊天】输入文本（中文、数字、英文、emoji表情、MD）
    @allure.title("聊天:發送文本")  # 用例標題
    @allure.description("發送文本（中文、數字、英文、emoji表情、MD,连接）")  # 用例描述
    @allure.severity(bsc.B[0])
    @pytest.mark.parametrize("data", CD.chat_data)
    def test_Group_chat_input_text(self, startApp_withReset, data):
        ctp = CTP(startApp_withReset)
        title = "群組【聊天】/訊息/聊天:發送文本（中文、數字、英文、emoji表情、MD）"
        global temp_num
        temp_num += 1
        case_name = "test_Group_chat_input_text"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 群組【聊天】:發送文本（中文、數字、英文、emoji表情、MD）    testID:8431 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建一個群組聊天")
        ctp.enter_group_chat()  # 創建一個群組聊天
        case_step = case_step + cbz.case_step("4、點擊輸入框")
        ctp.click_chat_text_input()  # 點擊輸入框
        case_step = case_step + cbz.case_step("5、輸入文本，點擊傳送")
        ctp.message_input_text_click_send(data["text"])  # 輸入文本，點擊傳送
        case_step = case_step + cbz.case_step("6、獲取最新消息")
        new_message = ctp.get_chat_new_message_text()  # 獲取最新消息
        case_step = case_step + cbz.case_step("檢查①：最新消息文本是否包含了輸入文本")
        try:
            assert new_message.find(data["result"]) != -1  # 檢查:最新消息文本包含了輸入文本
            case_step = case_step + cbz.case_step("檢查成功")
            logging.info("檢查成功")
        except:
            actual = "檢查失敗！發送‘{}’文本出錯".format(data["text"])
            expect = "最新消息文本包含了輸入文本"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()

    # 群組【聊天】:發送語音
    @allure.title("聊天:語音-長按發語音")  # 用例標題
    @allure.description("聊天-語音-長按發語音")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_Group_chat_send_voice(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "群組【聊天】/訊息/聊天:語音-長按發語音"
        global temp_num
        temp_num += 1
        case_name = "test_Group_chat_send_voice"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 群組【聊天】:語音-長按發語音     testID:8418 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建一個群組聊天")
        ctp.enter_group_chat()  # 創建一個群組聊天
        case_step = case_step + cbz.case_step("4、點擊語音icon")
        ctp.click_voice_icon()  # 點擊語音icon
        while ctp.is_group_chat_authority() == True:
            ctp.allow_authorization(model_name="獲取允許權限")  # 获取允许权限
            time.sleep(1)
        logging.info("获取允许权限")
        case_step = case_step + cbz.case_step("5、長按【按住說話】3秒發送語音")
        ctp.long_press_voice_icon()  # 長按【按住說話】3秒發送語音
        case_step = case_step + cbz.case_step("檢查①：聊天窗口中是否有語音")
        is_time = ctp.find_chat_new_voice_time()
        try:  # 檢查:聊天窗口中有語音
            assert is_time in [3, 4]  # 語音時間等於3秒
            case_step = case_step + cbz.case_step("檢查成功。發送語音成功")
            logging.info("檢查成功。發送語音成功")
        except:
            actual = "檢查失敗！發送語音失敗"
            expect = "發送語音成功"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()

    # 群組【聊天】:發送語音-取消操作
    @allure.title("聊天:語音-長按上滑後取消")  # 用例標題
    @allure.description("聊天-語音-長按上滑後取消")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_Group_chat_send_voice_cancel(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "群組【聊天】/訊息/聊天:語音-長按上滑後取消"
        global temp_num
        temp_num += 1
        case_name = "test_Group_chat_send_voice_cancel"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 群組【聊天】:語音-長按上滑後取消     testID:8418 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建一個群組聊天")
        ctp.enter_group_chat()  # 創建一個群組聊天
        case_step = case_step + cbz.case_step("4、點擊語音icon")
        ctp.click_voice_icon()  # 點擊語音icon
        while ctp.is_group_chat_authority() == True:
            ctp.allow_authorization(model_name="獲取允許權限")  # 获取允许权限
            time.sleep(1)
        logging.info("获取允许权限")
        case_step = case_step + cbz.case_step("5、長按【按住說話】3秒後上滑取消發送")
        ctp.cancel_long_press_voice_icon()  # 長按【按住說話】4秒後上滑取消發送
        case_step = case_step + cbz.case_step("檢查①：是否有彈出“取消傳送”toast")
        is_toast = ctp.get_cancel_voice_toast()
        try:
            assert is_toast == True  # 檢查:有彈出“取消傳送”toast
            case_step = case_step + cbz.case_step("檢查成功。取消發送語音有彈出‘取消傳送’toast提示")
            logging.info("檢查成功。取消發送語音有彈出‘取消傳送’toast提示")
        except:
            actual = "檢查失敗！取消發送語音失敗"
            expect = "取消發送語音成功"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 群組【聊天】:可即時拍攝圖片、視頻發送
    @allure.title("聊天:可即時拍攝圖片、視頻發送")  # 用例標題
    @allure.description("群組聊天-可即時拍攝圖片、視頻發送")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_Group_chat_send_video(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "群組【聊天】/訊息/聊天:可即時拍攝圖片、視頻發送"
        global temp_num
        temp_num += 1
        case_name = "test_Group_chat_send_video"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 群組【聊天】:可即時拍攝圖片、視頻發送     testID:9211 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建一個群組聊天")
        ctp.enter_group_chat()  # 創建一個群組聊天
        case_step = case_step + cbz.case_step("4、点击拍摄icon")
        ctp.click_chat_shoot_icon()  # 点击拍摄icon
        case_step = case_step + cbz.case_step("5、获取允许权限")
        while ctp.is_group_chat_authority() == True:
            ctp.allow_authorization(model_name="獲取允許權限")  # 获取允许权限
            time.sleep(1)
            logging.info("获取允许权限")
        case_step = case_step + cbz.case_step("6、點擊快門")
        ctp.click_chat_shutter_button()  # 點擊快門
        case_step = case_step + cbz.case_step("7、點擊傳送")
        ctp.click_chat_shoot_send_button()  # 點擊傳送
        case_step = case_step + cbz.case_step("檢查①：最新生成文件時間与系統時間时间间隔小于1分钟")
        system_time = ctp.get_system_time()
        news_time = ctp.get_chat_news_time()
        time_difference = ctp.get_difference(news_time, system_time)
        try:  # 檢查:最新生成文件時間=系統時間
            assert time_difference <= 60  # 时间间隔小于1分钟（60s）
            case_step = case_step + cbz.case_step("檢查成功。拍攝圖片發送成功")
            logging.info("檢查成功。拍攝圖片發送成功")
        except:
            actual = "檢查失敗！拍攝圖片發送異常"
            expect = "拍攝圖片發送正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            time.sleep(1)
            case_step = case_step + cbz.case_step("8、点击拍摄icon")
            ctp.click_chat_shoot_icon()  # 点击拍摄icon
            case_step = case_step + cbz.case_step("9、长按快門拍摄视频")
            ctp.longpress_chat_shutter_button()  # 长按快門拍摄视频
            case_step = case_step + cbz.case_step("10、点击发送")
            ctp.click_chat_shoot_send_button()  # 点击发送
            case_step = case_step + cbz.case_step("檢查②：聊天窗口中是否存在视频播放icon")
            is_video = ctp.find_chat_news_video()
            try:  # 检查:聊天窗口中找打视频播放icon
                assert is_video == True
                case_step = case_step + cbz.case_step("檢查成功。發送視頻成功")
                logging.info("檢查成功。發送視頻成功")
            except:
                actual = "檢查失敗！發送消息異常"
                expect = "發送消息正常"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            finally:
                ctp.return_button_one()

    # 群組【聊天】:可發送圖片、視頻
    @allure.title("聊天:可發送圖片、視頻")  # 用例標題
    @allure.description("聊天:可發送圖片、視頻")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_Group_chat_send_images(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "群組【聊天】/訊息/聊天:可發送圖片、視頻"
        global temp_num
        temp_num += 1
        case_name = "test_Group_chat_send_images"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 群組【聊天】: 可發送圖片、視頻     testID:9211 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建一個群組聊天")
        ctp.enter_group_chat()  # 創建一個群組聊天
        case_step = case_step + cbz.case_step("4、點擊圖片icon")
        ctp.click_chat_image_icon()  # 點擊圖片icon
        case_step = case_step + cbz.case_step("5、選多個圖片")
        ctp.click_chat_select_photo_tick(5)  # 勾選多個圖片
        case_step = case_step + cbz.case_step("6、點擊【完成】")
        ctp.click_chat_image_done()  # 點擊【完成】
        case_step = case_step + cbz.case_step("檢查①：發送圖片是否成功")
        system_time = ctp.get_system_time()
        news_time = ctp.get_chat_news_time()
        try:  # 檢查:最新生成文件時間=系統時間
            assert system_time == news_time
            case_step = case_step + cbz.case_step("檢查成功。發送圖片成功")
            logging.info("檢查成功。發送圖片成功")
        except:
            actual = "檢查失敗！發送圖片檢查異常"
            expect = "發送圖片檢查正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()

    # 群組【聊天】: 快速回到底部功能
    @allure.title("聊天:快速回到底部功能")  # 用例標題
    @allure.description("聊天:快速回到底部功能")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_Group_chat_send_images_aa(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "群組【聊天】/訊息/聊天: 快速回到底部功能"
        global temp_num
        temp_num += 1
        case_name = "test_Group_chat_send_images_aa"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 群組【聊天】: 快速回到底部功能      *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建一個群組聊天")
        ctp.enter_group_chat()  # 創建一個群組聊天
        case_step = case_step + cbz.case_step("4、製造數據：發送多條消息")
        ctp.send_data_chat(20)  # 製造數據：發送多條消息
        case_step = case_step + cbz.case_step("5、滑屏：下滑聊天記錄")
        ctp.swipe_chat_recording()
        case_step = case_step + cbz.case_step("檢查①：快速回到底部button是否出現")  # 滑屏：下滑聊天記錄
        is_back_button = ctp.is_chat_recording_back_button()
        try:  # 檢查：快速回到底部button出現
            assert is_back_button == True
            case_step = case_step + cbz.case_step("檢查成功。上滑聊天記錄，快速回到底部button出現")
            logging.info("檢查成功。上滑聊天記錄，快速回到底部button出現")
        except:
            actual = "檢查失敗。上滑聊天記錄-快速回到底部button沒有出現"
            expect = "上滑聊天記錄，快速回到底部button出現"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("6、點擊：回到底部button出現")
            ctp.click_chat_recording_back_button()  # 點擊：回到底部button出現
            case_step = case_step + cbz.case_step("檢查②：回到最底部（回到底部button是否消失）")  # 滑屏：下滑聊天記錄
            is_button = ctp.is_chat_recording_back_button()
            try:  # 檢查：回到最底部（回到底部button消失）
                assert is_button == False
                case_step = case_step + cbz.case_step("檢查成功。快速回到底部正常")
                logging.info("檢查成功。快速回到底部正常")
            except:
                actual = "檢查失敗！快速回到聊天底部異常"
                expect = "快速回到聊天底部正常"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
        finally:
            ctp.return_button_one()

    # 群組【聊天]:@功能-所有人
    @allure.title("聊天:@功能-所有人")  # 用例標題
    @allure.description("聊天:@功能-所有人")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_Group_chat_at_all(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "群組【聊天】/訊息/聊天: @功能-所有人"
        global temp_num
        temp_num += 1
        case_name = "test_Group_chat_at_all"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 群組【聊天】: @功能-所有人      *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建一個群組聊天")
        ctp.enter_group_chat()  # 創建一個群組聊天
        case_step = case_step + cbz.case_step("4、點擊：工具欄@icon")
        ctp.click_group_chat_at_icon()  # 點擊：工具欄@icon
        case_step = case_step + cbz.case_step("5、點擊：列表中「所有人」後，點擊「傳送」按鈕")
        ctp.click_at_list_user(0)  # 點擊：列表中「所有人」後，點擊「傳送」按鈕
        time.sleep(1)
        is_at = ctp.is_group_chat_message()
        case_step = case_step + cbz.case_step("檢查①：@所有人功能是否正常")
        try:  # 檢查：最新發送的消息中是否有@文案
            assert is_at == True
            case_step = case_step + cbz.case_step("檢查成功。@所有人功能呢正常")
            logging.info("檢查成功。@所有人功能呢正常")
        except:
            actual = "檢查失敗！@所有人功能出錯"
            expect = "@所有人功能正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()

    # 群組【聊天]:@功能-單用戶
    @allure.title("聊天:@功能-單用戶")  # 用例標題
    @allure.description("聊天:@功能-單用戶")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_Group_chat_at_single_user(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "群組【聊天】/訊息/聊天: @功能-單用戶"
        global temp_num
        temp_num += 1
        case_name = "test_Group_chat_at_single_user"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 群組【聊天】: @功能-單用戶      *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()  # 点击【讯息】tab
        case_step = case_step + cbz.case_step("3、創建一個群組聊天")
        ctp.enter_group_chat()  # 創建一個群組聊天
        case_step = case_step + cbz.case_step("4、點擊：工具欄@icon")
        ctp.click_group_chat_at_icon()  # 點擊：工具欄@icon
        case_step = case_step + cbz.case_step("5、點擊：列表中「所有人」後，點擊「傳送」按鈕")
        ctp.click_at_list_user(1)  # 點擊：列表中第一個用戶後，點擊「傳送」按鈕
        time.sleep(1)
        is_at = ctp.is_group_chat_message()
        case_step = case_step + cbz.case_step("檢查①：@單用戶功能是否正常")
        try:  # 檢查：最新發送的消息中是否有@文案
            assert is_at == True
            case_step = case_step + cbz.case_step("檢查成功。@單用戶功能呢正常")
            logging.info("檢查成功。@單用戶功能呢正常")
        except:
            actual = "檢查失敗！@單用戶功能出錯"
            expect = "@單用戶功能正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()


# ----------------------------【聊天】-通訊錄tab---------------------------------
@pytest.mark.chat
@allure.feature("聊天/通訊錄")
@allure.story("搜索、地區篩選、字母快速查找、全部展開模塊功能")
@pytest.mark.all
@pytest.mark.usefixtures("startApp_withReset")
class TestBookSearch:

    # 搜索
    @allure.title("搜索:用戶暱稱")  # 用例標題
    @allure.description("搜索:通過搜索用戶暱稱來快速找到對象")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_search(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄:搜索"
        global temp_num
        temp_num += 1
        case_name = "test_book_search"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/通訊錄：搜索     testID:7880 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 点击【聊天】tab
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()  # 點擊【通訊錄】tab
        case_step = case_step + cbz.case_step("3、點擊輸入框後輸入文本'C'，觸發搜索")
        ctp.input_book_text_search()  # 點擊輸入框後輸入文本，觸發搜索
        case_step = case_step + cbz.case_step("檢查①：結果數量是否不為0")
        count_item = ctp.get_book_count_item()
        try:
            assert count_item != 0  # 檢查搜索數量：結果數量不為0
            case_step = case_step + cbz.case_step("檢查結果數量成功，輸入‘{}’後有結果".format("C"))
            logging.info("檢查結果數量成功，輸入‘{}’後有結果".format("C"))
        except:
            actual = "檢查結果數量失敗，搜索結果為0"
            expect = "搜索結果不為0"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("檢查②：第一个搜索結果暱稱是否包含關鍵詞")
            one_name = ctp.get_book_search_one_name().lower()
            try:
                book_one_user_name = one_name
                logging.info("搜索到的結果為,{}".format(book_one_user_name))
                assert book_one_user_name.find("c") != -1
                case_step = case_step + cbz.case_step("檢查搜索結果內容成功，第一个搜索結果暱稱為‘{}’".format(book_one_user_name))
                logging.info("檢查搜索結果內容成功，第一个搜索結果暱稱為‘{}’".format(book_one_user_name))
            except:
                actual = "檢查搜索結果內容失敗！結果中沒有包含關鍵詞"
                expect = "檢查搜索結果內容成功！結果中包含關鍵詞"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
        finally:
            ctp.delete_inpute_text()  # 删除文本操作

    # 按地區篩選功能
    @allure.title("按地區篩選功能")  # 用例標題
    @allure.description("按地區篩選功能")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_filter(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄:按地區篩選功能"
        global temp_num
        temp_num += 1
        case_name = "test_book_filter"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********  聊天/通訊錄:按地區篩選功能    testID:7877 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()  # 點擊【聊天】
        case_step = case_step + cbz.case_step("2、點擊通訊錄tab")
        ctp.click_address_book_tab()  # 點擊通訊錄tab
        case_step = case_step + cbz.case_step("3、點擊篩選icon")
        ctp.click_book_not_filter_icon()  # 點擊篩選icon
        case_step = case_step + cbz.case_step("4、點擊第一個地區")
        ctp.click_filter_page_one_row()  # 點擊第一個地區
        case_step = case_step + cbz.case_step("檢查①：勾選按鈕是否展示")
        is_selected = ctp.is_selected_icon_elevisible()
        try:
            assert is_selected == True  # 檢查：勾選按鈕是否展示
            case_step = case_step + cbz.case_step("檢查成功。點擊地區後勾選icon可見")
            logging.info("檢查成功。點擊地區後勾選icon可見")
        except:
            actual = "檢查失敗！點擊地區後勾選按鈕沒有出現"
            expect = "點擊地區後勾選icon可見"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("5、點擊篩選頁面-「完成」按鈕")
            ctp.click_book_filter_done_button()  # 點擊篩選頁面-「完成」按鈕
            itme = ctp.get_book_filter_result()
            case_step = case_step + cbz.case_step("檢查②:")
            try:
                assert itme != 0  # 判斷篩選搜索結果是否為0
                case_step = case_step + cbz.case_step("檢查成功。篩選第一個地區篩選有{}個結果".format(itme))
                logging.info("檢查成功。篩選第一個地區篩選有{}個結果".format(itme))
            except:
                actual = "檢查失敗！點擊第一個地區結果為'{}'".format(itme)
                expect = "篩選第一個地區篩選有{}個結果".format(itme)
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            finally:
                ctp.click_book_filter_icon()  # 點擊篩選icon，
                ctp.click_book_filter_popup_edit()  # 出彈框，筛选弹框【编辑筛选】按钮,點擊[全部清除]
                ctp.click_book_filter_done_button()  # 点击【完成】按钮

    # 全部展開功能
    @allure.title("全部展開功能")  # 用例標題
    @allure.description("全部展開功能:展開所有下拉列表")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_allexpend(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄:全部展開功能"
        global temp_num
        temp_num += 1
        case_name = "test_book_allexpend"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/通訊錄：全部展開功能     testID:7874 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()  # 點擊【通訊錄】tab
        if ctp.if_allexpend() == True:  # 判断有地区下拉列表展开,连续点击【全部展开】2次使下拉列表闭合
            case_step = case_step + cbz.case_step("点击【全部展开】按钮")
            ctp.click_allexpend_button()  # 点击【全部展开】按钮
            time.sleep(2)
            ctp.click_allexpend_button()  # 点击【全部展开】按钮
        case_step = case_step + cbz.case_step("3、点击【全部展开】按钮")
        time.sleep(1)  # 等待列表展開
        ctp.click_allexpend_button()  # 点击【全部展开】按钮
        case_step = case_step + cbz.case_step("檢查①：")
        is_allexpend = ctp.if_allexpend()
        try:
            assert is_allexpend == True  # 判断下拉列表打开
            case_step = case_step + cbz.case_step("檢查成功。此时下拉列表为打开状态")
            logging.info("檢查成功。此时下拉列表为打开状态")
        except:
            actual = "檢查失敗！點擊「全部展開」後列表没有展開"
            expect = "此时下拉列表为打开状态"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("4、点击【全部展开】按钮")
            time.sleep(2)
            ctp.click_allexpend_button()  # 点击【全部展开】按钮
            case_step = case_step + cbz.case_step("檢查②：關閉")
            is_if_allexpend = ctp.if_allexpend()
            try:
                assert is_if_allexpend == False  # 判断下拉列表關閉
                case_step = case_step + cbz.case_step("檢查成功。此时下拉列表为關閉状态")
                logging.info("檢查成功。此时下拉列表为關閉状态")
            except:
                actual = "檢查失敗！列表展開後再次點擊「全部展開」後列表没有關閉"
                expect = "此时下拉列表为關閉状态"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise

    # # 字母導航快速查找功能
    # @allure.title("字母導航快速查找功能")  # 用例標題
    # @allure.description("通訊錄：字母導航快速查找功能")  # 用例描述
    # @allure.severity(bsc.C[0])
    # def test_book_navigation_letter_find(self, startApp_withReset):
    #     ctp = CTP(startApp_withReset)
    #     title = "聊天/通訊錄:字母導航快速查找功能"
    #     bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
    #     case_step = ''  # BUG复现步骤
    #     ctp.return_home()  # 用例前置--返回首页
    #     logging.info("*********聊天/通訊錄：字母導航快速查找功能     testID:7874 *********")
    #     case_Preposition = "无"  # 前置条件
    #     case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
    #     case_step = case_step + cbz.case_step("1、點擊【聊天】")
    #     ctp.click_chat_tab()
    #     case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
    #     ctp.click_address_book_tab()
    #     if ctp.if_allexpend() == False:  # 判断有地区下拉列表展开,连续点击【全部展开】2次使下拉列表闭合
    #         case_step = case_step + cbz.case_step("3、点击【全部展开】按钮")
    #         ctp.click_allexpend_button()
    #     case_step = case_step + cbz.case_step("4、滑屏：至字母導航可見")
    #     ctp.book_user_swipe()
    #     case_step = case_step + cbz.case_step("5、點擊：字母導航欄-W")
    #     ctp.click_book_navigation_W()
    #     click_navigation = ctp.get_book_navigation_letter_text()
    #     case_step = case_step + cbz.case_step("檢查：")
    #     try:                                                         #檢查：
    #         assert click_navigation == "W"
    #         case_step = case_step + cbz.case_step("檢查成功。點擊字母快速導航W成功")
    #         logging.info("檢查成功。點擊字母快速導航W成功")
    #     except:
    #         actual = "檢查失敗！點擊字母快速導航欄W搜索失敗"
    #         expect = "快捷搜索功能正常"
    #         video_download_url = ctp.get_bug_video_url(android_video_path,video_name)
    #         ctp.screenshot(actual)
    #         with allure.step(actual):
    #             # 调用禅道api，报BUG单
    #             bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
    #             with allure.step(bug_link):
    #                 raise
    #     finally:
    #         ctp.swipe_above()


@pytest.mark.chat
@allure.feature("聊天/通訊錄/人員列表")
@allure.story("人員列表中各項相關功能點")
@pytest.mark.all
@pytest.mark.usefixtures("startApp_withReset")
class TestPeopleList:

    # 人員列表:可查看頭像、暱稱"
    @allure.title("可查看頭像、暱稱")  # 用例標題
    @allure.description("人員列表:可查看頭像、暱稱")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_view_user_name_avatar(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:可查看頭像、暱稱"
        global temp_num
        temp_num += 1
        case_name = "test_view_user_name_avatar"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/通訊錄/人員列表:可查看頭像、暱稱  *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()  # 點擊【通訊錄】tab
        case_step = case_step + cbz.case_step("3、点击第一个地区下拉列表")
        if ctp.is_ele_visible() == False:
            ctp.click_area_one_drop_list()  # 点击第一个地区下拉列表
        case_step = case_step + cbz.case_step("检查①:地区列表中用户昵称展示")
        is_user_name = ctp.is_find_user_name()
        try:  # 检查用户昵称展示
            assert is_user_name == True
            case_step = case_step + cbz.case_step("檢查成功。地区列表中用戶昵称展示成功")
            logging.info("檢查成功。地区列表中用戶昵称展示成功")
        except:
            actual = "檢查失敗！地区列表中用戶昵称展示異常"
            expect = "地区列表中用戶昵称展示正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot("檢查失敗！地区列表中用戶昵称展示異常")
            with allure.step("檢查失敗！地区列表中用戶昵称展示異常"):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("检查②：用户头像展示")
            is_user_avatar = ctp.is_find_user_avatar()
            try:  # 检查用户头像展示
                assert is_user_avatar == True
                with allure.step("檢查成功。用戶頭像展示成功"):
                    logging.info("檢查成功。用戶頭像展示成功")
            except:
                actual = "檢查失敗！用戶頭像展示異常"
                expect = "用戶頭像展示成功"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            finally:
                ctp.click_area_one_drop_list()

    # 人員列表:可查看複製郵箱、傳送電郵
    @allure.title("可查看複製郵箱、傳送電郵")  # 用例標題
    @allure.description("人員列表:可查看複製郵箱、傳送電郵")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_userdata_email_copy(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:可查看複製郵箱、傳送電郵"
        global temp_num
        temp_num += 1
        case_name = "test_book_userdata_email_copy"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/通訊錄/人員列表:可查看複製郵箱、傳送電郵   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()  # 點擊【通訊錄】tab
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        if ctp.is_ele_visible() == False:
            ctp.click_area_one_drop_list()
        # ctp.click_area_one_drop_list()                      # 點擊第一個地區下拉列表
        case_step = case_step + cbz.case_step("4、進入有郵箱的用戶資料頁中")
        ctp.enter_user_is_email()  # 進入有郵箱的用戶資料頁中
        case_step = case_step + cbz.case_step("5、點擊郵箱")
        ctp.click_book_user_data_email()  # 點擊郵箱
        case_step = case_step + cbz.case_step("6、選擇複製")
        ctp.click_email_list_copy()  # 選擇複製
        case_step = case_step + cbz.case_step("檢查：彈出toast提示'已經複製到剪切板'")
        is_copy_toast = ctp.is_find_email_copy_toast()
        try:  # 檢查：彈出toast提示"已經複製到剪切板"
            assert is_copy_toast == True
            case_step = case_step + cbz.case_step("檢查成功。點擊複製後有彈出toast提示")
            logging.info("檢查成功。點擊複製後有彈出toast提示")
        except:
            actual = "檢查失敗！點擊複製後沒有彈出toast提示"
            expect = "點擊複製後有彈出toast提示"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.click_area_one_drop_list()

    # 人員列表:隸屬部門
    @allure.title("隸屬部門")  # 用例標題
    @allure.description("人員列表:隸屬部門")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_userdata_section(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:隸屬部門"
        global temp_num
        temp_num += 1
        case_name = "test_book_userdata_section"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/通訊錄/人員列表:隸屬部門   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()  # 點擊【通訊錄】tab
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        ctp.click_area_one_drop_list()  # 點擊第一個地區下拉列表
        case_step = case_step + cbz.case_step("4、點擊第一個用戶，進入個人資料頁面")
        ctp.click_area_one_user()  # 點擊第一個用戶，進入個人資料頁面
        case_step = case_step + cbz.case_step("檢查：查找對象")
        data_name = ctp.get_book_user_data_section_name()
        is_data_section = ctp.is_find_book_user_data_section()
        try:  # 檢查：查找對象
            assert is_data_section == True
            case_step = case_step + cbz.case_step("檢查成功。資料頁面有展示'隸屬部門'，對應的部門名稱為'{}'".format(data_name))
            logging.info("檢查成功。資料頁面有展示'隸屬部門'，對應的部門名稱為'{}'".format(data_name))
        except:
            actual = "檢查失敗！資料頁面沒有展示'隸屬部門'"
            expect = "對應的部門名稱為'{}'".format(data_name)
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.click_area_one_drop_list()

    # 人員列表:辦公室/場館
    @allure.title("辦公室/場館")  # 用例標題
    @allure.description("人員列表:辦公室/場館")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_userdata_office(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:辦公室/場館"
        global temp_num
        temp_num += 1
        case_name = "test_book_userdata_office"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/通訊錄/人員列表:辦公室/場館   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()  # 點擊【通訊錄】tab
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        ctp.click_area_one_drop_list()  # 點擊第一個地區下拉列表
        case_step = case_step + cbz.case_step("4、點擊第一個用戶，進入個人資料頁面")
        ctp.click_area_one_user()  # 點擊第一個用戶，進入個人資料頁面
        case_step = case_step + cbz.case_step("5、檢查：查找對象")
        data_name = ctp.get_book_user_data_office_name()
        is_data_office = ctp.is_find_book_user_data_office()
        try:  # 檢查：查找對象
            assert is_data_office == True
            case_step = case_step + "<br/>檢查成功。資料頁面有展示'辦公室/場館',對應的辦公室名稱為'{}'".format(data_name)
            logging.info("檢查成功。資料頁面有展示'辦公室/場館',對應的辦公室名稱為'{}'".format(data_name))
        except:
            actual = "檢查失敗！資料頁面沒有展示'辦公室/場館'"
            expect = "對應的辦公室名稱為'{}'".format(data_name)
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.click_area_one_drop_list()

    # 人員列表:地區
    @allure.title("地區")  # 用例標題
    @allure.description("人員列表:地區")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_userdata_area(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:地區"
        global temp_num
        temp_num += 1
        case_name = "test_book_userdata_area"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/通訊錄/人員列表:地區   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        ctp.click_area_one_drop_list()
        case_step = case_step + cbz.case_step("4、點擊第一個用戶，進入個人資料頁面")
        ctp.click_area_one_user()
        case_step = case_step + cbz.case_step("檢查：查找對象")
        data_name = ctp.get_book_user_data_area_name()
        is_data_area = ctp.is_find_book_user_data_area()
        try:  # 檢查：查找對象
            assert is_data_area == True
            case_step = case_step + cbz.case_step("檢查成功。資料頁面有展示'地區',對應的地區為'{}'".format(data_name))
            logging.info("檢查成功。資料頁面有展示'地區',對應的地區為'{}'".format(data_name))
        except:
            actual = "檢查失敗！資料頁面沒有展示'地區'"
            expect = "資料頁面有展示'地區',對應的地區為'{}'".format(data_name)
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.click_area_one_drop_list()

    # 人員列表:部門同事
    @allure.title("部門同事")  # 用例標題
    @allure.description("人員列表:部門同事")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_userdata_colleague(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:部門同事"
        global temp_num
        temp_num += 1
        case_name = "test_book_userdata_colleagu"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/通訊錄/人員列表:部門同事   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()  # 點擊【通訊錄】tab
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        ctp.click_area_one_drop_list()  # 點擊第一個地區下拉列表
        case_step = case_step + cbz.case_step("4、點擊第一個用戶，進入個人資料頁面")
        ctp.click_area_one_user()  # 點擊列表中一个随机用戶，進入個人資料頁面
        case_step = case_step + cbz.case_step("檢查①：")
        itme = ctp.get_book_user_data_colleague_itme()
        is_data_colleague = ctp.is_find_book_user_data_colleague()
        try:  # 檢查：
            assert is_data_colleague == True
            case_step = case_step + cbz.case_step("檢查成功。資料頁面有展示'部門同事',个数为'{}'".format(itme))
            logging.info("檢查成功。資料頁面有展示'部門同事',个数为'{}'".format(itme))
        except:
            actual = "檢查失敗！資料頁面沒有展示'部門同事'"
            expect = "資料頁面有展示'部門同事'"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("5、點擊：部門同事")
            ctp.click_book_user_data_colleague_itme()  # 點擊：部門同事
            case_step = case_step + cbz.case_step("檢查②：")
            is_title = ctp.is_colleague_page_title()
            try:
                assert is_title == True
                logging.info("檢查成功。跳轉部門同事頁面正常")
            except:
                actual = "檢查失敗！跳轉部門同事頁面錯誤"
                expect = "跳轉部門同事頁面正常"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            finally:
                ctp.return_button_one()
        finally:
            ctp.return_button_one()
            ctp.click_area_one_drop_list()

    # 人員列表:設定暱稱
    @allure.title("設定暱稱")  # 用例標題
    @allure.description("人員列表:設定暱稱")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_userdata_setup_nickname(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:設定暱稱"
        global temp_num
        temp_num += 1
        case_name = "test_book_userdata_setup_nickname"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/通訊錄/人員列表:設定暱稱   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        ctp.click_area_one_drop_list()
        case_step = case_step + cbz.case_step("4、點擊第一個用戶，進入個人資料頁面")
        ctp.click_area_one_user()
        case_step = case_step + cbz.case_step("5、點擊：設定昵稱和標簽")
        ctp.click_book_user_data_site_name_label()  # 點擊：設定昵稱和標簽
        case_step = case_step + cbz.case_step("6、輸入：暱稱文本'{}'，並點擊「完成」".format(CD.name_label_data))
        ctp.input_book_user_data_site_name_label_input(CD.name_label_data)  # 輸入：暱稱文本，並點擊「完成」
        case_step = case_step + cbz.case_step("7、再次點擊：設定昵稱和標簽")
        case_step = case_step + "<br/>再次點擊：設定昵稱和標簽"
        ctp.click_book_user_data_site_name_label()  # 再次點擊：設定昵稱和標簽
        label_name = ctp.get_name_label_input_text()
        case_step = case_step + cbz.case_step("檢查：輸入框中記錄上次輸入文本")
        try:  # 檢查：輸入框中記錄上次輸入文本
            assert label_name == CD.name_label_data
            case_step = case_step + cbz.case_step("檢查成功。設置暱稱為'{}'".format(label_name))
            logging.info("檢查成功。設置暱稱為'{}'".format(label_name))
        except:
            actual = "檢查失敗！設置暱稱功能出錯"
            expect = "設置暱稱能够成功"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 人員列表:標註訊息
    @allure.title("標註訊息")  # 用例標題
    @allure.description("人員列表:標註訊息")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_userdata_callout(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:標註訊息"
        global temp_num
        temp_num += 1
        case_name = "test_book_userdata_callout"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********     聊天/通訊錄/人員列表:標註訊息   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        ctp.click_area_one_drop_list()
        case_step = case_step + cbz.case_step("4、點擊第一個用戶，進入個人資料頁面")
        ctp.click_area_one_user()
        case_step = case_step + cbz.case_step("5、點擊：傳送訊息")
        ctp.click_book_user_data_sendmessag()  # 點擊：傳送訊息
        case_step = case_step + cbz.case_step("6、进入聊天窗口中，标注信息")
        ctp.create_callout()  # 进入聊天窗口中，标注信息
        case_step = case_step + cbz.case_step("7、返回上一頁面")
        ctp.return_button_one()  # 返回上一頁面
        case_step = case_step + cbz.case_step("8、點擊：「標註信息」")
        ctp.click_colleague_page_more_callout()  # 點擊：「標註信息」
        case_step = case_step + cbz.case_step("9、點擊：「標註信息」頁面一行標註跳轉")
        ctp.click_more_callout_page_jump_icon()  # 點擊：「標註信息」頁面一行標註跳轉
        case_step = case_step + cbz.case_step("檢查：跳轉對應的聊天窗口界面")
        is_callout_star = ctp.is_more_callout_star()
        try:  # 檢查：跳轉對應的聊天窗口界面
            assert is_callout_star == True
            case_step = case_step + cbz.case_step("檢查成功。跳轉對應標註信息正常")
            logging.info("檢查成功。跳轉對應標註信息正常")
        except:
            actual = "檢查失敗！設置暱稱功能出錯"
            expect = "設置暱稱能够成功"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 人員列表:所有媒體、連結和文件--媒體
    @allure.title("所有媒體、連結和文件--媒體")  # 用例標題
    @allure.description("人員列表:所有媒體、連結和文件--媒體")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_userdata_all_media(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:所有媒體、連結和文件--媒體"
        global temp_num
        temp_num += 1
        case_name = "test_book_userdata_all_media"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********     聊天/通訊錄/人員列表:所有媒體、連結和文件--媒體   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        ctp.click_area_one_drop_list()
        case_step = case_step + cbz.case_step("4、點擊第一個用戶，進入個人資料頁面")
        ctp.click_area_one_user()
        case_step = case_step + cbz.case_step("5、點擊：傳送訊息")
        ctp.click_book_user_data_sendmessag()
        # 发送：图片
        case_step = case_step + cbz.case_step("6、拍摄一张图片发送")
        ctp.click_chat_shoot_icon()  # 点击拍摄icon
        while ctp.is_group_chat_authority() == True:
            ctp.allow_authorization(model_name="獲取允許權限")  # 获取允许权限
            time.sleep(1)
        ctp.click_chat_shutter_button()  # 點擊快門
        ctp.click_chat_shoot_send_button()  # 点击发送
        time.sleep(1)
        case_step = case_step + cbz.case_step("7、返回上一頁面")
        ctp.return_button_one()
        case_step = case_step + cbz.case_step("8、點擊：「所有媒體、連結和文件」")
        ctp.click_colleague_page_more_rl_file()
        case_step = case_step + cbz.case_step("檢查：媒體tab是否展示圖片和視頻")
        is_tab_list = ctp.is_more_rl_file_media_tab_list()
        try:
            assert is_tab_list == True
            case_step = case_step + cbz.case_step("檢查成功。媒體tab中有展示圖片或視頻")
            logging.info("檢查成功。媒體tab中有展示圖片或視頻")
        except:
            actual = "檢查失敗！媒體tab中展示文件異常"
            expect = "媒體tab中有展示圖片或視頻"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 人員列表:所有媒體、連結和文件--連結
    @allure.title("所有媒體、連結和文件--連結")  # 用例標題
    @allure.description("人員列表:所有媒體、連結和文件--連結")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_userdata_all_link(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:所有媒體、連結和文件--連結"
        global temp_num
        temp_num += 1
        case_name = "test_book_userdata_all_link"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********     聊天/通訊錄/人員列表:所有媒體、連結和文件--連結   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        ctp.click_area_one_drop_list()
        case_step = case_step + cbz.case_step("4、點擊第一個用戶，進入個人資料頁面")
        ctp.click_area_one_user()
        case_step = case_step + cbz.case_step("5、點擊：傳送訊息")
        ctp.click_book_user_data_sendmessag()
        case_step = case_step + cbz.case_step("6、发送连接：https://www.baidu.com/?tn=98010089_dg&ch=16/")
        ctp.message_input_text_click_send("https://www.baidu.com/?tn=98010089_dg&ch=16/")  # 发送：连接
        time.sleep(1)
        case_step = case_step + cbz.case_step("7、返回上一頁面")
        ctp.return_button_one()
        case_step = case_step + cbz.case_step("8、點擊：「所有媒體、連結和文件」")
        ctp.click_colleague_page_more_rl_file()
        case_step = case_step + cbz.case_step("9、點擊：「連接」tab")
        ctp.click_more_rl_link_tab()
        case_step = case_step + cbz.case_step("檢查：列表中是否展示連接")
        is_link_tab_list = ctp.is_more_rl_file_link_tab_list()
        try:  # 檢查：列表中是否展示連接
            assert is_link_tab_list == True
            case_step = case_step + cbz.case_step("檢查成功。「連接」tab中有連接")
            logging.info("檢查成功。「連接」tab中有連接")
        except:
            actual = "檢查失敗！「連接」中展示連接異常"
            expect = "「連接」tab中有連接"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 人員列表:共同群組
    @allure.title("共同群組")  # 用例標題
    @allure.description("人員列表:共同群組")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_common_people(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:共同群組"
        global temp_num
        temp_num += 1
        case_name = "test_book_common_people"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/通訊錄/人員列表:共同群組   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        ctp.click_area_one_drop_list()
        case_step = case_step + cbz.case_step("4、點擊第一個用戶，進入個人資料頁面")
        ctp.click_area_one_user()
        case_step = case_step + cbz.case_step("5、點擊：共同群組")
        ctp.click_book_user_data_common_people()
        case_step = case_step + cbz.case_step("檢查：")
        is_page_titl = ctp.is_book_user_data_people_page_titl()
        common_people_itme = ctp.get_common_people_itme()
        try:  # 檢查：
            assert is_page_titl == True
            case_step = case_step + cbz.case_step("檢查成功。跳轉至「共同群組」頁面成功,共有'{}'個群組".format(common_people_itme))
            logging.info("檢查成功。跳轉至「共同群組」頁面成功,共有'{}'個群組".format(common_people_itme))
        except:
            actual = "檢查失敗！跳轉至「共同群組」頁面異常"
            expect = "跳转【共同群组】页面正常，且正常显示群组"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()
            ctp.click_area_one_drop_list()

    # 人員列表:靜音
    @allure.title("靜音")  # 用例標題
    @allure.description("人員列表:靜音")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_common_mute_switch(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:靜音"
        global temp_num
        temp_num += 1
        case_name = "test_book_common_mute_switch"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 聊天/通訊錄/人員列表:靜音   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        ctp.click_area_one_drop_list()
        case_step = case_step + cbz.case_step("4、點擊第一個用戶，進入個人資料頁面")
        ctp.click_area_one_user()
        case_step = case_step + cbz.case_step("5、滑動：上滑屏幕至「靜音」設置項可")
        ctp.swipe_personal_page()
        before_status_text = ctp.get_personal_page_mute_switch_text()  # 设置前：开关状态
        case_step = case_step + cbz.case_step("6、點擊：「靜音」開關-改變狀態(設置前開關狀態為'{}'".format(before_status_text))
        ctp.click_personal_page_mute_switch()  # 點擊：「靜音」開關-改變狀態
        time.sleep(5)  # 等待设置时间
        rear_status_text = ctp.get_personal_page_mute_switch_text()  # 设置后：开关状态
        case_step = case_step + cbz.case_step("檢查：(點擊靜音開關後狀態為'{}')".format(rear_status_text))
        try:  # 檢查：设置前后状态不相同
            assert before_status_text != rear_status_text
            case_step = case_step + cbz.case_step("檢查成功。設置靜音功能正常")
            logging.info("檢查成功。設置靜音功能正常")
        except:
            actual = "檢查失敗！設置靜音功能異常"
            expect = "設置靜音功能正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()

    # 人員列表:聊天置頂
    @allure.title("聊天置頂")  # 用例標題
    @allure.description("人員列表:聊天置頂")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_common_chat_sticky(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:聊天置頂"
        global temp_num
        temp_num += 1
        case_name = "test_book_common_chat_sticky"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 聊天/通訊錄/人員列表:聊天置頂   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        ctp.click_area_one_drop_list()
        case_step = case_step + cbz.case_step("4、隨機點擊一個用戶，進入個人資料頁面")
        ctp.click_area_one_user()
        case_step = case_step + cbz.case_step("5、滑動：上滑屏幕至「靜音」設置項可")
        ctp.swipe_personal_page()
        before_sticky_text = ctp.get_personal_page_chat_sticky_text()  # 设置前：开关状态
        case_step = case_step + cbz.case_step("6、點擊：「聊天置頂」開關-改變狀態(設置前開關狀態為'{}')".format(before_sticky_text))
        ctp.click_personal_page_chat_sticky()  # 點擊：「聊天置頂」開關-改變狀態
        time.sleep(5)  # 等待设置时间
        rear_sticky_text = ctp.get_personal_page_chat_sticky_text()  # 设置后：开关状态
        case_step = case_step + cbz.case_step("檢查：(點擊聊天置頂開關後狀態為'{}')".format(rear_sticky_text))
        try:  # 檢查：设置前后状态不相同
            assert before_sticky_text != rear_sticky_text
            case_step = case_step + cbz.case_step("檢查成功。設置聊天置頂功能正常")
            logging.info("檢查成功。設置聊天置頂功能正常")
        except:
            actual = "檢查失敗！設置靜音功能異常"
            expect = "設置置顶后该聊天被置顶"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()

    # 人員列表:查找聊天內容
    @allure.title("查找聊天內容")  # 用例標題
    @allure.description("人員列表:查找聊天內容")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_common_chat_find_chat_content(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:查找聊天內容"
        global temp_num
        temp_num += 1
        case_name = "test_book_common_chat_find_chat_conten"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 聊天/通訊錄/人員列表:查找聊天內容   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        ctp.click_area_one_drop_list()
        case_step = case_step + cbz.case_step("4、點擊第一個用戶，進入個人資料頁面")
        ctp.click_area_one_user()
        case_step = case_step + cbz.case_step("5、滑屏后點擊：傳送訊息")
        ctp.click_book_user_data_sendmessag()
        case_step = case_step + cbz.case_step("6、輸入文本'{}'，點擊傳送".format(CD.find_chat_text))
        ctp.click_chat_text_input()
        ctp.message_input_text_click_send(CD.find_chat_text)
        case_step = case_step + cbz.case_step("7、返回上一頁面")
        ctp.return_button_one()
        case_step = case_step + cbz.case_step("8、點擊：「查找聊天內容」")
        ctp.click_personal_page_find_chat_text()
        case_step = case_step + cbz.case_step("9、輸入文本：輸入文本'{}'觸發搜索".format(CD.find_chat_text))
        ctp.input_text_personal_page_find_search_input(CD.find_chat_text)  # 輸入文本：輸入文本觸發搜索
        time.sleep(1)
        is_search_result = ctp.is_personal_page_find_search_result()  # 有无搜索结果
        case_step = case_step + cbz.case_step("檢查①：有无搜索結果")
        try:  # 檢查：有搜索結果，且搜索結果包含關鍵詞
            assert is_search_result == True
            case_step = case_step + cbz.case_step("檢查成功。輸入關鍵詞有搜索結果")
            logging.info("檢查成功。輸入關鍵詞有搜索結果")
        except:
            actual = "檢查失敗！輸入關鍵詞'{}'搜索無結果".format(CD.find_chat_text)
            expect = "輸入關鍵詞有搜索結果"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            search_result_data = ctp.find_personal_page_find_search_result()
            case_step = case_step + cbz.case_step("檢查②：搜索結果內容")
            try:
                assert search_result_data == CD.find_chat_text
                case_step = case_step + cbz.case_step("檢查成功。內容文本中包含搜索關鍵詞'{}'".format(CD.find_chat_text))
                logging.info("檢查成功。內容文本中包含搜索關鍵詞'{}'".format(CD.find_chat_text))
            except:
                actual = "檢查失敗！搜索結果沒有包含搜索關鍵詞'{}'".format(CD.find_chat_text)
                expect = "內容文本中包含搜索關鍵詞'{}'".format(CD.find_chat_text)
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()  # 少了一步返回@jinwei

    # 人員列表:傳送訊息
    @allure.title("傳送訊息")  # 用例標題
    @allure.description("人員列表:傳送訊息")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_send_message(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:傳送訊息"
        global temp_num
        temp_num += 1
        case_name = "test_book_send_message"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/通訊錄/人員列表:傳送訊息   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        ctp.click_area_one_drop_list()
        case_step = case_step + cbz.case_step("4、點擊第一個用戶，進入個人資料頁面")
        ctp.click_area_one_user()
        case_step = case_step + cbz.case_step("5、點擊：傳送訊息")
        ctp.click_book_user_data_sendmessag()
        case_step = case_step + cbz.case_step("檢查：跳轉至聊天窗口")
        is_data_sendmessag = ctp.is_book_user_data_sendmessag_page()
        try:  # 檢查：跳轉至聊天窗口
            assert is_data_sendmessag == True
            case_step = case_step + cbz.case_step("檢查成功。跳轉聊天窗口成功")
            logging.info("檢查成功。跳轉聊天窗口成功")
        except:
            actual = "檢查失敗！跳轉聊天窗口異常"
            expect = "跳轉聊天窗口成功"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()
            ctp.click_area_one_drop_list()

    # 人員列表:邀请群組
    @allure.title("邀请群組")  # 用例標題
    @allure.description("人員列表:邀请群組")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_book_Invite_group(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/通訊錄/人員列表:邀请群組"
        global temp_num
        temp_num += 1
        case_name = "test_book_Invite_group"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/通訊錄/人員列表:邀请群組   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()
        case_step = case_step + cbz.case_step("3、點擊第一個地區下拉列表")
        ctp.click_area_one_drop_list()
        case_step = case_step + cbz.case_step("4、點擊第一個用戶，進入個人資料頁面")
        ctp.click_area_one_user()
        case_step = case_step + cbz.case_step("5、點擊：邀請群組")
        ctp.click_book_user_data_Invite_group()
        case_step = case_step + cbz.case_step("6、點擊：一個群組")
        ctp.click_Invite_group_page_one()
        case_step = case_step + cbz.case_step("檢查：")
        is_invite = ctp.is_return_invite()
        try:  # 檢查：
            assert is_invite == True
            case_step = case_step + cbz.case_step("檢查成功。邀請群組加入成功")
            logging.info("檢查成功。邀請群組加入成功")
        except:
            actual = "檢查失敗！邀請加入群組失敗"
            expect = "邀請群組功能正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()
            ctp.click_area_one_drop_list()


# ----------------------------【聊天】-更多tab---------------------------------

@pytest.mark.chat
@allure.feature("聊天/更多")
@allure.story("更多tab下個項功能")
@pytest.mark.all
@pytest.mark.usefixtures("startApp_withReset")
class TestChatMore:
    #個人頭像與暱稱
    @allure.title("個人頭像與暱稱")  # 用例標題
    @allure.description("聊天/更多:加入群組")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_more_user(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/更多:個人頭像與暱稱"
        global temp_num
        temp_num += 1
        case_name = "test_more_user"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/更多:個人頭像與暱稱   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊：「更多」tab")
        ctp.click_more_tab()
        case_step = case_step + cbz.case_step("檢查②：是否展示用戶信息")
        is_tab_user = ctp.is_more_tab_user()
        user_name = ctp.get_more_tab_user_name()
        try:  # 檢查：是否展示用戶信息
            assert is_tab_user == True
            case_step = case_step + cbz.case_step("检查成功。展示用户的昵称为：{}".format(user_name))
            logging.info("检查成功。展示用户的昵称为：{}".format(user_name))
        except:
            actual = "检查失败！展示用户信息异常"
            expect = "展示用户昵称正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            case_step = case_step + cbz.case_step("3、點擊跳轉icon")
            ctp.click_more_user_jump_icon()
            case_step = case_step + cbz.case_step("檢查②：")
            is_data = ctp.is_user_data()
            try:
                assert is_data == True
                case_step = case_step + cbz.case_step("檢查成功。點擊信息欄跳轉用戶資料頁面正常")
                logging.info("檢查成功。點擊信息欄跳轉用戶資料頁面正常")
            except:
                actual = "檢查失敗！跳轉用戶資料頁面失敗"
                expect = "點擊信息欄跳轉用戶資料頁面正常"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise

    # 所有標註信息
    @allure.title("所有標註信息")  # 用例標題
    @allure.description("聊天/更多:所有標註信息")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_more_callout(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/更多:所有標註信息"
        global temp_num
        temp_num += 1
        case_name = "test_more_callout"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/更多:所有標註信息   *********")
        case_Preposition = "已经有聊天中备注的信息"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        ctp.click_message_tab()  # 點擊：「訊息」tab
        ctp.click_all_tab_list_one()  # 點擊：第一個聊天記錄
        ctp.create_callout()  # 进入聊天窗口中，标注信息
        ctp.return_button_one()  # 返回讯息页
        case_step = case_step + cbz.case_step("2、點擊：「更多」tab")
        ctp.click_more_tab()
        case_step = case_step + cbz.case_step("3、點擊：所有標註信息")
        ctp.click_more_callout()
        case_step = case_step + cbz.case_step("4、點擊：「標註信息」頁面一行標註跳轉")
        ctp.click_more_callout_page_jump_icon()
        case_step = case_step + cbz.case_step("檢查：跳轉對應的聊天窗口界面")
        is_star = ctp.is_more_callout_star()
        try:  # 檢查：跳轉對應的聊天窗口界面
            assert is_star == True
            case_step = case_step + cbz.case_step("檢查成功。跳轉對應標註信息正常")
            logging.info("檢查成功。跳轉對應標註信息正常")
        except:
            actual = "檢查失敗！跳轉對應標註信息失敗，聊天界面沒有找到標註圖標"
            expect = "跳轉對應標註信息正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 所有媒體、連結和文件-媒体
    @allure.title("所有媒體、連結和文件--媒體")  # 用例標題
    @allure.description("聊天/更多:所有媒體、連結和文件--媒體")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_more_rl_file_media_tab(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/更多:所有媒體、連結和文件--媒體"
        global temp_num
        temp_num += 1
        case_name = "test_more_rl_file_media_tab"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/更多:所有媒體、連結和文件--媒體   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊：「更多」tab")
        ctp.click_more_tab()
        case_step = case_step + cbz.case_step("3、點擊：「所有媒體、連結和文件」")
        ctp.click_more_rl_file()
        case_step = case_step + cbz.case_step("檢查：媒體tab是否展示圖片和視頻")
        is_list = ctp.is_more_rl_file_media_tab_list()
        try:  # 檢查：媒體tab是否展示圖片和視頻
            assert is_list == True
            case_step = case_step + cbz.case_step("檢查成功。媒體tab中有展示圖片或視頻")
            logging.info("檢查成功。媒體tab中有展示圖片或視頻")
        except:
            actual = "檢查失敗！媒體tab中展示文件異常"
            expect = "媒體tab中有展示圖片或視頻"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()

    # 所有媒體、連結和文件-連接
    @allure.title("所有媒體、連結和文件--連結")  # 用例標題
    @allure.description("聊天/更多:所有媒體、連結和文件--連結")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_more_rl_file_link_tab(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/更多:所有媒體、連結和文件--連結"
        global temp_num
        temp_num += 1
        case_name = "test_more_rl_file_link_tab"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/更多:所有媒體、連結和文件--連結   *********")
        case_Preposition = "历史聊天窗口中有发送连接"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊：「更多」tab")
        ctp.click_more_tab()
        case_step = case_step + cbz.case_step("3、點擊：「所有媒體、連結和文件」")
        ctp.click_more_rl_file()
        case_step = case_step + cbz.case_step("4、點擊：「連接」tab")
        ctp.click_more_rl_link_tab()
        case_step = case_step + cbz.case_step("檢查：列表中是否展示連接")
        is_list = ctp.is_more_rl_file_link_tab_list()
        try:  # 檢查：列表中是否展示連接
            assert is_list == True
            ase_step = case_step + cbz.case_step("檢查成功。「連接」tab中有連接")
            logging.info("檢查成功。「連接」tab中有連接")
        except:
            actual = "檢查失敗！「連接」中展示連接異常"
            expect = "「連接」tab中有連接"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()

    # 所有媒體、連結和文件-文件
    @allure.title("所有媒體、連結和文件--文件")  # 用例標題
    @allure.description("聊天/更多:所有媒體、連結和文件--文件")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_more_rl_file_file_tab(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/更多:所有媒體、連結和文件--文件"
        global temp_num
        temp_num += 1
        case_name = "test_more_rl_file_file_tab"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/更多:所有媒體、連結和文件--文件   *********")
        case_Preposition = "有在聊天窗口中发送过文件"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊：「更多」tab")
        ctp.click_more_tab()
        case_step = case_step + cbz.case_step("3、點擊：「所有媒體、連結和文件」")
        ctp.click_more_rl_file()
        case_step = case_step + cbz.case_step("4、點擊：「文件」tab")
        ctp.click_more_rl_file_tab()
        case_step = case_step + cbz.case_step("檢查：是否還有文件")
        is_tab_list = ctp.is_more_rl_file_file_tab_list()
        try:  # 檢查：是否還有文件
            assert is_tab_list == True
            case_step = case_step + cbz.case_step("檢查成功。[文件]tab中有顯示文件")
            logging.info("檢查成功。[文件]tab中有顯示文件")
        except:
            actual = "檢查失敗！「文件」中沒有展示文件"
            expect = "[文件]tab中有顯示文件"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()

    # @有提到你的對話
    @allure.title("@有提到你的對話")  # 用例標題
    @allure.description("聊天/更多:@有提到你的對話")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_more_at_dialog(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/更多:@有提到你的對話"
        global temp_num
        temp_num += 1
        case_name = "test_more_at_dialog"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********聊天/更多:@有提到你的對話   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊：「更多」tab")
        ctp.click_more_tab()
        case_step = case_step + cbz.case_step("3、點擊：@有提到你的對話")
        ctp.click_more_rl_at()
        case_step = case_step + cbz.case_step("4、點擊：@列表中首行跳轉icon")
        ctp.click_moar_at_list_jump_icon()
        case_step = case_step + cbz.case_step("檢查：聊天窗口中有顯示@內容")
        is_an_atuser = ctp.is_at_jump_chat_an_atuser()
        try:  # 檢查：聊天窗口中有顯示@內容
            assert is_an_atuser == True
            case_step = case_step + cbz.case_step("檢查成功。跳轉對應@聊天信息正常")
            logging.info("檢查成功。跳轉對應@聊天信息正常")
        except:
            actual = "檢查失敗！@跳轉異常"
            expect = "跳轉對應@聊天信息正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button_one()
            ctp.return_button_one()

    # 聽筒模式開關
    @allure.title("聽筒模式開關")  # 用例標題
    @allure.description("聊天/更多:聽筒模式開關")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_more_headphone_mode(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/更多:聽筒模式開關"
        global temp_num
        temp_num += 1
        case_name = "test_more_headphone_mode"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********     聊天/更多:聽筒模式開關   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊：「更多」tab")
        ctp.click_more_tab()
        before_setup_status = ctp.get_more_headphone_mode_text()  # 獲取當前耳筒模式狀態
        case_step = case_step + cbz.case_step("3、獲取當前開關狀態為{};然後點擊：耳筒模式開關".format(before_setup_status))
        ctp.click_more_headphone_mode()  # 點擊：耳筒模式開關
        time.sleep(1)
        rear_setup_status = ctp.get_more_headphone_mode_text()  # 獲取點擊開關後的耳筒模式狀態
        case_step = case_step + cbz.case_step("獲取點擊開關後裔的狀態為{},進行檢查：".format(rear_setup_status))
        try:  # 檢查：
            assert before_setup_status != rear_setup_status
            case_step = case_step + cbz.case_step("檢查成功。設置「聽筒模式」開關功能正常")
            logging.info("檢查成功。設置「聽筒模式」開關功能正常")
        except:
            actual = "檢查失敗！設置「聽筒模式」開關功能出錯"
            expect = "設置「聽筒模式」開關功能正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise

    # 設定字體大小
    @allure.title("設定字體大小")  # 用例標題
    @allure.description("聊天/更多:設定字體大小")  # 用例描述
    @allure.severity(bsc.C[0])
    def test_more_setup_font_size(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天/更多:設定字體大小"
        global temp_num
        temp_num += 1
        case_name = "test_more_setup_font_size"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        per_list = []
        global per_num, data_lsit2
        per_num += 1
        module = '聊天'
        per_list = append_data(per_list, per_num, module, case_name, title)
        data_lsit2.append(per_list)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("*********     聊天/更多:設定字體大小   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊：「更多」tab")
        ctp.click_more_tab()
        case_step = case_step + cbz.case_step("3、點擊：「字體大小」")
        ctp.click_more_more_setup_font_size()
        before_setup_size = ctp.get_ele_size_height()  # 獲取當前文案字體大小
        case_step = case_step + cbz.case_step("4、设置前字體大小為'{}'".format(before_setup_size))
        logging.info("设置前字體大小為'{}'".format(before_setup_size))
        case_step = case_step + cbz.case_step("5、點擊：最大設置icon，重新設置大小")
        ctp.click_setup_font_size_max()
        case_step = case_step + cbz.case_step("6、點擊：「完成」按鈕")
        ctp.click_more_setup_done_button()
        case_step = case_step + cbz.case_step("7、點擊：「字體大小」")
        ctp.click_more_more_setup_font_size()
        rear_setup_size = ctp.get_ele_size_height()
        case_step = case_step + cbz.case_step("8、设置后字體大小為'{}'".format(rear_setup_size))
        logging.info("设置后字體大小為'{}'".format(rear_setup_size))
        case_step = case_step + cbz.case_step("檢查：字體是否設置成功")
        try:  # 檢查：字體是否設置成功
            assert before_setup_size != rear_setup_size
            case_step = case_step + cbz.case_step("檢查成功。設置字體大小成功")
            logging.info("檢查成功。設置字體大小成功")
        except:
            actual = "檢查失敗！設置字體大小出錯"
            expect = "設置字體大小成功"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.C[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.click_setup_font_size_default()
            ctp.click_more_setup_done_button()


@pytest.mark.demotest
@pytest.mark.chat
@allure.feature("回归测试救命清单/聊天/发送消息")
@allure.story("发送消息")
@pytest.mark.all
@pytest.mark.usefixtures("startApp_withReset")
class TestChatSendTxt:

    # 发送消息:IM中聊天发送消息
    @allure.title("发送消息:IM中聊天发送消息")  # 用例標題
    @allure.description("发送消息:IM中聊天发送消息")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_IM_chat_send_text(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "聊天:在 IM 發布普通文本消息、圖片、視頻、語音	可以成功發出"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_send_voice"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()                               # 用例前置--返回首页
        logging.info("********* 发送消息:IM中聊天发送消息   *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        start_time = ctp.get_system_time_time()  # 执行开始时间
        logging.info("[回归测试救命清单/聊天/发送消息]脚本开始执行时间：{}".format(start_time))
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【訊息】tab")
        ctp.click_message_tab()
        case_step = case_step + cbz.case_step("3、創建一個群組聊天")
        ctp.enter_group_chat()
        case_step = case_step + cbz.case_step("4、點擊輸入框")
        ctp.click_chat_text_input()
        case_step = case_step + cbz.case_step("5、輸入文本'{}'，點擊傳送".format(CD.IM_chat_send_text1))
        ctp.message_input_text_click_send(CD.IM_chat_send_text1)
        new_message = ctp.get_chat_new_message_text()       # 获取最新发送的文本内容
        case_step = case_step + cbz.case_step("检查1：發送‘{}’文本是否成功".format(CD.IM_chat_send_text1))
        try:
            assert new_message.find(CD.IM_chat_send_text1) != -1  # 檢查:最新消息文本包含了輸入文本
            case_step = case_step + cbz.case_step("檢查成功")
            logging.info("檢查成功")
            end_time = ctp.get_system_time_time()  # 结束时间
            ctp.demo_get_time_interval_time(start_time, end_time)  # 统计执行脚本所耗费时间
        except:
            actual = "檢查失敗！發送‘{}’文本出錯".format(CD.IM_chat_send_text1)
            expect = "發送‘{}’文本成功".format(CD.IM_chat_send_text1)
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            end_time = ctp.get_system_time_time()  # 结束时间
            ctp.demo_get_time_interval_time(start_time, end_time)  # 统计执行脚本所耗费时间
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        else:
            # 发送图片
            case_step = case_step + cbz.case_step("6、點擊圖片icon")
            ctp.click_chat_image_icon()
            case_step = case_step + cbz.case_step("7、选择一张圖片发送")
            ctp.click_chat_one_photo()
            case_step = case_step + cbz.case_step("檢查2：發送圖片是否成功")
            find_photo = ctp.find_chat_photo()
            try:  # 檢查:最新生成文件時間=系統時間
                assert find_photo == True
                case_step = case_step + cbz.case_step("檢查成功。發送圖片成功")
                logging.info("檢查成功。發送圖片成功")
                end_time = ctp.get_system_time_time()  # 结束时间
                ctp.demo_get_time_interval_time(start_time, end_time)  # 统计执行脚本所耗费时间
            except:
                actual = "檢查失敗！發送圖片檢查異常"
                expect = "發送圖片檢查正常"
                video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                ctp.screenshot(actual)
                end_time = ctp.get_system_time_time()  # 结束时间
                ctp.demo_get_time_interval_time(start_time, end_time)  # 统计执行脚本所耗费时间
                with allure.step(actual):
                    # 调用禅道api，报BUG单
                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                    with allure.step(bug_link):
                        raise
            else:
                # 点击图片，检查放大功能
                case_step = case_step + cbz.case_step("8、點擊聊天窗中的图片")
                ctp.click_chat_img()
                case_step = case_step + cbz.case_step("检查3：图片放大功能")
                if_download_icon = ctp.if_chat_img_enlarge_download()
                try:
                    assert if_download_icon == True
                    case_step = case_step + cbz.case_step("檢查成功。放大图片正常")
                    logging.info("檢查成功。放大图片正常")
                    end_time = ctp.get_system_time_time()  # 结束时间
                    ctp.demo_get_time_interval_time(start_time, end_time)  # 统计执行脚本所耗费时间
                except:
                    actual = "檢查失敗！点击图片，放大图片异常"
                    expect = "放大图片正常"
                    video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
                    case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                    ctp.screenshot(actual)
                    end_time = ctp.get_system_time_time()  # 结束时间
                    ctp.demo_get_time_interval_time(start_time, end_time)  # 统计执行脚本所耗费时间
                    with allure.step(actual):
                        # 调用禅道api，报BUG单
                        bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                        with allure.step(bug_link):
                            raise
                else:
                    ctp.return_button()             # 返回退出图片详情
                    # 拍摄视频并发送
                    case_step = case_step + cbz.case_step("9、点击拍摄icon")
                    ctp.click_chat_shoot_icon()
                    while ctp.is_group_chat_authority() == True:
                        ctp.allow_authorization(model_name="獲取允許權限")
                        time.sleep(1)
                        logging.info("获取允许权限")
                    case_step = case_step + cbz.case_step("10、长按快門拍摄视频并点击发送按钮")
                    ctp.longpress_chat_shutter_button()
                    ctp.click_chat_shoot_send_button()          # 点击发送
                    case_step = case_step + cbz.case_step("檢查4：发送视频")
                    video_size = ctp.get_chat_video_size()
                    try:  # 检查:聊天窗口中找打视频播放icon
                        assert video_size <= 45
                        case_step = case_step + cbz.case_step("檢查成功。發送視頻成功")
                        logging.info("檢查成功。發送視頻成功")
                        end_time = ctp.get_system_time_time()  # 结束时间
                        ctp.demo_get_time_interval_time(start_time, end_time)  # 统计执行脚本所耗费时间
                    except:
                        actual = "檢查失敗！發送消息異常"
                        expect = "發送消息正常"
                        video_download_url = ctp.get_bug_video_url(android_video_path, video_name, pull_time=25)
                        case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                        ctp.screenshot(actual)
                        end_time = ctp.get_system_time_time()  # 结束时间
                        ctp.demo_get_time_interval_time(start_time, end_time)  # 统计执行脚本所耗费时间
                        with allure.step(actual):
                            # 调用禅道api，报BUG单
                            bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1],
                                                                 "聊天")  # 传入BUG标题，BUG复现步骤
                            with allure.step(bug_link):
                                raise
                    else:
                        # 发送语音
                        case_step = case_step + cbz.case_step("11、點擊語音icon")
                        ctp.click_voice_icon()
                        while ctp.is_group_chat_authority() == True:
                            ctp.allow_authorization(model_name="獲取允許權限")  # 获取允许权限
                            time.sleep(1)
                        logging.info("获取允许权限")
                        case_step = case_step + cbz.case_step("12、長按【按住說話】3秒發送語音")
                        ctp.long_press_voice_icon()
                        case_step = case_step + cbz.case_step("检查4：發送語音是否成功")
                        time_text = ctp.find_chat_new_voice_time()
                        try:                                                    # 檢查:聊天窗口中有語音
                            assert time_text in [3,4]                           # 語音時間等於3秒
                            case_step = case_step + cbz.case_step("檢查成功。發送語音成功")
                            logging.info("檢查成功。發送語音成功")
                            end_time = ctp.get_system_time_time()  # 结束时间
                            ctp.demo_get_time_interval_time(start_time, end_time)  # 统计执行脚本所耗费时间
                        except:
                            actual = "檢查失敗！發送語音失敗"
                            expect = "檢查成功。發送語音成功"
                            video_download_url = ctp.get_bug_video_url(android_video_path,video_name, pull_time=25)
                            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                            ctp.screenshot(actual)
                            end_time = ctp.get_system_time_time()  # 结束时间
                            ctp.demo_get_time_interval_time(start_time, end_time)  # 统计执行脚本所耗费时间
                            with allure.step(actual):
                                # 调用禅道api，报BUG单
                                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1],"聊天")  # 传入BUG标题，BUG复现步骤
                                with allure.step(bug_link):
                                    raise
                        else:
                            # 发语音小于1s弹出toast提示
                            case_step = case_step + cbz.case_step("13、點擊語音icon")
                            ctp.click_voice_icon()
                            case_step = case_step + cbz.case_step("14、短按【按住說話】0.5秒發送語音")
                            ctp.short_press_voice_icon()
                            time_text = ctp.find_chat_new_voice_time()      # 获取最新发送语音时长
                            case_step = case_step + cbz.case_step("检查4：發送語音小于1s是否弹出提示")
                            try:
                                # assert time_text in [3,4]           # 判断依据，没有产生新的语言，已上条记录为准
                                assert time_text == 9  # 判断依据，没有产生新的语言，已上条记录为准
                                case_step = case_step + cbz.case_step("檢查成功。發送語音时间小于1s时无法发出")
                                logging.info("檢查成功。發送語音时间小于1s时无法发出")
                                end_time = ctp.get_system_time_time()  # 结束时间
                                ctp.demo_get_time_interval_time(start_time, end_time)  # 统计执行脚本所耗费时间
                            except:
                                actual = "檢查失敗！语言时间小于1s发送能成功"
                                expect = "檢查成功。發送語音时间小于1s时无法发出"
                                video_download_url = ctp.get_bug_video_url(android_video_path, video_name, pull_time=30)
                                case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
                                ctp.screenshot(actual)
                                end_time = ctp.get_system_time_time()  # 结束时间
                                ctp.demo_get_time_interval_time(start_time, end_time)  # 统计执行脚本所耗费时间
                                with allure.step(actual):
                                    # 调用禅道api，报BUG单
                                    bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                                    with allure.step(bug_link):
                                        raise
        finally:
            ctp.return_button()

    # 通讯录中点击头像检查放大功能
    @allure.title("通讯录中点击头像:放大功能")  # 用例標題
    @allure.description("通讯录中点击头像:放大功能")  # 用例描述
    @allure.severity(bsc.B[0])
    def test_click_book_user_avatar(self, startApp_withReset):
        ctp = CTP(startApp_withReset)
        title = "通讯录中点击头像:放大功能"
        global temp_num
        temp_num += 1
        case_name = "test_personal_chat_send_voice"
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        my_data = ">>步骤{} -- {}-- {}-- {}\n".format(temp_num, case_name, title, now_time)
        with open(os.path.join(base_path, "Neptune-runcase.txt"), "a", encoding="utf-8") as f:
            f.write(my_data)
        bug_title = "[Neptune.AI][{0}][{1}]自动化检测到功能异常".format(ctp.get_app_environment(), title)  # BUG标题
        case_step = ''  # BUG复现步骤
        ctp.return_home()  # 用例前置--返回首页
        logging.info("********* 通讯录中点击头像:放大功能 *********")
        case_Preposition = "无"  # 前置条件
        case_step = case_step + cbz.case_condition(case_Preposition)  # 测试环境
        list_data = ctp.Start_recording()  # 开始录屏
        android_video_path = list_data[0]  # 生成视频路径
        video_name = list_data[1]  # 视频名
        case_step = case_step + cbz.case_step("1、點擊【聊天】")
        ctp.click_chat_tab()
        case_step = case_step + cbz.case_step("2、點擊【通訊錄】tab")
        ctp.click_address_book_tab()
        case_step = case_step + cbz.case_step("3、点击列表中有头像的用户")
        ctp.click_book_user_avatar()
        case_step = case_step + cbz.case_step("4、个人资料页点击用户头像")
        ctp.click_book_personal_user_avatar()
        find_download  = ctp.if_chat_img_enlarge_download()
        try:
            assert find_download == True
            case_step = case_step + cbz.case_step("檢查成功。图像放大正常")
            logging.info("檢查成功。图像放大正常")
        except:
            actual = "檢查失敗！图像放大异常"
            expect = "檢查成功。图像放大正常"
            video_download_url = ctp.get_bug_video_url(android_video_path, video_name)
            case_step = case_step + cbz.case_result(actual, expect, video_download_url)  # 测试结果
            ctp.screenshot(actual)
            with allure.step(actual):
                # 调用禅道api，报BUG单
                bug_link = ZenTaoBugApi().submit_bug(bug_title, case_step, bsc.B[1], "聊天")  # 传入BUG标题，BUG复现步骤
                with allure.step(bug_link):
                    raise
        finally:
            ctp.return_button()
