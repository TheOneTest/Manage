# _author_='Administrator'
# -*- coding: utf-8 -*-
import unittest
import LoginPage
from selenium import webdriver
import time

class Caselogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver.implicitly_wait=3
        # self.driver.set_page_load_timeout=5
        self.url = "http://www.atstudy.com/"
        self.username = "weipeng_yyp"
        self.password = "wp890920"




    #用户登陆
    def test_login_user(self):
        login_page = LoginPage.LoginPage(self.driver,self.url,u"博为峰")
        login_page.open()
        #点击首页登陆链接 进入登陆页面
        login_page.click_element_login()
        time.sleep(1)
        login_page.input_username(self.username)    
        login_page.input_password(self.password)
        login_page.click_submit()
        time.sleep(3)

    #购买课程
           


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()