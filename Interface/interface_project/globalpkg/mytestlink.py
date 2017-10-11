#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'shouke'

from testlink import TestLinkHelper, TestlinkAPIClient
import testlink
#from testlink.testlinkerrors import TLResponseError
from globalpkg.log import logger

class TestLink():
    def __init__(self):
        tlk_helper = TestLinkHelper()
        url = "http://192.168.199.13:81/testlink/lib/api/xmlrpc/v1/xmlrpc.php"
        key = "68194d618ccb4ce674f3935d73bf77ac"

        try:
            self.testlink = testlink.TestlinkAPIClient(url, key)  # 连接TestLink
        except Exception as e:
            logger.error('连接testlink失败：%s' % e)
            exit()

    def get_testlink(self):
        return self.testlink


