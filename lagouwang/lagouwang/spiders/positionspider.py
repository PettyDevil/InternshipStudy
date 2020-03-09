# -*- coding: utf-8 -*-
import scrapy


class PositionspiderSpider(scrapy.Spider):
    name = 'positionspider'
    allowed_domains = ['51job.com']
    start_urls = ['http://51job.com/']

    def parse(self, response):
        pass
