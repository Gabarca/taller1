# -*- coding: utf-8 -*-
import scrapy


class DipsySpider(scrapy.Spider):
    name = 'dipsy'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        self.log('pase por aca choro mota' + response.url)
