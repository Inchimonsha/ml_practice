import json

import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class RaspSpider(scrapy.Spider):
    name = 'rasp'
#     allowed_domains = ['eios-po.kosgos.ru']
    start_urls = ['https://eios.kosgos.ru/WebApp/#/Rasp/List']

#     def parse(self, response):
#         items = response.css('table')
#         # for item in items:
#         #     yield {
#         #         'field1': item.css('div::text').get(),
#         #         # и т.д.
#         #     }


    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Запуск браузера в режиме без GUI
        self.driver = webdriver.Chrome(options=chrome_options)
        super().__init__()

    def parse(self, response):
        self.driver.get(response.url)  # Открыть страницу в Selenium
        
        # Опционально: можно добавить ожидание загрузки элементов, например:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.some-class')))
        
        # Получить полностью отрендеренный HTML
        rendered_html = self.driver.page_source
        
        # Создать Selector Scrapy для парсинга
        response_obj = Selector(text=rendered_html)
        
        # Пример: извлечь заголовок страницы
        title = response_obj.css('div::text').get()
        
        yield {
            'title': title
        }
    
    def closed(self, reason):
        self.driver.quit()  # Закрыть драйвер при завершении паука
