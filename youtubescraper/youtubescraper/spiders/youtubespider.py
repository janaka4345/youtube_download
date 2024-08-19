from typing import Iterable
import scrapy


class YoutubespiderSpider(scrapy.Spider):
    name = "youtubespider"
    allowed_domains = ["youtube.com"]

    def start_requests(self):
        pass

    def parse(self, response):
        pass
