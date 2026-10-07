from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes2" #each spider name must be unique in the project

    async def start(self):
        urls = [
            "https://www.pap.pl/aktualnosci/atak-w-szkole-w-ostrolece-co-najmniej-siedem-osob-rannych",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")