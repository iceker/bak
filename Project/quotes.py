# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['http://quotes.toscrape.com/page/1']
    start_urls = ['http://http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        pass
