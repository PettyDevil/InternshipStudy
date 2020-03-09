# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QianchengwuyouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positioname=scrapy.Field()  # 职位名
    companyname=scrapy.Field()  # 公司名
    workplace=scrapy.Field()    # 工作地点
    salary=scrapy.Field()       # 薪资
    publishtime=scrapy.Field()  # 发布时间
    pass
