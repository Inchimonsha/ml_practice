import scrapy


class AjaxSpider(scrapy.Spider):
    name = "ajax_spider"
    start_urls = ["https://webscraper.io/test-sites/e-commerce/ajax"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta={"playwright": True}  # Важный параметр для рендеринга через Playwright
            )

    def parse(self, response):
        # Каждый товар находится в блоке с классом 'thumbnail'
        products = response.css("div.thumbnail")
        for product in products:
            title = product.css("a.title::text").get()
            price = product.css("h4.price::text").get()
            yield {
                "title": title,
                "price": price,
            }

        # Опционально можно парсить постраничную навигацию, если есть
        next_page = response.css("ul.pagination li.next a::attr(href)").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(
                next_page_url,
                meta={"playwright": True},
                callback=self.parse
            )
