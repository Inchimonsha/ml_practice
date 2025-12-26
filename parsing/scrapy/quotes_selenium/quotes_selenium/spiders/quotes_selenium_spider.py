import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector


class QuotesSeleniumSpider(scrapy.Spider):
    name = "quotes_selenium"
    start_urls = ["https://quotes.toscrape.com/js/"]

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=chrome_options)
        super().__init__()

    def parse(self, response):
        self.driver.get(response.url)
        html = self.driver.page_source
        resp_obj = Selector(text=html)

        quotes = resp_obj.css("div.quote")
        for quote in quotes:
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

    def closed(self, reason):
        self.driver.quit()
