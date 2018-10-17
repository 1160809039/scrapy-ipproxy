#!/usr/bin/python

# @File : EmailUtils.py
# @Author: 邵泽铭
# @Date : 10/9/18
# @Desc :

# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from utils.ValidateIP import ValidateIP
from utils.SpiderNameUtils import SpiderNameUtils
from db.MongoConnect import MongoConnect
from datetime import datetime
from db.MongoDao import MongoDao

class IpproxycrawlerPipeline(object):
    def process_item(self, item, spider):

        # utcnow() 是获取UTC时间
        item["spiderTime"] = datetime.utcnow()
        # 爬虫名
        item["spider"] = SpiderNameUtils.getSpiderName(spider.name)
        # if ValidateIP().validate(ip=item["ip"],port=item["port"],httpType=item["httpType"]):
        if MongoDao.selectByIp(ip=item["ip"],port=item["port"],httpType=item["httpType"]).count()==0:
               MongoDao.insert(item)

        return item

    def open_spider(self, spider):
        print("pipline start "+spider.name)

    def close_spider(self, spider):
        ValidateIP.scanMongoIP(spider.name)
        MongoConnect.conn.close()
        print("pipline close "+spider.name)