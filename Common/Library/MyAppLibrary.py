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
        

