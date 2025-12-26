from scrapy.crawler import CrawlerProcess

from scraper.spiders.schedule import QuotesSeleniumSpider


if __name__ == '__main__':
    process = CrawlerProcess({
        'LOG_ENABLED': False
    })
    process.crawl(QuotesSeleniumSpider)
    process.start()
