# http://books.toscrape.com/

import scrapy

# Define the BookSpider class, which inherits from scrapy.Spider

class BookSpider(scrapy.Spider):
        name = 'bookspider'
        start_urls = ['http://books.toscrape.com/']

        # Define the parse method, which tells scrapy how we want to parse the result of the request
        def parse(self, response):
                # Start by calling response.css (similar to soup.select in BeautifulSoup)
                for article in response.css("article.product_pod"):
                        # We then want to yield the 
                        yield {
                                'price': article.css(".price_color::text").extract_first(), 
                                'title': article.css("h3 > a::attr(title)").extract_first()
                        }

                        # This is the logic for moving to another page
                        next = response.css('.next > a::attr(href)').extract_first()
                        if next:
                                yield response.follow(next, self.parse)
