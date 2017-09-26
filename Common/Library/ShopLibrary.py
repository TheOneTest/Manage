#coding=utf-8
import hashlib
import random
import string
import re
import os
import win32com.client
import datetime
import sys
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
        
        
            


    