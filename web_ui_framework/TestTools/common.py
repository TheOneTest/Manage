#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
import readConfig
import traceback


# localConfigHttp = httpConfig.ConfigHttp()
# log = Log.get_log()
# logger = log.logger
upPath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

# 从xml文件中读取sql语句
database = {}
def set_xml():
    if len(database) == 0:
        sql_path = os.path.join(readConfig.proDir, "testFile", "SQL.xml")
        tree = ElementTree.parse(sql_path)
        for db in tree.findall("database"):
            db_name = db.get("name")
            # print(db_name)
            table = {}
            for tb in db.getchildren():
                table_name = tb.get("name")
                # print(table_name)
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    # print(sql_id)
                    sql[sql_id] = data.text
                table[table_name] = sql
            database[db_name] = table

def get_xml_dict(database_name, table_name):
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict

def get_sql(database_name, table_name, sql_id):
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql