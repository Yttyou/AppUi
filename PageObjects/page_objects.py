import time
from Common.BasePage import BasePage
from PageLocators.page_locators import PageLocators as PL


class PageObject(BasePage):
    # 查找：是否踢出提示弹框
    def get_out_confirm_button(self):
        name = "查找：是否踢出提示弹框"
        time.sleep(1)
        try:
            self.get_element(PL.confirm_button, model=name)
            return True
        except:
            return False

    # 点击：踢出提示弹出框【确定】按钮
    def click_kick_out_confirm_button(self):
        name = "点击：踢出提示弹出框【确定】按钮"
        self.wait_eleVisible(PL.confirm_button, model=name)
        self.click_element(PL.confirm_button, model=name)
        return self

    # 获取文本：设置tab文本
    def get_setting_text(self):
        name = "获取文本：设置tab文本"
        self.wait_eleVisible(PL.setting_button, model=name)
        return self.get_text(PL.setting_button, model=name)

    # 点击：语言选择-繁体中文
    def click_language_setting(self):
        name = "点击：语言选择-繁体中文"
        self.wait_eleVisible(PL.setting_button)
        self.click_element(PL.setting_button)
        self.wait_eleVisible(PL.iphone_icon, model=name)
        if self.is_language_setting() == False:
            self.swipe_screen(0.5, 0.8, 0.5, 0.4)
        self.wait_eleVisible(PL.setting_language, model=name)
        self.click_element(PL.setting_language, model=name)  # 点击【语言选择】
        self.wait_eleVisible(PL.language_china, model=name)
        self.click_element(PL.language_china, model=name)  # 点击【繁体中文】
        return self

    # 判断：【语言选择】是否可见
    def is_language_setting(self):
        name = "判断：【语言选择】是否可见"
        time.sleep(2)
        try:
            self.get_element(PL.setting_language, model=name)
            return True
        except:
            return False

    # 输入用户名
    def input_username(self, user):
        name = "输入用户名"
        self.wait_eleVisible(PL.username_input, model=name)
        self.input_text(PL.username_input, user, model=name)
        return self

    # 输入密码
    def input_passwd(self, passwd):
        name = "输入密码"
        self.wait_eleVisible(PL.password_input, model=name)
        self.input_text(PL.password_input, passwd, model=name)
        return self

    # 点击登录
    def click_login(self):
        name = "点击登录"
        self.wait_eleVisible(PL.login_button, model=name)
        self.click_element(PL.login_button, model=name)
        return self

    # 查找【聊天】按钮
    def is_chat_tab(self):
        name = "查找【聊天】按钮"
        try:
            self.wait_eleVisible(PL.chat_tab, wait_times=20, poll_frequency=1, model=name)
            return True
        except:
            return False

    # 点击导航-【设置】
    def click_setting(self):
        name = "点击导航-【设置】"
        self.wait_eleVisible(PL.setting_button, model=name)
        self.click_element(PL.setting_button, model=name)
        return self

    # 点击【登出】-确认登出
    def click_signout_button(self):
        name = "点击【登出】-确认登出"
        self.wait_eleVisible(PL.signout_button, model=name)
        self.click_element(PL.signout_button, model=name)
        self.wait_eleVisible(PL.confirm_signout_button, model=name)
        self.click_element(PL.confirm_signout_button, model=name)
        return self

    # 等待聊天页面消息加载完成
    def wait_msg(self):
        name = "等待聊天页面消息加载完成"
        self.wait_eleVisible(PL.msg_list, wait_times=30)
        return self

    # 進入新增對話頁面，且數據加載完成
    def enter_personal_chat_page(self):
        self.click_create_new_message()  # 点击+号-【新增对话】
        while self.is_new_message_one_low() == False:
            self.return_button_one()
            self.click_create_new_message()  # 点击+号-【新增对话】
            time.sleep(2)
        self.return_button()
        return self

    # 点击：新增对话（点击加号创建-再点击新增对话）
    def click_create_new_message(self):
        name = "点击：新增对话"
        self.wait_eleVisible(PL.create_icon)
        self.click_element(PL.create_icon)
        self.wait_eleVisible(PL.create_new_message_button)
        self.click_element(PL.create_new_message_button)
        return self

    # 判断：新增对话页面列表数据是否加载出来
    def is_new_message_one_low(self):
        try:
            self.get_element(PL.create_message_one_low_text)
            return True
        except:
            return False

    # 【返回】物理按键（一步）
    def return_button_one(self):
        self.return_button()
        return self


def append_data(per_list,per_num,module,case_name,title):
    per_list.append(per_num)
    per_list.append(module)
    per_list.append(case_name)
    per_list.append(title)
    return per_list