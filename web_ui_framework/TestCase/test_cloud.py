# _author_='Administrator'
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest
from TestPage.Public import login

import time



class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver.implicitly_wait(5)
        self.driver.implicitly_wait= 5
        self.base_url = "http://manage-dev.xiaoyezi.com/#!/pandect/dashboard"
        self.verificationErrors = []
        self.accept_next_alert = True

        #用户登陆用例
    # def test_login(self):
    #     drvier = self.driver
    #     drvier.get(self.base_url)
    #     drvier.maximize_window()
    #     #登陆
    #     drvier.find_element_by_xpath("//a[text()='登录']").click()
    #     time.sleep(5)
    #     drvier.find_element_by_id("login-id").clear()
    #     drvier.find_element_by_id("login-id").send_keys("13162085635")
    #     drvier.find_element_by_id("password").clear()
    #     drvier.find_element_by_id("password").send_keys("123456")
    #     drvier.find_element_by_xpath("//a[text()='登录']").click()
    #     time.sleep(3)
    def test_login(self):
        login.login(self)
        print("Is Good")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

