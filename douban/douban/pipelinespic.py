# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import urllib
# 主程序拿到一条数据就往处理程序传值
class DoubanPipeline(object):
    # 将图片对应的图片下载下来保存

    def process_item(self,item, spider):   # 只要接受一个对象，就会执行一次
        urllib.urlretrieve(['picPath'][0],)
        return item