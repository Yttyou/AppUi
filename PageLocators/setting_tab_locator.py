__author__ = 'developer'

# 【设定】tab页面元素定位

from appium.webdriver.common.mobileby import MobileBy as Mb


class SettingTabLocator:
    setting_button = (Mb.ID, "com.suncity.sunpeople.qa:id/tv_setting")  # 导航栏【设定】
    signout_button = (Mb.ID, "com.suncity.sunpeople.qa:id/tv_signout")  # 【登出】按钮
    confirm_signout_button = (
    Mb.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.TextView\").textContains(\"登出\")")
    signout_button_load = (Mb.ID,"com.suncity.sunpeople.qa:id/lcv_circleload")      # 登出load
    set_button = (Mb.ID, "com.suncity.sunpeople.qa:id/rl_setting")  # 设定按钮
    user_image = (Mb.ID, "com.suncity.sunpeople.qa:id/sdv_avatar")  # 用户图像
    taking_pictures = (Mb.CLASS_NAME, "android.widget.TextView")  # 拍照
    the_shutter = (Mb.ID, "NONE")  # 快门
    is_ok = (Mb.ID, "com.sec.android.app.camera:id/okay")  # 确定






