# _author_='Administrator'
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import BasePage
from selenium.common.exceptions import TimeoutException
class LoginPage(BasePage.BasePage):
    
    username_loc = (By.NAME,'email')
    password_loc = (By.NAME,'password')
    submit_loc = (By.ID,'dologin')
    span_loc = (By.CSS_SELECTOR,"div.error-tt>p")
    dynpw_loc = (By.ID,"ibDynpw")
    userid_loc = (By.ID,"spnUid")

    #用户登陆
    login_loc = (By.XPATH,"html/body/div[1]/header/nav/div/ul/li[2]/a")     #登录页面入口
    login_username_loc = (By.XPATH,".//*[@id='login_username']")            #用户名
    login_password_loc = (By.XPATH,".//*[@id='login_password']")            #密码    
    login_submit_loc = (By.XPATH,".//*[@id='login-form']/div[4]/button")    #登录按钮

    #搜索课程
    # course_library = (By.XPATH,"//a[text()='课程库']")




    def open(self):
        try:
            self._open(self.base_url,self.pagetitle)
        except TimeoutException:
            print("页面加载超时，停止等待！！")
            self.driver.excute_script('window.stop()')

    def input_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)


    def input_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)
    #点击登陆链接
    def click_element_login(self):
        try:
            return self.find_element(*self.login_loc).click()
        except TimeoutException:
            print("加载超时，停止等待！")
            self.driver.excute_script('window.stop()')


    #点击按钮
    def click_submit(self):
        try:
            return self.find_element(*self.login_submit_loc).click()
        except TimeoutException:
            print("页面加载超时，停止等待")
            self.driver.execute_script('window.stop()')


    def show_span(self):
        return self.find_element(*self.span_loc).text

    def swich_DynPw(self):
        self.find_element(*self.dynpw_loc).click()

    def show_userid(self):
        return self.find_element(*self.userid_loc).text