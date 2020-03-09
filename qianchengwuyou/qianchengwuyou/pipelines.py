# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import xlwt

wb = xlwt.Workbook()
sheet = wb.add_sheet("前程无忧岗位信息")
msg = ["职位名", "公司名", "工作地点", "薪资", "发布时间"]
for i in range(len(msg)):
    sheet.write(0, i, msg[i])
class QianchengwuyouPipeline(object):
    def __init__(self):
        self.k=1
    def process_item(self,item, spider):
        positionData=[item['positioname'][0],item['companyname'][0],item['workplace'][0],item['salary'][0],item['publishtime'][0]]
        j=0
        for i in range(len(positionData)):
            sheet.write(self.k, j, positionData[i])
            j+=1
        self.k+=1
        wb.save("前程无忧岗位信息.xls")
        print("excel操作成功！")
        return item
