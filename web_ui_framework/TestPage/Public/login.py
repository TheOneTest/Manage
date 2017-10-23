# _author_='Administrator'
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest,time
#登陆模块（函数）
def login(self):
    drvier = self.driver
    drvier.get(self.base_url)
    # drvier.maximize_window()
    #登陆
    # drvier.find_element_by_xpath("//a[text()='登录']").click()
    # time.sleep(5)
    # drvier.find_element_by_id("login-id").clear()
    drvier.find_element_by_xpath("//html/body/div[1]/div/form/table/tbody/tr[1]/td[2]/input").send_keys("wenhaiyuan1")
    # drvier.find_element_by_id("login-id").send_keys("wenhaiyuan1")
    # drvier.find_element_by_id("password").clear()
    drvier.find_element_by_xpath("//html/body/div[1]/div/form/table/tbody/tr[2]/td[323]/input").send_keys("a123456")
    drvier.find_element_by_xpath("//html/body/div[1]/div/form/table/tbody/tr[3]/td[2]/input").click()
    time.sleep(3)