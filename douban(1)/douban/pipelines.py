# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

#主程序拿到一条数据就往处理程序传值
class DoubanPipeline(object):
    #将值存入mysql数据库
    def __init__(self):
        self.conn=pymysql.connect(host="localhost",port=3306,database="test",user="root",password="123456",charset="utf8")
        self.cursor=self.conn.cursor()
        sql="create table movie(mid int primary key AUTO_INCREMENT,rank varchar(20),name varchar(20),score varchar(20),commentNum varchar(20),firstComment varchar(20))CHARACTER SET UTF8"
        self.cursor.execute(sql)
    def process_item(self, item, spider):
        moiveData=[item['rank'][0],item['name'][0],item['score'][0],item['commentNum'][0],item['firstComment'][0]]
        sql="insert into "
        return item
