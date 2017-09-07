# _author_='Administrator'
# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep
import random
import string
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class MyAppLibrary():
    #生成1000-9999 随机数
    def random_NUM(self):
        num=random.randint(1,9)
        return num

    def random_ABC(self):
        str=''.join(random.sample(string.ascii_lowercase,6))
        return str

    #验证智能钢琴--名曲速成列表中向上滑动加载数据功能
    def list_Loading(self,name_list):
        num = len(name_list)
        list_string = list(set(name_list))
        num_new = len(list_string)

        if num != num_new:            
            print "列表中存在相同数据，校验失败"
            raise ValueError

    #视频教程详情页数据校验
    def inspect_Vedio(self,title,desc,list_num):
        if title == '' or title == None or desc == '' or desc == None or int(list_num) < 5:
            raise ValueError
    
    #个人中心导航校验
    def inspect_usercenter(self,username,collection,record,sound,tools,sett):
        if username != '我的账号' or collection != '我的收藏' or record != '历史记录' or sound != '我的录音' or tools != '学习工具' or sett != '音色设置':
            raise ValueError
            
        

