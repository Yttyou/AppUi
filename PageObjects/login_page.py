__author__ = 'developer'

from Common.BasePage import BasePage
from PageLocators.login_locator import LoginLocator as loc
import logging
import time

class LoginPage(BasePage):
    #输入用户名
    def input_username(self,user):
        name = "输入用户名"
        self.wait_eleVisible(loc.username_input,model=name)
        self.input_text(loc.username_input,user,model=name)
        return self

    #输入密码
    def input_passwd(self,passwd):
        name = "输入密码"
        self.wait_eleVisible(loc.password_input,model=name)
        self.input_text(loc.password_input,passwd,model=name)
        return self

    # 点击登录
    def click_login(self):
        name = "点击登录"
        self.wait_eleVisible(loc.login_button,model=name)
        self.click_element(loc.login_button,model=name)
        self.wait_loading_done()
        self.wait_login_loading_tips()
        self.click_statement_dialog_agree()         # 处理声明弹框
        return self

    # 等待數據加載完成
    def wait_loading_done(self):
        name = "等待數據加載完成..."
        self.wait_element_vanish(loc.login_page_loading,model=name)
        return self

    # 登录后等待讯息加载完成
    def wait_login_loading_tips(self):
        name = '登录后等待讯息加载完成'
        try:
            self.wait_element_vanish(loc.login_loading_tips,model=name)
            logging.info("登录：讯息加载完成")
        except:
            logging.exception("登录加载出错！请检查网络是否正常")
            self.screenshot("登录加载出错！请检查网络是否正常")
            raise

    # 点击：踢出提示弹出框【确定】按钮
    def click_kick_out_confirm_button(self):
        name = "点击：踢出提示弹出框【确定】按钮"
        self.wait_eleVisible(loc.confirm_button,model=name)
        self.click_element(loc.confirm_button,model=name)
        return self

    # 查找：是否踢出提示弹框
    def get_out_confirm_button(self):
        name = "查找：是否踢出提示弹框"
        time.sleep(1)
        try:
            self.get_element(loc.confirm_button,model=name)
            return True
        except:
            return False

    # 判断：声明弹框(5s内有效)
    def find_statement_dialog_title(self):
        name = '判断：声明弹框(5s内有效)'
        self.wait_eleVisible_pass(loc.statement_dialog_title,wait_times=5,model=name)
        try:
            self.get_element(loc.statement_dialog_agree,model=name)
            return True
        except:
            return False

    # 获取当前【同意】按钮是否可点击状态
    def get_button_if_click_action(self):
        clickable = self.get_element_attribute(loc.statement_dialog_agree, "clickable")
        logging.info("当前声明弹框【同意】按钮的属性为：{}".format(clickable))
        return clickable

    # 点击声明弹框【同意】按钮
    def click_statement_dialog_agree(self):
        name = "点击声明弹框【同意】按钮"
        if self.find_statement_dialog_title() == True:
            swipe_number = 0
            while self.get_button_if_click_action() == "false":          # 【同意】按钮置灰不可点击
                logging.info("循环第{}次滑屏".format(swipe_number+1))
                self.swipe_screen(0.5,0.7,0.5,0.4)      # 下滑屏
                swipe_number = swipe_number+1
                time.sleep(0.5)
                if swipe_number >= 15:
                    break                           # 循环次数大于5次退出循环
            self.wait_eleVisible(loc.statement_dialog_agree,model=name)
            self.click_element(loc.statement_dialog_agree,model=name)
        return self

