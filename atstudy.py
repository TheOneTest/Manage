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
    print (u"测试通过")
except Exception as e:
    print(u"Test Fail")

driver.find_element_by_xpath(".//*[@id='course-filter']/ul/li[2]/a").click()        #选择课程分类
driver.find_element_by_xpath(".//*[@id='course-list-section']/div/div[3]/div/div[7]/div/div[2]/div[1]/a").click() #选择课程

#切换窗口
handle_now = driver.current_window_handle
all_handle = driver.window_handles

for handle in all_handle:
    if handle != handle_now:
        driver.switch_to_window(handle)

price1 = driver.find_element_by_xpath("//html/body/div[1]/div[3]/div/div[2]/div[2]/div[1]/span[2]/b").text


driver.find_element_by_xpath("html/body/div[1]/div[3]/div/div[2]/div[2]/div[5]/a").click()  #点击购买

price2 = driver.find_element_by_xpath(".//*[@id='course-buy-form']/div[2]/div[2]/span/strong").text

driver.find_element_by_xpath(".//*[@id='form-submit-btn']").click() #点击去支付

driver.find_element_by_xpath(".//*[@id='js-order-create-sms-btn']").click()
time.sleep(1)

if price1 == price2:
    print(u"测试通过,商品价格为" + price2)
else:
    print(u"测试失败")
    
time.sleep(5)

driver.quit()