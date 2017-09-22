# _author_='Administrator'
# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
class BasePage(object):

    def __init__(self,selenium_driver,base_url,pagetitle):
        self.driver = selenium_driver
        self.base_url = base_url
        self.pagetitle = pagetitle

    def on_page(self,pagetitle):
        return pagetitle in self.driver.title

    def _open(self,url,pagetitle):
        try:
            self.driver.get(url)
        except TimeoutException:
            self.driver.execute_script('window.stop()')
        finally:
            # self.driver.maximize_window()

            assert self.on_page(pagetitle),u"打开页面失败 %s"%url

    def open(self):
        self._open(self.base_url,self.pagetitle)

    #重写元素定位方法
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except TimeoutException:
            print("%s页面中未找到 %s 元素"%(self,loc))

    #重写switch_frame方法
    def switch_frame(self,loc):
        return self.driver.switch_to_frame(loc)

    #定义script方法 用于执行脚本
    def script(self,src):
        self.driver.execute_script(src)

    #重写定义send_keys方法
    def send_keys(self,loc,value,clear_first=True,click_first=True):
        try:
            loc = getattr(self,"_%s"% loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("%s页面中未找到 %s元素"%(self,loc))
