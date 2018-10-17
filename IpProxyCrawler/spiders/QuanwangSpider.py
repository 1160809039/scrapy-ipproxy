#!/usr/bin/python

# @File : QuanwangSpider.py
# @Author: 邵泽铭
# @Date : 10/9/18
# @Desc :

from enums.HttpType import HttpType
import scrapy
from items.items import IpproxycrawlerItem
from scrapy.spiders import CrawlSpider

from utils.SeleniumUtils import SeleniumUtils


class QuanwangSpider(CrawlSpider):


    allowed_domains = ['www.goubanjia.com']
    name = 'QuanwangSpider'
    start_urls=["http://www.goubanjia.com/"]





    def parse(self, response):
        html = SeleniumUtils.getEndHtml("http://www.goubanjia.com/")
        ipList = html.xpath("//*[@id='services']/div/div[2]/div/div/div/table/tbody/tr")
        for ipItem in ipList:
            item = IpproxycrawlerItem()
            ipAttrs = ipItem.xpath("./td")
            ips = ipAttrs[0].xpath("./*[@style!='display: none;' or @style!='display:none;']/text()")
            item["ip"] = self.getStr(ips)
            item["port"] = ipAttrs[0].xpath("./span[last()]/text()")[0]
            item["address"] = self.getStr(ipAttrs[3].xpath("./a/text()"))

            item["anonymous"] = ipAttrs[1].xpath("./a/text()")[0]
            httpType = ipAttrs[2].xpath("./a/text()")[0]
            item["httpType"] = self.getHttpType(httpType)
            item["validateTime"] = ipAttrs[6].xpath("./text()")[0]
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

    def getStr(self,ips):
        res=""
        for ip in ips:
            res=res+ip
        return res