# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HooklinesinkerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    site = scrapy.Field()
    date = scrapy.Field()
    date_exp = scrapy.Field()
    type = scrapy.Field()
    rating = scrapy.Field()
    gps = scrapy.Field()
    report = scrapy.Field()
    access = scrapy.Field()
