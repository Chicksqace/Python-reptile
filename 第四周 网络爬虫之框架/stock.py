import scrapy


class StockSpider(scrapy.Spider):
    name = "stock"
    allowed_domains = ["quote.eastmoney.com"]
    start_urls = ["http://quote.eastmoney.com/"]

    def parse(self, response):
        pass
