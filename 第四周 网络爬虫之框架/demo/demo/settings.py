# -*- coding: utf-8 -*-
BOT_NAME = 'demo'

SPIDER_MODULES = ['demo.spiders']
NEWSPIDER_MODULE = 'demo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'demo.pipelines.stockPipeline': 300,
}
