# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
__author__ = 'hejianjun'

import redis
from TestTools import readConfig

class RedisExcute:
    def __init__(self):
        rc = readConfig.ReadConfig()
        host = rc.get_redis("host")
        port = rc.get_redis("port")
        db = rc.get_redis("db")
        pool = redis.ConnectionPool(host=host,port=port,db=db)
        self.r = redis.Redis(connection_pool=pool)

    def getUser(self,mobile):
        userid = self.r.get('username:%s'% mobile)
        userInfo = self.r.hgetall("user:%s" % userid)    #获取全部
        #userInfo = r.hget("user:%s" % userid,"username")#获取username
        return userInfo

    def delUser(self,mobile):
        if self.r.exists("username:%s" % mobile):
            res =  self.r.delete("username:%s" % mobile)
            if res == 1:
                # return True
                return True
            else:
                return False
        else:
            return False

    def setUser(self,mobile,module,changeName,param):
        userid = self.r.get('username:%s'% mobile)
        rest = self.r.hset('%s:%s' % (module,userid),changeName,param)
        print rest

    def setUsers(self,mobile,*args):
        userid = self.r.get('username:%s'% mobile)
        # for item in args:
        #     rest = self.r.hset('%s:%s' % (item[0],userid),item[1],item[2])
        #     print rest
        rest = self.r.hset('%s:%s' % (args[0], userid), args[1], args[2])
        print rest

        #
        # print rest



