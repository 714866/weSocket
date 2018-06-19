# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:21:58 2018

@author: Administrator
"""

import pymongo
import json
class Monogo(object):
    def __init__(self):
        #创建mongodb连接
        self.mongoClient = pymongo.MongoClient(host='127.0.0.1',port=27017) 
        #mongodb的库，如mongodb没有这个库，则创建这个库，
        self.db = self.mongoClient['btc_usdt']
        #连接到表
        self.sheet = self.db['ticket']
        print('连接成功')
    def m_add(self,value):    
 

        print('进入mongodb_add')
        item = json.loads(value)
        self.sheet.insert(item)
        print('ok')


