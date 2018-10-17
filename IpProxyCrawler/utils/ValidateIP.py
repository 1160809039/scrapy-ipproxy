#!/usr/bin/python

# @File : ValidateIP.py
# @Author: 邵泽铭
# @Date : 10/10/18
# @Desc :
import urllib3
from enums.HttpType import HttpType
from utils.SpiderNameUtils import SpiderNameUtils
import requests
import re,time,threadpool
from db.MongoDao import MongoDao
from lxml import etree

class MyIp:
    url = "http://2018.ip138.com/ic.asp"
    def __init__(self):
        response = requests.get(self.url)
        selector = etree.HTML(response.text)
        content = selector.xpath("//center/text()")[0]
        self.content= content

myIp=MyIp().content

class ValidateIP:


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    url = "http://2018.ip138.com/ic.asp"

    def validate(self,ip,port,httpType):
        if httpType==HttpType.http.value:
             proxyDict={
                 "http": "%s://%s:%s"%(HttpType.http.value,ip,port)
             }
        elif httpType==HttpType.https.value:
            proxyDict = {
                "http": "%s://%s:%s" % (HttpType.http.value, ip, port),
                "https": "%s://%s:%s" % (HttpType.https.value, ip, port)
            }
        else:
            proxyDict = {
                "http": "%s://%s:%s" % (HttpType.socks.value, ip, port),
                "https": "%s://%s:%s" % (HttpType.socks.value, ip, port)
            }
        urllib3.disable_warnings()
        try:
            response=requests.get(ValidateIP.url,headers=ValidateIP.headers,proxies=proxyDict,verify=False, timeout=5)
            if response.status_code !=200 :
                return False
            else:
                print("SUCCESS:" + ip)
                return True
                # selector= etree.HTML(response.text)
                # res= selector.xpath("//center/text()")[0]
                # searchObj = re.search(r'\[(.*)\]', res, re.M | re.I)
                # if searchObj :
                #     ipNow= searchObj.group(1)
                #     if ipNow not in myIp:
                #         print("SUCCESS:"+ip)
                #         return True
                #     else:
                #         print("NOT:%s:%s" %(ip,port))
        except Exception as e:
            print("error: " +ip)
        return False

    @classmethod
    def scanMongoIP(cls,spideName):
        self=cls()
        spider = SpiderNameUtils.getSpiderName(spideName)
        datas = MongoDao.selectByName(spider)
        pool = threadpool.ThreadPool(10)
        request = threadpool.makeRequests(self.exec, datas)
        [pool.putRequest(req) for req in request]
        pool.wait()


    def exec(self,data):
        ip=data["ip"]
        port=data["port"]
        httpType=data["httpType"]
        try:
            res = self.validate(ip,port,httpType)
            if not res:
                MongoDao.deleteById(data["_id"])
        except Exception as e:
            MongoDao.deleteById(data["_id"])








