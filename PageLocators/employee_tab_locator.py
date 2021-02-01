__author__ = 'developer'
# 导航栏-【聊天】页面元素定位

from appium.webdriver.common.mobileby import MobileBy as Mb


class EmpTabLocator:
    employee_self_buttom = (Mb.ID, "com.suncity.sunpeople.qa:id/tv_news")  # 底部导航栏【員工自助】
    # 【員工自助】頁面第二級標題
    employee_information_text = (Mb.XPATH, '//*[@resource-id="com.suncity.sunpeople.qa:id/tvFeasure" '
                                           'or @resource-id="com.suncity.sunpeople.qa:id/tvEmployee" '
                                           'or @resource-id="com.suncity.sunpeople.qa:id/tvDevDept"]')
    attendance_calendar_text = (Mb.ID, "com.suncity.sunpeople.qa:id/ess_tv_item")  # 【員工自助】頁面第三級標題

    # 【員工自助】頁面 加載中--請稍後
    # employ_waiting_text = (Mb.ID, "com.suncity.sunpeople.qa:id/ess_tv_item")
    employ_waiting_text = (Mb.XPATH, "//*[@text='加載中，請稍候']")
    loading_icon = (Mb.ID, "com.suncity.sunpeople.qa:id/blv_pb")
