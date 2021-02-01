from appium.webdriver.common.mobileby import MobileBy as Mb


class PageLocators:
    # 提示踢下线弹窗
    confirm_button = (Mb.ID, "android:id/button1")  # 确定按钮
    chat_tab = (Mb.ID, "com.suncity.sunpeople.qa:id/rl_chat")  # 底部导航栏【聊天】
    setting_button = (Mb.ID, "com.suncity.sunpeople.qa:id/tv_setting")  # 导航栏【设定】
    iphone_icon = (Mb.ID, "com.suncity.sunpeople.qa:id/tv_phone_image")  # 电话icon
    setting_language = (Mb.ID, "com.suncity.sunpeople.qa:id/rl_language")  # 语言选择
    language_china = (Mb.ID, "com.suncity.sunpeople.qa:id/fra_language_item_tv_name")  # 繁体中文
    username_input = (Mb.ID, "com.suncity.sunpeople.qa:id/usernameView")  # 登录账户
    password_input = (Mb.ID, "com.suncity.sunpeople.qa:id/passwordView")  # 登录密码
    login_button = (Mb.ID, "com.suncity.sunpeople.qa:id/loginView")  # 登录按钮
    signout_button = (Mb.ID, "com.suncity.sunpeople.qa:id/tv_signout")  # 【登出】按钮
    confirm_signout_button = (Mb.ANDROID_UIAUTOMATOR,
                              "new UiSelector().className(\"android.widget.TextView\").textContains(\"登出\")")

    msg_list = (Mb.ID, "com.suncity.sunpeople.qa:id/tv_item_given_name")  # 讯息tab消息栏
    create_icon = (Mb.ID, "com.suncity.sunpeople.qa:id/iv_create")  # 讯息tab-加号创建icon
    create_new_message_button = (Mb.ID, "com.suncity.sunpeople.qa:id/tv_create_new_message")  # 创建-下拉列表：【新增对话】
    create_message_one_low_text = (
    Mb.ID, "com.suncity.sunpeople.qa:id/view_channelmembers_item_tv_givenname")  # 新增对话页-第一行用户名文本定位（多个，不唯一）
