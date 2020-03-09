# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#声明需要爬取的数据
class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank=scrapy.Field()#排名
    name=scrapy.Field()#电影名称
    socre=scrapy.Field()#评分
    commentNum=scrapy.Field()#评论数
    firstComment=scrapy.Field()#第一条评论
    pass
