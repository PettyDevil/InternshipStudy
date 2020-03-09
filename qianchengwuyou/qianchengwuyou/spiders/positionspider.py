# -*- coding: utf-8 -*-
import scrapy
from ..items import QianchengwuyouItem

def panduan(value):
    if len(value)==0:
        value=["！此处暂无信息！"]
    else:
        value[0]=value[0].replace(" ","")
    return value

class PositionspiderSpider(scrapy.Spider):
    name = 'positionspider'
    allowed_domains = ['51job.com']
    # start_urls = ['http://51job.com/']
    url="https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}


    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        work_data=response.xpath("//div[@class='el']")
        # print(work_data)
        for i in work_data:
            # print(i,"????????????????????????????/")
            work=QianchengwuyouItem()
            work['positioname']=i.xpath("p[@class='t1 ']/span/a/text()").extract()
            work['positioname']=panduan(work['positioname'])
            # print(len(work['positioname']),"!!@#@!#@!#!$#@%^^%$$#$%$^%$!!!!!!!!!!!!!!!!!!!!!!!!")
            work['companyname']=i.xpath("span[@class='t2']/a/text()").extract()
            work['companyname']=panduan(work['companyname'])
            work['workplace']=i.xpath("span[@class='t3']/text()").extract()
            work['workplace']=panduan(work['workplace'])
            work['salary']=i.xpath("span[@class='t4']/text()").extract()
            work['salary']=panduan(work['salary'])
            work['publishtime']=i.xpath("span[@class='t5']/text()").extract()
            work['publishtime'] = panduan(work['publishtime'])
            yield work

        pass

        nextpage = response.xpath("//li[@class='bk'][2]/a/@href")
        print(nextpage,"124234546576655443233234565765434233435467")
        if nextpage:  # 不为空时证明有下一页的链接
            url = response.urljoin(nextpage[0].extract())  # 将获取到的字符串转换为url对象
            print(url,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            yield scrapy.Request(url=url, callback=self.parse,headers=self.headers)