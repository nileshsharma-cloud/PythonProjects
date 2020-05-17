import scrapy


class QuotesSpider(scrapy.Spider):
    name = "Quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.xpath('.//div[@class="quote"]'):
            yield {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.xpath('span/text()').get(),
            }

        next_page = response.xpath('.//li[@class="next"]/a').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
