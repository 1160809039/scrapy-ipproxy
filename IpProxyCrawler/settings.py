#!/usr/bin/python

# @File : EmailUtils.py
# @Author: 邵泽铭
# @Date : 10/9/18
# @Desc :


#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'IpProxyCrawler'

SPIDER_MODULES = ['IpProxyCrawler.spiders']
NEWSPIDER_MODULE = 'IpProxyCrawler.spiders'
COMMANDS_MODULE = 'IpProxyCrawler.commands'

#
# # 指定使用scrapy-redis的调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# # 指定使用scrapy-redis的去重
# DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
#
# # 指定排序爬取地址时使用的队列，
# # 默认的 按优先级排序(Scrapy默认)，由sorted set实现的一种非FIFO、LIFO方式。
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
# # 可选的 按先进先出排序（FIFO）
# # SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
# # 可选的 按后进先出排序（LIFO）
# # SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'
#
# # 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理redis queues
# SCHEDULER_PERSIST = True
#
# # 只在使用SpiderQueue或者SpiderStack是有效的参数，指定爬虫关闭的最大间隔时间
# # SCHEDULER_IDLE_BEFORE_CLOSE = 10
#
# # 通过配置RedisPipeline将item写入key为 spider.name : items 的redis的list中，供后面的分布式处理item
# # 这个已经由 scrapy-redis 实现，不需要我们写代码
# #默认情况下,RFPDupeFilter只记录第一个重复请求。将DUPEFILTER_DEBUG设置为True会记录所有重复的请求。
# DUPEFILTER_DEBUG =True

#
# # 指定redis数据库的连接参数
# # REDIS_PASS是我自己加上的redis连接密码（默认不做）
# REDIS_HOST = '39.104.108.111'
# REDIS_PORT = 6379
# #REDIS_PASS = 'redisP@ssw0rd'








# LOG等级
LOG_LEVEL = 'ERROR'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'IpProxyCrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 覆盖默认请求头，可以自己编写Downloader Middlewares设置代理和UserAgent
DEFAULT_REQUEST_HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch'
}
# 修改编码为utf-8
FEED_EXPORT_ENCODING = 'utf-8'
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'IpProxyCrawler.middleware.middlewares.IpproxycrawlerSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'IpProxyCrawler.middleware.middlewares.IpproxycrawlerDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'IpProxyCrawler.pipline.pipelines.IpproxycrawlerPipeline': 300,
}

DOWNLOAD_DELAY = 3
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 3
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
