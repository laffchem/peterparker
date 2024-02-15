# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from datetime import datetime

class UrlStatuses(scrapy.Item):
    timestamp = scrapy.Field()
    url = scrapy.Field()
    status = scrapy.Field()
