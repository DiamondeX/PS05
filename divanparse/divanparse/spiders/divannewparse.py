import scrapy


class DivannewparseSpider(scrapy.Spider):
    name = "divannewparse"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        pass
