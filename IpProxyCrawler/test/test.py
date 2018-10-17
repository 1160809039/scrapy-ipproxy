#!/usr/bin/python

# @File : test.py
# @Author: 邵泽铭
# @Date : 10/10/18
# @Desc :
import re
import subprocess

from db.MongoConnect import mongo
from enums.SpiderName import SpiderName
from db.MongoDao import MongoDao
from datetime import datetime
import uuid
import sched
import requests
import time
import threadpool


# def sayhello(str):
#     print("aa "+str)
#     time.sleep(2)
#
# name_list =['xiaozi','aa','bb','cc']
# start_time = time.time()
# pool = threadpool.ThreadPool(10)
# request = threadpool.makeRequests(sayhello, name_list)
# [pool.putRequest(req) for req in request]
# pool.wait()
# print('%d second'% (time.time()-start_time))
# from utils.ValidateIP import ValidateIP
#
# ValidateIP.scanMongoIP("QuanwangSpider")

# proxyDict = {
#     "http": 'http://101.231.50.154:8000'
# }
# response=requests.get("http://www.ip3366.net/")
# print(response.text)
# print(re.match(r"/\?stype=1&page=5/",response.text))
#
#
# print(response.text.find("?stype=1&page=5"))

#
# print(str("   aaa   ").strip())


# lifeline = re.compile(r"(\d) received")
# report = ("No response", "Partial Response", "Alive")
#
# print(time.ctime())
#
#
# for host in range(1, 10):
#     ip = "www.baidu.com"
#     pingaling = subprocess.Popen(["ping", "-q", "-c 2", "-r", ip], shell=False, stdin=subprocess.PIPE,
#                                  stdout=subprocess.PIPE)
#     print("Testing ", ip)
#
#     while 1:
#         pingaling.stdout.flush()
#         line = pingaling.stdout.readline()
#         if not line: break
#         igot = re.findall(lifeline, str(line))
#         if igot:
#             print( report[int(igot[0])])
#
#
# print(time.ctime())


#
# import socket
#
# def getIP(domain):
#     myaddr = socket.getaddrinfo(domain, 'http')
#     print(myaddr[0][4][0])
#
# getIP("www.baidu11.com")
