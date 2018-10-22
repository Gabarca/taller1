# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Parte1Item(scrapy.Item):
    autor=scrapy.Field()
    cita=scrapy.Field()
    etiqueta=scrapy.Field()
    pass
