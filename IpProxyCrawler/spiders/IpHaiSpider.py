#!/usr/bin/python

# @File : IpHaiSpider.py
# @Author: 邵泽铭
# @Date : 10/9/18
# @Desc :
import uuid

from enums.HttpType import HttpType
import scrapy
from items.items import IpproxycrawlerItem
from scrapy.spiders import CrawlSpider
from utils.StringUtils import StringUtils

class IpHaiSpider(CrawlSpider):


    allowed_domains = ['www.iphai.com']
    name = 'IpHaiSpider'

    def start_requests(self):
        yield scrapy.Request("http://www.iphai.com/")

    def parse(self, response):


        ipList= response.xpath("/html/body/div[4]/div[2]/table/tr")
        for ipItem in ipList:
                 item = IpproxycrawlerItem()
                 ipAttrs= ipItem.xpath("./td")
                 if len(ipAttrs)==0:
                     continue
                 item["address"] = StringUtils.strTrim(ipAttrs[5].xpath("./text()").extract()[0])
                 item["ip"] = StringUtils.strTrim(ipAttrs[0].xpath("./text()").extract()[0])
                 item["port"] = StringUtils.strTrim(ipAttrs[1].xpath("./text()").extract()[0])
                 item["anonymous"] = StringUtils.strTrim(ipAttrs[2].xpath("./text()").extract()[0])
                 httpType = StringUtils.strTrim(ipAttrs[3].xpath("./text()").extract()[0])
                 item["validateTime"] = StringUtils.strTrim(ipAttrs[7].xpath("./text()").extract()[0])

                 httpType = httpType.lower()
                 if httpType == "http":
                     item["httpType"] = HttpType.http.value
                     yield item
                 if httpType == "https":
                     item["httpType"] = HttpType.https.value
                     yield item
                 if "http" in httpType and "https" in httpType:
                     item["httpType"] = "http"
                     item["_id"] = str(uuid.uuid4()).replace("-", "")
                     yield item
                     item["_id"] = str(uuid.uuid4()).replace("-", "")
                     item["httpType"] = "https"
                     yield item
