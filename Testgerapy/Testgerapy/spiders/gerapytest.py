# -*- coding: utf-8 -*-
import scrapy


class GerapytestSpider(scrapy.Spider):
    name = 'gerapytest'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
