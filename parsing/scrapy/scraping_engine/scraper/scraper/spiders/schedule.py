import time
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.selector import Selector
from selenium.common.exceptions import TimeoutException


class QuotesSeleniumSpider(scrapy.Spider):
    name = "rasp"
    start_urls = ["https://eios.kosgos.ru/WebApp/#/Rasp/List"]

    def __init__(self, *args, **kwargs):
        super().__init__()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=chrome_options)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        self.driver.get(response.url)
        wait = WebDriverWait(self.driver, 30)

        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "circle")))
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "spinner")))
        # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table")))

        # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.v-data-table__wrapper table")))
        time.sleep(10)
        self.driver.save_screenshot("page_screenshot.png")

        html = self.driver.page_source
        resp_obj = Selector(text=html)

        divs = resp_obj.css("div")
        print(divs)

        rows = resp_obj.css("div.v-data-table__wrapper table tbody tr")
        for row in rows:
            group = row.css("td:nth-child(1) a::text").get()
            faculty = row.css("td:nth-child(2)::text").get()
            course = row.css("td:nth-child(3)::text").get()
            yield {
                "group": group.strip() if group else None,
                "faculty": faculty.strip() if faculty else None,
                "course": course.strip() if course else None,
            }
            print(course)

    def closed(self, reason):
        self.driver.quit()
