#coding:utf-8
__author__ = 'Administrator'
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import traceback
import unittest
from TestTools import savescreen

class Base(unittest.TestCase):

    def get(self,url):
        self.driver.get(url)

    def find_element(self,*loc):
        try:
            return self.driver.find_element(*loc[0:2])
        except NoSuchElementException:
            raise Exception(u"页面找不到%s"%loc[-1])
    def find_elements(self,*loc):
        try:
            return self.driver.find_elements(*loc[0:2])
        except NoSuchElementException:
            raise Exception(u"页面找不到%s"%loc[-1])

    def get_elemnet_text(self,element):
        u"""获取element文字并最小化"""
        return self.find_element(*element).text.lower()

    def get_elements_len(self,elements):
        u"""返回元素个数"""
        return len(elements)


    def click(self,element):
        u"""点击元素"""
        self.find_element(*element).click()

    def clicks(self,elements,index):
        try:
            elements[index].click()
        except IndexError:
            raise Exception(u"索引超出范围")

    def send(self,element,value):
        u"""查找元素，并输入内容"""
        self.find_element(*element).send_keys(value)

    def wait_until_visibility(self,loc,timeout=30):
        try:
            WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located (loc[0:2]))
        except Exception,e:
            print traceback.print_exc(),e

    def assert_text(self,*args):
        try:
            except_text = args[1]
            element_name = args[0][2]
            text_present = ec.text_to_be_present_in_element(args[0][0:2],except_text)
            self.msg = u"%s is not in element %s"%(except_text,element_name)
            self.assertTrue(text_present(self.driver),self.msg)
        except Exception,e:
            self.wait_until_visibility(args[0][0:2],30)
            self.assertTrue(text_present(self.driver),self.msg)

    def assert_title(self,*args):
        try:
            title = args[0]
            ec_title = self.driver.title
            self.msg = u"%s is not in current title"%title
            self.assertIn(title,ec_title)
        except Exception,e:
            self.assertTrue(0)

    def mouse_move(self,args):
        try:
            ActionChains(self.driver).move_to_element(self.find_element(*args)).perform()

        except Exception,e:
            WebDriverWait(self.driver, 30).until(ActionChains(self.driver).move_to_element(self.find_element(*args)).perform())
            self.assertTrue(0)

    def assert_js(self,*args):
        try:
            text = args[1]
            js=args[0][1]
            js_value = self.driver.execute_script(js)
            self.msg = u"%s is not in %s" % (text,js_value)
            self.assertIn(text,js_value)
        except Exception,e:
            self.assertTrue(0)

    def save_screen(self):
        savescreen.savescreen(self.driver)










