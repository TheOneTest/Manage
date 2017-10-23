#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
from xlrd import open_workbook
import traceback
from TestTools import readConfig
import string
from TestPage.Public import BasePage

class GetCases():
    # localConfigHttp = httpConfig.ConfigHttp()
    # log = Log.get_log()
    # logger = log.logger
    def __init__(self):
        rc = readConfig.ReadConfig()
        # self.url = rc.get_http("mainurl")
        case_file_name = rc.get_file("case_file")
        page_file_name = rc.get_file("page_file")
        # module = self.set_module_list()
        # xls_name = "%s.xlsx"%module[0]
        # self.sheet_name = module[1]
        self.case_file = self.open_xlsx(case_file_name)
        self.page_file = self.open_xlsx(page_file_name)
        self.pre_cases = self.get_pre_cases()

    def open_xlsx(self,xlsx_name):
        self.upPath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
        self.xlsPath = os.path.join(self.upPath, "TestData", xlsx_name)
        return open_workbook(self.xlsPath)


    def set_module_list(self):
        try:
            # 要测试的用例文件路径
            moduleListFile = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")), "TestData","module_list.txt")
            # print moduleListFile
            fb = open(moduleListFile)
            data = fb.readline()
            # module = data.replace("\n", "").split("/")
            fb.close()
            return data
        except Exception, e:
            print traceback.print_exc()

    def get_case_suit(self):
        caseList = []
        module = self.set_module_list()
        try:
            setup_import,cases = self.get_cases(module)
            # caseList.extend(cases)
        except Exception,e:
            print traceback.print_exc(),e
        finally:
            return setup_import,cases,module

    def get_cases_by_target(self,cls):
        caselist = []
        for case in cls:
            if case[3]:
                caselist.append(case)
        if  len(caselist) == 0:
            caselist = cls
        return caselist

    def get_cases(self,sheet_name):
        cls = []
        setup_import = []
        sheet = self.case_file.sheet_by_name(sheet_name)
        # get one sheet's rows
        nrows = sheet.nrows
        case = [sheet_name]#加入模块名称
        for i in range(nrows):
            if sheet.row_values(i)[0] == u'import':
                classname = sheet.row_values(i)[1]
                setup_import.append(classname)

            elif sheet.row_values(i)[0] != u'id':
                if sheet.row_values(i)[0] != u'':
                    if len(case) == 1:
                        case.append(sheet.row_values(i)[0])#加入caseid
                        case.append(sheet.row_values(i)[1])#加入用例名称
                        case.append(sheet.row_values(i)[2])#加入target
                        if sheet.row_values(i)[4] in self.pre_cases.keys():#如果是公共用例，则加入公共用例步骤
                            params = iter(string.split(sheet.row_values(i)[7],","))
                            for pre_case_step in self.pre_cases[sheet.row_values(i)[4]]:
                                #如果参数位显示是para，表示要传入参数，这里用调用时的参数来替换
                                if pre_case_step[-2] == "para":
                                    pre_case_step[-2] = next(params)
                                case.append(pre_case_step)
                        else:
                            case.append(sheet.row_values(i)[3:])#加入测试步骤
                        if i >= (nrows-1) or sheet.row_values(i+1)[0] != u'':
                            cls.append(case)
                            case = [sheet_name]
                    else:
                        pass
                else:
                    if len(case) == 1:
                        pass
                    else:
                        case.append(sheet.row_values(i)[3:])
                        if i >= (nrows-1) or sheet.row_values(i+1)[0] != u'':
                            cls.append(case)
                            case = [sheet_name]
            else:
                pass
        cls = self.get_cases_by_target(cls)
        return setup_import,cls

    def getlocator(self,sheet_name,element):
        # file = self.open_xlsx("pjs_page_hxb.xlsx")
        sheet = self.page_file.sheet_by_name(sheet_name)
        nrows = sheet.nrows
        for i in range(1,nrows):
            if element == sheet.row_values(i)[0]:
                locator = '("%s","%s",u"%s")'%(sheet.row_values(i)[1],sheet.row_values(i)[2],sheet.row_values(i)[0])
                return locator

    def get_pre_cases(self):
        sheet = self.case_file.sheet_by_name("public_case")
        nrows = sheet.nrows
        casename = ""
        case = []
        pre_cases = {}
        if nrows>1:
            for i in range(1,nrows):
                if sheet.row_values(i)[1]:
                    if i != 1:
                        pre_cases[casename] = case
                        case = []
                    casename = sheet.row_values(i)[1]
                case.append(sheet.row_values(i)[2:])
        pre_cases[casename] = case
        return pre_cases




