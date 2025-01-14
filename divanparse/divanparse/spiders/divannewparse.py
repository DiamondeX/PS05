import scrapy


class DivannewparseSpider(scrapy.Spider):
    name = "divannewparse"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
            yield {
                'name': divan.css('div.lsooF span[itemprop=name]::text').get(),
                'price': int(divan.css('div.lsooF meta[itemprop=price]').attrib['content']),
                'url': divan.css('div.lsooF a.qUioe').attrib['href']
            }

