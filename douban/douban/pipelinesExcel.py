# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import xlwt

wb = xlwt.Workbook()
sheet = wb.add_sheet("豆瓣电影")
msg = ["rank", "name", "socre", "commentNum", "firstComment"]
for i in range(len(msg)):
    sheet.write(0, i, msg[i])


# 主程序拿到一条数据就往处理程序传值
class DoubanPipeline(object):
    def __init__(self):
        self.k=1
    def process_item(self,item, spider):
        moiveData=[item['rank'][0],item['name'][0],item['socre'][0],item['commentNum'][0],item['firstComment'][0]]
        j=0
        for i in range(len(moiveData)):
            sheet.write(self.k, j, moiveData[i])
            j+=1
        self.k+=1
        wb.save("douban/豆瓣电影.xls")
        print("excel操作成功！")
        return item
