# -*- coding: utf-8 -*-
import scrapy


class InfSpider(scrapy.Spider):
    name = "infspider"
    allowed_domains = ["inf.ucv.cl"]
    start_urls = ['http://inf.ucv.cl/']
    
    def parse(self, response):
        pass
    def make_requests_from_url(self, url):
        return Request(url, method='HEAD', dont_filter=True)