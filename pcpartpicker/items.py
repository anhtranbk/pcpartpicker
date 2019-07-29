# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    # define the fields for your item here like:
    category = scrapy.Field()
    name = scrapy.Field()
    merchant = scrapy.Field()
    base_price = scrapy.Field()
    total_price = scrapy.Field()
    in_stock = scrapy.Field()
    url = scrapy.Field()

    def __repr__(self):
        return ''
