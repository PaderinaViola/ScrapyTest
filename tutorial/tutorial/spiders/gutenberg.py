import scrapy
from pathlib import Path

class GutenbergSpider(scrapy.Spider):
    name = "gutenberg"

    async def start(self): #THE PROBLEM WAS WITH START HERE
        url = "https://gutenberg.org/ebooks/search/?sort_order=random"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        Path("gutenberg-random.html").write_bytes(response.body)

        for book in response.css('li.booklink'):
            link = book.css('a.link::attr(href)').get()
            cover = book.css('img.cover-thumb::attr(src)').get()
            yield {
                'title': book.css('span.title::text').get(default='').strip(),
                'author': book.css('span.subtitle::text').get(default='').strip(),
                'link': response.urljoin(link) if link else None,
                'cover_image': response.urljoin(cover) if cover else None,
            }