# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

# 主程序拿到一条数据就往处理程序传值
class DoubanPipeline(object):
    # 将值存入mysql数据库
    def __init__(self):
        self.conn=pymysql.connect(host="localhost",port=3306,database="mysql",user="root",password="998506",charset="utf8")
        self.cursor=self.conn.cursor()
        sql = "show tables"
        self.cursor.execute(sql)  # 执行sql语句
        for i in self.cursor.fetchall():
            if i[0] == "douban_movie":
                break
        else:
            sql="create table douban_movie(mid int primary key AUTO_INCREMENT,mrank varchar(60),name1 varchar(60),socre varchar(60),commentNum varchar(60),firstComment varchar(60)) CHARACTER SET UTF8"
            self.cursor.execute(sql)
            self.cursor.close()
    def process_item(self,item, spider):   # 只要接受一个对象，就会执行一次
        moiveData=[item['rank'][0],item['name'][0],item['socre'][0],item['commentNum'][0],item['firstComment'][0]]
        # print("-"*100)
        # print(item['name'][0])
        # print("-" * 100)
        with self.conn.cursor() as cursor1:
            sql = "insert into douban_movie(mrank,name1,socre,commentNum,firstComment)values (%s,%s,%s,%s,%s)"
            cursor1.execute(sql, moiveData)
            self.conn.commit()
        print("mysql操作成功！")
        return item
