#!/usr/bin/python

# @File : SpiderNameUtils.py
# @Author: 邵泽铭
# @Date : 10/10/18
# @Desc :

from enums.SpiderName import SpiderName


class SpiderNameUtils:
    @staticmethod
    def getSpiderName(spider):
        if spider==None:
            return ""
        elif spider==SpiderName.XiciSpider.name:
            return  SpiderName.XiciSpider.value
        elif spider==SpiderName.kuaiSpider.name:
            return  SpiderName.kuaiSpider.value
        elif spider == SpiderName.KaixinSpider.name:
            return SpiderName.KaixinSpider.value
        elif spider == SpiderName.YunSpider.name:
            return SpiderName.YunSpider.value
        elif spider == SpiderName.IpHaiSpider.name:
            return SpiderName.IpHaiSpider.value
        elif spider == SpiderName.XiaosuSpider.name:
            return SpiderName.XiaosuSpider.value
        elif spider == SpiderName.QuanwangSpider.name:
            return SpiderName.QuanwangSpider.value
        elif spider == SpiderName.YiQieSpider.name:
            return SpiderName.YiQieSpider.value