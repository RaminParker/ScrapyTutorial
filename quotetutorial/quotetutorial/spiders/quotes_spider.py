import scrapy
from quotetutorial.items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
      'http://quotes.toscrape.com/'
    ]

    def parse(self, response):

        items = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:

            title = all_div_quotes.css('span.text::text').extract()
            author = all_div_quotes.css('.author::text').extract()
            tag = all_div_quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items