import scrapy
from scrapy_selenium4 import SeleniumRequest
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ReviewsSpider(scrapy.Spider):
    name = "gutenberg"
    allowed_domains = ["https://www.gutenberg.org"]

    async def start(self):
        yield SeleniumRequest(
            url="https://www.gutenberg.org/ebooks/search/?sort_order=random",
            callback=self.parse,
            wait_time=60,
            wait_until=EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='review']")
            ),
        )

    def parse(self, response):
    
        for book in response.css('li.booklink'):
            yield {
                'title': book.css('span.title::text').get(default='').strip(),
                'author': book.css('span.subtitle::text').get(default='').strip(),
                'link': response.urljoin(book.css('a.link::attr(href)').get()),
                'cover_image': response.urljoin(book.css('img.cover-thumb::attr(src)').get())
            }


def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)