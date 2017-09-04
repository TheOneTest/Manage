# _author_='Administrator'
# -*- coding: utf-8 -*-
import unittest
from LoginPage import LoginPage
from selenium import webdriver
import time

class Caselogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait= 3
        self.driver.set_page_load_timeout= 3
        self.url = "http://manage-dev.xiaoyezi.com/#!/pandect/dashboard"
        self.username = "wenhaiyuan1"
        self.password = "a123456"

        # 后台登录
        login_page = LoginPage(self.driver,self.url,u"Piano Classroom")
        login_page.open()
        login_page.input_manage_username(self.username)
        login_page.input_manage_passwd(self.password)
        # time.sleep(3)
        login_page.click_manage_login()


    def test_xinxiyulan(self):
        return self.driver.find_element_by_xpath("//html/body/div/div[1]/nav/ul/li[1]/nav/ul/li[1]/a/span").click()
    def test_youkelili(self):
        return self.driver.find_element_by_xpath("//html/body/div/div[1]/nav/ul/li[1]/nav/ul/li[2]/a/span").click()







    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()