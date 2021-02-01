__author__ = 'developer'

from Common.BasePage import BasePage
from PageLocators.employee_tab_locator import EmpTabLocator as emp
from TestDatas import COMMON_DATA
import re
import time
import logging
import random


class EmpTabPage(BasePage):
    def click_employee_self_tab(self):
        name = "点击【員工自助】tab"
        self.wait_eleVisible(emp.employee_self_buttom, model=name)
        time.sleep(1)
        self.click_element(emp.employee_self_buttom, model=name)
        return self

    def get_employee_information_text(self):
        name = "獲取【員工自助】tab頁面第二級模塊名"
        self.wait_eleVisible(emp.employee_information_text, model=name)
        time.sleep(1)
        return self.find_elements(emp.employee_information_text, model=name)

    def get_attendance_calendar_text(self):
        name = "獲取【員工自助】tab頁面第三級模塊名"
        self.wait_eleVisible(emp.attendance_calendar_text, model=name)
        time.sleep(1)
        return self.find_elements(emp.attendance_calendar_text, model=name)

    def is_find_calendar_text(self):
        name = "查找【員工自助】tab頁面第三級模塊名"
        self.wait_ele_visible_pass(emp.attendance_calendar_text, wait_times=30, poll_frequency=1, model=name)
        try:
            self.get_element(emp.attendance_calendar_text)
            return True
        except:
            return False

    def is_find_waiting_text(self):
        name = "查找【員工自助】tab頁面是否存在加載中-請稍後字樣"
        time.sleep(2)
        try:
            self.get_element(emp.attendance_calendar_text, model=name)
            return True
        except:
            return False

    # 加载load文案1
    def wait_loading_done(self):
        name = '加载load文案1'
        time.sleep(1)
        self.wait_element_vanish(emp.loading_icon,wait_times=60,model=name)
        return self
