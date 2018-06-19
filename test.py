# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 08:26:36 2018

@author: Administrator
"""
import time
from vnzb import *

# 在zb网站申请这两个Key，分别对应用户名和密码
apiKey = 'apikey'
secretKey = 'secretkey'
#暂时不需要
# 创建API对象
class Test(object):
    def __init__(self):
        self.api = ZB_Sub_Spot_Api()
#        self.api.connect_Subpot(apiKey, secretKey, True)
        self.i=0
    def test_send(self,value):
        self.api.connect_Subpot(apiKey, secretKey, True)
        while self.api.open_status==0:
            #循环直到建立好连接
            time.sleep(1)
            
        while True:
            try:
                self.api.subscribeSpotTicker('btc_usdt')
                print('send_success')
                break
        
            except:
                pass
        while True:
            #检查是否断开，断开重连
            
            #测试断开重连的代码
#            if self.i==0:
#                self.api.close()
#                print('关闭')
            if self.api.close_status==1:
                self.api.reconnect()
                self.i=2
                break
        print('重启test_send')
        self.test_send(value)
if __name__=='__main__':
    test=Test()
    val = input('请输入要查询ticker数据货币名:')
    test.test_send('btc_usdt')
            
