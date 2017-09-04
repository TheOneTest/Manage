# _author_='Administrator'
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from BasePage import BasePage
from  selenium.common.exceptions import TimeoutException

class LoginPage(BasePage):
    username_loc = (By.NAME,'email')
    password_loc = (By.NAME,'password')
    submit_loc = (By.ID,'dologin')
    span_loc = (By.CSS_SELECTOR,"div.error-tt>p")
    dynpw_loc = (By.ID,"ibDynpw")
    userid_loc = (By.ID,"spnUid")

    #用户登陆
    login_loc = (By.XPATH,"//a[text()='登录']")
    login_username_loc = (By.ID,'login-id')
    login_password_loc = (By.ID,'password')
    login_submit_loc = (By.XPATH,"//a[@class='login_wz' and text()='登录']")

    #管理 后台 用户登录
    login_manage_name = (By.XPATH,"//html/body/div[1]/div/form/table/tbody/tr[1]/td[2]/input")        #用户名
    login_manage_passwd = (By.XPATH,"//html/body/div[1]/div/form/table/tbody/tr[2]/td[2]/input")      #密码
    login_manage_submit = (By.XPATH,"//html/body/div[1]/div/form/table/tbody/tr[3]/td[2]/input")      #登录


    #左侧目录导航链接
    xinxiyulan=(By.XPATH,"//html/body/div/div[1]/nav/ul/li[1]/nav/ul/li[1]/a/span")
    youkelili=(By.XPATH,"//html/body/div/div[1]/nav/ul/li[1]/nav/ul/li[2]/a/span")
    Tongjixinxi=(By.XPATH,"//html/body/div[1]/div[1]/nav/ul/li[2]/a")
    jigoushuaixuan=(By.XPATH,"//html/body/div[1]/div[1]/nav/ul/li[2]/nav/ul/li[1]/a/span")
    banbenshuaixuan=(By.XPATH,"//html/body/div[1]/div[1]/nav/ul/li[2]/nav/ul/li[2]/a/span")






    #搜索课程
    course_library = (By.XPATH,"//a[text()='课程库']")
    
    course_hdkf = (By.XPATH,"//div[@id='dictionary']/a[3]")

    course_JavaEE=(By.XPATH,"//div[@id='classify']/a[6]")

    # course_jcjj=(By.XPATH,"id('difficulty')/x:a[2]")

    course_element=(By.XPATH,"//div[@id='courseList']/a[1]")


    def open(self):
        try:
            self._open(self.base_url,self.pagetitle)
        except TimeoutException:
            print("页面加载超时，停止等待！！")
            self.driver.excute_script('window.stop()')

    def input_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)
    def input_manage_username(self,username):
        self.find_element(*self.login_manage_name).send_keys(username)
    def input_manage_passwd(self,password):
        self.find_element(*self.login_manage_passwd).send_keys(password)
    def input_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)

    #管理后台点击登录按钮
    def click_manage_login(self):
        try:
            return self.find_element(*self.login_manage_submit).click()
        except TimeoutException:
            print ("加载时间过长，强制停止！！！")
            self.driver.excute_script('window.stop()')
    #点击登陆链接
    def click_element_login(self):
        try:
            return self.find_element(*self.login_loc).click()
        except TimeoutException:
            print("加载超时，停止等待！")
            self.driver.excute_script('window.stop()')

    #点击管理后台链接
    def click_xxzl(self):
        return self.find_element(*self.xinxiyulan).click()
    def click_youkelili(self):
        return self.find_element(*self.youkelili).click()
    def click_Tongjixinxi(self):
        return self.find_element(*self.Tongjixinxi).click()
    def click_jigoushuaixuan(self):
        return self.find_element(*self.jigoushuaixuan).click()
    def click_banbenshuaixuan(self):
        return self.find_element(*self.banbenshuaixuan).click()

    #点击首页课程库
    def click_element_course(self):
        return self.find_element(*self.course_library).click()
    
    def click_element_hdkf(self):
        return self.find_element(*self.course_hdkf).click()

    def click_element_JavaEE(self):
        return self.find_element(*self.course_JavaEE).click()

    def click_element_jcjj(self):
        return self.find_element(*self.course_jcjj).click()

    def click_element_course_element(self):
        return self.find_element(*self.course_element).click()


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