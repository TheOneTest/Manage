# _author_='Administrator'
#coding=utf-8
from selenium import webdriver
import time
import hashlib
import random
import string
import re
import os
import win32com.client
import datetime
import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
reload(sys)
sys.setdefaultencoding('utf8')

class ShopLibrary():
    
    def kill_driver(self,kill_name):
        WMI = win32com.client.GetObject('winmgmts:')
        processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % kill_name)
        static = True
        if len(processCodeCov) > 0:
            static = True
        else:
            static = False

        if static == True:
            command = 'taskkill /F /IM ' + kill_name
            os.system(command)

    def substring_num(self,str_name):       
        p1 = r'\d+'
        patter = re.compile(p1)
        str_num = patter.findall(str_name)
        return str_num[0]

    def inspect_Price(self,shop_name,shop_price,name,price):
        shop_price = self.substring_num(shop_price)
        price = self.substring_num(price)
        if shop_price != price:
            raise ValueError
        if shop_name != name:
            raise ValueError

    def open_h5(self,url):
        mobileEmulation = {'deviceName':'iPhone 6'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation',mobileEmulation)
        try:
            driver = webdriver.Chrome(executable_path="chromedriver",chrome_options=options)
            driver.set_page_load_timeout(6)
            driver.maximize_window()
            driver.get(url)
            time.sleep(2)
            driver.find_element_by_xpath(".//*[@id='app']/div/div[3]/div[4]/img").click()
            time.sleep(2)
        except TimeoutException:
            print(u"打开首页超时，页面无响应")
        return driver

    def login_In(self,driver,username,password):
        driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/div[1]/div[1]/input").send_keys("13162085635")
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/div[1]/div[3]/input").send_keys("123456")
        time.sleep(1)     
        driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/div[2]").click()
        time.sleep(1)
        try:
            assert u"我的订单" in driver.page_source
        except Exception as e:
            print(e)
        return driver
    def buy_item(self,driver):
        time.sleep(2)
        num=random.randint(1,4)
        driver.find_element_by_xpath(".//*[@id='app']/div/div[3]/div[2]/img").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='prod-1']/div[3]/div["+str(num)+"]/img").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='submit-button dark active']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='submit-button dark active']").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/div[2]/div[2]/div[2]/div[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='payment-submit ng-scope']").click()
        time.sleep(1)
        driver.get("http://shop.1tai.com/h5/#/profile")     #进入个人中心
        return driver
    def del_item(self,driver):
        time.sleep(2)        
        driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/div[2]/div[1]").click()    #点击我的订单
        time.sleep(2)        
        driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/div[2]/div[1]/div[3]/div[3]").click()  #点击取消订单
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='dialog']/div[2]/div[3]/div[2]").click() #点击确定取消
        return driver
    def get_text_h5(self,driver):
        time.sleep(2)
        static_name = driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/div[2]/div[1]/div[1]/div[2]").getText()
        return static_name

    