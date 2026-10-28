# import scrapy
# from scrapy_selenium4 import SeleniumRequest
# from pathlib import Path
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC


# class ReviewsSpider(scrapy.Spider):
#     name = "reviews3"
#     allowed_domains = ["web-scraping.dev"]

#     async def start(self):
#         yield SeleniumRequest(
#             url="https://web-scraping.dev/reviews",
#             callback=self.parse,
#             wait_time=60,
#             wait_until=EC.presence_of_element_located(
#                 (By.CSS_SELECTOR, "[data-testid='review']")
#             ),
#         )

#     def parse(self, response):
#         reviews = response.css("[data-testid='review']")
#         yield {
#             "title": response.css("title::text").get(),
#             "reviews_rendered": len(reviews),
#             "first_review": reviews.css("[data-testid='review-text']::text").get(),
#         }

# def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = f"quotes-{page}.html"
#         Path(filename).write_bytes(response.body)