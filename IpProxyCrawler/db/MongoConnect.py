#!/usr/bin/python

# @File : MongoConnect.py
# @Author: 邵泽铭
# @Date : 10/10/18
# @Desc :
from pymongo import MongoClient

class MongoConnect:
    url="127.0.0.1"
    port=27017
    # user="szm"
    # password="123456"
    conn = MongoClient(url,port)
    def __init__(self):
        db = self.conn.blogs  # 连接iptable数据库
        # db.authenticate(self.user, self.password)
        ipproxy=db.ipproxy
        self.ipproxy=ipproxy
mongo=MongoConnect().ipproxy