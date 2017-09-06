# _author_='Administrator'
# -*- coding: utf-8 -*-
from os.path import join
from xlutils.copy import copy
import os,sys,xdrlib
import xlrd
import xlwt
import datetime,time
def open_excel(self,file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def Write_Excel(L=None):
    if L is None:
        L=[]

    file_f = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    file = file_f + '\\execl\\smart_piano_user.xls'
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheet_by_index(0)
    rowNum = sheet.nrows
    colNum = sheet.ncols

    newbook = copy(workbook)
    now = datetime.datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    newsheet = newbook.get_sheet(0)
    newsheet.write(rowNum,0,L)
    newsheet.write(rowNum,1,'a123456')
    newsheet.write(rowNum,2,str(now_str))    
    newbook.save(file)
