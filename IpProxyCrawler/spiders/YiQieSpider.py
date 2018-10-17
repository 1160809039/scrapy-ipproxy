#!/usr/bin/python

# @File : YiQieSpider.py
# @Author: 邵泽铭
# @Date : 10/9/18
# @Desc :

from enums.HttpType import HttpType
import scrapy
from items.items import IpproxycrawlerItem
from scrapy.spiders import CrawlSpider



class YiQieSpider(CrawlSpider):
    allowed_domains = ['ip.yqie.com']
    name = 'YiQieSpider'

    def start_requests(self):
        yield scrapy.Request("http://ip.yqie.com/ipproxy.htm")

    def parse(self, response):
        ipList= response.xpath("//table/tr")

        for ipItem in ipList:
                 item = IpproxycrawlerItem()
                 ipAttrs= ipItem.xpath("./td")
                 if len(ipAttrs)==0:
                     continue
                 item["address"] = ipAttrs[2].xpath("./text()").extract()[0]
                 item["ip"] = ipAttrs[0].xpath("./text()").extract()[0]
                 item["port"] = ipAttrs[1].xpath("./text()").extract()[0]
                 item["anonymous"] = ipAttrs[3].xpath("./text()").extract()[0]
                 httpType = ipAttrs[4].xpath("./text()").extract()[0]
                 item["httpType"] = self.getHttpType(httpType)
                 yield item

    #获取http类型
    def getHttpType(self,http):
        http=http.lower()
        if http=="http":
            return  HttpType.http.value
        if http == "https":
            return HttpType.https.value
        if "socks" in http:
            return HttpType.socks.value