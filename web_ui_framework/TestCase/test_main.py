#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import unittest
import traceback
from selenium import webdriver
from TestTools import savescreen
from TestTools import getcases
from parameterized import parameterized
from config.common import G_LOCAL_KEY
from TestPage.Public import BasePage
import string
import ExtendFunc

__author__ = 'weipeng'

class TestMain(BasePage.Base):
    objlist = []
    all_funclist = []
    xls = getcases.GetCases()
    modulenamelist,caseList, module = xls.get_case_suit()
    __doc__ = module

    def setUp(self):
        print u"开始测试"
        self.driver = webdriver.Chrome()

    def custom_name_func(testcase_func=None, param_num=None, param=None):
        casename= str(param.args[2])
        funcname = "test_%s"%casename
        return funcname

    ef = ExtendFunc.ExtendFunc()
    for modulename in modulenamelist:
        objlist,all_funclist = ef.importfunc(modulename)

    @parameterized.expand(caseList,testcase_func_name=custom_name_func)
    def testfunc(self,*args):
        try:
            # print args
            print u"case_%s"%args[1]
            if args[3] is not False:
                vardict = {}
                for index,step in enumerate(args[4:]):
                    var = ""
                    index += 1
                    #打印步骤
                    print "%s:%s"%(index,step[0])
                    keyword = step[1]
                    page = step[2]
                    element = step[3]
                    param = self.ef.set_param(step[4],**vardict)
                    varparam = step[5]
                    if keyword in self.all_funclist:
                        for obj in self.objlist:
                            if keyword in obj:
                                func = getattr(obj[-1],keyword)
                                paramlist = tuple(string.split(param,","))
                                var = func(*paramlist)
                                break
                    else:
                        locator = ""
                        stepeval = u'self.' + keyword + '('
                        if element:
                            locator = self.xls.getlocator(page,element)
                            stepeval = stepeval + locator
                            if param:
                                stepeval = stepeval + ',"' + param + '")'
                            else:
                                stepeval = stepeval + ')'
                        elif param:
                            stepeval = stepeval + '"' + param + '")'
                        print stepeval
                        expression = compile(stepeval, '', 'eval')
                        var = eval(expression)
                    if varparam:
                        vardict[varparam] = var


        except Exception,e:
            print traceback.print_exc(),e
            self.assertTrue(0)


    def tearDown(self):
        savescreen.savescreen(self.driver)
        self.driver.close()
        print u"已结束测试"

if __name__=="__main__":
    unittest.main()