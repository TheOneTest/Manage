# _author_='Administrator'
# -*- coding: utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.atstudy.com/')

driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_xpath("html/body/div[1]/header/nav/div/ul/li[2]/a").click()  #点击登录按钮，进入登录页面

driver.find_element_by_xpath(".//*[@id='login_username']").send_keys("weipeng_yyp")
driver.find_element_by_xpath(".//*[@id='login_password']").send_keys("wp890920")
time.sleep(1)

driver.find_element_by_xpath(".//*[@id='login-form']/div[4]/button").click()

time.sleep(2)
try:
    assert u"weipeng_yyp" in driver.page_source
    print (u"Test Pass")
except Exception as e:
    print(u"Test Fail")

driver.find_element_by_xpath(".//*[@id='course-filter']/ul/li[2]/a").click()
driver.find_element_by_xpath(".//*[@id='course-list-section']/div/div[3]/div/div[7]/div/div[2]/div[1]/a").click()

time.sleep(5)

driver.quit()