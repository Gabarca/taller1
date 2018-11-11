# -*- coding: utf-8 -*-
import scrapy


import scrapy
# import pandas as pd
import functools
from parte2.items import Parte2Item
from scrapy.http import Request
from scrapy.http.request import Request




#InfSpider es la araña encargada de recorrer  http://www.inf.ucv.cl
class InfSpider(scrapy.Spider):
    name = 'InfSpider'
    allowed_domains = ['inf.ucv.cl']
    start_urls = ['http://www.inf.ucv.cl']
    out_links = set()
    def start_requests(self):
        yield scrapy.Request('http://www.inf.ucv.cl', self.parse)

    def parse(self, response):
        links = scrapy.linkextractors.LinkExtractor().extract_links(response)
        for i in links:
            if i.url.find(self.allowed_domains[0])!=-1:
                yield Request(i.url, method='HEAD', dont_filter=True,callback=self.parse_2)
        print (self.out_links) # no funciona

    def parse_2(self, response):
        if "text/html" in str(response.headers['Content-type']):
            # print(response.url)
            self.out_links.add(response.url)
            yield Parte2Item(
                linky=response.url,
                status=response.status,
                content_type=response.headers['Content-type'],
                content_length=response.headers['Content-length']
            )
    
    def prueba(self,response):
        print("funciono")

"""   
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
        yield Request(url, method='HEAD', dont_filter=True,callback=self.info)

    
    def info(self,response):
        item = response.meta['item']       
        item["status"]=int(response.status)
        print ("hola papi")
        return item["status"]
"""