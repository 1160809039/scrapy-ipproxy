# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items.items import IpproxycrawlerItem
from enums.HttpType import HttpType

class KuaiSpider(CrawlSpider):
    name = 'kuaiSpider'
    allowed_domains = ['www.kuaidaili.com']
    linkintr= LinkExtractor(allow=(r"/free/intr/[1-3]/"))
    linkinha = LinkExtractor(allow=(r"/free/inha/[1-3]/"))
    rules = [
        Rule(linkintr,callback="parse_page",follow=False),
        Rule(linkinha, callback="parse_page", follow=False)
    ]

    def start_requests(self):
        yield scrapy.Request("https://www.kuaidaili.com/free/inha/1/")
        yield scrapy.Request("https://www.kuaidaili.com/free/intr/1/")

    def parse_page(self,response):
        resList= response.xpath("//*[@id ='list']/table/tbody/tr")
        for res in resList:
            item=IpproxycrawlerItem()
            ipAttrs = res.xpath("./td")
            item["address"] = ipAttrs[4].xpath("./text()").extract()[0]
            item["ip"] = ipAttrs[0].xpath("./text()").extract()[0]
            item["port"] = ipAttrs[1].xpath("./text()").extract()[0]
            item["anonymous"] = ipAttrs[2].xpath("./text()").extract()[0]
            httpType = ipAttrs[3].xpath("./text()").extract()[0]
            item["httpType"] = self.getHttpType(httpType)
            item["validateTime"] = ipAttrs[6].xpath("./text()").extract()[0]
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