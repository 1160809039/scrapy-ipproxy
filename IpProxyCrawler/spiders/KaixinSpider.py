#!/usr/bin/python

# @File : KaixinSpider.py
# @Author: 邵泽铭
# @Date : 10/9/18
# @Desc :

from enums.HttpType import HttpType
import scrapy
from items.items import IpproxycrawlerItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import uuid



class KaixinSpider(CrawlSpider):


    allowed_domains = ['ip.kxdaili.com']
    name = 'KaixinSpider'
    link = LinkExtractor(allow=(r"/ipList/[\d]\.html#ip"))

    rules = [
        Rule(link, callback="parse_page", follow=False),
    ]

    def start_requests(self):
        yield scrapy.Request("http://ip.kxdaili.com/")


    def parse_page(self, response):
        trs= response.xpath("//*[@id='nav_btn01']/div[5]/table/tbody/tr")
        for tr in trs:
            item = IpproxycrawlerItem()
            ipAttrs = tr.xpath("./td")
            item["address"] = ipAttrs[5].xpath("./text()").extract()[0]
            item["ip"] = ipAttrs[0].xpath("./text()").extract()[0]
            item["port"] = ipAttrs[1].xpath("./text()").extract()[0]
            item["anonymous"] = ipAttrs[2].xpath("./text()").extract()[0]
            item["validateTime"] = ipAttrs[6].xpath("./text()").extract()[0]

            httpType = ipAttrs[3].xpath("./text()").extract()[0]
            httpType = httpType.lower()
            if httpType == "http":
                item["httpType"] = HttpType.http.value
                yield item
            if httpType == "https":
                item["httpType"] = HttpType.https.value
                yield item
            if "http" in httpType and "https" in httpType:
                item["httpType"] = "http"
                item["_id"]= str(uuid.uuid4()).replace("-","")
                yield item
                item["_id"] = str(uuid.uuid4()).replace("-", "")
                item["httpType"] = "https"
                yield item


