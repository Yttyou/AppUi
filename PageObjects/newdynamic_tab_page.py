__author__ = 'developer'

# coding=utf-8
# 【最新动态】页各操作
import re
import logging
from Common.BasePage import BasePage
from PageLocators.newdynamic_tab_locator import NewdynamicTabLocator as ntl
from TestDatas.COMMON_DATA import keycode
import datetime
import time
import math


class NewDynamicTabPage(BasePage):

    # 【返回】物理按键（一步）
    def return_button_one(self):
        self.return_button()
        return self

    # 点击【最新动态】tab
    def click_newdynamic(self):
        name = "点击【最新动态】tab"
        self.wait_eleVisible(ntl.Newdynamic_tab, model=name)
        self.click_element(ntl.Newdynamic_tab, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 查找【最新动态】tab,True--找到，False--未找到
    def find_newdynamic_tab(self):
        name = "查找【最新动态】tab"
        self.wait_eleVisible(ntl.Newdynamic_tab, wait_times=10, model=name)
        try:
            self.get_element(ntl.Newdynamic_tab, model=name)
            return True
        except:
            return False

    # --------------------------- 【全部】相关元素操作  ------------------------------------------------

    # 发帖中加载load
    def wait_fend_post_loading_icon(self):
        name = '发帖中加载load'
        time.sleep(1)
        self.wait_element_vanish(ntl.send_post_cancel, model=name)
        return self

    # 点击【全部】tab
    def click_all_tab(self):
        name = "查找【全部】tab"
        self.wait_eleVisible(ntl.all_tab, model=name)
        self.click_element(ntl.all_tab, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 获取【全部】tab下第一个帖子用户昵称
    def get_all_tab_user_name(self):
        self.wait_eleVisible(ntl.all_tab_user_name)
        return self.get_text(ntl.all_tab_user_name).strip()

    # 查找：全部tab中数据是否展示
    def find_all_tab_user_name(self):
        name = "查找：全部tab中数据是否展示"
        self.wait_eleVisible_pass(ntl.all_tab_user_name, wait_times=6, poll_frequency=0.5)
        try:
            self.get_element(ntl.all_tab_user_name, model=name)
            return True
        except:
            return False

    # 點擊：帖子列表用户头像
    def click_all_tab_post_user_avatar(self):
        self.wait_eleVisible(ntl.all_tab_post_user_avatar)
        self.click_element(ntl.all_tab_post_user_avatar)
        time.sleep(2)
        self.wait_qroup_loading_icon()
        return self

    # 獲取：群組或用戶主頁用戶暱稱
    def get_group_or_user_homepage_name(self):
        name = "獲取：群組主頁用戶暱稱"
        if self.if_group_home_page_quit_button() == True:           # 判斷是否進入群組主頁
            return self.get_text(ntl.group_page_group_title, model=name)    # 返回群組名稱
        else:
            user_name = self.get_text(ntl.user_homepage_name)
            return user_name.split('| ')[-1]                        # 返回用戶主頁暱稱

    # 判斷：是否是群組主頁
    def if_group_home_page_quit_button(self):
        time.sleep(3)
        try:
            self.get_element(ntl.group_home_page_quit_button)
            return True
        except:
            return False

    # 點擊：[你在想什麼?]入口
    def click_all_tab_post_entrance(self):
        name = '點擊：[你在想什麼?]入口'
        self.wait_eleVisible(ntl.all_tab_post_entrance, model=name)
        self.click_element(ntl.all_tab_post_entrance, model=name)
        return self

    # 點擊：全部tab-拍照icon
    def click_all_tab_photo_icon(self):
        name = '點擊：全部tab-拍照icon'
        self.wait_eleVisible(ntl.all_tab_photo_icon, model=name)
        self.click_element(ntl.all_tab_photo_icon, model=name)
        return self

    # 獲取文本：全部tab第一個帖子文本
    def get_all_tab_post_text(self):
        name = "獲取文本：全部tab第一個帖子文本"
        self.wait_eleVisible(ntl.personal_tab_post_text, model=name)
        return self.get_text(ntl.personal_tab_post_text, model=name).strip()

    # 點擊：全部tab中-帖子文本
    def click_all_tab_post_text(self):
        name = "點擊：全部tab中-帖子文本"
        self.wait_eleVisible(ntl.all_tab_post_text, model=name)
        self.click_element(ntl.all_tab_post_text, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 查找：帖子詳情-分享icon
    def find_post_page_share_icon(self):
        name = '查找：帖子詳情-分享icon'
        time.sleep(1)
        try:
            self.get_element(ntl.post_page_share_icon, model=name)
            return True
        except:
            return False

    # 获取文本：帖子详情页点击次数
    def get_post_detail_like_count_icon(self):
        if self.find_post_detail_like_count_icon() == True:         # 判断点赞计数icon是否可见
            data = self.get_text(ntl.post_detail_like_count_icon)
            like_number = int(data.split(' ',2)[1])
        else:
            like_number = 0                     # 不可见返回0次
        return like_number

    # 查找：帖子詳情-点击计数icon
    def find_post_detail_like_count_icon(self):
        self.wait_eleVisible(ntl.post_like_icon)
        try:
            self.get_element(ntl.post_detail_like_count_icon)
            return True
        except:
            return False

    # 點擊： 帖子詳情-分享icon
    def click_post_page_share_icon(self):
        name = '點擊： 帖子詳情-分享icon'
        if self.find_post_page_share_icon() == False:
            self.swipe_screen(0.5,0.8,0.5,0.6, model=name)
            time.sleep(1)
        self.wait_eleVisible(ntl.post_page_share_icon, model=name)
        self.click_element(ntl.post_page_share_icon, model=name)
        return self

    # 全部tab中，点击第一个动态下留言计数按钮
    def click_one_message_count(self):
        name = "全部tab中，点击第一个动态下留言计数按钮"
        # 等待数据加载完成
        while self.is_find_comment() == False:  # 屏幕中是否有展示留言计数，没有则滑屏为可见
            self.swipe_screen(0.5, 0.6, 0.5, 0.3, model=name)
        self.find_elements(ntl.message_count, model=name)[0].click()  # 查找到多个留言按钮，点击第一个动态留言
        self.wait_qroup_loading_icon()
        return self

    # 查找动态信息里的留言输入框
    def is_find_message_input(self):
        name = "查找动态信息里的留言输入框"
        try:
            self.wait_eleVisible(ntl.message_input, wait_times=15, model=name)
            self.get_element(ntl.message_input, model=name)
            return True  # 找到
        except:
            return False  # 未找到

    # 贴子中-输入留言并点击【发布】
    def send_messag_text(self, text):
        name = "贴子中-输入留言并点击【发布】"
        self.wait_eleVisible(ntl.message_input, model=name)  # 等待
        self.input_text(ntl.message_input, text, model=name)  # 输入文本，messag_text传string
        self.click_element(ntl.send_button, model=name)  # 点击发布按钮
        return self

    # 多次留言
    def double_send_messag_text(self,send_number,text):
        name = '{}次留言'.format(send_number)
        self.wait_eleVisible(ntl.message_input, model=name)  # 等待
        a = 1
        while a <= send_number:
            self.input_text(ntl.message_input, text, model=name)        # 输入文本，messag_text传string
            logging.info("第{}次留言".format(a))
            name = "点击【發布】按鈕"
            time.sleep(1)
            self.wait_eleVisible(ntl.send_button, model=name)
            self.click_element(ntl.send_button, model=name)             # 点击发布按钮
            a = a + 1
            self.wait_qroup_loading_icon()
        return self

    # 动态列表中--获取留言次数
    def get_message_time(self):
        name = "动态列表中--获取留言次数"
        if self.is_find_comment() == False:  # 屏幕中是否有展示留言计数，没有则滑屏为可见
            self.swipe_screen(0.5, 0.8, 0.5, 0.4)
        # 获取属性文本
        self.wait_eleVisible(ntl.message_count, model=name)
        list = self.get_text(ntl.message_count, model=name)  # 获取text文本
        message_time = eval(list.split()[0])  # 切换字符串获取点击次数
        return message_time

    # 动态详情页中--获取留言次数
    def get_message_details_time(self):
        name = "动态详情页中--获取留言次数"
        # 获取属性文本
        while self.is_find_comment_reply() == False:
            self.swipe_screen(0.5, 0.8, 0.5, 0.4)
        self.wait_eleVisible(ntl.message_count, model=name)
        list = self.get_text(ntl.message_count, model=name)  # 获取text文本
        message_time = eval(list.split()[0])  # 切换字符串获取点击次数
        return message_time

    # 帖子详情页点赞
    def click_like_button(self):
        name = "点赞"
        self.wait_eleVisible(ntl.post_page_like_icon, model=name)
        self.click_element(ntl.post_page_like_icon, model=name)  # 点击【点赞】icon
        return self

    # 动态评论中-回复(默认第一个回复按钮)
    def send_comment_reply(self, text):
        name = "动态评论中-回复"
        self.wait_eleVisible(ntl.comment_reply, model=name)
        self.click_element(ntl.comment_reply, model=name)
        self.input_text(ntl.message_input, text, model=name)
        self.click_element(ntl.send_button, model=name)
        return self

    # 点击动态详情页-返回按钮
    def click_message_details_retun_button(self):
        name = "动态详情页-返回按钮"
        self.wait_eleVisible(ntl.message_details_retun_button, model=name)
        self.click_element(ntl.message_details_retun_button, model=name)
        return self

    # 列表中动态下方留言在当前屏幕可见，True-可见，False-不可见
    def is_find_comment(self):
        name = "动态下方留言icon可见"
        time.sleep(2)
        try:
            self.get_element(ntl.message_count, model=name)
            return True
        except:
            return False

    # 动态详情页中-第一个评论中回复按钮是否可见
    def is_find_comment_reply(self):
        name = "动态详情页中-第一个评论中回复按钮是否可见"
        try:
            self.get_element(ntl.comment_reply, model=name)
            return True
        except:
            return False

    # 动态详情页中-第一个分享icon可见
    def is_find_share_one(self):
        name = "动态详情页中-第一个分享icon可见"
        time.sleep(1)
        try:
            self.get_element(ntl.one_share_icon, model=name)
            return True
        except:
            return False

    # 点击分享icon
    def click_one_share_icon(self):
        name = "点击分享icon"
        while self.is_find_share_one() == False:  # 查找第一个动态分享icon是否可见，不可见这滑屏直到滑动为止
            self.swipe_screen(0.5, 0.8, 0.5, 0.5)
        self.click_element(ntl.one_share_icon, model=name)
        return self

    # 点击列表中【分享】选项
    def click_list_share_button(self):
        name = "点击列表中【分享】选项"
        self.wait_eleVisible(ntl.list_share_button, model=name)
        self.click_element(ntl.list_share_button, model=name)
        return self

    # 分享输入文本-分享
    def input_text_share(self, text):
        name = "分享输入文本-分享"
        self.wait_eleVisible(ntl.share_input, model=name)
        self.input_text(ntl.share_input, text, model=name)
        self.wait_eleVisible(ntl.share_page_share_button, model=name)
        self.click_element(ntl.share_page_share_button, model=name)
        return self

    # 不輸入文本，直接分享
    def click_share_button(self):
        name = "不輸入文本，直接分享"
        self.wait_eleVisible(ntl.share_page_share_button, model=name)
        self.click_element(ntl.share_page_share_button, model=name)
        return self

    # 点击列表中[分享至SunPeople]
    def click_list_share_sp(self):
        name = "点击列表中[分享至SunPeople]"
        self.wait_eleVisible(ntl.share_to_SP_button, model=name)
        self.click_element(ntl.share_to_SP_button, model=name)
        self.wait_loading_done()
        return self

    # 分享至SP-最近对话选择分享对象(第一个)
    def click_share_user(self):
        name = "分享至SP-最近对话选择分享对象(第一个)"
        self.wait_eleVisible(ntl.dialog_page_one_user, model=name)
        self.click_element(ntl.dialog_page_one_user, model=name)
        return self

    # 获取分享成功toast提示
    def get_share_toast(self):
        name = '获取分享成功toast提示'
        try:
            self.get_toastMsg("分享成功", model=name)
            return True
        except:
            return False

    # 滑動使第一個分享icon可見
    def search_swipe_one_share(self):
        name = '滑動使第一個分享icon可見'
        while self.is_find_share_one() == False:  # 查找第一个动态分享icon是否可见，不可见这滑屏直到滑动为止
            self.swipe_screen(0.5, 0.8, 0.5, 0.5, model=name)
        return self

    # 獲取分享次數
    def get_share_time(self):
        name = '獲取分享次數'
        while self.is_find_share_one() == False:  # 查找第一个动态分享icon是否可见，不可见这滑屏直到滑动为止
            self.swipe_screen(0.5, 0.8, 0.5, 0.5, model=name)
            time.sleep(1)
        text = self.get_text(ntl.share_time, model=name)
        return eval(text.split()[0])  # 通过空格切割获取第一个元素，即次数

    # 點擊分享計數
    def click_share_time(self):
        name = "點擊分享計數"
        self.wait_eleVisible(ntl.share_time, model=name)
        self.click_element(ntl.share_time, model=name)
        return self

    # 分享帖子頁-獲取分享用戶總數
    def get_actual_share_time(self):
        name = "分享帖子頁-獲取分享用戶總數"
        self.wait_eleVisible(ntl.share_users, model=name)
        user_list = self.find_elements(ntl.share_users, model=name)
        return len(user_list)

    # 點擊：'你在想什麼?'發帖入口
    def click_publish_dynamic(self):
        name = "點擊：'你在想什麼?'發帖入口"
        self.wait_eleVisible(ntl.publish_dynamic, model=name)
        time.sleep(3)
        self.click_element(ntl.publish_dynamic, model=name)
        return self

    # 輸入文本：「建立貼文」頁面-輸入框
    def inptu_publish_input(self,text):
        name = '輸入文本：「建立貼文」頁面-輸入框'
        self.wait_eleVisible(ntl.publish_input, model=name)
        self.input_text(ntl.publish_input,text, model=name)
        return self

    # 获取文本：建立贴文-编辑框中的文本
    def get_publish_input_text(self):
        self.wait_eleVisible(ntl.publish_input)
        text = self.get_text(ntl.publish_input)
        return text

    # 点击：[個人動態]跳转按钮
    def click_personal_dynamic(self):
        name = "点击：[個人動態]跳转按钮"
        self.wait_eleVisible(ntl.personal_dynamic, model=name)
        self.click_element(ntl.personal_dynamic, model=name)
        return self

    # 查找：[個人動態]跳转頁'分享至'
    def find_share_page_list(self):
        name = "查找：[個人動態]跳转頁'分享至'"
        time.sleep(3)
        try:
            self.get_element(ntl.share_page_list, model=name)
            return True
        except:
            return False

    # 点击第2個群組对象（非[個人動態]）
    def click_random_Object(self):
        name = "点击第2個群組对象（非[個人動態]））"
        self.wait_eleVisible(ntl.share_page_list, model=name)
        self.find_elements(ntl.share_page_list, model=name)[1].click()
        time.sleep(1)
        self.click_share_done_button()
        return self

    # 隨機選擇一個群組
    def click_random_index_Object(self,index):
        name = "点击第{}個群組对象".format(index+1)
        self.wait_eleVisible(ntl.share_page_list, model=name)
        self.find_elements(ntl.share_page_list, model=name)[index].click()
        time.sleep(1)
        self.click_share_done_button()
        return self


    # --------------------------- 【群组】相关元素操作 zjj ------------------------------------------------

    # 加载load文案1
    def wait_loading_done(self):
        name = '加载load文案1'
        time.sleep(1)
        self.wait_element_vanish(ntl.loading_icon, model=name)
        return self

    # 加载load文案2
    def wait_qroup_loading_icon(self):
        name = '加载load文案2'
        time.sleep(0.5)
        self.wait_element_vanish(ntl.qroup_loading_icon,wait_times=100,model=name)
        return self

    # 點擊群組 tab
    def click_group_tab(self):
        name = "點擊【群組】 tab"
        self.wait_eleVisible(ntl.group_tab, model=name)
        self.click_element(ntl.group_tab, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 點擊：[探索群組]按鈕
    def click_explore_group_button(self):
        name = '點擊：[探索群組]按鈕'
        time.sleep(3)
        self.wait_eleVisible(ntl.group_post_list_user_name, model=name)
        self.click_element(ntl.explore_group_button, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 點擊：[查看全部] 按鈕
    def click_view_all_button(self):
        name = '點擊：[查看全部] 按鈕'
        self.wait_eleVisible(ntl.view_all_button, model=name)
        time.sleep(2)
        self.click_element(ntl.view_all_button, model=name)
        return self

    # 查找對應群組並點擊
    def find_click_group(self, group_name):
        name = '查找對應群組並點擊'
        a = 0
        while self.find_group_name(group_name) == False:
            self.swipe_screen(0.5,0.8,0.5,0.5)
            a = a + 1
            time.sleep(1)
            if a >= 8:
                break
        self.text_find_and_click(group_name, model=name)
        logging.info("点击群组'{}'成功".format(group_name))
        return self

    # 查找群組
    def find_group_name(self,group_name):
        name = '查找群組'
        time.sleep(1)
        try:
            self.text_find(group_name, model=name)
            return True
        except:
            return False

    # 獲取文本：群組主頁中的名稱
    def get_group_page_group_title_name(self):
        name = '獲取文本：群組主頁中的名稱'
        self.wait_eleVisible(ntl.group_page_group_title, model=name)
        return self.get_text(ntl.group_page_group_title, model=name)

    # 點擊：群組tab-「查看全部」icon
    def click_group_tab_view_all(self):
        name = '點擊：群組tab-「查看全部」icon'
        time.sleep(1)
        self.wait_qroup_loading_icon()              # 等待load
        self.wait_eleVisible(ntl.group_post_list_user_name, model=name)
        time.sleep(3)
        self.click_element(ntl.group_tab_view_all, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 點擊："你的群組"頁面列表中第一個群組
    def click_your_group_page_list(self):
        name = '點擊："你的群組"頁面列表中第一個群組'
        self.wait_eleVisible(ntl.your_group_page_list, model=name)
        self.click_element(ntl.your_group_page_list, model=name)
        return self

    # 查找指定群組
    def find_your_group_page_specify_group(self,group_name):
        name = '查找指定群組'
        time.sleep(2)
        try:
            self.text_find(group_name, model=name)
            return True
        except:
            return False

    # 點擊："你的群組"頁面列表中指定的群組
    def click_your_group_page_specify_group(self,group_name):
        name = '點擊："你的群組"頁面列表中指定的群組'
        self.wait_eleVisible(ntl.your_group_page_list, model=name)
        if self.find_your_group_page_specify_group(group_name) == False:
            self.swipe_screen(0.5,0.9,0.5,0.3, model=name)
        self.text_find_and_click(group_name, model=name)
        return self

    # 獲取文本：群組主頁展示成員個數
    def get_group_home_group_count(self):
        name = '獲取文本：群組主頁展示成員個數'
        self.wait_eleVisible(ntl.group_home_group_count, model=name)
        data = self.get_text(ntl.group_home_group_count, model=name)
        return int(data.split(' ',3)[-2])

    # 點擊：群組主頁-成員頭像
    def click_group_home_member_avatar(self):
        name = '點擊：群組主頁-成員頭像'
        self.wait_eleVisible(ntl.group_home_member_avatar, model=name)
        self.click_element(ntl.group_home_member_avatar, model=name)
        return self

    # 獲取列數："成員和粉絲"頁面用戶數
    def get_group_member_list(self):
        name = '獲取列數："成員和粉絲"頁面用戶數'
        self.wait_eleVisible(ntl.group_member_list, model=name)
        member_nunmber = len(self.find_elements(ntl.group_member_list))
        time.sleep(2)
        # self.click_element(ntl.fend_page_admin_tab, model=name)
        self.text_find_and_click("位成員")
        admin_number = self.find_group_member_list()
        return member_nunmber+admin_number        # 成员数+管理员数

    #查找成员数量
    def find_group_member_list(self):
        self.wait_eleVisible_pass(ntl.group_member_list,wait_times=2, poll_frequency=0.5)
        try:
            self.get_element(ntl.group_member_list)
            return len(self.find_elements(ntl.group_member_list))
        except:
            return 0


    # 點擊："你的群组"页面-【追踪中】tab
    def click_your_group_following_tab(self):
        name = '點擊："你的群组"页面-【追踪中】tab'
        self.wait_eleVisible(ntl.your_group_following_tab, model=name)
        self.find_elements(ntl.your_group_following_tab, model=name)[1].click()
        logging.info("点击【追踪中】tab成功")
        return self

    # 获取索引：查找对应群组获取对应的索引
    def get_following_tab_group_index(self,group_name):
        name = '获取索引：查找对应群组获取对应的索引'
        self.wait_eleVisible(ntl.your_group_following_tab_list, model=name)
        group_number = len(self.find_elements(ntl.your_group_following_tab_list))
        for index in range(0,group_number):
            if self.find_elements(ntl.your_group_following_tab_list, model=name)[index].text == group_name:
                logging.info("查找目标群组'{}'在第{}行".format(group_name,index+1))
                return int(index)

    # 點擊：查找目標群組的『追蹤中』按鈕
    def click_following_tab_list_following_button(self,index):
        name = '點擊：查找目標群組的『追蹤中』按鈕'
        self.wait_eleVisible(ntl.following_tab_list_following_button, model=name)
        self.find_elements(ntl.following_tab_list_following_button, model=name)[index].click()
        logging.info("点击目前群组的『追蹤中』按鈕成功")
        name = '點擊「確認取消」按鈕'
        self.wait_eleVisible(ntl.personal_home_page_trace_fix, model=name)
        self.click_element(ntl.personal_home_page_trace_fix, model=name)  # 點擊「確認取消」按鈕
        self.wait_qroup_loading_icon()
        return self

    # 點擊："你的群组"页面-【其他】tab
    def click_your_group_page_other_tab(self):
        name = '點擊："你的群组"页面-【其他】tab'
        self.wait_eleVisible(ntl.your_group_page_other_tab, model=name)
        self.click_element(ntl.your_group_page_other_tab, model=name)
        return self

    # 獲取文本： "你的群组"页面-【其他】tab 第一個用戶暱稱
    def get_other_tab_user_list(self):
        name = '獲取文本： "你的群组"页面-【其他】tab 第一個用戶暱稱'
        self.wait_eleVisible(ntl.other_tab_user_list, model=name)
        return self.get_text(ntl.other_tab_user_list, model=name)

    # 點擊："你的群组"页面-【其他】tab - [追踪]按钮
    def click_other_tab_track_button(self):
        name = '點擊："你的群组"页面-【其他】tab - [追踪]按钮'
        self.wait_eleVisible(ntl.other_tab_track_button, model=name)
        self.click_element(ntl.other_tab_track_button, model=name)
        return self

    # 點擊：第一個帖子用戶頭像
    def click_group_page_one_post_user_name(self):
        name ="點擊：第一個帖子用戶頭像"
        self.wait_eleVisible(ntl.group_page_one_post_user_avatar, model=name)
        self.click_element(ntl.group_page_one_post_user_avatar, model=name)
        return self

    # 獲取文本：第一個帖子用戶暱稱
    def get_group_page_one_post_user_name(self):
        name = "獲取文本：第一個帖子用戶暱稱"
        self.wait_eleVisible(ntl.group_page_one_post_user_name, model=name)
        return self.get_text(ntl.group_page_one_post_user_name, model=name)

    # 判斷是否為個人主頁
    def is_personal_page_user_name(self):
        name = "判斷是否為個人主頁"
        time.sleep(2)
        try:
            self.get_element(ntl.personal_page_user_name, model=name)
            return True
        except:
            return False

    # 判斷是否為群組主頁
    def is_group_home_page(self):
        name = "判斷是否為群組主頁"
        time.sleep(2)
        try:
            self.get_element(ntl.group_home_page_quit_button, model=name)
            return True
        except:
            return False

    # 判斷：是否跳轉到對象的主頁
    def is_jump_home_page(self):
        self.wait_qroup_loading_icon()  # 等待加載
        if self.is_personal_page_user_name() == True or self.is_group_home_page() == True:
            result = True
        else:
            result = False
        return result

    # 获取文本：群组tab中第一个贴子的文本
    def get_group_tab_one_post_text(self):
        name = "获取文本：群组tab中第一个贴子的文本"
        self.wait_eleVisible(ntl.group_tab_one_post_text, model=name)
        return self.get_text(ntl.group_tab_one_post_text, model=name).strip()

    # 点击：群组tab中第一个贴子的文本
    def click_group_tab_one_post_text(self):
        name = '点击：群组tab中第一个贴子的文本'
        self.wait_eleVisible(ntl.group_tab_one_post_text, model=name)
        self.click_element(ntl.group_tab_one_post_text, model=name)
        return self

    # 查找：帖子详情分享icon
    def find_group_tab_post_share_icon(self):
        name = "查找：帖子详情分享icon"
        self.wait_eleVisible(ntl.group_tab_post_leave_icon, model=name)
        try:
            self.get_element(ntl.group_tab_post_share_icon, model=name)
            return True
        except:
            return False

    # 查找：建立贴文页面-【管理员身份】下拉按钮
    def find_set_post_admin_button(self):
        name = "查找：建立贴文页面-【管理员身份】下拉按钮"
        time.sleep(2)
        try:
            self.get_element(ntl.set_post_admin_button, model=name)
            return True
        except:
            return False

    # 點擊：建立贴文页面-【管理员身份】下拉按钮
    def click_set_post_admin_button(self):
        name ="點擊：建立贴文页面-【管理员身份】下拉按钮"
        self.wait_eleVisible(ntl.set_post_admin_button, model=name)
        self.click_element(ntl.set_post_admin_button, model=name)
        return self

    # 點擊：下拉列表選項「個人身份」
    def click_set_post_page_admin_list_one(self):
        name = "點擊：下拉列表選項「個人身份」"
        self.wait_eleVisible(ntl.set_post_admin_button, model=name)
        time.sleep(2)
        self.tap_click_ele(0.543,0.236, model=name)
        return self

    # 查找：建立贴文页面- [公開帖文]下拉列表
    def find_public_post_buttn(self):
        name = '查找：建立贴文页面- [公開帖文]下拉列表'
        time.sleep(2)
        try:
            self.get_element(ntl.public_post_buttn, model=name)
            return True
        except:
            return False

    # 點擊：建立贴文页面- [公開帖文]下拉列表-[私密貼文]選項
    def click_public_post_buttn(self):
        name = "點擊：建立贴文页面- [公開帖文]下拉列表-[私密貼文]選項"
        self.wait_eleVisible(ntl.public_post_buttn, model=name)
        self.click_element(ntl.public_post_buttn, model=name)
        time.sleep(2)
        self.tap_click_ele(0.767,0.276)
        time.sleep(2)
        return self

    # 點擊：建立贴文页面- [公開帖文]下拉列表
    def click_public_post_list_buttn(self):
        name = "點擊：建立贴文页面- [公開帖文]下拉列表"
        self.wait_eleVisible(ntl.public_post_buttn, model=name)
        self.click_element(ntl.public_post_buttn, model=name)
        time.sleep(2)
        return self

    # 查找：點讚icon
    def find_group_tab_post_like_icon(self):
        name = "查找：點讚icon"
        time.sleep(1)
        try:
            self.get_element(ntl.group_tab_post_like_icon, model=name)
            return True
        except:
            return False

    # 查找：分享icon
    def find_group_tab_post_share_icon2(self):
        name = "查找：點讚icon"
        time.sleep(1)
        try:
            self.get_element(ntl.group_tab_post_share_icon, model=name)
            return True
        except:
            return False
    # 處理帖子點讚icon可見
    def action_group_tab_post_like_icon(self):
        name = "處理帖子點讚icon可見"
        self.wait_eleVisible(ntl.group_post_list_user_name, model=name)      # 等待數據加載
        a = 1
        while self.find_group_tab_post_like_icon() == False:
            self.swipe_screen(0.5,0.8,0.5,0.6, model=name)
            time.sleep(1)
            a = a+1
            if a >=6:
                break

    # 處理帖子分享icon可見
    def action_group_tab_post_share_icon(self):
        name = "處理帖子分享icon可見"
        self.wait_eleVisible(ntl.group_post_list_user_name, model=name)  # 等待數據加載
        a = 1
        while self.find_group_tab_post_share_icon2() == False:
            self.swipe_screen(0.5, 0.8, 0.5, 0.6, model=name)
            time.sleep(1)
            a = a + 1
            if a >= 6:
                break

    # 獲取文本:[群組]tab中第一個帖子的點讚次數
    def get_group_tab_list_one_post_like(self):
        name = "獲取文本:[群組]tab中第一個帖子的點讚次數"
        self.wait_eleVisible(ntl.group_tab_post_like_count, model=name)
        data = self.get_text(ntl.group_tab_post_like_count, model=name)
        return int(data.split(' ',2)[1])

    # 點擊：給第一個帖子點讚
    def click_group_tab_list_like_icon(self):
        name = "點擊：給第一個帖子點讚"
        self.wait_eleVisible(ntl.group_tab_post_like_icon, model=name)
        self.click_element(ntl.group_tab_post_like_icon, model=name)
        return self

    # 點擊：列表帖子留言icon
    def click_group_tab_post_leave_icon(self):
        name = "點擊：列表帖子留言icon"
        self.wait_eleVisible(ntl.group_tab_post_leave_icon, model=name)
        self.click_element(ntl.group_tab_post_leave_icon, model=name)
        return self

    # 點擊：列表帖子分享icon
    def click_group_tab_post_share_icon(self):
        name = "點擊：列表帖子分享icon"
        self.wait_eleVisible(ntl.group_tab_post_share_icon, model=name)
        self.click_element(ntl.group_tab_post_share_icon, model=name)
        name = "选项【分享】"
        self.wait_eleVisible(ntl.group_tab_post_share_Option, model=name)
        self.click_element(ntl.group_tab_post_share_Option, model=name)               # 选项【分享】
        name = "[分享動態]頁面-分享按鈕"
        self.wait_eleVisible(ntl.group_tab_post_share_Option_to_done, model=name)
        self.click_element(ntl.group_tab_post_share_Option_to_done, model=name)       # [分享動態]頁面-分享按鈕
        return self

    # 點擊："追蹤更多"頁面-[導航欄]-M或N
    def click_track_more_navigate_M(self):
        name = '點擊："追蹤更多"頁面-[導航欄]-M或N'
        self.wait_eleVisible(ntl.track_more_navigate, model=name)
        time.sleep(2)
        self.tap_click_ele(0.963,0.725, model=name)
        return self

    # 獲取：群組列表中群組首字母第一個
    def get_list_head_title(self):
        name = '獲取：群組列表中群組首字母第一個'
        self.wait_eleVisible(ntl.list_head_title, model=name)
        return self.get_text(ntl.list_head_title, model=name)

    # 點擊：[建立群組]按鈕
    def click_create_group_button(self):
        name = '點擊：[建立群組]按鈕'
        time.sleep(3)
        self.wait_eleVisible(ntl.create_group_button, model=name)
        self.click_element(ntl.create_group_button, model=name)
        return self

    # 輸入文本：「建立群組」-名稱輸入框
    def input_create_group_name_input(self,group_name):
        name = ' 輸入文本：「建立群組」-名稱輸入框'
        self.wait_eleVisible(ntl.create_group_name_input, model=name)
        self.input_text(ntl.create_group_name_input,group_name, model=name)
        return self

    # 點擊：[建立群組]完成按鈕
    def click_create_group_done_button(self):
        name = '點擊：[建立群組]完成按鈕'
        self.wait_eleVisible(ntl.create_group_done_button, model=name)
        self.click_element(ntl.create_group_done_button, model=name)
        time.sleep(1)
        self.wait_qroup_loading_icon()
        time.sleep(2)
        self.wait_qroup_loading_icon()
        return self

    # 輸入群組名後觸發搜索
    def input_track_more_search_box(self,letter1,letter2,letter3):
        name = '輸入群組名後觸發搜索'
        self.wait_eleVisible(ntl.track_more_search_box, model=name)
        self.click_element(ntl.track_more_search_box, model=name)
        self.adb_keycode(45)
        self.adb_keycode(29)
        self.adb_keycode(45)
        self.adb_keycode(keycode[letter1])
        self.adb_keycode(keycode[letter2])
        self.adb_keycode(keycode[letter3])
        logging.info("输入文本：'test{0}{1}{2}'后触发搜索".format(letter1,letter2,letter3))
        self.keyboard_search()      # 觸發搜索
        return self

    # 點擊：'建立群組'頁面-[新增成員]
    def click_create_group_add_member_icon(self):
        name = "點擊：'建立群組'頁面-[新增成員]"
        self.wait_eleVisible(ntl.create_group_add_member_icon, model=name)
        self.click_element(ntl.create_group_add_member_icon, model=name)
        return self

    # [新增成員]頁面選中多個人員
    def click_double_add_member_list(self,member_number):
        name = '[新增成員]頁面選中多個人員'
        self.wait_eleVisible(ntl.add_member_list, model=name)
        for i in range(0,member_number):
            self.find_elements(ntl.add_member_list, model=name)[i].click()
        name = "点击'新增成員'頁面-[完成]按鈕"
        self.wait_eleVisible(ntl.add_member_done_button, model=name)
        self.click_element(ntl.add_member_done_button, model=name)
        return self

    # 判斷是否有搜索結果
    def is_track_more_search_grouplist(self):
        name = '判斷是否有搜索結果'
        self.wait_eleVisible(ntl.track_more_search_grouplist, model=name)
        try:
            self.get_element(ntl.track_more_search_grouplist, model=name)
            return True
        except:
            return False

    # 查找：搜索結果中查找對象群組
    def find_track_more_search_grouplist(self,text):
        name = '查找：搜索結果中查找對象群組'
        time.sleep(2)
        try:
            self.text_find(text, model=name)
            return True
        except:
            return False

    # 查找：未输入关键字时有无展示群组列表
    def find_track_more_grouplist(self):
        name = '查找：未输入关键字时有无展示群组列表'
        self.wait_eleVisible(ntl.track_more_search_grouplist, model=name)
        try:
            self.get_element(ntl.track_more_search_grouplist, model=name)
            return True
        except:
            return False

    # 點擊："追蹤更多"頁面-[個人]tab
    def click_track_more_personal_tab(self):
        name = '點擊："追蹤更多"頁面-[個人]tab'
        self.wait_eleVisible(ntl.track_more_personal_tab, model=name)
        self.click_element(ntl.track_more_personal_tab, model=name)
        return self

    # 獲取索引：個人tab中第一個"追蹤"的控件索引
    def get_list_one_track_index(self):
        name = '獲取索引：個人tab中第一個"追蹤"的控件索引'
        self.wait_eleVisible(ntl.track_page_personal_track_button, model=name)
        find_number = len(self.find_elements(ntl.track_page_personal_track_button))
        for index in range(0,find_number):
            button_text = self.find_elements(ntl.track_page_personal_track_button, model=name)[index].text
            if button_text == '追蹤':
                logging.info("列表中第{}個用戶可最終".format(index+1))
                return index

    # 獲取文本：[追蹤更多]頁面個人tab中第一個"追蹤"的用戶名稱並點擊「追蹤」按鈕
    def get_list_one_track_name(self,index):
        name = '獲取文本：[追蹤更多]頁面個人tab中第一個"追蹤"的用戶名稱並點擊「追蹤」按鈕'
        self.wait_eleVisible(ntl.track_page_personal_track_button, model=name)
        user_name = self.find_elements(ntl.list_one_track_name, model=name)[index].text
        logging.info("第一個可「追蹤」的用戶暱稱為'{}'".format(user_name))
        self.find_elements(ntl.track_page_personal_track_button, model=name)[index].click()
        return user_name

    # 獲取索引：群組tab中第一個可"追蹤"的控件索引
    def get_list_one_group_track_index(self):
        name = '獲取索引：群組tab中第一個可"追蹤"的控件索引'
        self.wait_eleVisible(ntl.track_more_track_button, model=name)
        find_number = len(self.find_elements(ntl.track_more_track_button))
        for index in range(0, find_number):
            button_text = self.find_elements(ntl.track_more_track_button, model=name)[index].text
            if button_text == '追蹤':
                logging.info("列表中第{}個群組可最終".format(index + 1))
                return index

    # 獲取文本：[追蹤更多]頁面群組tab中第一個"追蹤"的群組名稱並點擊「追蹤」按鈕
    def get_list_one_group_track_name(self, index):
        name = '獲取文本：[追蹤更多]頁面群組tab中第一個"追蹤"的群組名稱並點擊「追蹤」按鈕'
        self.wait_eleVisible(ntl.track_more_track_button, model=name)
        group_name = self.find_elements(ntl.track_more_group_list, model=name)[index].text
        logging.info("第一個可「追蹤」的群組名稱為'{}'".format(group_name))
        self.find_elements(ntl.track_more_track_button, model=name)[index].click()
        return group_name

    # 獲取索引：群組tab中第一個可"追蹤"的控件索引
    def get_list_one_personal_track_index(self):
        name = '獲取索引：個人tab中第一個可"追蹤"的控件索引'
        self.wait_eleVisible(ntl.track_more_personal_track_button, model=name)
        find_number = len(self.find_elements(ntl.track_more_personal_track_button))
        for index in range(0, find_number):
            button_text = self.find_elements(ntl.track_more_personal_track_button, model=name)[index].text
            if button_text == '追蹤':
                logging.info("列表中第{}個用戶可最終".format(index + 1))
                return index

    # 獲取文本：[追蹤更多]頁面個人tab中第一個"追蹤"的用戶名並點擊「追蹤」按鈕
    def get_list_one_personal_track_name(self, index):
        name = '獲取文本：[追蹤更多]頁面個人tab中第一個"追蹤"的用戶名稱並點擊「追蹤」按鈕'
        self.wait_eleVisible(ntl.track_more_personal_track_button, model=name)
        user_name = self.find_elements(ntl.track_more_personal_list, model=name)[index].text
        logging.info("第一個可「追蹤」的用戶名為'{}'".format(user_name))
        self.find_elements(ntl.track_more_personal_track_button, model=name)[index].click()
        return user_name

    # 點擊：追蹤更多-取消追蹤
    def click_ist_one_personal_cancel_track(self, index):
        name = '點擊：追蹤更多-取消追蹤'
        self.wait_eleVisible(ntl.track_more_personal_track_button, model=name)
        self.find_elements(ntl.track_more_personal_track_button, model=name)[index].click()
        time.sleep(1)
        name = '点击：[確認取消]按鈕'
        self.wait_eleVisible(ntl.personal_home_page_trace_fix, model=name)
        self.click_element(ntl.personal_home_page_trace_fix, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 獲取文本：[追蹤更多]頁面個人tab中获取取消追蹤按钮文案
    def get_list_one_track_button_name(self, index):
        name = '獲取文本：[追蹤更多]頁面個人tab中获取取消追蹤按钮文案'
        self.wait_eleVisible(ntl.track_page_personal_track_button, model=name)
        button_name = self.find_elements(ntl.track_page_personal_track_button, model=name)[index].text
        return button_name

    # 獲取文本：[追蹤更多]頁面群組tab中获取取消追蹤按钮文案
    def get_list_group_one_track_button_name(self,index):
        name = '獲取文本：[追蹤更多]頁面群組tab中获取取消追蹤按钮文案'
        self.wait_eleVisible(ntl.track_more_track_button, model=name)
        return self.find_elements(ntl.track_more_track_button, model=name)[index].text

    # 點擊：【個人】tab
    def click_personal_tab(self):
        name = '點擊：【個人】tab'
        self.wait_eleVisible(ntl.personal_tab, model=name)
        self.click_element(ntl.personal_tab, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 點擊：個人tab「追踪中」
    def click_personal_trace(self):
        name = '點擊：個人tab「追踪中」'
        self.wait_eleVisible(ntl.personal_trace, model=name)
        self.click_element(ntl.personal_trace, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 查找：個人tab「追蹤中」
    def find_personal_trace(self):
        time.sleep(1)
        try:
            self.get_element(ntl.personal_trace)
            return True
        except:
            return False

    # 获取追踪的人数
    def get_personal_trace_number(self):
        name = "获取追踪的人数"
        self.wait_eleVisible(ntl.personal_trace_number, model=name)
        data = self.get_text(ntl.personal_trace_number, model=name)
        return int(data.split('人')[0])

    # 删除多余的追踪个人，只保留2个
    def delete_personal_trace_user(self):
        trace_number = self.get_personal_trace_number()         # 追踪用户个数
        trace_group_number = self.get_list_track_group_title_bumber()     # 追踪群组个数
        logging.info("追踪用户个数为'{}'，追踪群组个数为'{}'".format(trace_number,trace_group_number))
        number = 1
        group_number = 1
        start_delete = self.get_system_time_time()
        if trace_number >2:
            logging.info("开始清理追踪的用户。。。")
            while number<=(trace_number-2):
                logging.info("第{}次清理个人追踪用户".format(number))
                name = "点击【追踪中】"
                self.wait_eleVisible(ntl.track_page_personal_track_button, model=name)
                self.click_element(ntl.track_page_personal_track_button, model=name)    # 点击【追踪中】
                name = "点击[確認取消]按鈕"
                self.wait_eleVisible(ntl.personal_home_page_trace_fix, model=name)
                self.click_element(ntl.personal_home_page_trace_fix, model=name)        # 点击[確認取消]按鈕
                self.wait_qroup_loading_icon()
                number = number + 1
                time.sleep(1)
                self.swipe_screen(0.5,0.3,0.5,0.7)              # 下拉刷新
                self.wait_qroup_loading_icon()
        if trace_group_number > 2:
            logging.info("开始清理追踪的群组。。。")
            while group_number <= (trace_group_number - 2):
                logging.info("第{}次清理追踪的群组".format(group_number))
                name = '点击追踪中的群组头像'
                self.wait_eleVisible(ntl.trace_group_Avatar, model=name)
                self.click_element(ntl.trace_group_Avatar, model=name)            # 点击追踪中的群组头像
                self.wait_qroup_loading_icon()
                self.click_personal_home_trace_group_cancel()         # 点击更多-取消追踪-确定取消
                group_number = group_number+1
                time.sleep(1)
                self.return_button()                                  # 返回
        end_delete = self.get_system_time_time()
        delta = self.get_demo_time_interval_time(start_delete, end_delete)
        hour = delta // 3600  # 时
        div = (delta % 3600) // 60  # 分
        mod = (delta % 3600) % 60  # 秒
        delete_number = trace_group_number + trace_number - 4
        logging.info("删除个人主页追踪中的{}个群组或用户所花时间：".format(delete_number))
        logging.info("{}小时{}分钟{}秒".format(hour, div, mod))
        return self

    # 點擊：「追蹤更多」跳轉
    def click_trace_more_icon(self):
        name = '點擊：「追蹤更多」跳轉'
        self.wait_eleVisible(ntl.list_track_group_title, model=name)
        a = 0
        while self.find_track_text() == False:
            self.swipe_screen(0.5,0.8,0.5,0.5, model=name)
            a= a +1
            if a>=4:
                break
        self.text_find_and_click("追蹤更多", model=name)
        return self

    # 查找：「追蹤更多」跳轉
    def find_track_text(self):
        name = '查找：「追蹤更多」跳轉'
        try:
            self.text_find("追蹤更多",model=name)
            return True
        except:
            return False

    # 點擊：'追蹤更多'頁面-「個人」tab
    def click_trace_more_personal_tab(self):
        name = "點擊：'追蹤更多'頁面-「個人」tab"
        self.wait_eleVisible(ntl.track_more_personal_tab, model=name)
        self.click_element(ntl.track_more_personal_tab, model=name)
        return self

    # 判斷：通過用戶暱稱查找用戶是否在追踪列表中
    def is_personal_trace_list_user(self,text):
        name = '判斷：通過用戶暱稱查找用戶是否在追踪列表中'
        self.wait_loading_done()
        self.wait_eleVisible(ntl.trace_too_list, model=name)
        try:
            self.text_find(text, model=name)
            return True
        except:
            return False

    # 點擊查找到的用戶
    def click_find_user(self,text):
        name = '點擊查找到的用戶'
        time.sleep(2)
        self.text_find_and_click(text, model=name)
        logging.info("點擊查找對象'{}'成功".format(text))
        return self

    # 點擊：用戶主頁[追踪中]按鈕
    def click_personal_home_page_trace(self):
        name = '點擊：用戶主頁[追踪中]按鈕'
        self.wait_eleVisible(ntl.personal_home_page_trace, model=name)
        self.click_element(ntl.personal_home_page_trace, model=name)                # 點擊：用戶主頁[追踪中]
        self.wait_eleVisible(ntl.personal_home_page_trace_fix, model=name)
        time.sleep(1)
        self.click_element(ntl.personal_home_page_trace_fix, model=name)            # 點擊：用戶主頁[追踪中]-[確認取消]按鈕
        self.wait_loading_done()
        time.sleep(1)
        return self

    # 獲取文本：個人tab-追蹤中追蹤群組的個數
    def get_list_track_group_title_bumber(self):
        name = '獲取文本：個人tab-追蹤中追蹤群組的個數'
        self.wait_eleVisible(ntl.list_track_group_title, model=name)
        data = self.get_text(ntl.list_track_group_title, model=name)
        return int(data.split('個')[0])

    # 查找群組：通過文本查找追蹤的群組
    def find_track_group_name(self,group_name):
        name = '查找群組：通過文本查找追蹤的群組'
        time.sleep(2)
        try:
            self.text_find(group_name, model=name)
            return True
        except:
            return False

    # 全部查找：個人tab-群組欄中查找當前追蹤中的群組
    def find_track_group_list_all(self,group_name):
        group_number = self.get_list_track_group_title_bumber()
        cycle_number = math.ceil(group_number/4)
        find_result = ''
        if cycle_number <= 1:                   # 群组小于等于4个不滑屏
            find_result = self.find_track_group_name(group_name)
        else:                                   # 群组大于4个滑屏
            number = 1
            while number < cycle_number:
                if self.find_track_group_name(group_name) == False:
                    name = '左滑屏幕'
                    self.swipe_screen(0.9,0.327,0.3,0.327, model=name)    # 左滑屏幕
                    time.sleep(2)
                    number = number + 1
                    if self.find_track_group_name(group_name) == True:    # 滑屏后继续查找
                        find_result = True
                        break
                    else:
                        find_result = False
                else:
                    find_result = True
                    break
        return find_result

    # 點擊：群組中更多icon-「取消追蹤」按鈕
    def click_personal_home_trace_group_cancel(self):
        name = '點擊：群組中更多icon-「取消追蹤」按鈕'
        self.wait_eleVisible(ntl.personal_home_trace_group, model=name)
        self.click_element(ntl.personal_home_trace_group, model=name)                  # 群組主頁點擊更多icon
        name = '點擊「取消追蹤」選項'
        self.wait_eleVisible(ntl.trace_group_cancel_button, model=name)
        self.click_element(ntl.trace_group_cancel_button, model=name)                   # 點擊「取消追蹤」選項
        name = '點擊「確認取消」按鈕'
        self.wait_eleVisible(ntl.personal_home_page_trace_fix, model=name)
        self.click_element(ntl.personal_home_page_trace_fix, model=name)                # 點擊「確認取消」按鈕
        self.wait_loading_done()
        return self

    # 點擊："追蹤更多"頁面群組tab-「追蹤」按鈕
    def click_track_more_track_button(self):
        name = '點擊："追蹤更多"頁面群組tab-「追蹤」按鈕'
        self.wait_eleVisible(ntl.track_more_track_button, model=name)
        self.click_element(ntl.track_more_track_button, model=name)
        return self

    # 查找：退出群组弹框
    def find_quit_group_button(self):
        time.sleep(2)
        try:
            self.get_element(ntl.quit_group_button)
            return True
        except:
            return False

    # 點擊：退出群组弹框-【確定退出】按钮
    def click_quit_group_button(self):
        self.wait_eleVisible(ntl.quit_group_button)
        self.click_element(ntl.quit_group_button)
        self.wait_qroup_loading_icon()
        return self

    # 查找：toast提示"您已經是該群組的成員，不能追蹤該群組"
    def find_toast_already_group_member(self):
        name = '查找：toast提示"您已經是該群組的成員，不能追蹤該群組"'
        try:
            self.get_toast_tips("您已經是該群組的成員", model=name)
            return True
        except:
            return False



    # --------------------------- 【通知】相关元素操作  ------------------------------------------------
    # --------------------------- 【个人】相关元素操作  ------------------------------------------------
    # 點擊【個人】tab
    # --------------------------- 【群组】相关元素操作  ------------------------------------------------

    # 查找群组："你的群组"页面查找创建的群组
    def find_create_group_name(self,group_name):
        name = '查找群组："你的群组"页面查找创建的群组'
        self.wait_eleVisible(ntl.your_group_admin, model=name)
        a = 0
        while a<=10:
            if self.find_group_text(group_name) == True:
                return True
            else:
                self.swipe_screen(0.5,0.8,0.5,0.5, model=name)
                a = a + 1
                time.sleep(1)

    # 通过文本查找群组
    def find_group_text(self,group_name):
        name = '通过文本查找群组'
        try:
            self.text_find(group_name, model=name)
            return True
        except:
            return False

    # --------------------------- 【通知】相关元素操作  ------------------------------------------------

    # --------------------------- 【个人】相关元素操作  ------------------------------------------------
    # 點擊【個人】tab
    def click_nf_personal_tab(self):
        name = "點擊【個人】tab"
        self.wait_nf_load()
        self.wait_eleVisible(ntl.personal_tab, model=name)
        self.click_element(ntl.personal_tab, model=name)
        self.wait_nf_load()
        return self

    # 等待加載load
    def wait_nf_load(self):
        name = '等待加載load'
        time.sleep(1)
        self.wait_element_vanish(ntl.nf_load_img, model=name)
        return self

    # 【个人】tab查找第一个动态分享icon
    def find_personal_shart_icon(self):
        name = "【个人】tab查找第一个动态分享icon"
        time.sleep(2)
        try:
            self.get_element(ntl.personal_tab_shart_icon, model=name)  # 查找可分享动态第一个分享icon
            return True
        except:
            return False

    # 个人tab中，滑屏至第一个帖子可见
    def swipe_to_post_find(self):
        self.wait_eleVisible_pass(ntl.user_homepage_name)
        time.sleep(1)
        bumber = 1
        while self.find_group_tab_post_like_icon() == False:
            self.swipe_screen(0.5,0.8,0.5,0.5)
            logging.info("第{}次滑屏让帖子点赞icon可见".format(bumber))
            time.sleep(1)
            bumber+=1
            if bumber >= 5:
                break

    # 查找追蹤的用戶
    def find_track_user(self,user_name):
        name = '查找追蹤的用戶'
        self.wait_eleVisible(ntl.list_track_group_title, model=name)
        time.sleep(1)
        try:
            self.text_find(user_name, model=name)
            return True
        except:
            return False

    # 獲取指定用戶所在的索引
    def find_personal_trace_user_name_index(self,user_name):
        name = '獲取指定用戶所在的索引'
        self.wait_eleVisible(ntl.personal_trace_user_name, model=name)
        list_number = len(self.find_elements(ntl.personal_trace_user_name, model=name))
        logging.info("用戶的個數為'{}'".format(list_number))
        for index in range(0,list_number):
            if self.find_elements(ntl.personal_trace_user_name, model=name)[index].text == user_name:
                return index

    # 點擊：指定用戶「追蹤中」按鈕
    def click_personal_trace_user_name_index(self,index):
        name = '點擊：指定用戶「追蹤中」按鈕'
        self.wait_eleVisible(ntl.personal_trace_item_button, model=name)
        self.find_elements(ntl.personal_trace_item_button, model=name)[index].click()
        time.sleep(1)
        name = '[確認取消]按鈕'
        self.wait_eleVisible(ntl.personal_home_page_trace_fix, model=name)
        self.click_element(ntl.personal_home_page_trace_fix, model=name)
        self.wait_qroup_loading_icon()
        return

    # 點擊[粉丝人數]
    def click_personal_fans(self):
        name = "點擊【個人】粉丝"
        self.wait_eleVisible(ntl.personal_tab_fan, model=name)
        self.click_element(ntl.personal_tab_fan, model=name)
        return self

    # 點擊:個人tab「追蹤中」
    def click_personal_trace_tab(self):
        name = "點擊【個人】追踪"
        self.wait_eleVisible(ntl.personal_trace, model=name)
        self.click_element(ntl.personal_trace, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 获取[个人]粉丝数量
    def get_personal_fans_count(self):
        name = "获取【個人】粉丝 数量"
        self.wait_eleVisible(ntl.personal_tab_fan, model=name)
        text = self.get_text(ntl.personal_tab_fan, model=name)
        return int(text.split("\n")[0])

    # 獲取文本：【個人】tab-粉丝计数-詳情頁-統計數
    def get_fan_list_count(self):
        name = '獲取文本：【個人】tab-粉丝计数-詳情頁-統計數'
        self.wait_eleVisible(ntl.fan_list_count, model=name)
        data = self.get_text(ntl.fan_list_count, model=name)
        return int(re.split('被|人',data)[1])

    # 获取個人tab追踪中数量
    def get_personal_trace_count(self):
        name = "获取【個人】追踪中 数量"
        self.wait_eleVisible(ntl.personal_trace, model=name)
        self.wait_until_not(ntl.personal_pro, model=name)
        text = self.get_text(ntl.personal_trace, model=name)
        return int(text.split("\n")[0])


    # [个人] 粉丝数对比 YangJi 未完成
    def verify_fans_count(self, count):
        name = "获取【個人粉丝列表】粉丝数组"
        self.wait_until_not(ntl.personal_fans_loading_view, model=name)
        user_list = self.find_elements(ntl.personal_fans_item, model=name)
        if len(user_list) == count:
            return True
        return False

    # 【个人】tab滑屏至第一个动态分享icon可见为止
    def swipe_personal_tab(self):
        name = '【个人】tab滑屏至第一个动态分享icon可见为止:'
        self.wait_eleVisible(ntl.personal_tab_fan, model=name)  # 等待个页tab数据加载完成
        self.swipe_screen(0.5, 0.4, 0.5, 0.8, model='下拉刷新')
        self.wait_qroup_loading_icon()          # 加载
        a = 0
        while self.find_personal_shart_icon() == False:
            self.swipe_screen(0.5, 0.8, 0.5, 0.6, model=name)
            a= a+1
            if a >= 5:
                break
        return self

    # 【个人】tab中點擊第一個可分享動態的分享icon
    def click_persomal_tab_share_icon(self):
        name = "【个人】tab中點擊第一個可分享動態的分享icon"
        self.wait_eleVisible(ntl.personal_tab_shart_icon, model=name)
        self.click_element(ntl.personal_tab_shart_icon, model=name)
        return self

    # 點擊：個人tab[在想些什麼?]发帖入口
    def click_personal_post_entrance_icon(self):
        name = '點擊：個人tab[在想些什麼?]发帖入口'
        self.wait_eleVisible(ntl.personal_post_entrance_icon, model=name)
        self.click_element(ntl.personal_post_entrance_icon, model=name)
        return self

    # 輸入文本：帖子文本
    def input_post_inptu_box_text(self,text):
        name = '輸入文本：帖子文本'
        self.wait_eleVisible(ntl.post_inptu_box, model=name)
        time.sleep(3)
        self.input_text(ntl.post_inptu_box,text, model=name)
        return self

    # 獲取文本：輸入框文本
    def get_post_inptu_box_text(self):
        name = "獲取文本：輸入框文本"
        self.wait_eleVisible(ntl.post_inptu_box, model=name)
        return self.get_text(ntl.post_inptu_box, model=name)

    # 點擊：「發布」按鈕(不需要等待)
    def click_post_publish_button_no(self):
        name = '點擊:「發布」按鈕(不需要等待)'
        self.wait_eleVisible(ntl.post_publish_button, model=name)
        time.sleep(1)
        self.click_element(ntl.post_publish_button, model=name)
        self.screenshot(name)
        return self

    # 點擊：「發布」按鈕
    def click_post_publish_button(self):
        name = '點擊:「發布」按鈕'
        self.wait_eleVisible(ntl.post_publish_button, model=name)
        time.sleep(1)
        self.click_element(ntl.post_publish_button, model=name)
        self.screenshot(name)
        if self.find_post_publish_button() == True:
            self.click_element(ntl.post_publish_button, model='再次点击【发布】按钮')
            self.screenshot('再次点击【发布】按钮')
        self.wait_fend_post_loading_icon()              # 发布中load
        self.wait_qroup_loading_icon()                  # 加载load
        return self

    # 查找：「發布」按鈕
    def find_post_publish_button(self):
        name = '查找：「發布」按鈕'
        time.sleep(0.5)
        try:
            self.get_element(ntl.post_publish_button, model=name)
            return True
        except:
            return False

    # 點擊：(發送圖片和視頻文本)「發布」按鈕
    def click_post_photo_publish_button(self):
        name = '點擊：「發布」按鈕'
        self.wait_eleVisible(ntl.post_publish_button, model=name)
        self.click_element(ntl.post_publish_button, model=name)
        self.screenshot("點擊發布按鈕立即截圖")
        self.wait_ele_invisible_pass(ntl.post_publish_cancel, wait_times=200)  # 發布上傳中
        # self.wait_qroup_loading_icon()
        # if self.find_post_publish_button() == True:         # 如果按鈕還在繼續點擊
        #     self.click_element(ntl.post_publish_button, model=name)
        #     logging.info("第一次发送未成功，再次点击【发送】")
        #     self.wait_ele_invisible_pass(ntl.post_publish_cancel, wait_times=200)  # 發布上傳中
        #     self.wait_qroup_loading_icon()
        return self

    # 点击：帖子中图片
    def click_all_tab_post_photo(self):
        name = "点击：帖子中的图片"
        self.wait_eleVisible(ntl.all_tab_post_photo, model=name)
        self.click_element(ntl.all_tab_post_photo, model=name)
        return self

    # 点击：帖子中的视频
    def click_all_tab_post_video(self):
        name = "点击：帖子中的视频"
        self.wait_eleVisible(ntl.all_tab_post_video, model=name)
        self.click_element(ntl.all_tab_post_video, model=name)
        return self

    # 查找：进入视频详情播放页（是否出现播放进度条）
    def find_post_video_play_progress(self):
        name = '查找：进入视频详情播放页'
        self.wait_eleVisible_pass(ntl.post_video_play_progress, wait_times=10, model=name)
        try:
            self.get_element(ntl.post_video_play_progress, model=name)
            return True
        except:
            return False

    # 查找：图片详情中下载按钮
    def find_photo_download(self):
        name = '查找：图片详情中下载按钮'
        self.wait_eleVisible_pass(ntl.photo_download,wait_times=10, model=name)
        try:
            self.get_element(ntl.photo_download, model=name)
            return True
        except:
            return False

    # 獲取：發布帖子展示時間
    def get_release_time(self):
        name = "獲取：發布帖子展示時間"
        self.swipe_action_release_post_time_visible()           # 处理至帖子可见
        self.wait_eleVisible(ntl.release_post_time, model=name)
        data = self.get_text(ntl.release_post_time, model=name)
        return int(data.split(':')[-1])

    # [個人]tab中处理至帖子时间展示栏可见
    def swipe_action_release_post_time_visible(self):
        name = '[個人]tab中处理至帖子时间展示栏可见'
        self.wait_eleVisible(ntl.personal_tab_photo_icon, model=name)      # 【个人】tab-拍照icon可见
        self.wait_qroup_loading_icon()                         # 加载load消失
        a = 0
        while self.if_release_post_time() == False:
            self.swipe_screen(0.5,0.8,0.5,0.6)
            a = a + 1
            time.sleep(1)
            if a >= 5:
                break

    # 判断：帖子时间展示栏是否可见
    def if_release_post_time(self):
        name = '判断：帖子时间展示栏是否可见'
        time.sleep(1)
        try:
            self.get_element(ntl.release_post_time, model=name)
            return True
        except:
            return False

    # 獲取文本：個人tab第一個帖子文本
    def get_personal_tab_post_text(self):
        name = "獲取文本：個人tab第一個帖子文本"
        self.wait_eleVisible(ntl.personal_post_entrance_icon, model=name)
        self.swipe_screen(0.5,0.8,0.5,0.5)     # 上滑
        time.sleep(1)
        self.wait_eleVisible(ntl.personal_tab_post_text, model=name)
        return self.get_text(ntl.personal_tab_post_text, model=name).strip()

    # 点击：【添加更多元素】icon
    def click_add_more_element_icon(self):
        name = "点击：【添加更多元素】icon"
        self.wait_eleVisible(ntl.add_more_element_icon, model=name)
        self.click_element(ntl.add_more_element_icon, model=name)
        return self

    # 点击：提交投票页面-添加更多元素-建立帖文
    def click_vote_page_set_post(self):
        name = "点击：提交投票页面-添加更多元素-建立帖文"
        self.wait_eleVisible(ntl.vote_page_set_post, model=name)
        self.click_element(ntl.vote_page_set_post, model=name)
        return self

    # 删除文本（一个字符）
    def delete_one_char(self):
        self.adb_keycode(67)
        time.sleep(2)
        return self

    # 点击：@列表第一行
    def click_set_post_at_list(self):
        time.sleep(2)
        self.tap_click_ele(0.5, 0.337)
        return self

    # 查找：文本框中聯繫人名稱
    def get_at_contact_name(self):
        text = self.get_publish_input_text()
        logging.info("輸入框文本為：'{}'".format(text))
        return text.strip()

    # '标注人名'頁面-[搜索]框输入文本并触发搜索
    def input_callout_name_page_search(self,text):
        name = "'标注人名'頁面-[搜索]框输入文本并触发搜索"
        self.wait_eleVisible(ntl.callout_name_page_search, model=name)
        self.input_text(ntl.callout_name_page_search,text, model=name)
        self.keyboard_search()
        return self

    # 点击：[提交投票]选项
    def click_submit_vote(self):
        name = "点击：[提交投票]选项"
        self.wait_eleVisible(ntl.submit_vote, model=name)
        self.click_element(ntl.submit_vote, model=name)
        return self

    # 點擊：[提交投票]-[添加選項]按鈕
    def click_submit_vote_add_Option(self):
        name = '點擊：[提交投票]-[添加選項]按鈕'
        self.wait_eleVisible(ntl.submit_vote_add_Option, model=name)
        self.click_element(ntl.submit_vote_add_Option, model=name)
        return self

    # 查找添加的[選項3]
    def find_add_Option3(self):
        name = '查找添加的[選項3]'
        time.sleep(2)
        try:
            self.get_element(ntl.add_Option3, model=name)
            return True
        except:
            return False

    # 查找添加的[選項4]
    def find_add_Option4(self):
        name = '查找添加的[選項4]'
        time.sleep(2)
        try:
            self.get_element(ntl.add_Option4, model=name)
            return True
        except:
            return False

    # [提交投票]頁-各項輸入文本
    def input_vote_title(self, index, data):
        name = "[提交投票]頁-各項輸入文本"
        self.wait_eleVisible(ntl.input_vote, model=name)
        self.find_elements(ntl.input_vote, model=name)[index].send_keys(data)
        logging.info("输入文本'{}'".format(data))
        return self

    # 點擊：「群組」分享跳轉按鈕
    def click_share_group(self):
        name = "點擊：分享「群組」跳轉按鈕"
        self.wait_eleVisible(ntl.share_group, model=name)
        self.click_element(ntl.share_group, model=name)
        return self

    # 获取[分享至]页-列表群组个数
    def get_share_list_number(self):
        name = "获取[分享至]页-列表群组个数"
        self.wait_qroup_loading_icon()  # 等待页面数据加载可见
        list_number = len(self.find_elements(ntl.share_list_number, model=name))
        logging.info("列表中有{}个群组".format(list_number-1))
        self.screenshot("列表中有{}个群组".format(list_number-1))
        return list_number

    # 隨機點擊：其中一個群組
    def click_random_Object_one(self,index):
        name = "点击第1個群組对象（非[個人動態]））"
        self.wait_eleVisible(ntl.share_list_number, model=name)
        self.find_elements(ntl.share_list_number, model=name)[index].click()
        logging.info("点击列表中第{}个群组成功".format(index+1))
        self.click_share_done_button()
        return self

    # 点击【完成】按钮
    def click_share_done_button(self):
        name = "点击【完成】按钮"
        self.wait_eleVisible(ntl.share_done_button, model=name)
        self.click_element(ntl.share_done_button, model=name)
        return self

    # 點擊：「發帖」按鈕
    def click_publish_button(self):
        name = "點擊：「發帖」按鈕"
        self.wait_eleVisible(ntl.publish_button, model=name)
        self.click_element(ntl.publish_button, model=name)
        time.sleep(0.5)
        self.screenshot("点击发布按钮后的截图")
        self.wait_post_publish()
        return self

    # 等待帖子发布中
    def wait_post_publish(self):
        name = '等待帖子发布中'
        self.wait_ele_visible_pass(ntl.post_publish_cancel,model=name)
        self.wait_element_vanish(ntl.post_publish_cancel,  wait_times=300,model=name)
        return self

    # 點擊：[投票結束時間]選項
    def click_vote_end_time(self):
        name = "點擊：[投票結束時間]選項"
        self.wait_eleVisible(ntl.vote_end_time, model=name)
        self.click_element(ntl.vote_end_time, model=name)
        return self

    # 獲取投票設置結束時間選項個數
    def get_setting_time_Option_number(self):
        name = '獲取投票設置結束時間選項個數'
        self.wait_eleVisible(ntl.list_time_days, model=name)
        number =  len(self.find_elements(ntl.list_time_days, model=name))
        logging.info("当前設置結束時間選項個數为'{}'".format(number))
        return number

    # 點擊：一个時間選項
    def click_list_time_days(self,index):
        name = "点击第'{}'个时间选项".format(index+1)
        self.wait_eleVisible(ntl.list_time_days, model=name)
        self.find_elements(ntl.list_time_days, model=name)[index].click()
        logging.info("点击第'{}'个时间选项".format(index+1))
        return self

    # 點擊：提交投票-「可多選」開關icon
    def click_multiple_choice_off(self):
        name = "點擊：提交投票-「可多選」開關icon"
        self.wait_eleVisible(ntl.multiple_choice_off, model=name)
        self.click_element(ntl.multiple_choice_off, model=name)
        return self

    # 获取文本：投票的titie
    def get_vote_title_text(self):
        name = "获取文本：投票的titie"
        self.wait_eleVisible(ntl.vote_title_text, model=name)
        return self.get_text(ntl.vote_title_text, model=name).strip()           # 返回字符串时处理空格

    # 获取文本：发布投票截止时间(年-月-日)
    def get_vote_end_time(self):
        name = "获取文本：发布投票截止时间(年-月-日)"
        self.wait_eleVisible(ntl.post_vote_cutoff_time, model=name)
        date = self.get_text(ntl.post_vote_cutoff_time, model=name)
        return re.split(':| ', date)[1]

    # 获取n天后时间
    def get_n_end_time(self, day_n):
        day_n_time = (datetime.datetime.now() + datetime.timedelta(days=day_n)).strftime("%Y-%m-%d")
        return day_n_time

    # 获取文本：全部tab中发布的投票内容
    def get_post_vote_text(self):
        name = "获取文本：全部tab中发布的投票内容"
        self.wait_eleVisible(ntl.post_vote_text, model=name)
        return self.get_text(ntl.post_vote_text, model=name).strip()

    # 获取文本：全部tab中发布的選項内容
    def get_post_vote_Option_text(self):
        name = "获取文本：全部tab中发布的選項内容"
        self.wait_eleVisible(ntl.post_vote_Option_text, model=name)
        return self.get_text(ntl.post_vote_Option_text, model=name).strip()

    # 點擊：帖子點讚計數icon
    def click_post_like_count_icon(self):
        name = "點擊：帖子點讚計數icon"
        self.wait_eleVisible(ntl.post_like_count_icon, model=name)
        self.click_element(ntl.post_like_count_icon, model=name)
        return self

    # 獲取文本：「讚好帖子」頁面-點讚數
    def get_like_page_count(self):
        name = "獲取文本：「讚好帖子」頁面-點讚數"
        self.wait_eleVisible(ntl.like_page_count, model=name)
        return int(self.get_text(ntl.like_page_count, model=name))

    # 點擊：帖子點讚icon
    def click_post_like_icon(self):
        name = "點擊：帖子點讚icon"
        self.wait_eleVisible(ntl.post_like_icon, model=name)
        self.click_element(ntl.post_like_icon, model=name)
        return self

    # 點擊：帖子留言icon
    def click_post_comment_icon(self):
        name = "點擊：帖子留言icon"
        self.wait_eleVisible(ntl.all_tab_post_user_avatar, model=name)
        a = 0
        while self.find_post_comment_icon() == False:
            self.swipe_screen(0.5,0.8,0.5,0.6)
            a = a + 1
            if a >= 6:
                break
        self.click_element(ntl.post_comment_icon, model=name)
        time.sleep(2)
        return self

    # 查找:帖子留言icon
    def find_post_comment_icon(self):
        name = '查找:帖子留言icon'
        time.sleep(1)
        try:
            self.get_element(ntl.post_comment_icon, model=name)
            return True
        except:
            return False

    # 点击：全部tab-拍摄icon
    def click_personal_tab_photo_icon(self):
        name = "点击：全部tab-拍摄icon"
        self.wait_eleVisible(ntl.personal_tab_photo_icon, model=name)
        self.click_element(ntl.personal_tab_photo_icon, model=name)
        return self

    # 輸入文本：帖子詳情頁留言輸入框
    def input_post_page_comment_input(self,text):
        name = "輸入文本：帖子詳情頁留言輸入框"
        self.wait_eleVisible(ntl.post_page_comment_input, model=name)
        self.input_text(ntl.post_page_comment_input,text, model=name)
        return self

    # 獲取文本：留言次數
    def get_post_comment_number_icon(self):
        name = "獲取文本：留言次數"
        self.wait_eleVisible(ntl.post_comment_number_icon, model=name)
        data = self.get_text(ntl.post_comment_number_icon, model=name)
        time.sleep(1)
        return int(data.split(' ')[0])

    # 點擊：留言「發布」按鈕
    def click_comment_release_button(self):
        name = "點擊：留言「發布」按鈕"
        self.wait_eleVisible(ntl.comment_release_button, model=name)
        self.click_element(ntl.comment_release_button, model=name)
        return self

    # 多次留言
    def comment_double(self,number,text):
        a = 1
        while a <= number:
            self.input_post_page_comment_input(text)
            logging.info("第{}次留言".format(a))
            self.click_comment_release_button()
            self.wait_qroup_loading_icon()
            time.sleep(1)
            a = a+1
        return self

    # 點擊：帖子分享icon
    def click_post_share_icon(self):
        name = "點擊：帖子分享icon"
        self.wait_eleVisible(ntl.post_share_icon, model=name)
        self.click_element(ntl.post_share_icon, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 獲取文本：分享次數
    def get_post_share_number_icon(self):
        name = "獲取文本：分享次數"
        self.wait_eleVisible(ntl.post_share_number_icon, model=name)
        data = self.get_text(ntl.post_share_number_icon, model=name)
        return int(data.split(' ')[0])

    # 點擊：帖子文本進入詳情頁
    def click_personal_tab_post_text(self):
        name = "點擊：帖子文本進入詳情頁"
        self.wait_eleVisible(ntl.personal_tab_post_text, model=name)
        self.click_element(ntl.personal_tab_post_text, model=name)
        return self

    # 點擊：「分享」-分享
    def click_post_share_to_share(self):
        name = "點擊：「分享」-分享"
        self.wait_eleVisible(ntl.post_share_to_share, model=name)
        self.click_element(ntl.post_share_to_share, model=name)
        name = "[分享動態]頁面-分享按鈕"
        self.wait_eleVisible(ntl.share_to_done, model=name)
        self.click_element(ntl.share_to_done, model=name)           # [分享動態]頁面-分享按鈕
        return self

    # 點擊：「分享至sp」
    def click_post_share_to_sp(self):
        name = "點擊：「分享至sp」"
        self.wait_eleVisible(ntl.post_share_to_sp, model=name)
        self.text_find_and_click("分享至", model=name)
        name = "选择一个群组"
        self.wait_eleVisible(ntl.post_share_to_sp_user, model=name)
        self.click_element(ntl.post_share_to_sp_user, model=name)
        return self

    # 隨機向上滑屏
    def random_swipe(self,number):
        name = "隨機向上滑屏"
        self.wait_eleVisible(ntl.personal_post_entrance_icon, model=name)
        a = 1
        while a <= number:
            self.swipe_screen(0.5,0.9,0.5,0.3, model=name)
            time.sleep(1)
            a = a + 1

    # 查找：帖子下方分享icon
    def find_personal_post_share_icon(self):
        name = "查找：帖子下方分享icon"
        time.sleep(2)
        try:
            self.get_element(ntl.personal_post_share_icon, model=name)
            return True
        except:
            return False

    # 點擊：個人tab下方帖子分享icon
    def click_personal_post_share_icon(self):
        name = "點擊：個人tab下方帖子分享icon"
        a = 1
        while self.find_personal_post_share_icon() == False:
            self.swipe_screen(0.5,0.8,0.5,0.6, model=name)
            a = a + 1
            time.sleep(2)
            if a > 10:
                break
        self.wait_eleVisible(ntl.personal_post_share_icon, model=name)
        self.click_element(ntl.personal_post_share_icon, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 點擊：分享icon-下拉選項「分享」
    def click_personal_post_share_to_share(self):
        name = '點擊：分享icon-下拉選項「分享」'
        self.wait_eleVisible(ntl.post_share_to_share, model=name)
        self.click_element(ntl.post_share_to_share, model=name)
        return self

    # 點擊：'分享動態'頁面-分享至跳轉选项群组并点击【完成】按钮
    def click_share_nf_Jump_icon(self):
        name = "點擊：'分享動態'頁面-分享至跳轉选项群组并点击【完成】按钮"
        self.wait_eleVisible(ntl.share_nf_Jump_icon, model=name)
        self.click_element(ntl.share_nf_Jump_icon, model=name)                  # 点击【分享至】跳转按钮
        name = "选择一个群组"
        self.wait_eleVisible(ntl.share_nf_group_list, model=name)
        self.find_elements(ntl.share_nf_group_list, model=name)[1].click()      # 选择一个群组
        name = "点击【完成】按钮"
        self.wait_eleVisible(ntl.share_nf_group_done, model=name)
        self.click_element(ntl.share_nf_group_done, model=name)             # 点击【完成】按钮
        return self

    # 输入文本：'分享動態'頁面-输入框
    def input_share_nf_input(self,text):
        name = "输入文本：'分享動態'頁面-输入框"
        self.wait_eleVisible(ntl.share_nf_input, model=name)
        self.input_text(ntl.share_nf_input,text, model=name)
        return self

    # 點擊：'分享動態'頁面-「分享」按鈕
    def click_share_to_done(self):
        name = "點擊：'分享動態'頁面-「分享」按鈕"
        self.wait_eleVisible(ntl.share_to_done, model=name)
        self.click_element(ntl.share_to_done, model=name)               # [分享動態]頁面-分享按鈕
        return self

    # 點擊：【标注人名】选项
    def click_callout_name(self):
        name = "點擊：【标注人名】选项"
        self.wait_eleVisible(ntl.callout_name, model=name)
        self.find_elements(ntl.callout_name, model=name)[3].click()
        return self

    # 獲取文本：'标注人名'頁面-列表第一個用戶暱稱
    def get_callout_name_page_list_name(self):
        name = "獲取文本：'标注人名'頁面-列表第一個用戶暱稱"
        self.wait_eleVisible(ntl.callout_name_page_list_name, model=name)
        return self.get_text(ntl.callout_name_page_list_name, model=name)

    # 點擊：'标注人名'頁面-列表第一個用戶
    def click_callout_name_page_list_name(self):
        name = "點擊：'标注人名'頁面-列表第一個用戶"
        self.wait_eleVisible(ntl.callout_name_page_list_name, model=name)
        self.click_element(ntl.callout_name_page_list_name, model=name)         # 點擊列表中第一個用戶
        self.wait_eleVisible(ntl.callout_name_page_done, model=name)
        self.click_element(ntl.callout_name_page_done, model=name)              # 點擊「完成」按鈕
        return self

    # 獲取文本：帖子展示的用戶名欄
    def get_post_user_name(self):
        name = "獲取文本：帖子展示的用戶名欄"
        self.wait_eleVisible(ntl.post_user_name, model=name)
        data =  self.get_text(ntl.post_user_name, model=name)
        return re.split('和 | ',data)[-2]

    # 點擊：跳轉帖子詳情頁（暱稱欄）
    def click_post_user_name(self):
        name = "點擊：跳轉帖子詳情頁（暱稱欄）"
        self.wait_eleVisible(ntl.post_user_name, model=name)
        self.click_element(ntl.post_user_name, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 查找：帖子详情页查找点赞icon
    def find_post_page_like_icon(self):
        name = "查找：帖子详情页查找点赞icon"
        time.sleep(2)
        try:
            self.get_element(ntl.post_page_like_icon, model=name)
            return True
        except:
            return False

    # 帖子详情页处理点赞icon可见
    def action_post_page_like_icon(self):
        if self.find_post_page_like_icon() == False:
            self.swipe_screen(0.5,0.8,0.5,0.6)
        return self

    # 获取帖子详情页点赞次数
    def get_post_detail_like_count_icon_number(self):
        self.action_post_page_like_icon()
        number = self.get_post_detail_like_count_icon()
        return number

    # 點擊：【相片/影片】选项
    def click_movie_photo(self):
        name = "點擊：【相片/影片】选项"
        self.wait_eleVisible(ntl.callout_name, model=name)
        self.find_elements(ntl.callout_name, model=name)[4].click()
        return self

    # 選擇多張圖片
    def click_douber_photo_send_button(self,photo_number):
        name = "選擇多張圖片"
        self.wait_eleVisible(ntl.photo_Check_button, model=name)
        time.sleep(2)
        for i in range(photo_number):
            self.find_elements(ntl.photo_Check_button, model=name)[i].click()
        return self

    # 获取：相册中照片相册数量
    def get_photo_Check_button_number(self):
        name = '获取：相册中照片相册数量'
        self.wait_eleVisible(ntl.photo_Check_button, model=name)
        return len(self.find_elements(ntl.photo_Check_button, model=name))

    # 點擊：「傳送」按鈕
    def click_photo_send_button(self):
        name = "點擊：「傳送」按鈕"
        self.wait_eleVisible(ntl.photo_send_button, model=name)
        self.click_element(ntl.photo_send_button, model=name)  # 點擊「傳送」按鈕
        return self

    # 獲取：照片選擇頁面照片的張數
    def get_photo_sum(self):
        time.sleep(2)
        return len(self.find_elements(ntl.photo_Check_button))

    # 點擊：指定的照片
    def click_index_photo(self,index):
        name = "點擊：指定的照片"
        self.wait_eleVisible(ntl.photo_Check_button, model=name)
        self.find_elements(ntl.photo_Check_button, model=name)[index].click()
        return self

    # 查找:删除图片按钮
    def find_photo_delete_button(self):
        name = "查找删除图片按钮"
        time.sleep(2)
        try:
            self.get_element(ntl.publish_input, model=name)
            return True
        except:
            logging.exception("删除照片按钮未找到")
            return False

    # 點擊：照片刪除按鈕
    def click_photo_delete_button(self):
        name = "點擊：照片刪除按鈕"
        if self.find_photo_delete_button() == False:
            self.swipe_screen(0.5,0.6,0.5,0.8)
            time.sleep(1)
        self.wait_eleVisible(ntl.photo_delete_button, model=name)
        self.find_elements(ntl.photo_delete_button, model=name)[1].click()
        return self

    # 查找："內容不能為空"tost
    def find_send_text_void_tost(self):
        name = '查找："內容不能為空"tost'
        try:
            self.get_toast_tips("內容不能為空", model=name)
            return True
        except:
            return False

    # 查找：[放棄發布]按鈕
    def find_return_quit_draft(self):
        name = '查找：[放棄發布]按鈕'
        time.sleep(1)
        try:
            self.get_element(ntl.return_quit_draft, model=name)
            return True
        except:
            return False

    # 如果有彈出[放棄發布]按鈕則點擊
    def is_click_return_quit_draft(self):
        name = "如果有彈出[放棄發布]按鈕則點擊"
        if self.find_return_quit_draft() == True:
            self.click_element(ntl.return_quit_draft, model=name)
        return self

    # 查找："最多只能選擇9張"tost
    def find_fuck_photo_sum_tost(self):
        name = '查找："最多只能選擇9張"tost'
        try:
            self.get_toast_tips("最多只能選擇9張", model=name)
            return True
        except:
            return False

    # 查找：【返回】按钮
    def find_return_button(self):
        name = '查找：【返回】按钮'
        time.sleep(2)
        try:
            self.get_element(ntl.set_post_page_return, model=name)
            return True
        except:
            return False

    # 处理发送图片失败，退出回到首页
    def process_send_failure(self):
        name = '处理发送图片失败，退出回到首页'
        if self.find_return_button() == True:
            self.return_button()
            time.sleep(1)
            self.wait_eleVisible(ntl.return_quit_draft, model=name)
            self.click_element(ntl.return_quit_draft, model=name)
        return self

    # 選擇照片頁面-「取消」按鈕
    def click_photo_page_cancel_button(self):
        name = '選擇照片頁面-「取消」按鈕'
        self.wait_eleVisible(ntl.photo_page_cancel_button, model=name)
        self.click_element(ntl.photo_page_cancel_button, model=name)
        return self

    # 點擊：【拍照】选项
    def click_action_photo(self):
        name = "點擊：【拍照】选项"
        self.wait_eleVisible(ntl.callout_name, model=name)
        self.find_elements(ntl.callout_name, model=name)[2].click()
        return self

    # 點擊：快門icon
    def click_personal_tab_shutter_button(self):
        name = '點擊：快門icon'
        self.wait_eleVisible(ntl.personal_tab_shutter_button, model=name)
        self.click_element(ntl.personal_tab_shutter_button, model=name)
        time.sleep(3)
        return self

    # 長按：拍攝視頻4s
    def long_tap_personal_tab_shutter_button(self):
        name = "長按：拍攝視頻4s"
        self.wait_eleVisible(ntl.personal_tab_shutter_button, model=name)
        time.sleep(1)
        self.long_press_action(ntl.personal_tab_shutter_button, model=name)
        time.sleep(3)
        return self

    # 長按拍摄视频4s后并上滑取消
    def long_tap_slide(self):
        name = "長按拍摄视频4s后并上滑取消"
        self.wait_eleVisible(ntl.personal_tab_shutter_button, model=name)
        time.sleep(1)
        self.long_press_action_slide_cancel(ntl.personal_tab_shutter_button, model=name)
        time.sleep(2)
        return self

    # 查找：快門icon
    def find_personal_tab_shutter_button(self):
        name = "查找：快門icon"
        time.sleep(2)
        try:
            self.get_element(ntl.personal_tab_shutter_button, model=name)
            return True
        except:
            return False

    # 點擊：[重做]按鈕
    def click_personal_tab_media_cancel(self):
        name = "點擊：[重做]按鈕"
        self.wait_eleVisible(ntl.personal_tab_media_cancel, model=name)
        self.click_element(ntl.personal_tab_media_cancel, model=name)
        return self

    # 點擊：拍照頁面-「傳送」按鈕
    def click_personal_tab_send_button(self):
        name = "點擊：拍照頁面-「傳送」按鈕"
        self.wait_eleVisible(ntl.personal_tab_send_button, model=name)
        self.click_element(ntl.personal_tab_send_button, model=name)
        time.sleep(2)
        return self

    # 查找：帖子發布成功toast提示
    def find_toast_send_success(self):
        name = '查找：帖子發布成功toast提示'
        try:
            self.get_toastMsg("發布成功", model=name)
            return True
        except:
            return False

    # 查找：[存為草稿]按鈕
    def find_save_draft_button(self):
        name = '查找：[存為草稿]按鈕'
        time.sleep(1)
        try:
            self.text_find('存為草稿', model=name)
            return True
        except:
            return False

    # 點擊：[存為草稿]按鈕
    def click_save_draft_button(self):
        name = '點擊：[存為草稿]按鈕'
        self.wait_eleVisible(ntl.save_draft_button, model=name)
        self.text_find_and_click('存為草稿', model=name)
        return self

    # 查找：[放棄發布]按鈕
    def find_abandon_post_button(self):
        name = '查找：[放棄發布]按鈕'
        time.sleep(1)
        try:
            self.text_find('放棄發布', model=name)
            return True
        except:
            return False

    # 點擊：[放棄發布]按鈕
    def click_abandon_post_button(self):
        name = '點擊：[放棄發布]按鈕'
        self.wait_eleVisible(ntl.abandon_post_button, model=name)
        self.text_find_and_click('放棄發布', model=name)
        return self

    # 點擊：'建立群組'頁面-「新增封面相片」
    def click_create_group_avatar_icon(self):
        name = "點擊：'建立群組'頁面-「新增封面相片」"
        self.wait_eleVisible(ntl.create_group_avatar_icon, model=name)
        self.click_element(ntl.create_group_avatar_icon, model=name)
        time.sleep(2)
        return self

    # 查找：「新增封面相片」-[相冊]
    def find_avatar_photo_icon(self):
        name = "查找：「新增封面相片」-[相冊]"
        time.sleep(2)
        try:
            self.get_element(ntl.avatar_photo_always, model=name)
            logging.info("弹出访问相册方式")
            return True
        except:
            return False

    # 查找：相册-【分类】tab
    def find_class_photo_tab(self):
        time.sleep(1)
        try:
            self.text_find("分类")
            return True
        except:
            return False

    # 進入相冊頁面
    def click_avatar_photo_icon(self):
        name = '進入相冊頁面'
        if self.find_avatar_photo_icon() == True:
            self.wait_eleVisible(ntl.avatar_photo_icon, model=name)
            self.find_elements(ntl.avatar_photo_icon, model=name)[1].click()        # 點擊：「相冊」
            self.wait_eleVisible(ntl.avatar_photo_always, model=name)
            self.click_element(ntl.avatar_photo_always, model=name)                 # 點擊：[相冊]-[始终]
        if self.find_class_photo_tab() == True:
            self.tap_click_ele(0.5,0.33)
        name = '點擊：[图片]tab'
        self.wait_eleVisible(ntl.avater_photo_button, model=name)
        self.click_element(ntl.avater_photo_button, model=name)                     # 點擊：[图片]tab
        return self

    # 點擊：相冊頁面選擇一張圖片
    def click_select_one_photo(self):
        name = "點擊：相冊頁面選擇一張圖片"
        time.sleep(2)
        self.wait_eleVisible(ntl.avatar_photo_list, model=name)
        self.click_element(ntl.avatar_photo_list, model=name)
        time.sleep(1)
        logging.info("選擇照片成功")
        return self

    # 點擊：'建立群組'頁面-[私密]單選按鈕
    def click_create_group_private_icon(self):
        name = "點擊：'建立群組'頁面-[私密]單選按鈕"
        self.click_element(ntl.create_group_private_icon, model=name)
        self.click_element(ntl.create_group_private_icon, model=name)
        return self

    # --------------------------- 【搜索】相关元素操作  ------------------------------------------------

    # 点击【搜索】按钮
    def click_search_button(self):
        name = "点击【搜索】按钮"
        self.wait_eleVisible(ntl.search_button, model=name)
        self.click_element(ntl.search_button, model=name)
        return self

    # 输入文本，进行搜索
    def input_search_text(self, text):
        name = "输入文本，进行搜索"
        self.wait_eleVisible(ntl.search_input, model=name)
        self.input_text(ntl.search_input, text, model=name)  # 输入文本
        time.sleep(1)
        self.keyboard_search(model=name)  # 点击系统命令触发搜索
        time.sleep(1)
        self.screenshot("触发搜索后的截图")
        self.wait_qroup_loading_icon()      # load加载
        return self

    # 全部展示下，查找‘查看全部’按钮
    def is_find_view(self):
        time.sleep(2)
        self.wait_qroup_loading_icon()
        try:
            self.text_find("查看全部")
            return True
        except:
            return False

    # 获取搜索用户【追踪】按钮的文本(判断是否被追踪)
    def get_search_user_track_button_text(self):
        self.wait_eleVisible(ntl.search_user_track_button)
        return self.get_text(ntl.search_user_track_button)

    # 點擊：搜索-用戶「追蹤」按鈕
    def click_search_user_track_button(self):
        name = '點擊：搜索-用戶「追蹤」按鈕'
        self.wait_eleVisible(ntl.search_user_track_button, model=name)
        self.click_element(ntl.search_user_track_button, model=name)
        return self

    # 全部展示下，查找用户‘查看全部’按钮
    def is_find_user_all_button(self):
        name = "全部展示下，查找用户‘查看全部’按钮"
        time.sleep(2)
        self.wait_eleVisible_pass(ntl.view_user_all_button, model=name)
        try:
            self.get_element(ntl.view_user_all_button, model=name)
            return True
        except:
            return False

    # 全部展示下，查找贴文‘查看全部’按钮
    def is_find_post_all_button(self):
        name = "全部展示下，查找贴文‘查看全部’按钮"
        time.sleep(2)
        self.wait_eleVisible_pass(ntl.view_post_all_button, model=name)
        try:
            self.get_element(ntl.view_post_all_button, model=name)
            return True
        except:
            return False

    # 用户下，查找‘追蹤’按钮
    def is_find_track(self):
        name = "用户下，查找‘追蹤’按钮"
        time.sleep(1)
        try:
            self.get_element(ntl.search_user_track_button, model=name)
            return True
        except:
            return False

    # 群组筛选-查找【公开群组】按钮
    def is_find_public_group_button(self):
        name = "群组筛选-查找【公开群组】按钮"
        self.wait_eleVisible_pass(ntl.public_group_icon, model=name)
        try:
            self.get_element(ntl.public_group_icon, model=name)
            return True
        except:
            return False

    # 点击【贴文】按钮
    def click_poat_button(self):
        name = "点击【贴文】按钮"
        self.wait_eleVisible(ntl.poat_button, model=name)
        self.click_element(ntl.poat_button, model=name)
        return self

    # 点击【群组】按钮
    def click_group_button(self):
        name = "点击【群组】按钮"
        self.wait_eleVisible(ntl.group_button, model=name)
        self.click_element(ntl.group_button, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 点击【用户】按钮
    def click_user_button(self):
        name = "点击【用户】按钮"
        self.wait_eleVisible(ntl.user_button, model=name)
        self.click_element(ntl.user_button, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 獲取索引：搜索'群組'第一個可追蹤的索引
    def get_search_group_track_button_index(self):
        name = "獲取索引：搜索'群組'第一個可追蹤的索引"
        self.wait_eleVisible(ntl.search_group_track_button, model=name)
        group_number = len(self.find_elements(ntl.search_group_track_button, model=name))
        logging.info("获取当前页面搜索群组个数为'{}'".format(group_number))
        for index in range(0,group_number):
            if self.find_elements(ntl.search_group_track_button, model=name)[index].text == '追蹤':
                return int(index)

    # 點擊：根據索引點擊指定的「追蹤」按鈕
    def click_index_search_group_track_button(self,index):
        name = "點擊：根據索引點擊指定的「追蹤」按鈕"
        self.wait_eleVisible(ntl.search_group_track_button, model=name)
        self.find_elements(ntl.search_group_track_button, model=name)[index].click()
        time.sleep(1)
        logging.info("點擊列表中第'{}'個「追蹤」按鈕正常".format(index+1))
        return self

    # 點擊：根據索引點擊指定的群組名稱
    def click_index_search_group_name_list(self,index):
        name = "點擊：根據索引點擊指定的群組名稱"
        self.wait_eleVisible(ntl.search_group_name_list, model=name)
        self.find_elements(ntl.search_group_name_list, model=name)[index].click()
        logging.info("點擊列表中第'{}'個群組名稱正常".format(index+1))
        time.sleep(2)
        self.wait_qroup_loading_icon()
        return self

    # 獲取文本：根據索引獲取button文案
    def get_search_group_track_button(self,index):
        name = '獲取文本：根據索引獲取button文案'
        self.wait_eleVisible(ntl.search_group_track_button, model=name)
        return self.find_elements(ntl.search_group_track_button, model=name)[index].text

    # 獲取索引(用戶)：搜索'用戶'第一個可追蹤的索引
    def get_search_user_track_button_index(self):
        name ="獲取索引(用戶)：搜索'用戶'第一個可追蹤的索引"
        self.wait_eleVisible(ntl.search_user_track_button , model=name)
        user_number = len(self.find_elements(ntl.search_user_track_button, model=name))
        logging.info("获取当前页面搜索用戶个数为'{}'".format(user_number))
        for index in range(0, user_number):
            if self.find_elements(ntl.search_user_track_button, model=name)[index].text == '追蹤':
                return index

    # 點擊(用戶)：根據索引點擊指定的「追蹤」按鈕
    def click_index_search_user_track_button(self, index):
        name = "點擊(用戶)：根據索引點擊指定的「追蹤」按鈕"
        self.wait_eleVisible(ntl.search_user_track_button, model=name)
        self.find_elements(ntl.search_user_track_button, model=name)[index].click()
        time.sleep(1)
        logging.info("點擊列表中第'{}'個「追蹤」按鈕正常".format(index + 1))
        return self

    # 點擊(用戶)：根據索引點擊指定的用戶名稱
    def click_index_search_user_name_list(self, index):
        name = "點擊(用戶)：根據索引點擊指定的用戶名稱"
        self.wait_eleVisible(ntl.search_user_name_list, model=name)
        self.find_elements(ntl.search_user_name_list, model=name)[index].click()
        logging.info("點擊列表中第'{}'個用戶名稱正常".format(index + 1))
        time.sleep(2)
        self.wait_qroup_loading_icon()
        return self

    # 獲取文本(用戶)：根據索引獲取button文案
    def get_search_user_track_button(self, index):
        name = "獲取文本(用戶)：根據索引獲取button文案"
        self.wait_eleVisible(ntl.search_user_track_button, model=name)
        return self.find_elements(ntl.search_user_track_button, model=name)[index].text

    # 点击搜索页-【取消】按钮
    def click_cancel_button(self):
        name = "点击搜索页-【取消】按钮"
        self.wait_eleVisible(ntl.cancel_button, model=name)
        self.click_element(ntl.cancel_button, model=name)
        return self

    # 判断：个人tab-帖子更多icon是否可见
    def if_personal_tab_post_more_button(self):
        name = "判断：个人tab-帖子更多icon是否可见"
        time.sleep(1)
        try:
            self.get_element(ntl.personal_tab_post_more_button, model=name)
            return True
        except:
            return  False

    # 点击：个人tab-帖子更多icon
    def click_personal_tab_post_more_button(self):
        name = "点击：个人tab-帖子更多icon"
        self.wait_eleVisible(ntl.personal_tab_post_more_button, model=name)
        self.click_element(ntl.personal_tab_post_more_button, model=name)
        return self

    # 獲取文本：[追蹤更多]頁面個人tab中第一個"追蹤"的用戶名
    def get_first_track_name(self, index):
        name = '頁面個人tab追踪列表中中第一個"追蹤"的用戶名稱'
        self.wait_eleVisible(ntl.personal_fans_first_username, model=name)
        user_name = self.find_elements(ntl.personal_fans_first_username, model=name)[index].text
        logging.info("第一個可「追蹤」的用戶暱稱為'{}'".format(user_name))
        return user_name

    # 点击搜索框,输入文本，进行搜索
    def input_search_fan_username(self, user_name1):
        name = "点击搜索框,输入文本，进行搜索"
        input_text2 = str(user_name1).split(" ")[1]
        self.wait_eleVisible(ntl.personal_fans_first_text, model=name)
        self.click_element(ntl.track_more_search_box, model=name)
        for i in input_text2:
            self.adb_keycode(keycode.get(i))
        self.keyboard_search(model=name)  # 点击系统命令触发搜索
        time.sleep(1)
        self.screenshot("触发搜索后的截图")
        self.wait_qroup_loading_icon()  # load加载
        return self

    # 点击搜索显示用户名进行跳转到用户中心
    def user_name_to_jump(self):
        name = '點擊："搜索出的用户名称进行跳转"'
        self.wait_eleVisible(ntl.list_one_search_name, model=name)
        self.click_element(ntl.list_one_search_name, model=name)
        return self

    # 点击搜索粉丝名称滑屏至第一个动态留言icon可见为止
    def swipe_personal_search_message(self):
        name = '点击搜索粉丝名称滑屏至第一个动态留言icon可见为止:'
        self.wait_eleVisible(ntl.all_tab_post_user_avatar, model=name)  # 等待帖子列表数据加载成功
        self.swipe_screen(0.5, 0.4, 0.5, 0.6, model='下拉刷新')
        self.wait_qroup_loading_icon()  # 加载
        a = 0
        while self.find_personal_message_icon() == False:
            self.swipe_screen(0.5, 0.8, 0.5, 0.6, model=name)
            a = a + 1
            if a >= 5:
                break
        return self

    # 获取留言次数
    def get_message_count_icon(self):
        name = "获取点击搜索粉丝名跳转后第一个留言的个数"
        self.wait_eleVisible(ntl.first_message_count, model=name)
        data = self.get_text(ntl.first_message_count, model=name)
        time.sleep(1)
        return int(data.split(' ')[0])

        # 点击搜索粉丝名称跳转给一个帖子留言

    def search_click_first_message_icon(self):
        name = "点击搜索粉丝名称跳转给一个帖子留言"
        self.wait_eleVisible(ntl.all_tab_post_user_avatar, model=name)
        a = 0
        while self.find_post_comment_icon() == False:
            self.swipe_screen(0.5, 0.8, 0.5, 0.6)
            a = a + 1
            if a >= 6:
                break
        self.click_element(ntl.first_message_icon, model=name)
        time.sleep(2)
        return self

    def swipe_personal_search_share2(self):
        name = '点击搜索粉丝名称滑屏至第一个动态留言icon可见为止:'
        self.wait_eleVisible(ntl.all_tab_post_user_avatar, model=name)  # 等待帖子列表数据加载成功
        self.swipe_screen(0.5, 0.4, 0.5, 0.85, model='下拉刷新')
        self.wait_qroup_loading_icon()  # 加载
        a = 0
        while self.find_personal_message_icon() == False:
            self.swipe_screen(0.5, 0.8, 0.5, 0.6, model=name)
            a = a + 1
            if a >= 5:
                break
        return self

    # 查找点击搜索粉丝名第一个动态评论icon
    def find_personal_message_icon(self):
        name = "查找点击搜索粉丝名第一个动态评论icon"
        time.sleep(2)
        try:
            self.get_element(ntl.first_message_icon, model=name)  # 查找可留言第一个分享icon
            return True
        except:
            return False

    def swipe_personal_search_share(self):
        name = '点击搜索粉丝名称滑屏至第一个分享icon可见为止:'
        self.wait_eleVisible(ntl.all_tab_post_user_avatar, model=name)  # 等待帖子列表数据加载成功
        self.swipe_screen(0.5, 0.4, 0.5, 0.6, model='下拉刷新')
        self.wait_qroup_loading_icon()  # 加载
        a = 0
        while self.find_personal_share_icon() == False:
            self.swipe_screen(0.5, 0.8, 0.5, 0.6, model=name)
            a = a + 1
            if a >= 5:
                break
        return self

    # 查找点击搜索粉丝名第一个分享icon
    def find_personal_share_icon(self):
        name = "查找点击搜索粉丝名第一个分享icon"
        time.sleep(2)
        try:
            self.get_element(ntl.first_share_icon, model=name)  # 查找可留言第一个分享icon
            return True
        except:
            return False

      # 获取分享次数
    def get_share_count_icon(self):
        name = "获取点击搜索粉丝名跳转后第一个分享的个数"
        self.wait_eleVisible(ntl.first_share_count, model=name)
        data = self.get_text(ntl.first_share_count, model=name)
        time.sleep(1)
        return int(data.split(' ')[0])

    def search_click_first_share_icon(self):
        name = "点击搜索粉丝名称跳转给一个帖子分享"
        self.wait_eleVisible(ntl.first_share_icon, model=name)
        a = 0
        while self.find_post_comment_icon() == False:
            self.swipe_screen(0.5,0.8,0.5,0.6)
            a = a + 1
            if a >= 6:
                break
        self.click_element(ntl.first_share_icon, model=name)
        self.wait_qroup_loading_icon()
        time.sleep(2)
        return self

    def group_name_to_jump(self):
        name = '點擊："搜索出的群组名称进行跳转"'
        self.wait_eleVisible(ntl.trace_group_Avatar, model=name)
        self.click_element(ntl.trace_group_Avatar, model=name)
        return self

    # 点击：【提交投票】icon
    def click_submit_to_vote_icon(self):
        name = "点击：提交投票"
        self.wait_eleVisible(ntl.submit_to_vote, model=name)
        self.click_element(ntl.submit_to_vote, model=name)
        return self

    # 选择天数
    def choose_days(self, index):
        name = "點擊：[投票結束時間]選項选择天数"
        self.wait_eleVisible(ntl.choose_day, model=name)
        self.find_elements(ntl.choose_day, model=name)[index].click()
        return self

    #点击投票单选
    def click_one_select(self,index):
        name = "投票单选"
        self.wait_eleVisible(ntl.one_select,model=name)
        self.find_elements(ntl.one_select, model=name)[index].click()
        logging.info("选项列表中第{}个投票成功".format(index + 1))
        self.click_push_vote()
        return self

    def find_vote_button(self):
        time.sleep(2)
        try:
            self.get_element("提交投票")
            return True
        except:
            return False

    # 點擊：[可多选]選項
    def can_more_select(self):
        name = "點擊：[可多选]選項"
        self.wait_eleVisible(ntl.more_select, model=name)
        self.click_element(ntl.more_select, model=name)
        return self

    # 投票多选
    def select_more_select(self, index):
        name = "投票多选"
        self.wait_eleVisible(ntl.one_select, model=name)
        self.find_elements(ntl.one_select, model=name)[index].click()
        return self

    # 提交投票
    def push_vote_more(self):
        time.sleep(2)
        self.click_push_vote()
        return self

    # 点击：[提交投票]按钮
    def click_push_vote(self):
        name = "点击：[提交投票]选项"
        self.wait_eleVisible(ntl.push_vote, model=name)
        self.click_element(ntl.push_vote, model=name)
        return self

    # 點擊：邀请
    def click_invitation(self):
        name = "點擊：邀请"
        time.sleep(1)
        self.wait_eleVisible(ntl.the_invitation,model=name)
        self.click_element(ntl.the_invitation, model=name)
        return self

    # 獲取文本：邀请成员中第一個成员用戶名
    def get_first_member_name(self, index):
        name = '獲取文本：邀请成员中第一個成员用戶名'
        self.wait_eleVisible(ntl.callout_name_page_list_name, model=name)
        member_name = self.find_elements(ntl.callout_name_page_list_name, model=name)[index].text
        logging.info("邀请成员中第一個成员用戶名'{}'".format(member_name))
        return member_name

        # 點擊：搜索出来的成员

    def click_search_one_member(self):
        name = "點擊：搜索出来的成员"
        time.sleep(1)
        self.wait_eleVisible(ntl.search_one_member, model=name)
        self.click_element(ntl.search_one_member, model=name)
        return self

    # 點擊：完成
    def click_finish(self):
        name = "點擊：完成"
        time.sleep(1)
        self.wait_eleVisible(ntl.add_member_done_button, model=name)
        self.click_element(ntl.add_member_done_button, model=name)
        return self

    # 查找：toast提示"success"
    def find_toast_invitation_success(self):
        name = '查找：toast提示"已成功邀請1人加入群組"'
        try:
            self.get_toast_tips("已成功邀請1人加入群組", model=name)
            return True
        except:
            return False

    # 点击：通知tab
    def click_notice_tab(self):
        name = "点击：通知tab"
        self.wait_eleVisible(ntl.notice_tab, model=name)
        self.click_element(ntl.notice_tab, model=name)
        return self

    # 点击【聊天】tab
    def click_chat_tab(self):
        name = "点击【聊天】tab"
        self.wait_eleVisible(ntl.chat_tab, model=name)
        self.click_element(ntl.chat_tab, model=name)
        return self

    # 双击【聊天】tab
    def double_click_chat_tab(self):
        name = "双击【聊天】tab"
        self.Action_double_tap(ntl.chat_tab, model=name)
        return self

    # 查找：通知tab数据是否展示正常
    def find_notice_list_message(self):
        name = "查找：通知tab数据是否展示正常"
        self.wait_eleVisible_pass(ntl.notice_list_message,wait_times=10, poll_frequency=0.5, model=name)
        try:
            self.get_element(ntl.notice_list_message, model=name)
            return True
        except:
            return False

    # 查找：个人tab中数据是否加载完成
    def find_user_homepage_name(self):
        name = "查找：个人tab中数据是否加载完成"
        self.wait_eleVisible_pass(ntl.user_homepage_name,wait_times=10, poll_frequency=0.5, model=name)
        try:
            self.get_element(ntl.user_homepage_name, model=name)
            return True
        except:
            return False

    # 点击：手机主页APP图标进入APP中
    def click_home_app_name(self):
        name = "点击：手机主页APP图标进入APP中"
        self.text_find_and_click("SunPeopleQA", model=name)
        time.sleep(1)
        return self

    # 处理app至当前页面可见
    def Action_app_home_vis(self):
        if self.find_app_Subscript() == False:
            self.swipe_screen(0.2,0.5,0.8,0.5)
            time.sleep(1)
            self.swipe_screen(0.2, 0.5, 0.8, 0.5)     # 右滑屏
            time.sleep(1)
            number = 1
            while self.find_app_Subscript() == False:
                self.swipe_screen(0.8, 0.5, 0.2, 0.5)   # 左滑屏
                logging.info("第 {} 次滑屏查找SP APP图标".format(number))
                time.sleep(1)
                number=+1
                if number >= 5:
                    break

    # 判断：SP在当前桌面是否可见
    def find_app_Subscript(self):
        name = '判断：SP在当前桌面是否可见'
        try:
            self.text_find("SunPeopleQA", model=name)
            return True
        except:
            return False

    # 获取app角标数
    def get_app_Subscript_bumber(self):
        self.wait_eleVisible(ntl.app_Subscript)
        return self.get_text(ntl.app_Subscript)

    # 切换至APP
    def start_ap_app(self):
        # self.driver.background_app()
        logging.info("切回APP")
        self.driver.start_activity("com.suncity.sunpeople.qa","com.suncity.sunpeople.ui.login.SplashActivity")
        time.sleep(2)
        return self

    # =============================================================================================
    #                      用例执行后置数据清除处理

    # 点击： 帖子更多icon-[删除]帖子
    def click_more_list_delete_button(self):
        name = '点击： 帖子更多icon-[删除]帖子'
        self.wait_eleVisible(ntl.more_list_delete_button, model=name)
        self.click_element(ntl.more_list_delete_button, model=name)                 # 点击[删除帖子]按钮
        name = "点击确认删除"
        self.wait_eleVisible(ntl.more_list_delete_button_confirm, model=name)
        self.click_element(ntl.more_list_delete_button_confirm, model=name)         # 点击确认删除
        self.wait_qroup_loading_icon()              # loading
        return self

    # 删除【个人】tab中所有帖子
    def delete_personal_tab_all_post(self):
        name = "删除【个人】tab中所有帖子"
        self.wait_eleVisible(ntl.personal_page_user_name, model=name)       # 等待个人tab页面数据加载完成
        post_number = 0
        start_delete = self.get_system_time_time()
        self.swipe_screen(0.5, 0.8, 0.5, 0.5)               # 上滑值帖子可见
        while self.if_personal_tab_post_more_button() == True:
            self.click_personal_tab_post_more_button()
            self.click_more_list_delete_button()            # 点击：【删除帖子】按钮
            time.sleep(1)
            post_number = post_number+1
            logging.info("本次执行已删除{}个帖子".format(post_number))
            if self.if_personal_tab_post_more_button() == False:      # 判断当前屏幕是否展示帖子
                self.swipe_screen(0.5, 0.8, 0.5, 0.5)       # 上滑一次
            if self.if_personal_tab_post_more_button() == False:      # 判断当前屏幕展示数据是否删除完
                self.swipe_screen(0.5, 0.3, 0.5, 0.7)       # 下拉刷新一次
                self.wait_qroup_loading_icon()              # 加载
                time.sleep(1)
                self.swipe_screen(0.5, 0.8, 0.5, 0.5)       # 上滑一次
            if post_number >=50:               # 超过50次退出循环
                break
        end_delete = self.get_system_time_time()
        delta = self.get_demo_time_interval_time(start_delete,end_delete)
        hour = delta // 3600  # 时
        div = (delta % 3600) // 60  # 分
        mod = (delta % 3600) % 60  # 秒
        logging.info("删除个人tab中的{}个帖子所花时间：".format(post_number))
        logging.info("{}小时{}分钟{}秒".format(hour, div, mod))
        return self

    # 拍摄10张照片
    def action_number_phtot(self):
        self.click_newdynamic()                                 # 點擊【最新動態】
        self.click_all_tab()                                    # 点击最新动态-全部tab
        self.click_all_tab_photo_icon()                         # 点击拍照icon
        number = 0
        while number <= 10:
            self.click_personal_tab_shutter_button()            # 點擊：快門icon
            self.click_personal_tab_media_cancel()              # 點擊：[重做]按鈕
            number = number + 1
        self.return_button()
        time.sleep(1)
        self.return_button()
        return self