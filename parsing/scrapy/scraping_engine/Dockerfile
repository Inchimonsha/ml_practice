FROM python:3.12
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY scraper/scraper ./scraper
CMD ["scrapy", "crawl", "rasp"]
