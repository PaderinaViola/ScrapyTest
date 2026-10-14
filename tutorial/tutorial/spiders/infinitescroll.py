import scrapy


class QuotesSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        "https://infiniteajaxscroll.com/examples/articles/",
    ]

    def parse(self, response):
        yield {
                "title": response.css("p.article__p--first  ").get(), #we look into the html to find the keys how to access certain elements wee need
                
        }


