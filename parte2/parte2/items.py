# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Parte2Item(scrapy.Item):
    linky=scrapy.Field()
    status=scrapy.Field()
    content_type=scrapy.Field()
    content_length=scrapy.Field()
    pass
