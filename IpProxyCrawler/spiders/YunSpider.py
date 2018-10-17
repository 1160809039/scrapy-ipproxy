# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items.items import IpproxycrawlerItem
from enums.HttpType import HttpType

class YunSpider(CrawlSpider):


    name = 'YunSpider'
    allowed_domains = ['www.ip3366.net']

    link= LinkExtractor(allow=(r"\?stype=1&page=[0-5]"))

    rules = [
        Rule(link, callback="parse_page", follow=True)
    ]
    def start_requests(self):
        yield scrapy.Request("http://www.ip3366.net/")


    def parse_page(self,response):
        resList= response.xpath("//*[@id='list']/table/tbody/tr")
        for res in resList:
            item=IpproxycrawlerItem()
            ipAttrs = res.xpath("./td")
            item["address"] = ipAttrs[5].xpath("./text()").extract()[0]
            item["ip"] = ipAttrs[0].xpath("./text()").extract()[0]
            item["port"] = ipAttrs[1].xpath("./text()").extract()[0]
            item["anonymous"] = ipAttrs[2].xpath("./text()").extract()[0]
            httpType = ipAttrs[3].xpath("./text()").extract()[0]
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