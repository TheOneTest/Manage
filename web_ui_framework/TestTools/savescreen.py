#coding:utf-8
__author__ = 'huangxb'
import os

import sorttime


def savepngname():
    u"""截图操作，文件存放testresult\日期\image"""
    tm= sorttime.gettime()
    day= sorttime.getday()
    mypath=os.path.abspath(os.getcwd())
    fp=mypath+"\\TestResult\\"+day+"\\image\\"
    if os.path.exists(fp):
        imgname=fp+str(tm)+'.png'
    else:
        try:
            os.mkdir(mypath+"\\TestResult\\")
        except Exception,e:
            pass
        try:
            os.mkdir(mypath+"\\TestResult\\"+day)
        except Exception,e:
            pass
        try:
            os.mkdir(fp)
        except Exception,e:
            pass

        imgname=fp+str(tm)+'.png'
    return imgname

def savescreen(driver):
    imagename=savepngname()
    image=driver.save_screenshot(imagename)
    return imagename


