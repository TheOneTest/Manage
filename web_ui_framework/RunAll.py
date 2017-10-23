# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import traceback
import unittest

from TestTools import HTMLTestRunner
from TestTools import sorttime
from TestTools.log import MyLog
from xlrd import open_workbook
import string

__author__ = 'huangxb'


"""
RunAll Version 1.0
根据命令行指定读取的txt文件，从txt文件中获取要执行的TestCase文件夹下的py文件；
py文件中指定了读取的xlsx文件，以获取用例
"""
class RunAll():
    def __init__(self):
        global reportFile,casepath,caseList
        self.log = MyLog.get_log()
        self.logger = self.log.logger
        self.caseList = []

        # 获取系统当前时间
        now = sorttime.gettime()
        day = sorttime.getday()
        #self.reportFile = '.\\TestResult\\' + day + '\\' + now + '_result.html'
        #self.reportFile = '.\\TestResult\\' + day + '\\' + '_result.html'
        self.reportFile = os.path.join('.','TestResult','test_result.html')

        # 定义用例存放路径
        self.casepath = os.path.join(".","TestCase")
        # self.casepath = ".\\TestCase\\"

        # 定义测试结果存放路径
        self.result = os.path.join(".","TestResult")
        # self.result = ".\\TestResult\\"

    def set_module_to_test(self,module):
        module_list_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "TestData","module_list.txt")
        fp = open(module_list_path,"w")
        fp.write(module)
        fp.close()

    def set_case_suite(self):
        try:
            test_suite = unittest.TestSuite()
            suite_model = []
            discover = unittest.defaultTestLoader.discover(self.casepath, pattern='*.py', top_level_dir=None)
            suite_model.append(discover)
            if len(suite_model) > 0:
                for suite in suite_model:
                    for test_name in suite:
                        test_suite.addTest(test_name)
            else:
                return None
            return test_suite
        except Exception, e:
            print traceback.print_exc()

    def set_all_case_suite(self,filename):
        try:
            if filename:
                #获取文件中所有sheet名称
                module_list_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "TestData","%s.xlsx"%filename)
                fp = open_workbook(module_list_path)
                modules = fp.sheet_names()
                modulelist = []
                for module in modules:
                    if module != "public_case" and module != "keyword":
                        modulelist.append(module)
                return self.set_suite(modulelist)
            else:
                return self.set_case_suite()
        except Exception,e:
            print traceback.print_exc(),e

    def set_suite(self,arglist):
        try:
            suite_list = []
            for module in arglist:
                self.set_module_to_test(module)
                suite_list.append(self.set_case_suite())
            suite_tuple = tuple(suite_list)
            return unittest.TestSuite(suite_tuple)
        except Exception,e:
            print traceback.print_exc(),e


    def run(self,type,module=False):
        try:
            if type == "all":
                suit = self.set_all_case_suite(module)
            elif type == "depart":
                modulelist = string.split(module,",")
                suit = self.set_suite(modulelist)
            if suit is not None:
                self.logger.info("********TEST START********")
                fp = open(self.reportFile, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suit)
                fp.close()
            else:
                self.logger.info("Have no case to test.")
        except Exception,ex:
            print traceback.print_exc(),ex
            self.logger.error(traceback.print_exc(),ex)
            self.logger.error(str(ex))
        finally:
            self.logger.info("*********TEST END*********")



#V 2.0.1
if __name__ == "__main__":
    argv_len = len(sys.argv)
    runall = RunAll()
    runall.run("depart","login")

# if __name__ == "__main__":
#     argv_len = len(sys.argv)
#     type = sys.argv[1]
#     module = sys.argv[2]
#     runall = RunAll()
#     # runall.run("depart","pjs/transfer,pjs/autoinvest")
#     # runall.run("all", "pjs")
#     runall.run(type, module)









