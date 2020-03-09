# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

#主程序拿到一条数据就往处理程序传值
class DoubanPipeline(object):
    #将值存入excel表格

    def process_item(self, item, spider):

        return item
