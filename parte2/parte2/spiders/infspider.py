# -*- coding: utf-8 -*-
import scrapy


import scrapy
import pandas as pd
import functools
from parte2.items import Parte2Item
from scrapy.http import Request





#InfSpider es la araña encargada de recorrer  http://www.inf.ucv.cl
class InfSpider(scrapy.Spider):
    name = 'InfSpider'
    allowed_domains = ['inf.ucv.cl']
    start_urls = ['http://www.inf.ucv.cl']

    def start_requests(self):
        yield scrapy.Request('http://www.inf.ucv.cl', self.parse)

    def parse(self, response):
        item=Parte2Item()
        links = scrapy.linkextractors.LinkExtractor().extract_links(response)
        for i in links:
            item["linky"]= i.url
            item["status"]= self.make_requests_from_url(i.url,item)
            print(item)
            
        print("soy al final")

    def make_requests_from_url(self, url,item):
        Request(url, method='HEAD', dont_filter=True,callback=self.info).meta["item"]=item
        print("peter parker")
        return Request(url, method='HEAD', dont_filter=True, callback=self.info)

    
    def info(self,response):
        item = response.meta['item']       
        item["status"]=int(response.status)
        print ("hola papi")
        return item["status"]
