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

