# -*- coding: utf-8 -*-
import scrapy
from taller1.items import Parte1Item

#Dipsy es la araña encargada de recorrer http://quotes.toscrape.com/page/1/
class DipsySpider(scrapy.Spider):
    name = 'dipsy'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield Parte1Item(
                autor= quote.css('small.author::text').extract_first(),
                cita= quote.css('span.text::text').extract_first(),
                etiqueta= quote.css('div.tags a.tag::text').extract()
            )
        