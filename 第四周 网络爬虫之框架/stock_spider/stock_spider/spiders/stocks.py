import scrapy

class StocksSpider(scrapy.Spider):
    name = "stocks"

    def start_requests(self):
        urls = [
            'http://quote.eastmoney.com/stocklist.html',  # 东方财富网
            'http://gupiao.baidu.com/stock/',  # 百度股票
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 从东方财富网提取股票数据
        if 'eastmoney' in response.url:
            for href in response.css('a[target="_blank"]::attr(href)').extract():
                if 'http://quote.eastmoney.com/sh' in href or 'http://quote.eastmoney.com/sz' in href:
                    yield scrapy.Request(url=href, callback=self.parse_stock)

        # 从百度股票提取股票数据
        if 'baidu' in response.url:
            for href in response.css('a::attr(href)').extract():
                if 'http://gupiao.baidu.com/stock/sh' in href or 'http://gupiao.baidu.com/stock/sz' in href:
                    yield scrapy.Request(url=href, callback=self.parse_stock)

    def parse_stock(self, response):
        # 提取股票名称和交易信息
        name = response.css('h1::text').extract_first()
        info = response.css('div.quote-wrap table tr td::text').extract()

        # 将数据保存到文件中
        with open('stocks.txt', 'a') as f:
            f.write(name + '\n')
            for i in range(0, len(info), 2):
                f.write(info[i] + ': ' + info[i+1] + '\n')
            f.write('\n')