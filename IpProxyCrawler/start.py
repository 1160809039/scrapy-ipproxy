#!/usr/bin/python

# @File : start.py
# @Author: 邵泽铭
# @Date : 10/9/18
# @Desc :

import os

import time,sched


s = sched.scheduler(time.time,time.sleep)
def crawler():
    os.system("scrapy crawlall")
def exec():
    s.enter(600, 1, exec, ())
    crawler()

s.enter(0,0,exec,())
s.run()


