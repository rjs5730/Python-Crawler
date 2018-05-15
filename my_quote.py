import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
<<<<<<< HEAD
                'text': quote.css('span.text::text').extract_first(),
=======
                'text': quote.css('span.text::text').extract(),
>>>>>>> hotfix
                'author': quote.css('small.author::text').extract(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
  
