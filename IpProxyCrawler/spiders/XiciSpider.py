#!/usr/bin/python

# @File : XiciSpider.py
# @Author: 邵泽铭
# @Date : 10/9/18
# @Desc :

from enums.HttpType import HttpType
import scrapy
from items.items import IpproxycrawlerItem
from scrapy.spiders import CrawlSpider


class XiciSpider(CrawlSpider):


    allowed_domains = ['www.xicidaili.com']
    name = 'XiciSpider'

    def start_requests(self):
        yield scrapy.Request("http://www.xicidaili.com/")

    def parse(self, response):
        content= response.xpath("//table[@id='ip_list']")
        ipList=content.xpath("//tr")

        for ipItem in ipList:
            className=ipItem.xpath("./@class").extract()
            if len(className)!=0  and className[0]!='subtitle':
                 item = IpproxycrawlerItem()
                 ipAttrs= ipItem.xpath("./td")
                 item["address"] = ipAttrs[3].xpath("./text()").extract()[0]
                 item["ip"] = ipAttrs[1].xpath("./text()").extract()[0]
                 item["port"] = ipAttrs[2].xpath("./text()").extract()[0]
                 item["anonymous"] = ipAttrs[4].xpath("./text()").extract()[0]
                 httpType = ipAttrs[5].xpath("./text()").extract()[0]
                 item["httpType"] = self.getHttpType(httpType)
                 item["validateTime"] = ipAttrs[7].xpath("./text()").extract()[0]
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