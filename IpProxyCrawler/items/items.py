#!/usr/bin/python

# @File : EmailUtils.py
# @Author: 邵泽铭
# @Date : 10/9/18
# @Desc :

# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IpproxycrawlerItem(scrapy.Item):

    #id
    _id= scrapy.Field()
    # 服务器地址
    address = scrapy.Field()
    # ip
    ip = scrapy.Field()
    # ip端口
    port = scrapy.Field()
    # 匿名
    anonymous = scrapy.Field()
    # http类型
    httpType = scrapy.Field()
    # 验证时间
    validateTime = scrapy.Field()
    # 爬虫名
    spider = scrapy.Field()
    # 爬取时间
    spiderTime = scrapy.Field()

    pass
