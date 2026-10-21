import scrapy
from pathlib import Path

class GutenbergSpider(scrapy.Spider):
    name = "gutenberg"
    # Stripped down to just the domain name
    # allowed_domains = ["www.gutenberg.org"] 

    # Corrected entry point method name
    def start_requests(self):
        url = "https://gutenberg.org/ebooks/search/?sort_order=random"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 1. Save the raw HTML page if you still need it
        page = response.url.split("=")[-1]  # Safely handle the query parameter
        filename = f"gutenberg-{page}.html"
        Path(filename).write_bytes(response.body)
        
        # 2. Extract and yield the book information
        for book in response.css('li.booklink'):
            yield {
                'title': book.css('span.title::text').get(default='').strip(),
                'author': book.css('span.subtitle::text').get(default='').strip(),
                'link': response.urljoin(book.css('a.link::attr(href)').get()),
                'cover_image': response.urljoin(book.css('img.cover-thumb::attr(src)').get())
            }
