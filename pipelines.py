# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class DoubanPipeline(object):
    conn = pymysql.connect(host="localhost", port=3306, database="test", user="root", password="123456", charset="utf8")
    cursor = conn.cursor()
    sql = "show tables"
    cursor.execute(sql)
    for i in cursor.fetchall():
        if i[0] == "movie1":
            break
    else:
        sql = "create table movie1(mid int primary key AUTO_INCREMENT,rank varchar(40),name1 varchar(100),score varchar(100),commentNum varchar(100),firstComment varchar(100))CHARACTER SET UTF8"
        cursor.execute(sql)
        cursor.close()
        conn.close()
    def process_item(self, item, spider):
        print("-"*100)
        print(item['name'][0])
        print(item['rank'][0])
        print(item['score'][0])
        print(item['commentNum'][0])
        print(item['firstComment'][0])
        print("-" * 100)
        moiveData = [item['rank'][0], item['name'][0], item['score'][0], item['commentNum'][0], item['firstComment'][0]]
        conn = pymysql.connect(host="localhost", port=3306, database="test", user="root", password="123456",charset="utf8")
        try:
            with conn.cursor() as cursor1:
                sql = "insert into movie1(rank,name1,score,commentNum,firstComment) values (%s,%s,%s,%s,%s)"
                # cursor1.execute(sql, item["rank"][0], item["name"][0], item["score"][0], item["commentNum"][0], item["firstComment"][0])
                cursor1.execute(sql, [moiveData[0], moiveData[1], moiveData[2], moiveData[3],moiveData[4]])
                # 事务 --》DML操作（增加、修改、删除）    事务的提交   事务的回滚
                conn.commit()  # 事务的提交
                # mysql的时间转换函数 str_to_date(%s,'%Y-%m-%d %h:%M:%s')
        except Exception as e:
            print("出现错误%s" % e)
            conn.rollback()  # 事务的回滚
        finally:
            cursor1.close()
        conn.close()
        return item
