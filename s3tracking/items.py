# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class S3TrackingItem(scrapy.Item):

    name = scrapy.Field()
    link = scrapy.Field()
    role = scrapy.Field()
    firm = scrapy.Field()
    location = scrapy.Field()
    details = scrapy.Field()
    ident = scrapy.Field()
    pass
