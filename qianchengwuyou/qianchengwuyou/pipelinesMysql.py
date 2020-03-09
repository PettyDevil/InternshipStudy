# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class QianchengwuyouPipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(host="localhost",port=3306,database="mysql",user="root",password="998506",charset="utf8")
        self.cursor=self.conn.cursor()
        sql = "show tables"
        self.cursor.execute(sql)
        for i in self.cursor.fetchall():
            if i[0] == "qiancheng_position":
                break
        else:
            sql="create table qiancheng_position(mid int primary key AUTO_INCREMENT,positioname varchar(60),companyname varchar(60),workplace varchar(60),salary varchar(60),publishtime varchar(60)) CHARACTER SET UTF8"
            self.cursor.execute(sql)
            self.cursor.close()
    def process_item(self,item, spider):
        positionData=[item['positioname'][0],item['companyname'][0],item['workplace'][0],item['salary'][0],item['publishtime'][0]]
        # print("-"*100)
        # print(item['name'][0])
        # print("-" * 100)
        with self.conn.cursor() as cursor1:
            sql = "insert into qiancheng_position(positioname,companyname,workplace,salary,publishtime)values (%s,%s,%s,%s,%s)"
            cursor1.execute(sql, positionData)
            self.conn.commit()
        print("mysql操作成功！")
        return item
