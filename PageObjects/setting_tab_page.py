__author__ = 'developer'
#设置页-各操作

from Common.BasePage import BasePage
import time
from PageLocators.setting_tab_locator import SettingTabLocator as STL

class SettingTabPage(BasePage):
    # 点击导航-【设置】
    def click_setting(self):
        name = "点击导航-【设置】"
        self.wait_eleVisible(STL.setting_button,model=name)
        self.click_element(STL.setting_button,model=name)
        return self

    # 点击【登出】-确认登出
    def click_signout_button(self):
        name = "点击【登出】-确认登出"
        self.wait_eleVisible(STL.signout_button,model=name)
        self.click_element(STL.signout_button,model=name)
        self.wait_eleVisible(STL.confirm_signout_button,model=name)
        self.click_element(STL.confirm_signout_button,model=name)
        self.wait_signout_button_load()
        return self

    # 登出load
    def wait_signout_button_load(self):
        name = "登出load"
        time.sleep(1)
        self.wait_ele_invisible_pass(STL.signout_button_load,model=name)
        return self

    # 点击设定tab
    def click_set(self):
        name = "点击设定tab"
        self.wait_eleVisible(STL.set_button, model=name)
        self.click_element(STL.set_button, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 点击用户图像
    def click_user_image(self):
        name = "点击用户图像"
        self.wait_eleVisible(STL.user_image, model=name)
        self.click_element(STL.user_image, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 点击拍照
    def click_taking_pictures(self, index):
        name = "点击拍照"
        self.wait_eleVisible(STL.taking_pictures, model=name)
        self.find_elements(STL.taking_pictures, model=name)[index].click()
        self.wait_qroup_loading_icon()
        return self

    # 点击快门
    def click_the_shutter(self):
        name = "点击快门"
        self.wait_eleVisible(STL.the_shutter, model=name)
        self.click_element(STL.the_shutter, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 点击确定
    def click_the_is_ok(self):
        name = "点击确定"
        self.wait_eleVisible(STL.is_ok, model=name)
        self.click_element(STL.is_ok, model=name)
        self.wait_qroup_loading_icon()
        return self

    # 点击完成
    def click_the_finish(self):
        name = "点击完成"
        time.sleep(1)
        self.text_find("完成", model=name).click()
        return self

    # 查找："上傳頭像成功"tost
    def find_send_text_photo_tost(self):
        name = '查找："上傳頭像成功"tost'
        try:
            self.get_toast_tips("上傳頭像成功", model=name)
            return True
        except:
            return False

