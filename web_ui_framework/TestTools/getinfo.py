__author__ = 'jyd'


import time
def gettime():
    nowtime=time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time()))
    return nowtime
def getday():
    day=time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return day

def getdate(days=0):
    nowdate = time.strftime("%Y-%m-%d",time.localtime(time.time()-60*60*24*int(days)))
    return nowdate

