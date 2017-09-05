#coding=utf-8
import hashlib
import random
import string
import re
import os
import win32com.client
import datetime,time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class MyLibrary():
    
    def random_ABC(self):
        str=''.join(random.sample(string.ascii_letters,4))
        return str

    def substr(self,add_name):
        new_name = ""
        if len(add_name) <=27: 
            new_name = add_name[0:len(add_name)]
            print len(add_name)
            print new_name
        else:
            new_name = add_name[0:27]
            print new_name
            print len(add_name)           
        return new_name

    def random_NUM(self):
        num=random.randint(1000,9999)
        return num

    def substring_num(self,str_name):
        p1 = r"\n.*"
        patter = re.compile(p1)
        str_num = patter.findall(str_name)
        str_convert = ''.join(str_num)
        str_list = str_convert.split('TheONE')
        if str_list.__len__() > 1:
            re_str = str_list[str_list.__len__() - 1]
        else:
            re_str = str_list[0]
        p2 = r'^\d+'
        patter = re.compile(p2)
        str11 = patter.findall(re_str)
        str_convert1 = ''.join(str11)
        # print str_convert1
        re_str_all = re_str.replace(str_convert1, '', 1)
        return re_str_all.lstrip('\n')

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
    
    def inspect_Macro(self,macro_num,room_num,class_num,teacher_num,student_num,class_p,time_all):
        
        if long(macro_num) == 0 or long(room_num) == 0 or long(class_num) == 0 or long(teacher_num) == 0 or long(student_num) == 0 or long(class_p) == 0:            
            print "机构中存在未统计出的列表信息，其值为0，请查证！！！"
            raise ValueError
        else:           
            now = datetime.datetime.now()
            delta = datetime.timedelta(days=1)
            n_days = now - delta

            day_m = n_days.strftime('%Y-%m-%d')

            time_a = datetime.datetime.strptime(time_all,"%Y-%m-%d %H:%M:%S").date()
           
            day_n = time_a.strftime('%Y-%m-%d')
            
            if day_n != day_m:
                print "宏观数据统计未及时更新，请查证统计脚本是否定期执行"

                raise ValueError

    def inspect_Macrobt(self,macro_num,room_num,class_num,teacher_num,student_num,class_p,macro_s,room_s,class_s,teacher_s,student_s,class_ps):
        num_p = int(macro_num)+int(room_num)+int(class_num)+int(teacher_num)+int(student_num)+int(class_p)

        num_m = int(macro_s)+int(room_s)+int(class_s)+int(teacher_s)+int(student_s)+int(class_ps)

        if num_m == num_p:
            print "宏观数据校验通过！！！"
        else:
            print "宏观数据校验失败！！！"
            raise ValueError

    def inspect_ykll(self,macro_num,class_num):
        if int(macro_num)>600:
            print "尤克里里机构总数显示正常，当前机构数为" + macro_num
        else:
            print "尤克里里机构总数显示异常，当前机构数为" + macro_num
            raise ValueError
        if int(class_num)>600:
            print "尤克里里教室总数显示正常，当前教室数为" + class_num           
        else:
            print "尤克里里教室总数显示异常，当前教室数为" + class_num
            raise ValueError
                