import os, json, contextlib, sqlite3

from scrapy.crawler import CrawlerProcess
from scraper.spiders import SBROddsSpider

SCRAPY_USER_AGENT = os.getenv('SCRAPY_USER_AGENT')
SCRAPY_LOG_LEVEL = os.getenv('SCRAPY_LOG_LEVEL')


class SBROddsTracker():
    def __init__(self):
        self.update()

    def update(self):
        self.crawl_spider()

    def crawl_spider(self):
        process = CrawlerProcess({
            "USER_AGENT": SCRAPY_USER_AGENT,
            "LOG_LEVEL": SCRAPY_LOG_LEVEL,
            "ITEM_PIPELINES": {
              'scraper.pipelines.SQLitePipeline': 300,
            }})
        process.crawl(SBROddsSpider)
        process.start()
