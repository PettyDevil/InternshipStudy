# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    workName=scrapy.Field()#岗位名称
    company=scrapy.Field()#公司名称
    maxSalary=scrapy.Field()#最高工资
    minSalary=scrapy.Field()#最低工资
    experience=scrapy.Field()#经验
    educational=scrapy.Field()#学历
    pass
