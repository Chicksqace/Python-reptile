import scrapy


class DemoSpider(scrapy.Spider):
    name = "demo"
    # 爬虫的名称
    # allowed_domains = ["python123.io"]
    # 最开始用户提交给命令行的域名，指的是爬虫在爬取网站的时候，它只能爬取这个域名以下的相关链接
    start_urls = ["http://python123.io/ws/demo.html"]
    # 以列表形式包含的一个或多个域名就是scrapy框架所要爬取页面的初始页面

    def parse(self, response):
        # 文件的名字
        fname=response.url.split('/')[-1]
        # 返回的内容保存为文字
        with open(fname,'wb') as f:
            f.write(response.body)
