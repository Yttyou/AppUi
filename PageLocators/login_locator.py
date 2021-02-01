__author__ = 'developer'
# 登录页面各控件元素定位

from appium.webdriver.common.mobileby import MobileBy as Mb

class LoginLocator:
    username_input = (Mb.ID,"com.suncity.sunpeople.qa:id/usernameView")   #登录账户
    password_input = (Mb.ID,"com.suncity.sunpeople.qa:id/passwordView")   #登录密码
    login_button = (Mb.ID,"com.suncity.sunpeople.qa:id/loginView")        #登录按钮

    loading_icon = (Mb.ID, "com.suncity.sunpeople.qa:id/blv_pb")  # loading提示
    login_page_loading= (Mb.ID,"com.suncity.sunpeople.qa:id/loadingIco")        # 登錄按鈕load
    login_loading_tips = (Mb.ID,"com.suncity.sunpeople.qa:id/view_sun_toolbar_tv_title")        # 首页顶部"收取訊息中…"
    statement_dialog_title = (Mb.ID,"com.suncity.sunpeople.qa:id/statement_dialog_title")       # 声明弹框title"聲明展示"
    statement_dialog_agree = (Mb.ID,"com.suncity.sunpeople.qa:id/statement_dialog_agree")       # 声明弹框[同意]按钮
    statement_dialog_refused = (Mb.ID,"com.suncity.sunpeople.qa:id/statement_dialog_refused")   # 声明弹框[拒絕]按钮

    # 提示踢下线弹窗
    confirm_button = (Mb.ID,"android:id/button1")                   # 确定按钮


