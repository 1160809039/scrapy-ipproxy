# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items.items import IpproxycrawlerItem
from enums.HttpType import HttpType
from utils.StringUtils import StringUtils


class XiaosuSpider(CrawlSpider):


    name = 'XiaosuSpider'
    allowed_domains = ['www.xsdaili.com']
    def start_requests(self):
        yield scrapy.Request("http://www.xsdaili.com/")


    def parse(self, response):
        reso= response.xpath("/html/body/div[5]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/a[1]/@href").extract()[0]
        rest = response.xpath("/html/body/div[5]/div/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/a[1]/@href").extract()[0]
        yield scrapy.Request(url="http://www.xsdaili.com/"+reso,callback=self.parse_page)
        yield scrapy.Request(url="http://www.xsdaili.com/"+rest, callback=self.parse_page)


    def parse_page(self,response):
        res=response.xpath("/html/body/div[5]/div/div[2]/div/div/div/div[2]/div/div[2]/div[2]/text()").extract()
        for re in res:
           re= StringUtils.strTrim(re)
           item=IpproxycrawlerItem()
           item["ip"] = str(re).split(":")[0]
           re = str(re).split(":")[1]
           item["port"] =str(re).split("@")[0]
           re = str(re).split("@")[1]

           httpType = re.split("#")[0]
           item["httpType"] = self.getHttpType(httpType)
           re = re.split("#")[1]
           item["anonymous"] = re.split("]")[0].strip("[")
           re = re.split("]")[1]
           item["address"] =re.split(" ")[0]
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