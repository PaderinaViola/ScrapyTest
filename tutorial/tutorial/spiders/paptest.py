import scrapy


class QuotesSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        "https://www.pap.pl/aktualnosci/zelenski-jestesmy-gotowi-do-rozejmu-ale-rosja-wlasnie-uderzyla-w-elektrocieplownie",
    ]

    def parse(self, response):
        yield {
                "title": response.css("h1.articleTitle span::text").get(), #we look into the html to find the keys how to access certain elements wee need
                
        }

      
#to be implemented: playwright, camoufox, optionally pi-hole + docker. traffic analysis



#<span class="text" itemprop="text">“...”</span>
#<small class="author" itemprop="author">Albert Einstein</small>

#so to get our needed element: 1. we take the type like <small></small>
#2. we take the class name like class="author"
#3. if it is a list/multiple divs, we take a general class name and also 
# the name of the list element quote.css("div.tags a.tag::text").getall()
#"name": quote.css("h1.articleTitle::text").get()