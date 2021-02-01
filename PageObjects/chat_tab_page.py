__author__ = 'developer'

from Common.BasePage import BasePage
from PageLocators.chat_tab_locator import ChatTabLocator as ctl
from TestDatas import COMMON_DATA
import re
import time
import logging
import random


class ChatTabPage(BasePage):
    # 查找【聊天】按钮
    def is_chat_tab(self):
        name = "查找【聊天】按钮"
        self.wait_ele_visible_pass(ctl.chat_tab, wait_times=20, poll_frequency=1, model=name)
        try:
            self.get_element(ctl.chat_tab)
            return True
        except:
            return False

    # 【返回】物理按键（一步）
    def return_button_one(self):
        self.return_button()
        time.sleep(1)
        return self

    # 点击【聊天】tab
    def click_chat_tab(self):
        name = "点击【聊天】tab"
        self.wait_eleVisible(ctl.chat_tab, model=name)
        self.click_element(ctl.chat_tab, model=name)
        return self

    #点击"+"
    def click_chat_es(self):
        name = "点击'+'"
        self.wait_eleVisible(ctl.chat_es, model=name)
        self.click_element(ctl.chat_es, model=name)
        return self

    # 点击"封存记录"
    def click_chat_sealed_records(self):
        name = "点击【封存记录】"
        self.wait_eleVisible(ctl.chat_sealed_record, model=name)
        self.click_element(ctl.chat_sealed_record, model=name)
        return self

    # 获取聊天记录个数
    def sum_to_chat(self):
        name = "获取聊天记录个数"
        # self.wait_ele_visible_pass(ctl.sealed_record_talk_list, model=name)
        time.sleep(2)
        try:
            self.get_element(ctl.sealed_record_talk_list, model=name)
            return len(self.find_elements(ctl.sealed_record_talk_list))
        except:
            return 0  # 没有则返回0

        # 清理封存列表中的数据
    def delete_archive(self):
        name = "清理封存列表中的数据"
        self.wait_eleVisible_pass(ctl.chat_es, model=name)
        self.click_element(ctl.chat_es, model=name)  # 点击+号
        self.wait_eleVisible_pass(ctl.chat_sealed_record,model=name)
        self.click_element(ctl.chat_sealed_record, model = name)  # 点击【封存记录】
        while self.find_sealed_record_talk_list() == True:
            self.swipe_screen(0.8, 0.15, 0.2, 0.15, model=name)  # 左滑
            self.click_left_archive_icon()
        self.adb_keycode(4)
        return self

    # 查找列表中是否有封存数据
    def find_sealed_record_talk_list(self):
        name = "查找列表中是否有封存数据"
        time.sleep(1)
        # self.wait_eleVisible_pass(ctl.sealed_record_talk_list,model = name)
        try:
            self.get_element(ctl.sealed_record_talk_list,model = name)
            return True
        except:
            return False

    # 点击【讯息】tab
    def click_message_tab(self):
        name = "点击【讯息】tab"
        self.wait_eleVisible(ctl.message_tab, model=name)
        self.click_element(ctl.message_tab, model=name)
        return self

    # 点击讯息tab中【搜索】输入框输入文本并进行搜索
    def click_message_search_input(self, text):
        name = "讯息中搜索"
        self.wait_eleVisible(ctl.message_search_input, model=name)
        self.click_element(ctl.message_search_input, model=name)  # 点击点击讯息tab中【搜索】输入框，跳转至搜索详情页
        self.wait_eleVisible(ctl.search_details_input, model=name)  # 跳转后等待输入框可见
        self.input_text(ctl.search_details_input, text, model=name)  # 输入文本
        self.keyboard_search(model=name)  # 触发搜索
        return self

    # 讯息tab搜索-【独立讯息】有搜索结果(获取讯息数量)
    def search_message_number(self):
        name = "讯息中搜索,【独立讯息】有搜索结果"
        self.wait_eleVisible_pass(ctl.message_tab_one, model=name)
        message_text = self.get_text(ctl.independent_message_tab, model=name)  # 获取独立讯息文本
        message_number = eval(re.split('\(|\)', message_text)[1])  # 对文本进行切割获取查询个数
        return message_number

    # 获取文本：【独立讯息】中第一行聊天文本
    def get_message_tab_one_text(self):
        name = "【独立讯息】中第一行聊天文本"
        self.wait_eleVisible(ctl.message_tab_one, model=name)
        text = self.get_text(ctl.message_tab_one, model=name)
        return text

    # 点击【独立讯息】中第一行讯息-下拉按钮
    def click_drop_down_list_button(self):
        name = "点击【独立讯息】中第一行讯息-下拉按钮"
        self.wait_eleVisible(ctl.drop_down_list_button, model=name)
        self.click_element(ctl.drop_down_list_button, model=name)
        if self.is_no_login_popup_cancel() == True:  # 如果有提示弹框则点击【取消】按钮
            self.click_element(ctl.user_chat_no_login_popup_cancel_button)
        return self

    # 查找元素：【独立讯息】跳转聊天窗口，通过文本来查找聊天记录中关键词元素
    def is_message_find(self, text):
        name = "跳转聊天窗口，通过文本来查找聊天记录中关键词元素"
        try:
            self.wait_eleVisible(ctl.user_avatar, model=name)
            self.get_element(ctl.user_avatar, model=name)
            return True
        except:
            return False

    # 点击讯息tab搜索-【群组类别】tab
    def click_group_category_tab(self):
        name = "点击讯息tab搜索-【群组类别】tab"
        self.wait_eleVisible(ctl.group_category_tab, model=name)
        self.click_element(ctl.group_category_tab, model=name)
        return self

    # 获取文本：讯息tab搜索-【群组类别】有搜索结果(获取讯息数量)
    def search_message_group_number(self):
        name = "获取讯息搜索结果个数"
        self.wait_eleVisible(ctl.group_category_tab, model=name)
        message_text = self.get_text(ctl.group_category_tab, model=name)  # 获取独立讯息文本
        message_group_number = eval(re.split('\(|\)', message_text)[1])  # 对文本进行切割获取查询个数
        return message_group_number

    # 点击群组类别中第一行数据下拉列表
    def click_message_group_one(self):
        name = "点击群组类别中第一行数据下拉列表"
        self.wait_eleVisible(ctl.group_tab_one, model=name)
        self.find_elements(ctl.group_tab_one)[0].click()
        return self

    # 获取群组类别-聊天记录页面列表第一行文本内容
    def get_group_one_text(self):
        name = "获取群组类别-聊天记录页面列表第一行文本内容"
        self.wait_eleVisible(ctl.group_tab_one_list_one, model=name)
        text = self.get_text(ctl.group_tab_one_list_one, model=name)
        return text

    # 点击群组类别-聊天记录列第一行进入聊天窗口
    def click_group_one(self):
        name = "点击群组类别-聊天记录列第一行进入聊天窗口"
        self.wait_eleVisible(ctl.group_tab_one_list_one, model=name)
        self.click_element(ctl.group_tab_one_list_one, model=name)
        return self

    # 查找群组类别-聊天记录列表
    def find_group_tab_one_list(self):
        name = "查找群组类别-聊天记录列表"
        try:
            self.get_element(ctl.group_tab_title, model=name)
            return True
        except:
            return False

    # 查找群组类别-通讯录弹框
    def find_pus_button(self):
        name = "查找群组类别-通讯录弹框"
        try:
            self.get_element(ctl.pus_button, model=name)
            return True
        except:
            return False

    # 点击：通讯录类型-提示弹框取消按钮
    def click_pus_button(self):
        name = "点击：通讯录类型-提示弹框取消按钮"
        self.wait_eleVisible(ctl.pus_button, model=name)
        self.click_element(ctl.pus_button, model=name)
        return self

    # 获取文本：群组类别-聊天室title
    def get_chatroom_title(self):
        name = "获取文本：群组类别-聊天室title"
        self.wait_eleVisible(ctl.chatroom_title, model=name)
        title = self.get_text(ctl.chatroom_title, model=name).lower()  # 获取文本后将字体转化为小写
        return title

    # 获取文本：群组类别-通讯录-窗口title
    def get_center_title(self):
        name = "获取文本：群组类别-通讯录-窗口title"
        self.wait_eleVisible(ctl.center_title, model=name)
        return self.get_text(ctl.center_title, model=name).lower()

    # --------------------------------------------   【新增对话】主要使用的Action     -------------------------

    # 点击：新增对话（点击加号创建-再点击新增对话）
    def click_create_new_message(self):
        name = "点击：新增对话"
        self.wait_eleVisible(ctl.create_icon)
        self.click_element(ctl.create_icon)
        self.wait_eleVisible(ctl.create_new_message_button)
        self.click_element(ctl.create_new_message_button)
        return self

    # 進入新增對話頁面，且數據加載完成
    def enter_personal_chat_page(self):
        self.click_create_new_message()  # 点击+号-【新增对话】
        while self.is_new_message_one_low() == False:
            self.return_button_one()
            self.click_create_new_message()  # 点击+号-【新增对话】
            time.sleep(2)
        return self

    # 点击：【新增对话】字母导航栏 W
    def click_create_new_message_letter_W(self):
        self.wait_eleVisible(ctl.create_indexsidebar)
        #self.tap_click_ele(0.95, 0.70)     #正式環境
        self.tap_click_ele(0.966, 0.718)   #s9/s10  by jinwei
        time.sleep(1)
        return self

    # 获取文本：【新增对话】页面可见第一个联系人堆首字母
    def get_create_new_message_letter_text(self):
        self.wait_eleVisible(ctl.create_new_message_letter_navig)
        return self.find_elements(ctl.create_new_message_letter_navig)[0].text   #獲取第一行出現的字幕
        #return self.find_elements(ctl.create_new_message_letter_navig)[1].text  # 獲取第二行出現的字幕 by jinwei

    # 获取文本：新增对话页第一行（第一个联系人名）
    def get_new_message_one_name(self):
        name = "获取[新增对话]列表第一个用户昵称"
        self.wait_eleVisible(ctl.create_message_one_low_text, model=name)
        return self.get_text(ctl.create_message_one_low_text, model=name)

    # 点击：新增对话页随机点击一个用户
    def click_new_message_one_low(self):
        name = "点击[新增对话]列表第一个用户昵称"
        # self.wait_eleVisible(ctl.create_message_one_low_text,model=name)
        #         # self.click_element(ctl.create_message_one_low_text,model=name)
        user_number = len(self.find_elements(ctl.create_message_one_low_text))
        random_number = random.randint(0, user_number - 1)
        logging.info("點擊列表中第{}個用戶".format(random_number + 1))
        self.find_elements(ctl.create_message_one_low_text)[random_number].click()
        time.sleep(1)
        if self.is_no_login_popup_cancel() == True:  # 如果有提示弹框则点击【取消】按钮
            self.click_element(ctl.user_chat_no_login_popup_cancel_button)
        return self

    # 点击：新增对话页点击第一个用户
    def click_new_message_list_one(self):
        name = "点击[新增对话]列表第一个用户昵称"
        logging.info("點擊列表中第{}個用戶".format(1))
        self.find_elements(ctl.create_message_one_low_text, model=name)[0].click()
        time.sleep(1)
        if self.is_no_login_popup_cancel() == True:  # 如果有提示弹框则点击【取消】按钮
            self.click_element(ctl.user_chat_no_login_popup_cancel_button, model=name)
        return self

    # 点击：新增对话页第(item+1)行（第(item+1)个联系人）
    def click_new_message_one_low_item(self, item):
        name = "点击[新增对话]列表第一个用户昵称"
        self.wait_eleVisible(ctl.create_message_one_low_text, model=name)
        self.find_elements(ctl.create_message_one_low_text, model=name)[item].click()
        return self

    # 判断：新增对话页面列表数据是否加载出来
    def is_new_message_one_low(self):
        name = "判断：新增对话页面列表数据是否加载出来"
        try:
            self.get_element(ctl.create_message_one_low_text, model=name)
            return True
        except:
            return False

    # 判断：新增群组页面列表数据是否加载出来
    def is_create_group_one_low_text(self):
        name = "判断：新增群组页面列表数据是否加载出来"
        self.wait_eleVisible_pass(ctl.create_group_one_low_text,wait_times=2, poll_frequency=0.2)
        try:
            self.get_element(ctl.create_group_one_low_text, model=name)
            return True
        except:
            return False

    # 获取文本：新增对话-个页聊天窗口title
    def get_personal_chat_title(self):
        name = "获取文本：新增对话-个页聊天窗口title"
        self.wait_eleVisible(ctl.personal_chat_title, model=name)
        return self.get_text(ctl.personal_chat_title, model=name)

    # 点击：头像为灰色用户（未上线用户）
    def click_offline_user(self):
        name = "点击：头像为灰色用户（未上线用户）"
        self.wait_eleVisible(ctl.online_user, model=name)  # 等待数据加载出来
        while self.make_offline_user() == False:  # 通过滑屏使得灰色头像在列表中可见
            self.swipe_screen(0.5, 0.8, 0.5, 0.4)
        self.click_element(ctl.offline_user, model=name)  # 点击第一个未在线用户头像
        return self

    # 獲取聊天窗口頁面title（用戶暱稱）
    def find_user_name(self):
        self.wait_elePrences(ctl.personal_chat_title)
        return self.get_text(ctl.personal_chat_title)

    # 查找灰色用户
    def make_offline_user(self):
        name = "查找灰色用户（未上线）"
        try:
            time.sleep(1)
            self.get_element(ctl.offline_user, model=name)
            return True
        except:
            return False

    # 判断是否弹出未在线拨打提示弹框
    def is_dial_box(self):
        name = "判断是否弹出未在线拨打提示弹框"
        try:
            time.sleep(3)
            self.get_element(ctl.tip_box_dial, model=name)
            return True  # 弹出
        except:
            return False  # 没有弹出

    # 点击：提示弹框点击拨打按钮
    def click_dial(self):
        name = "点击：提示弹框点击拨打按钮"
        self.wait_eleVisible(ctl.tip_box_dial, model=name)
        self.click_element(ctl.tip_box_dial, model=name)
        return self

    # 判断是否点击拨打按钮后是否展示下拉列表
    def is_dial_box_list(self):
        name = "判断是否点击拨打按钮后是否展示下拉列表"
        try:
            time.sleep(3)
            self.get_element(ctl.dial_list_cancel_button, model=name)
            return True  # 弹出
        except:
            return False  # 没有弹出

    # 点击拨打-下拉列表中-取消按钮
    def click_dial_list_cancel(self):
        name = "点击拨打-下拉列表中-取消按钮"
        self.wait_eleVisible(ctl.dial_list_cancel_button, model=name)
        self.click_element(ctl.dial_list_cancel_button, model=name)
        return self

    # -----------【新增群组】主要使用的Action-----------
    # 点击：新增群组（点击加号创建-再点击新增群组）
    def click_create_channel(self):
        name = "点击：新增群组（点击加号创建-再点击新增群组"
        self.wait_eleVisible(ctl.create_icon, model=name)
        self.click_element(ctl.create_icon, model=name)  # 点击创建icon
        self.wait_eleVisible(ctl.create_channel_button, model=name)
        self.click_element(ctl.create_channel_button, model=name)  # 列表中点击新增群组
        return self

    # 获取文本：新增群组页面输入框可输入字符个数
    def get_count_input_number(self):
        name = "获取新增群组页面-可输入字符个数"
        self.wait_eleVisible(ctl.default_count_item, model=name)
        return int(self.get_text(ctl.default_count_item, model=name))  # 返回元素文本信息个数,转化为int类型

    # 输入文本：新增群组页面输入框输入文本
    def input_count_text(self, text):
        name = "新增群组页面输入框输入文本"
        self.wait_eleVisible(ctl.default_count_input, model=name)
        self.input_text(ctl.default_count_input, text, model=name)  # 输入文本，text传参
        return self

    # 获取输入文本字符长度
    def get_input_count_text_length(self, text):
        return len(text)

    # 点击：【新增照片】icon(未上传图像前)
    def click_add_photo(self):
        name = "点击【新增照片】icon(未上传图像前）"
        self.wait_eleVisible(ctl.add_photo, model=name)
        self.click_element(ctl.add_photo, model=name)
        return self

    # 点击：【新增照片】icon（上传图像后）
    def click_add_photo_to(self):
        name = "点击【新增照片】icon(上传头像后）"
        self.wait_eleVisible(ctl.add_to_photo, model=name)
        self.click_element(ctl.add_to_photo, model=name)
        return self

    # 点击：【新增相片】列表以外的部分
    def click_touch_outside(self):
        name = "点击【新增相片】列表以外的部分"
        self.wait_eleVisible(ctl.take_photo_button, model=name)
        self.click_element(ctl.touch_outside, model=name)
        return self

    # 点击：新增相片-下拉列表中-【拍照】-按快门
    def click_take_photo_button(self):
        name = "【拍照】-按快门"
        self.wait_eleVisible(ctl.take_photo_button, model=name)
        self.click_element(ctl.take_photo_button, model=name)  # 点击列表中-【拍照】选项
        time.sleep(3)
        self.tap_click_ele(0.5,0.962, model=name)  # 点击【快门】icon s9s10通用
        return self

    # 点击：确定页-【重试】-拍照-确定-完成
    def click_retry(self):
        name = "创建群组头像【重试】-拍照-确定-完成"
        self.wait_eleVisible(ctl.take_photo_retry, model=name)
        self.click_element(ctl.take_photo_retry, model=name)  # 点击【重试】
        time.sleep(3)
        self.tap_click_ele(0.5, 0.962, model=name)  # 点击【快门】icon s9s10通用
        self.wait_eleVisible(ctl.take_photo_confirm, model=name)
        self.click_element(ctl.take_photo_confirm, model=name)  # 点击【确定】按钮
        self.wait_eleVisible(ctl.cutting_done, model=name)
        self.click_element(ctl.cutting_done, model=name)  # 照片剪切页-【完成】按钮
        return self

    # 查找：新增相片下拉列表是否隐藏
    def is_add_photo_list(self):
        name = "查找-新增相片下拉列表是否隐藏"
        self.wait_eleVisible(ctl.next_step_button, model=name)  # 等待[下一步]可见
        try:
            self.get_element(ctl.take_photo_button, model=name)  # 查找【拍照】
            return True
        except:
            return False

    # 查找：点击新增相片下拉列表中是否有【删除图片】选项
    def is_find_delete_photo(self):
        name = "查找新增相片下拉列表中是否含有【删除图片】选项"
        self.wait_eleVisible(ctl.take_photo_button, model=name)  # 拍照选项可见代表列表加载完成
        try:
            self.get_element(ctl.delete_photo_button, model=name)  # 查找【删除图片】选项
            return True
        except:
            return False

    # 点击：列表中【选择照片】
    def click_choose_photo(self):
        name = "新增群组头像点击列表中【选择照片】"
        self.wait_eleVisible(ctl.choose_photo_button, model=name)
        self.click_element(ctl.choose_photo_button, model=name)
        return self

    # 点击：新增群组-【下一步】按钮
    def click_next_step_button(self):
        name = "点击-新增群组-【下一步】按钮"
        self.wait_eleVisible(ctl.next_step_button, model=name)
        self.click_element(ctl.next_step_button, model=name)
        return self

    # 点击：新增成员页-加号icon
    def click_add_people_icon(self):
        name = "点击-新增成员页-加号icon"
        self.wait_eleVisible(ctl.add_people_icon, model=name)
        self.click_element(ctl.add_people_icon, model=name)
        return self

    # 点击：联络人页—勾选用户-创建
    def check_uesr_done(self, times):  # times:勾选人数
        name = "点击-联络人页—勾选用户-创建"
        self.wait_eleVisible(ctl.check_icon, model=name)
        # 勾选多人
        for time in range(times):  # 勾选多名联系人
            self.find_elements(ctl.check_icon)[time].click()
        self.wait_eleVisible(ctl.check_done, model=name)
        self.click_element(ctl.check_done, model=name)  # 点击完成
        self.wait_eleVisible(ctl.create_button, model=name)
        self.click_element(ctl.create_button, model=name)  # 点击建立
        return self

    # 获取toast结果：创建群组成功
    def get_create_success_toast(self):
        name = "获取创建群组成功toast提示"
        try:
            self.get_toastMsg("創建成功", model=name)
            return True
        except:
            return False

    # 判斷：创建群组-「設有群組管理員」開關狀態      checked:true 开；false 关
    def is_site_admin_switch(self):
        self.wait_eleVisible(ctl.default_count_admin_switch)
        if self.get_element_attribute(ctl.default_count_admin_switch, "checked") == "true":
            return True
        else:
            return False

    # 判斷：创建群组-【允許成員自動退出群組】 關閉      checked:true 开；false 关
    def is_leave_group(self):
        self.wait_eleVisible(ctl.default_count_admin_switch)
        if self.get_element_attribute(ctl.default_count_leave_group, "checked") == "true":
            return True
        else:
            return False

    # 點擊：聊天中-右上角頭像icon
    def click_droup_chat_avatar(self):
        name = "點擊：聊天中-右上角頭像icon"
        self.wait_eleVisible(ctl.droup_chat_avatar, model=name)
        self.click_element(ctl.droup_chat_avatar, model=name)
        return self

    # 判断：【群組資訊】頁-「設有群組管理員」狀態
    def is_droup_page_site_admin_switch(self):
        name = "判断：【群組資訊】頁-「設有群組管理員」狀態"
        self.wait_eleVisible(ctl.chat_droup_admin_switchv, model=name)
        if self.find_elements(ctl.chat_droup_admin_switchv)[0].text == "開啟":
            return True
        else:
            return False

    # 判断：【群組資訊】頁-【允許成員自動退出群組】狀態
    def is_droup_page_leave_group(self):
        name = "判断：【群組資訊】頁-【允許成員自動退出群組】狀態"
        self.wait_eleVisible(ctl.chat_droup_admin_switchv, model=name)
        if self.find_elements(ctl.chat_droup_admin_switchv)[1].text == "開啟":
            return True
        else:
            return False

    # 邀请加入群组
    def invite_to_group_data(self):
        a = 0
        while self.is_book_user_data_Invite_group() == False:
            self.swipe_screen(0.5, 0.8, 0.5, 0.4)
            a = a + 1
            if a > 3:
                break  # 滑屏至「邀请群组」可见
        self.wait_eleVisible(ctl.book_user_data_Invite_group)
        self.click_element(ctl.book_user_data_Invite_group)  # 点击【邀请群组】
        self.wait_eleVisible(ctl.book_Invite_group_page_list)
        itme = len(self.find_elements(ctl.book_Invite_group_page_list))
        index_itme = random.randint(0, itme - 1)
        logging.info("点击第{}个群组".format(index_itme + 1))
        self.find_elements(ctl.book_Invite_group_page_list)[index_itme].click()  # 随机点击一个群组
        time.sleep(1)
        self.return_button_one()
        return self

    # 判断：【邀请群组】可见
    def is_book_user_data_Invite_group(self):
        time.sleep(1)
        try:
            self.get_element(ctl.book_user_data_Invite_group)
            return True
        except:
            return False

    # -----------【列表左滑】主要使用的Action-----------

    # 获取文本：讯息tab[封存聊天记录]的个数
    def get_chat_record_time(self):
        name = "获取文本：讯息tab[封存聊天记录]的个数"
        self.wait_eleVisible_pass(ctl.list_one_name, model=name)
        time = eval(self.get_text(ctl.archive_drop_down)[-2])
        return time

    # 滑屏：对讯息列表中第一个进行左滑操作
    def swipe_left_list_one(self):
        name = "滑屏：对讯息列表中第一个进行左滑操作"
        self.wait_eleVisible_pass(ctl.list_one_name, model=name)  # 等待第一个数据加载完成
        self.swipe_screen(0.8, 0.33, 0.4, 0.33, model=name)  # 左滑
        return self

    # 滑屏：存对话页，对第一个进行左滑操作
    def swipe_dialogue_list_one(self):
        name = "滑屏：存对话页，对第一个进行左滑操作"
        self.wait_eleVisible(ctl.dialogue_list_one_name, model=name)  # 等待第一个数据加载完成
        self.swipe_screen(0.8, 0.15, 0.2, 0.15, model=name)  # 左滑
        return self

    # 点击【标为未读】
    def click_left_read_icon(self):
        name = "点击【标为未读】"
        self.wait_eleVisible(ctl.left_read_icon, model=name)
        self.click_element(ctl.left_read_icon, model=name)
        return self

    # 点击【静音】
    def click_left_mute_icon(self):
        name = "点击【静音】"
        self.wait_eleVisible(ctl.left_mute_icon, model=name)
        self.click_element(ctl.left_mute_icon, model=name)
        return self

    # 点击【存档】
    def click_left_archive_icon(self):
        name = "点击【存档】"
        self.wait_eleVisible(ctl.left_archive_icon, model=name)
        self.click_element(ctl.left_archive_icon, model=name)
        return self

    # 获取text：讯息tab列表中获取第一行用户或群组名称
    def find_list_one_name(self):
        name = "获取text：讯息tab列表中获取第一行用户或群组名称"
        self.wait_eleVisible(ctl.list_one_name, model=name)
        return self.get_text(ctl.list_one_name, model=name)

    # 获取text：封存对话页获取第一行用户或群组名称
    def find_dialogue_list_one_name(self):
        name = "获取text：封存对话页获取第一行用户或群组名称作"
        self.wait_eleVisible(ctl.dialogue_list_one_name, model=name)
        return self.get_text(ctl.dialogue_list_one_name, model=name)

    # 點擊：訊息頁-點擊[封存的聊天記錄]icon
    def click_chat_record(self):
        name = "點擊：訊息頁-點擊[封存的聊天記錄]icon"
        self.wait_eleVisible(ctl.archive_drop_down, model=name)
        self.click_element(ctl.archive_drop_down, model=name)
        return self

    # 查找取消封存的-聊天记录
    def find_archive_chat(self, text):
        name = "查找取消封存的-聊天记录"
        try:
            self.text_find(text, model=name)
            return True  # 找到
        except:
            return False  # 未找到

    # 查找靜音圖標
    def find_mute_icon(self):
        name = "查找靜音圖標"
        self.wait_eleVisible(ctl.dialogue_list_one_name, model=name)
        time.sleep(2)
        try:
            self.get_element(ctl.mute_icon, model=name)
            return True
        except:
            return False

    # 獲取文本：設置靜音按鈕狀態文案
    def find_status_text(self):
        name = "獲取文本：設置靜音按鈕狀態文案"
        self.wait_eleVisible(ctl.left_mute_icon, model=name)
        return self.get_text(ctl.left_mute_icon, model=name)

    # 查找“未讀”圖標
    def find_msg_count_icon(self):
        name = "查找“未讀”圖標"
        self.wait_eleVisible(ctl.dialogue_list_one_name, model=name)
        try:
            self.get_element(ctl.msg_count_icon, model=name)
            return True
        except:
            return False

    # 獲取文本：設置未讀按鈕狀態文案
    def get_msg_count_icon_text(self):
        name = "獲取文本：設置未讀按鈕狀態文案"
        self.wait_eleVisible(ctl.left_read_icon, model=name)
        return self.get_text(ctl.left_read_icon, model=name)

    # -----------【訊息】-聊天主要使用的Action-----------
    # 进入个人聊天窗口
    def enter_personal_chat(self):
        self.click_create_new_message()  # 点击+号-【新增对话】
        while self.is_new_message_one_low() == False:
            self.return_button_one()
            self.click_create_new_message()  # 点击+号-【新增对话】
            time.sleep(2)
        self.click_new_message_one_low()   # 点击【新增对话】页面随机点击一个用户
        return self

    # 進入有郵箱的個人資料頁面
    def enter_personal_chat_email(self):
        self.click_create_new_message()  # 点击+号-【新增对话】
        while self.is_new_message_one_low() == False:
            self.return_button_one()
            self.click_create_new_message()  # 点击+号-【新增对话】
            time.sleep(2)
        self.add_conversation_enter_user_is_email()  # 点击【新增对话】页面第一个用户

        return self

    # 新增对话-進入到有郵箱的詳情頁
    def add_conversation_enter_user_is_email(self):
        name = "進入到有郵箱的詳情頁"
        a = 0
        while 1 > 0:
            self.wait_eleVisible(ctl.create_message_one_low_text, model=name)
            time.sleep(1)
            self.find_elements(ctl.create_message_one_low_text)[a].click()  # 新增对话页面，点击一个用户
            if self.is_no_login_popup_cancel() == True:  # 如果有提示弹框则点击【取消】按钮
                self.click_element(ctl.user_chat_no_login_popup_cancel_button)
            self.click_droup_chat_avatar()  # 点击聊天窗口中右上角图像icon,进入个人资料页面
            time.sleep(1)
            if self.is_user_data_mail() == True:
                break
            else:
                a = a + 1
                self.return_button()
                self.return_button()

    # 进入群组聊天窗口
    def enter_group_chat(self):
        self.click_create_channel()  # 点击加号创建-再点击新增群组
        name = str(self.random_int_one(9))+self.random_english_letter()
        self.input_count_text("回归测试IM消息群-{}".format(name))  # 输入文本
        self.click_next_step_button()  # 点击【下一步】
        self.click_add_people_icon()  # 点击+号
        while self.is_create_group_one_low_text() == False:
            self.return_button_one()
            self.click_add_people_icon()  # 点击+号
            time.sleep(4)
        self.check_uesr_done(2)  # 勾选2个联系人后点击【建立】
        return self

    # 發送多個消息，製造數據，為快速回到底部功能所用
    def send_data_chat(self, messages_number):  # messages_number:發消息次數
        number = 1
        while number <= messages_number:
            self.wait_eleVisible(ctl.text_input)
            self.input_text(ctl.text_input, "嘿！是不偷偷給我發消息了{}".format(number))
            self.click_element(ctl.sendView_button)
            number = number + 1
        return self

    # 輸入文本：20020個文本,讓後點擊『傳送』按鈕
    def input_text_overrun(self):
        name = "輸入文本：20020個文本,讓後點擊『傳送』按鈕"
        self.wait_eleVisible(ctl.text_input)
        text = ""
        a = 0
        while a < 100:
            text = text + "過來留個言吧小鬼頭！"
            a = a + 1
        b = 0
        while b < 20:
            self.input_text(ctl.text_input, text)
            b = b + 1
        self.click_element(ctl.sendView_button, model=name)
        return self

    # 獲取文本長度：輸入框裡的文本長度
    def input_text_len(self):
        time.sleep(3)  # 等待消息傳送
        text_len = len(self.get_text(ctl.text_input))
        return text_len

    # 點擊第一個聊天記錄
    def click_all_tab_list_one(self):
        name = "點擊第一個聊天記錄"
        self.wait_eleVisible(ctl.list_one_name, model=name)
        time.sleep(1)
        self.find_elements(ctl.list_one_name)[0].click()
        if self.is_no_login_popup_cancel() == True:  # 如果有提示弹框则点击【取消】按钮
            self.click_element(ctl.user_chat_no_login_popup_cancel_button)
        return self

    # 点击聊天窗口中输入框
    def click_chat_text_input(self):
        name = "点击聊天窗口中输入框"
        self.wait_eleVisible(ctl.text_input, model=name)
        self.click_element(ctl.text_input, model=name)
        return self

    # 输入文本后，点击【传送】按钮
    def message_input_text_click_send(self, text):
        name = "输入文本后，点击【传送】按钮作"
        self.click_chat_text_input()
        self.input_text(ctl.text_input, text, model=name)
        self.wait_eleVisible(ctl.sendView_button, model=name)
        self.click_element(ctl.sendView_button, model=name)
        time.sleep(3)
        return self

    # 获取最新消息文本
    def get_chat_new_message_text(self):
        time.sleep(3)
        return self.find_elements(ctl.new_message)[-1].text.strip('xxxx00:00')  # 獲取列表中最後一個元素

    # 判断：點擊語音後允許權限按鈕是否存在
    def is_group_chat_authority(self):
        name = "判断：點擊語音後允許權限按鈕是否存在"
        time.sleep(1)
        try:
            self.get_element(ctl.group_chat_authority, model=name)
            return True
        except:
            return False

    # 点击语音icon
    def click_voice_icon(self):
        name = "点击语音icon"
        self.wait_eleVisible_pass(ctl.imagebutton_icon,wait_times=10, model=name)
        self.find_elements(ctl.imagebutton_icon, model=name)[0].click()
        return self

    # 判断：是否为图片详情页
    def if_chat_photo_image_button(self):
        name = '判断：是否为图片详情页'
        self.wait_eleVisible(ctl.chat_photo_done_button,wait_times=10)
        try:
            self.get_element(ctl.chat_photo_image_button, model=name)
            return True           # 图片
        except:
            return False            # 视频

    # 聊天-相册选中一张图片
    def click_chat_one_photo(self):
        self.wait_eleVisible_pass(ctl.chat_photo_video_view)
        el_list = len(self.find_elements(ctl.chat_photo_video_view))
        logging.info("相册中展示了 {} 个媒体文件".format(el_list))
        for i in range(el_list):
            self.find_elements(ctl.chat_photo_video_view)[i].click()    # 顺序依次点击进入详情
            logging.info("点击相册中第 {} 个媒体文件".format(i+1))
            if self.if_chat_photo_image_button() == True:            # 判断为图片
                logging.info("当前文件为图片。。。")
                self.wait_eleVisible_pass(ctl.chat_preview_tv_num)
                self.click_element(ctl.chat_preview_tv_num)             # 点击勾选按钮
                self.wait_eleVisible_pass(ctl.chat_photo_done_button)
                self.click_element(ctl.chat_photo_done_button)          # 点击完成按钮
                break
            else:
                self.return_button()                     # 判断为视频

    # 长按【按住说话】--默认3秒
    def long_press_voice_icon(self):
        name = "长按【按住说话】--默认3秒"
        self.wait_eleVisible(ctl.keep_talking_button, model=name)
        self.long_press_action(ctl.keep_talking_button, model=name)
        return self

    # 短按0.5s
    def short_press_voice_icon(self):
        name = "短按【按住说话】0.5s"
        self.wait_eleVisible(ctl.keep_talking_button, model=name)
        self.click_element(ctl.keep_talking_button, model=name)
        return self

    # 点击：图片放大（进入详情页)
    def click_chat_img(self):
        name = '点击：图片放大（进入详情页)'
        self.wait_eleVisible(ctl.chat_img, model=name)
        self.find_elements(ctl.chat_img, model=name)[-1].click()
        logging.info("点击最新的消息（图片），进行放大")
        return self

    # 判断：是否进入详情
    def if_chat_img_enlarge_download(self):
        name = "判断是否进入图片详情页"
        self.wait_eleVisible_pass(ctl.chat_img_enlarge_download,wait_times=3, poll_frequency=0.5, model=name)
        try:
            self.get_element(ctl.chat_img_enlarge_download, model=name)
            return True
        except:
            return False

    # 查找聊天窗口中新生成語音長度時間值
    def find_chat_new_voice_time(self):
        name = "找聊天窗口中新生成語音長度時間值"
        time.sleep(2)
        voice_time = self.find_elements(ctl.chat_new_voice_time, model=name)[-1].text[0]
        return eval(voice_time)

    # 長按【按住說話】上滑取消
    def cancel_long_press_voice_icon(self):
        name = "長按【按住說話】上滑取消"
        self.wait_eleVisible(ctl.keep_talking_button, model=name)
        self.long_press_action_slide_cancel(ctl.keep_talking_button, model=name)
        return self

    # 查找：取消語音toast提示"取消傳送"
    def get_cancel_voice_toast(self):
        name = "查找：取消語音toast提示'取消傳送'"
        try:
            self.get_toastMsg("取消傳送", model=name)
            return True
        except:
            return False

    # 點擊：圖片icon
    def click_chat_image_icon(self):
        name = "點擊：圖片icon"
        self.wait_eleVisible(ctl.imagebutton_icon, model=name)
        self.find_elements(ctl.imagebutton_icon, model=name)[2].click()
        return self

    # 點擊：拍攝icon
    def click_chat_shoot_icon(self):
        name = "點擊：拍攝icon"
        self.wait_eleVisible(ctl.imagebutton_icon, model=name)
        time.sleep(1)
        self.find_elements(ctl.imagebutton_icon, model=name)[3].click()
        return self

    # 点击：聊天中拍摄-快门
    def click_chat_shutter_button(self):
        name = "点击：聊天中拍摄-快门"
        self.wait_eleVisible(ctl.chat_shutter_button, model=name)
        self.click_element(ctl.chat_shutter_button, model=name)
        return self

    # 长按：聊天中拍视频-长按3秒
    def longpress_chat_shutter_button(self):
        name = "长按：聊天中拍视频-长按3秒"
        self.wait_eleVisible(ctl.chat_shutter_button, model=name)
        self.long_press_action(ctl.chat_shutter_button, model=name)
        return self

    # 点击【传送】按钮（长按快门后）
    def click_chat_shoot_send_button(self):
        name = "点击【传送】按钮（长按快门后）"
        self.wait_eleVisible(ctl.chat_shoot_send_button, model=name)
        self.click_element(ctl.chat_shoot_send_button, model=name)
        return self

    # 查找聊天中视频消息
    def find_chat_news_video(self):
        name = "查找聊天中视频消息"
        time.sleep(3)
        try:
            self.find_elements(ctl.chat_news_video, model=name)
            return True
        except:
            return False

    # 勾選多張圖片
    def click_chat_select_photo_tick(self, amount):  # amount-照片數量
        name = "勾選多張圖片"
        self.wait_eleVisible(ctl.chat_select_photo_tick, model=name)
        for i in range(amount):
            self.find_elements(ctl.chat_select_photo_tick, model=name)[i].click()
            if self.get_tick_video_image_toast() == True:  # 如果有選中視頻則跳出循環
                break
        return self

    # 獲取toast提示：同時選擇視頻和照片
    def get_tick_video_image_toast(self):
        name = "獲取toast提示：同時選擇視頻和照片"
        try:
            self.get_toast_tips("同時選取", model=name)
            return True
        except:
            return False

    # 判断：聊天窗口中是否有图片
    def find_chat_photo(self):
        name = '判断：聊天窗口中是否有图片'
        self.wait_eleVisible_pass(ctl.chat_photo_view, model=name)
        try:
            self.get_element(ctl.chat_photo_view, model=name)
            return True
        except:
            return False

    # 選擇圖片頁，點擊【完成】
    def click_chat_image_done(self):
        name = "選擇圖片頁，點擊【完成】"
        self.wait_eleVisible(ctl.chat_image_done, model=name)
        self.click_element(ctl.chat_image_done, model=name)
        return self

    # 獲取：聊天窗口最新消息的時間
    def get_chat_news_time(self):
        name = "獲取：聊天窗口最新消息的時間"
        self.wait_eleVisible(ctl.chat_news_time, model=name)
        time.sleep(5)
        return self.find_elements(ctl.chat_news_time, model=name)[-1].text

    # 滑屏：聊天記錄下滑
    def swipe_chat_recording(self):
        name = "滑屏：聊天記錄下滑"
        self.wait_eleVisible(ctl.text_input, model=name)
        self.swipe_screen(0.5, 0.3, 0.5, 0.8)
        return self

    # 判断：快速回到底部button是否存在
    def is_chat_recording_back_button(self):
        name = "判断：快速回到底部button是否存在"
        time.sleep(1)
        try:
            self.get_element(ctl.chat_recording_back_button, model=name)
            return True
        except:
            return False

    # 點擊：快速回到底部button
    def click_chat_recording_back_button(self):
        name = "點擊：快速回到底部button"
        self.wait_eleVisible(ctl.chat_recording_back_button, model=name)
        self.click_element(ctl.chat_recording_back_button, model=name)
        return self

    # 點擊：群組聊天窗口下方@icon
    def click_group_chat_at_icon(self):
        name = "點擊：群組聊天窗口下方@icon"
        self.wait_eleVisible(ctl.imagebutton_icon, model=name)
        time.sleep(1)
        self.find_elements(ctl.imagebutton_icon)[-1].click()
        return self

    # 點擊：@功能列表中用戶,再點擊「傳送」按鈕
    def click_at_list_user(self, index):  # "0"代表所有人 ；"1"第一个用户
        name = "點擊：@功能列表中用戶,再點擊「傳送」按鈕"
        self.wait_eleVisible(ctl.group_chat_ar_list, model=name)
        self.find_elements(ctl.group_chat_ar_list)[index].click()
        self.wait_eleVisible(ctl.sendView_button, model=name)
        self.click_element(ctl.sendView_button, model=name)
        return self

    # 判斷：聊天窗口中最新消息中是否包含@效果
    def is_group_chat_message(self):
        name = "判斷：聊天窗口中最新消息中是否包含@效果"
        self.wait_eleVisible(ctl.group_chat_message, model=name)
        time.sleep(1)
        if self.find_elements(ctl.group_chat_message)[-1].text[0] == '@':
            return True
        else:
            return False

    # -----------个人资料页面 -主要使用的Action-----------
    # 判断：个人资料页面用户昵称
    def is_personal_chat_page_user_name(self):
        name = "判断：个人资料页面用户昵称"
        try:
            self.wait_eleVisible(ctl.book_personal_user_name, model=name,wait_times=60)
            return True
        except:
            return False

    # 判断：个人资料页面用户头像
    def is_personal_chat_page_user_avatar(self):
        name = "判断：个人资料页面用户头像"
        try:
            self.wait_eleVisible(ctl.book_personal_user_avatar, model=name,wait_times=60)
            return True
        except:
            return False

    # 点击：个人资料页用户头像
    def click_book_personal_user_avatar(self):
        self.wait_eleVisible(ctl.book_personal_user_avatar)
        self.click_element(ctl.book_personal_user_avatar)
        return self

    # 獲取文本：隸屬部門-部门名称
    def get_book_user_data_section_name(self):
        name = "獲取文本：隸屬部門-部门名称"
        self.wait_eleVisible(ctl.book_user_data_section_name, model=name)
        return self.get_text(ctl.book_user_data_section_name, model=name)

    # 獲取文本：辦公室/場館-办公室名称
    def get_book_user_data_office_name(self):
        name = "獲取文本：辦公室/場館-办公室名称"
        self.wait_eleVisible(ctl.book_user_data_office_name, model=name)
        return self.get_text(ctl.book_user_data_office_name, model=name)

    # 獲取文本：地區:地区名称
    def get_book_user_data_area_name(self):
        name = "獲取文本：地區:地区名称"
        self.wait_eleVisible(ctl.book_user_data_area_name, model=name)
        return self.get_text(ctl.book_user_data_area_name, model=name)

    # 获取文本：部门同事个数
    def get_book_user_data_colleague_itme(self):
        name = "获取文本：部门同事个数"
        self.wait_eleVisible(ctl.book_user_data_colleague_itme, model=name)
        return self.get_text(ctl.book_user_data_colleague_itme)

    # 点击：部门同事
    def click_book_user_data_colleague_itme(self):
        name = "点击：部门同事"
        self.wait_eleVisible(ctl.book_user_data_colleague_itme, model=name)
        self.click_element(ctl.book_user_data_colleague_itme, model=name)
        return self

    # 判斷：部門同事title可見
    def is_colleague_page_title(self):
        name = "判斷：部門同事title可見"
        try:
            self.wait_eleVisible(ctl.colleague_page_title, model=name)
            return True
        except:
            return False

    # 點擊：「設定昵稱和標簽」
    def click_book_user_data_site_name_label(self):
        name = "點擊：「設定昵稱和標簽」"
        self.wait_eleVisible(ctl.book_user_data_site_name_label, model=name)
        self.click_element(ctl.book_user_data_site_name_label, model=name)
        return self

    # 輸入文本：暱稱輸入框，然後點擊「完成」按鈕
    def input_book_user_data_site_name_label_input(self, data):
        name = "輸入文本'{}'，然後點擊「完成」按鈕".format(data)
        self.wait_eleVisible(ctl.book_user_data_site_name_label_input, model=name)
        self.click_element(ctl.book_user_data_site_name_label_input, model=name)  # 點擊輸入框
        self.input_text(ctl.book_user_data_site_name_label_input, data, model=name)  # 輸入文本
        self.click_element(ctl.book_user_data_site_name_label_page_done, model=name)  # 點擊「完成」按鈕
        time.sleep(1)
        return self

    # 獲取文本：輸入框中文本內容
    def get_name_label_input_text(self):
        name = "獲取文本：輸入框中文本內容"
        self.wait_eleVisible(ctl.book_user_data_site_name_label_input, model=name)
        return self.get_text(ctl.book_user_data_site_name_label_input)

    # 點擊:「標註信息」
    def click_colleague_page_more_callout(self):
        name = "點擊:「標註信息」"
        self.wait_eleVisible(ctl.colleague_page_more_callout, model=name)
        self.click_element(ctl.colleague_page_more_callout, model=name)
        return self

    # 點擊：媒體，鏈接和文件
    def click_colleague_page_more_rl_file(self):
        name = "點擊：媒體，鏈接和文件"
        self.wait_eleVisible(ctl.colleague_page_more_rl_file, model=name)
        self.click_element(ctl.colleague_page_more_rl_file, model=name)
        return self

    # 滑屏：個人資料頁面下滑
    def swipe_personal_page(self):
        name = "滑屏：個人資料頁面下滑"
        self.wait_eleVisible(ctl.book_personal_user_name, model=name)
        self.swipe_screen(0.5, 0.8, 0.5, 0.4)
        return self

        # 點擊：共同群組（无滑屏）

    def click_chat_page_common_group_no(self):
        name = "點擊：共同群組"
        self.wait_eleVisible(ctl.book_user_data_common_people, model=name)
        self.click_element(ctl.book_user_data_common_people, model=name)
        return self

    # 點擊：共同群組（有滑屏）
    def click_chat_page_common_group(self):
        name = "點擊：共同群組"
        self.swipe_personal_page()
        self.wait_eleVisible(ctl.book_user_data_common_people, model=name)
        self.click_element(ctl.book_user_data_common_people, model=name)
        return self

    # 判断：共同群组页面是否含有数据
    def is_chat_page_common_group_data(self):
        name = "判断：共同群组页面是否含有数据"
        try:
            self.wait_eleVisible(ctl.book_user_data_people_page_list, model=name)
            return True
        except:
            return False

    # 獲取文本：「靜音」開關狀態
    def get_personal_page_mute_switch_text(self):
        name = "獲取文本：「靜音」開關狀態"
        self.wait_eleVisible(ctl.personal_page_mute_switch, model=name)
        return self.get_text(ctl.personal_page_mute_switch)

    # 點擊：「靜音」開關狀態文本
    def click_personal_page_mute_switch(self):
        name = "點擊：「靜音」開關狀態文本"
        self.wait_eleVisible(ctl.personal_page_mute_switch, model=name)
        self.click_element(ctl.personal_page_mute_switch)
        return

    # 獲取文本：「聊天訊息置頂」開關狀態
    def get_personal_page_chat_sticky_text(self):
        name = "獲取文本：「聊天訊息置頂」開關狀態"
        self.wait_eleVisible(ctl.personal_page_mute_switch, model=name)
        return self.find_elements(ctl.personal_page_mute_switch)[1].text

    # 點擊：「聊天訊息置頂」開關狀態文本
    def click_personal_page_chat_sticky(self):
        name = "點擊：「聊天訊息置頂」開關狀態文本"
        self.wait_eleVisible(ctl.personal_page_mute_switch, model=name)
        self.find_elements(ctl.personal_page_mute_switch)[1].click()
        return

    # 點擊：「查找聊天內容」
    def click_personal_page_find_chat_text(self):
        name = "點擊：「查找聊天內容」"
        self.wait_eleVisible(ctl.personal_page_find_chat_text, model=name)
        self.click_element(ctl.personal_page_find_chat_text, model=name)
        return self

    # 輸入文本：聊天搜索欄
    def input_text_personal_page_find_search_input(self, text):
        name = "輸入文本：聊天搜索欄"
        self.wait_eleVisible(ctl.personal_page_find_search_input, model=name)
        self.click_element(ctl.personal_page_find_search_input, model=name)
        self.input_text(ctl.personal_page_find_search_input, text, model=name)
        return self

    # 判斷：是否有搜索結果
    def is_personal_page_find_search_result(self):
        name = "判斷：是否有搜索結果"
        try:
            self.wait_eleVisible(ctl.personal_page_find_search_result, model=name)
            return True
        except:
            return False

    # 獲取：搜索結果文本
    def find_personal_page_find_search_result(self):
        name = "獲取：搜索結果文本"
        self.wait_eleVisible(ctl.personal_page_find_search_result, model=name)
        data = self.get_text(ctl.personal_page_find_search_result, model=name)
        search_result_data = re.split('<|>', data)[2]
        return str(search_result_data)

    # -----------【通訊錄】-主要使用的Action-----------

    # 點擊【通訊錄】tab
    def click_address_book_tab(self):
        name = "點擊【通訊錄】tab"
        self.wait_eleVisible(ctl.address_book_tab, model=name)
        self.click_element(ctl.address_book_tab, model=name)
        return self

    # 清除文本操作
    def delete_inpute_text(self):
        self.driver.press_keycode("67")
        return self

    # 點擊輸入框後輸入文本後，觸發搜索
    def input_book_text_search(self):
        name = "點擊輸入框後輸入文本後，觸發搜索"
        self.wait_eleVisible(ctl.book_area, model=name)
        self.click_element(ctl.book_search_input, model=name)  # 點擊輸入框
        self.adb_keycode(31)
        self.keyboard_search(model=name)  # 觸發搜索
        return self

    # 獲取搜索結果個數
    def get_book_count_item(self):
        name = "獲取搜索結果個數"
        self.wait_eleVisible(ctl.book_search_count_item, model=name)
        text = self.get_text(ctl.book_search_count_item)  # 獲取文本
        return eval(re.split("共|個", text)[1])  # 切割獲取數據，得到int類型

    # 獲取第一行用戶的暱稱
    def get_book_search_one_name(self):
        name = "獲取第一行用戶的暱稱"
        self.wait_eleVisible(ctl.book_user_name, model=name)
        return self.find_elements(ctl.book_user_name)[0].text

    # 获取文本：通讯录tab中筛选按钮数量
    def get_book_filter_icon_amount(self):
        name = "获取文本：通讯录tab中筛选按钮数量"
        self.wait_eleVisible(ctl.book_area, model=name)  # 等待筛选结果加载成功
        return self.get_text(ctl.book_filter_icon, model=name)

    # 点击；筛选icon(有筛选条件时)
    def click_book_filter_icon(self):
        name = "点击；通讯录tab中筛选icon"
        self.wait_eleVisible(ctl.book_filter_result, model=name)  # 等待列表地区数据加载完之后再点击筛选icon操作
        self.click_element(ctl.book_filter_icon, model=name)
        return self

    # 点击：筛选icon(没有筛选条件时)
    def click_book_not_filter_icon(self):
        name = "点击；通讯录tab中筛选icon"
        self.wait_eleVisible(ctl.book_area, model=name)  # 等待列表地区数据加载完之后再点击筛选icon操作
        self.click_element(ctl.book_filter_icon, model=name)
        return self

    # 点击：筛选页面第一个地区
    def click_filter_page_one_row(self):
        name = "点击：筛选页面第一个地区"
        self.wait_eleVisible(ctl.book_filter_page_one, model=name)
        self.click_element(ctl.book_filter_page_one, model=name)
        return self

    # 勾选按钮可见
    def is_selected_icon_elevisible(self):
        name = "勾选按钮可见"
        time.sleep(2)
        try:
            self.get_element(ctl.book_filter_select_icon, model=name)
            return True
        except:
            return False

    # 点击：【完成】按钮
    def click_book_filter_done_button(self):
        name = "点击：【完成】按钮"
        self.wait_eleVisible(ctl.book_filter_done_button, model=name)
        self.click_element(ctl.book_filter_done_button, model=name)
        return self

    # 获取文本：筛选结果数量(int类型)
    def get_book_filter_result(self):
        name = "获取文本：筛选结果数量(int类型)"
        self.wait_eleVisible(ctl.book_filter_result, model=name)
        text = self.get_text(ctl.book_filter_result)
        return eval(re.split("共|個", text)[1])

    # 点击：筛选弹框【编辑筛选】按钮,點擊[全部清除]
    def click_book_filter_popup_edit(self):
        name = "点击：筛选弹框【编辑筛选】按钮,點擊[全部清除]，點擊第一行"
        self.wait_eleVisible(ctl.book_filter_popup_edit, model=name)
        self.click_element(ctl.book_filter_popup_edit, model=name)
        self.wait_eleVisible(ctl.book_filter_allcleal_button, model=name)
        self.click_element(ctl.book_filter_allcleal_button, model=name)
        return self

    # 判斷地區列表是否有展開，（以用戶可見為依據）
    def if_allexpend(self):
        name = "判斷地區列表是否有展開，（以用戶可見為依據）"
        self.wait_eleVisible_pass(ctl.book_area, model=name)  # 等待第一個地區下拉可見
        try:
            self.get_element(ctl.book_user_name, model=name)  # 查找用戶名稱是否可見
            return True
        except:
            return False

    # 获取用户昵称
    def get_book_list_user_name(self,number):
        if self.if_allexpend() == False:
            self.click_allexpend_button()
        self.wait_eleVisible(ctl.book_list_user_name)
        user_name = self.find_elements(ctl.book_list_user_name)[number].text
        logging.info("獲取第{}個用戶的暱稱為'{}'".format(number+1,user_name))
        return user_name

    # 點擊：列表第一個用戶
    def click_book_list_user_name(self,number):
        self.wait_eleVisible(ctl.book_list_user_name)
        self.find_elements(ctl.book_list_user_name)[number].click()
        return self

    # 點擊：「全部展開」按鈕
    def click_allexpend_button(self):
        name = "點擊：「全部展開」按鈕"
        self.wait_eleVisible(ctl.book_allexpend_button, model=name)
        self.click_element(ctl.book_allexpend_button, model=name)
        return self

    # 點擊：通訊錄tab第一個下拉列表
    def click_area_one_drop_list(self):
        name = "點擊：通訊錄tab第一個下拉列表"
        if self.if_allexpend() == False:
            self.wait_eleVisible(ctl.book_area, model=name)
            self.click_element(ctl.book_area, model=name)
        return self

    # 滑屏：通訊錄滑屏
    def book_user_swipe(self):
        self.wait_eleVisible(ctl.book_user_name)
        self.swipe_screen(0.5, 0.8, 0.5, 0.5)
        return self

    # 点击：通讯录字母快速导航-W
    def click_book_navigation_W(self):
        self.wait_eleVisible(ctl.book_indexsidebar)
        #self.tap_click_ele(0.95, 0.70)   #正式環境
        self.tap_click_ele(0.966, 0.73)  #本地環境 by jinwei
        time.sleep(1)
        return self

    # 獲取：通訊錄列表中-首字母文本
    def get_book_navigation_letter_text(self):
        self.wait_eleVisible(ctl.book_navigation_letter)
        return self.find_elements(ctl.book_navigation_letter)[0].text

    # 滑屏：通讯录tab上滑至搜索框可见
    def swipe_above(self):
        self.swipe_screen(0.5, 0.3, 0.5, 0.8)
        time.sleep(1)
        return self

    # 查找:用戶暱稱
    def is_find_user_name(self):
        name = "查找:用戶暱稱"
        time.sleep(1)
        try:
            self.get_element(ctl.book_user_name, model=name)
            return True
        except:
            return False

    # 查找:用戶頭像
    def is_find_user_avatar(self):
        name = "查找:用戶頭像"
        time.sleep(1)
        try:
            self.get_element(ctl.book_user_avatar, model=name)
            return True
        except:
            return False

    # 点击：通讯录列表中有头像的用户
    def click_book_user_avatar(self):
        name = "点击：通讯录列表中有头像的用户"
        self.click_area_one_drop_list()
        self.wait_eleVisible(ctl.book_user_avatar, model=name)
        self.click_element(ctl.book_user_avatar, model=name)
        return self

    # 判斷：资料页邮箱是否有郵箱
    def is_user_data_mail(self):
        name = "判斷：资料页邮箱是否有郵箱"
        self.wait_eleVisible(ctl.book_user_data_email, model=name)
        rmail_text = self.get_text(ctl.book_user_data_email, model=name)
        if len(rmail_text) > 0:
            return True
        else:
            return False

    # 進入到有郵箱的詳情頁
    def enter_user_is_email(self):
        name = "進入到有郵箱的詳情頁"
        a = 0
        while 1 > 0:
            self.wait_eleVisible(ctl.book_user_name, model=name)
            time.sleep(1)
            self.find_elements(ctl.book_user_name)[a].click()
            if self.is_user_data_mail() == True:
                break
            else:
                a = a + 1
                self.return_button()

    # 點擊：郵箱
    def click_book_user_data_email(self):
        name = "點擊：郵箱"
        self.wait_eleVisible(ctl.book_user_data_email, model=name)
        self.click_element(ctl.book_user_data_email, model=name)
        return self

    # 点击：邮件下拉-复制
    def click_email_list_copy(self):
        name = "点击：邮件下拉-复制"
        self.wait_eleVisible(ctl.book_user_data_email_list_option, model=name)
        self.click_element(ctl.book_user_data_email_list_option, model=name)
        return self

    # 判斷：通訊錄列表是否加載完成
    def is_ele_visible(self):
        name = "判斷：通訊錄列表是否加載完成"
        self.wait_eleVisible_pass(ctl.book_user_name, model=name)
        try:
            self.get_element(ctl.book_user_name, model=name)
            return True
        except:
            return False

    # 判断：聊天窗口用户未上线提示弹框
    def is_no_login_popup_cancel(self):
        name = "判断：聊天窗口用户未上线提示弹框"
        time.sleep(2)
        try:
            self.get_element(ctl.user_chat_no_login_popup_cancel_button, model=name)
            return True
        except:
            return False

    # 點擊：随机点击地區中的用戶
    def click_area_one_user(self):
        name = "點擊：地區中的用戶"
        if self.is_ele_visible() == False:
            self.click_area_one_drop_list()
        self.wait_eleVisible(ctl.book_user_name, model=name)
        time.sleep(1)
        user_number = len(self.find_elements(ctl.book_user_list))
        random_number = random.randint(0, user_number - 1)
        logging.info("點擊列表中第{}個用戶".format(random_number + 1))
        self.find_elements(ctl.book_user_list)[random_number].click()
        if self.is_no_login_popup_cancel() == True:  # 如果有提示弹框则点击【取消】按钮
            self.click_element(ctl.user_chat_no_login_popup_cancel_button)
        return self

    # 查找：复制邮箱toast"已經複製到剪切板"
    def is_find_email_copy_toast(self):
        try:
            self.get_toast_tips("已經複製到剪切板")
            return True
        except:
            return False

    # 查找：资料页【隸屬部門】
    def is_find_book_user_data_section(self):
        name = "查找：资料页【隸屬部門】"
        self.wait_eleVisible(ctl.book_user_data_email, model=name)
        try:
            self.get_element(ctl.book_user_data_section, model=name)
            return True
        except:
            return False

    # 查找：资料页【辦公室/場館】
    def is_find_book_user_data_office(self):
        name = "查找：资料页【辦公室/場館】"
        self.wait_eleVisible(ctl.book_user_data_email, model=name)
        try:
            self.get_element(ctl.book_user_data_office, model=name)
            return True
        except:
            return False

    # 查找：资料页【地區*】
    def is_find_book_user_data_area(self):
        name = "查找：资料页【地區*】"
        self.wait_eleVisible(ctl.book_user_data_email, model=name)
        try:
            self.get_element(ctl.book_user_data_area, model=name)
            return True
        except:
            return False

    # 查找：资料页【部門同事】
    def is_find_book_user_data_colleague(self):
        name = "查找：资料页【部門同事】"
        self.wait_eleVisible(ctl.book_user_data_email, model=name)
        try:
            self.get_element(ctl.book_user_data_colleague, model=name)
            return True
        except:
            return False

    # 点击：资料页【共同群组】
    def click_book_user_data_common_people(self):
        name = "点击：资料页【共同群组】"
        self.wait_eleVisible(ctl.book_personal_user_name, model=name)
        self.swipe_screen(0.5, 0.8, 0.5, 0.2)
        self.click_element(ctl.book_user_data_common_people, model=name)
        return self

    # 查找：【共同群组】页面title
    def is_book_user_data_people_page_titl(self):
        name = "查找：【共同群组】页面title"
        self.wait_ele_visible_pass(ctl.book_user_data_people_page_titl, model=name)
        try:
            self.get_element(ctl.book_user_data_people_page_titl, model=name)
            return True
        except:
            return False

    # 查找：【共同群组】页面群组个数
    def get_common_people_itme(self):
        name = "查找：【共同群组】页面群组个数"
        self.wait_ele_visible_pass(ctl.book_user_data_people_page_list, model=name)  # 有群组返回个数
        try:
            self.get_element(ctl.book_user_data_people_page_list, model=name)
            return len(self.find_elements(ctl.book_user_data_people_page_list))
        except:
            return 0  # 没有则返回0

    # 点击：资料页【傳送訊息】
    def click_book_user_data_sendmessag(self):
        name = "点击：资料页【傳送訊息】"
        self.wait_eleVisible(ctl.book_personal_user_name, model=name)
        self.swipe_screen(0.5, 0.8, 0.5, 0.2)
        self.click_element(ctl.book_user_data_sendmessag, model=name)
        if self.is_no_login_popup_cancel() == True:  # 如果有提示弹框则点击【取消】按钮
            self.click_element(ctl.user_chat_no_login_popup_cancel_button)
        return self

    # 判断：是否是個人聊天界面
    def is_book_user_data_sendmessag_page(self):
        name = "判断：是否是個人聊天界面"
        try:
            self.wait_eleVisible(ctl.book_user_data_sendmessag_input, model=name)
            return True
        except:
            return False

    # 判斷，是否獲取toast提示"聯繫人已加入該群組"
    def is_Invite_group_toast(self):
        try:
            self.get_toast_tips("聯繫人已加入該群組")
            return True
        except:
            return False

    # 邀請加入群組成功最終結果
    def is_return_invite(self):
        if self.is_Invite_group_toast() == False:
            if self.is_book_user_data_people_page_titl() == False:
                return False
        return True

    # 點擊：邀請群組（需要滑屏）
    def click_book_user_data_Invite_group(self):
        name = "點擊：邀請群組（需要滑屏）"
        self.wait_eleVisible(ctl.book_personal_user_name, model=name)
        self.swipe_screen(0.5, 0.8, 0.5, 0.2)
        self.click_element(ctl.book_user_data_Invite_group, model=name)
        return self

    # 點擊：群組列表頁-點擊一個群組
    def click_Invite_group_page_one(self):
        name = "點擊：群組列表頁-點擊一個群組"
        self.wait_eleVisible(ctl.book_Invite_group_page_list, model=name)
        self.find_elements(ctl.book_Invite_group_page_list)[0].click()
        return self

    # -----------【更多】tab-主要使用的Action-----------
    # 点击：更多tab
    def click_more_tab(self):
        name = "点击：更多tab"
        self.wait_eleVisible(ctl.more_tab, model=name)
        self.click_element(ctl.more_tab, model=name)
        return self

    # 判断：是否有展示用户信息栏
    def is_more_tab_user(self):
        name = "判断：是否有展示用户信息栏"
        try:
            self.wait_eleVisible(ctl.more_user_name, model=name)
            return True
        except:
            return False

    # 获取文本：更多tab-用户昵称
    def get_more_tab_user_name(self):
        name = "取文本：更多tab-用户昵称"
        self.wait_eleVisible(ctl.more_user_name, model=name)
        return self.get_text(ctl.more_user_name, model=name)

    # 点击：用户信息跳转icon
    def click_more_user_jump_icon(self):
        name = "点击：用户信息跳转icon"
        self.wait_eleVisible(ctl.more_user_jump_icon, model=name)
        self.click_element(ctl.more_user_jump_icon, model=name)
        return self

    # 判断：是否有跳转至用户信息页
    def is_user_data(self):
        name = "判断：是否有跳转至用户信息页"
        try:
            self.wait_eleVisible(ctl.more_user_jump_phone_icon, model=name)
            return True
        except:
            return False

    # 創建標註信息
    def create_callout(self):
        name = "創建標註信息"
        self.click_chat_text_input()  # 点击输入框
        self.message_input_text_click_send("这是一条发起的标注信息")  # 输入文本，点击传送按钮
        self.long_press_chat_message(ctl.chat_window_message_box, model=name)  # 长按2s聊天窗口中最新消息
        time.sleep(1)
        self.wait_eleVisible(ctl.chat_window_callout_img, model=name)
        self.click_element(ctl.chat_window_callout_img, model=name)  # 点击：标注icon
        return self

    # 點擊：所有標註信息
    def click_more_callout(self):
        name = "點擊：所有標註信息"
        self.wait_eleVisible(ctl.more_callout, model=name)
        self.click_element(ctl.more_callout, model=name)
        return self

    # 點擊：「標註信息」頁面一行標註跳轉icon
    def click_more_callout_page_jump_icon(self):
        name = "點擊：「標註信息」頁面一行標註跳轉icon"
        self.wait_eleVisible(ctl.more_callout_page_jump_icon, model=name)
        self.click_element(ctl.more_callout_page_jump_icon, model=name)
        if self.is_no_login_popup_cancel() == True:  # 如果有提示弹框则点击【取消】按钮
            self.click_element(ctl.user_chat_no_login_popup_cancel_button)
        return self

    # 判斷：是否存在標註☆圖標
    def is_more_callout_star(self):
        name = "判斷：是否存在標註☆圖標"
        self.wait_eleVisible(ctl.more_chat_interface_user_avatar, model=name)
        try:
            self.get_element(ctl.more_callout_star, model=name)
            return True
        except:
            return False

    # 點擊：「所有媒體、連結和文件」
    def click_more_rl_file(self):
        name = "點擊：「所有媒體、連結和文件」"
        self.wait_eleVisible(ctl.more_rl_file, model=name)
        self.click_element(ctl.more_rl_file, model=name)
        return self

    # 判斷：媒體tab是否展示圖片或視頻
    def is_more_rl_file_media_tab_list(self):
        name = "判斷：媒體tab是否展示圖片或視頻"
        self.wait_eleVisible(ctl.more_rl_file_tab_list_time, model=name)
        try:
            self.get_element(ctl.more_rl_file_media_tab_list, model=name)
            return True
        except:
            return False

    # 長按並點擊：頂部sunpeople-觸發sos彈框,點擊「確定」按鈕
    def long_press_sunpeople(self):
        name = "長按並點擊：頂部sunpeople-觸發sos彈框,點擊「確定」按鈕"
        self.wait_eleVisible(ctl.sunpeople_title, model=name)
        self.long_press_action(ctl.sunpeople_title, model=name)
        self.wait_eleVisible(ctl.more_sos_popup, model=name)
        self.click_element(ctl.more_sos_popup, model=name)
        return self

    # 點擊：連接tab
    def click_more_rl_link_tab(self):
        name = "點擊：連接tab"
        self.wait_eleVisible(ctl.more_rl_file_media_tab, model=name)
        self.find_elements(ctl.more_rl_file_media_tab)[1].click()
        return self

    # 判斷：連接tab是否展示連接
    def is_more_rl_file_link_tab_list(self):
        name = "判斷：連接tab是否展示連接"
        self.wait_eleVisible(ctl.more_rl_file_tab_list_time, model=name)
        try:
            self.get_element(ctl.more_rl_file_link_tab_list, model=name)
            return True
        except:
            return False

    # 點擊：「文件」tab
    def click_more_rl_file_tab(self):
        name = "點擊：「文件」tab"
        self.wait_eleVisible(ctl.more_rl_file_media_tab, model=name)
        self.find_elements(ctl.more_rl_file_media_tab)[2].click()
        return self

    # 判斷：文件tab中是否含有文件
    def is_more_rl_file_file_tab_list(self):
        name = "判斷：文件tab中是否含有文件"
        try:
            self.wait_eleVisible(ctl.more_rl_file_file_tab_list, model=name)
            return True
        except:
            return False

    # 點擊：【有提到你的對話】
    def click_more_rl_at(self):
        name = "點擊：【有提到你的對話】"
        self.wait_eleVisible(ctl.more_rl_at, model=name)
        self.click_element(ctl.more_rl_at, model=name)
        return self

    # 點擊：@對話跳轉icon
    def click_moar_at_list_jump_icon(self):
        name = "點擊：@對話跳轉icon"
        self.wait_eleVisible(ctl.moar_at_list_jump_icon, model=name)
        self.click_element(ctl.moar_at_list_jump_icon, model=name)
        return self

    # 檢查：界面中文本列消失是否含有@
    def is_at_jump_chat_an_atuser(self):
        name = "檢查：界面中文本列消失是否含有@"
        self.wait_eleVisible(ctl.moar_at_jump_chat_list, model=name)  # 等待頁面加載可見
        at_list = self.find_elements(ctl.moar_at_jump_chat_list)
        # 遍历
        a = ""
        for i in range(len(at_list)):
            if at_list[i].text[0] == "@":
                a = True
                break
            else:
                a = False
        return a

    # 获取文本：耳筒模式开关状态
    def get_more_headphone_mode_text(self):
        name = "获取文本：耳筒模式开关状态"
        self.wait_eleVisible(ctl.more_headphone_mode, model=name)
        return self.get_text(ctl.more_headphone_mode, model=name)

    # 點擊：耳筒模式開關
    def click_more_headphone_mode(self):
        name = "點擊：耳筒模式開關"
        self.wait_eleVisible(ctl.more_headphone_mode, model=name)
        self.click_element(ctl.more_headphone_mode, model=name)
        return self

    # 點擊：更多tab「字體大小」
    def click_more_more_setup_font_size(self):
        name = "點擊：更多tab「字體大小」"
        self.wait_eleVisible(ctl.more_setup_font_size, model=name)
        self.click_element(ctl.more_setup_font_size, model=name)
        return self

    # 點擊：设置默认字体大小
    def click_setup_font_size_default(self):
        name = "點擊：设置默认字体大小"
        self.wait_eleVisible(ctl.more_setup_page_seekbar, model=name)
        self.tap_click_ele(0.33, 0.94)
        return self

    # 點擊：设置最大字体
    def click_setup_font_size_max(self):
        name = "點擊：设置最大字体"
        self.wait_eleVisible(ctl.more_setup_page_seekbar, model=name)
        self.tap_click_ele(0.96, 0.94)
        return self

    # 獲取元素控件高：「設定字體大小」頁面-文案"選擇下面的形。。。"框大小
    def get_ele_size_height(self):
        name = "獲取元素控件高：「設定字體大小」頁面-文案'選擇下面的形。。。'框大小"
        self.wait_eleVisible(ctl.more_setup_page_copywrting, model=name)
        size_list = self.get_element(ctl.more_setup_page_copywrting).size  # 获取元素的宽和高，字典格式返回
        return size_list["height"]  # 返回值为int类型

    # 获取视频播放播放图案宽的大小
    def get_chat_video_size(self):
        self.wait_eleVisible(ctl.chat_news_video)
        el = self.find_elements(ctl.chat_news_video)[-1]    # 得到最新的消息元素
        video_size = el.size["height"]
        logging.info("获取最新视频播放图案的高为：{}".format(video_size))
        return video_size   # 高

    # 點擊："設定字體大小"頁面-「完成」按鈕
    def click_more_setup_done_button(self):
        name = "點擊：設定字體大小頁面-「完成」按鈕"
        self.wait_eleVisible(ctl.more_setup_done_button, model=name)
        self.click_element(ctl.more_setup_done_button, model=name)
        return self

    # 获取：获取用户名称
    def get_user_nickname(self):
        name = "获取：获取用户名称"
        self.wait_eleVisible(ctl.book_personal_user_name, model=name)
        return self.get_text(ctl.book_personal_user_name, model=name)

    # 獲取相冊中照片數量
    def get_photo_Check_button_number(self):
        self.wait_eleVisible_pass(ctl.chat_select_photo_tick)
        return len(self.find_elements(ctl.chat_select_photo_tick))

    # 拍攝10張照片
    def action_number_phtot(self):
        self.click_chat_shoot_icon()            # 點擊拍攝icon
        time.sleep(1)
        number = 1
        while number <=10:
            self.wait_eleVisible_pass(ctl.chat_shutter_button)
            self.click_element(ctl.chat_shutter_button)
            self.wait_eleVisible_pass(ctl.media_cancel_button)
            self.click_element(ctl.media_cancel_button)         # 點擊「重做」按鈕
            time.sleep(1)
            number = number + 1
        self.return_button()
        self.return_button()

    # 判断相册有无10张图片，没有则拍摄10张
    def if_get_photo_Check_button_number(self):
        self.click_chat_tab()                                   # 点击【聊天】tab
        self.click_message_tab()                                # 点击【讯息】tab
        self.click_drop_down_list_button()                      # 点击【独立讯息】中第一行讯息-下拉按钮
        self.click_chat_image_icon()                            # 聊天窗口中，點擊：圖片icon
        photo_number = self.get_photo_Check_button_number()     # 获取相册中的照片数量
        time.sleep(1)
        self.return_button()
        time.sleep(1)
        if photo_number < 10:    # 如果照片小于10张
            self.action_number_phtot()              # 拍摄10张图片
        return self