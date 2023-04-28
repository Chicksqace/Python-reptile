# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re

class StockSpider(scrapy.Spider):
    name = 'stock'
    # allowed_domains = ['quote.eastmoney.com']
    start_urls = ['http://quote.eastmoney.com/stock_list.html']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.search(r"[s][hz]\d{6}", href).group(0)
                stock = stock.upper()
                url = 'https://xueqiu.com/S/' + stock
                yield scrapy.Request(url, callback = self.parse_stock)
            except:
                continue

    def parse_stock(self, response):
        infoDict = {}
        if response == "":
            exit()
        try:
            name = re.search(r'<div class="stock-name">(.*?)</div>', response.text).group(1)
            infoDict.update({'股票名称': name.__str__()})
            tableHtml = re.search(r'"tableHtml":"(.*?)",', response.text).group(1)
            soup = BeautifulSoup(tableHtml, "html.parser")
            table = soup.table
            for i in table.find_all("td"):
                line = i.text
                l = line.split("：")#这里的冒号为中文的冒号(：)!!!而不是英文的(:)
                infoDict.update({l[0].__str__(): l[1].__str__()})
            yield infoDict
        except:
            print("error")
