import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        header = response.css('h1::text').get()
        paragraphs = response.css('p::text').get()

        yield {
            "header":header,
            "paragraphs":paragraphs
        }
