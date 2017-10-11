#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import testlink
manual = 1   #自动
automation = 2  #手动
#连接testlink
url = "http://192.168.199.13:81/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
key = "68194d618ccb4ce674f3935d73bf77ac"
tlc = testlink.TestlinkAPIClient(url,key)

#获取TestLink上的信息：
def get_information_test_project():
    print("Number of Projects      in TestLink: %s " % tlc.countProjects())
    print("Number of Platforms  (in TestPlans): %s " % tlc.countPlatforms())
    print("Number of Builds                   : %s " % tlc.countBuilds())
    print("Number of TestPlans                : %s " % tlc.countTestPlans())
    print("Number of TestSuites               : %s " % tlc.countTestSuites())
    print("Number of TestCases (in TestSuites): %s " % tlc.countTestCasesTS())
    print("Number of TestCases (in TestPlans) : %s " % tlc.countTestCasesTP())
    tlc.listProjects()

#获取test suite：
def get_test_suite():
    projects = tlc.getProjects()
    top_suites = tlc.getFirstLevelTestSuitesForTestProject(projects[0]["id"])
    for suite in top_suites:
        print suite["id"], suite["name"]

#创建测试用例集
def create_test_suite(project_id, test_suite_name, test_suite_describe, father_id):
    if father_id == "":
        tlc.createTestSuite(project_id, test_suite_name, test_suite_describe)
    else:
        tlc.createTestSuite(project_id, test_suite_name, test_suite_describe, parentid=father_id)

#创建测试用例
def create_test_case(father_id, data):
    tlc.initStep(data[0][2], data[0][3], automation)
    for i in range(1, len(data)):
        tlc.appendStep(data[i][2], data[i][3], automation)
    tlc.createTestCase(data[0][0], father_id, "1", "timen.xu", "", preconditions=data[0][1])

#获取测试用例
def get_test_case(test_case_id):
    test_case = tlc.getTestCase(None, testcaseexternalid=test_case_id)
    for i in test_case:
        print ("序列,执行步骤,预期结果")
        for m in i.get("steps"):
            print (m.get("step_number") + m.get("actions") + m.get("expected_results"))

#发送测试结果给TestLink
def report_test_result(test_plan_id, test_case_id, test_result):
    tlc.reportTCResult(None, test_plan_id, None, test_result, "", guess=True,testcaseexternalid=test_case_id, platformname="0")

if __name__ == '__main__':
    # get_information_test_project()
    get_test_suite()
    # get_test_case('01-1')