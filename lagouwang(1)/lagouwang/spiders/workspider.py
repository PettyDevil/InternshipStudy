# -*- coding: utf-8 -*-
import scrapy
import requests
import time
import json
from ..items import LagouwangItem

class WorkspiderSpider(scrapy.Spider):
    name = 'workspider'
    allowed_domains = ['lagou.com']
    url="https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    headers={"Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    first="true"
    pn=1
    kd="python"
    cookies_msg=""

    def start_requests(self):
        #主网页的地址
        main_url="https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
        #通过主网页的请求获取网站给我们创造的cookie的jar对象
        cookies=requests.get(main_url,headers=self.headers).cookies
        #通过requests库的方法将cookie的jar对象转变为字典类型
        self.cookies_msg=requests.utils.dict_from_cookiejar(cookies)
        time.sleep(0.5)
        yield scrapy.FormRequest(url=self.url,formdata={"first":self.first,"pn":str(self.pn),"kd":self.kd},headers=self.headers,cookies=self.cookies_msg,callback=self.parse)



    #提交表单数据，如果速度太快，就会被网站认为是爬虫（解决方式：增加间隔时间）
    def parse(self, response):
        data=json.loads(response.body)
        #先拿到整页数据的条数
        size=data["content"]["positionResult"]["resultSize"]
        work_msg=data["content"]["positionResult"]["result"]
        for i in range(size):
            lagou=LagouwangItem()
            lagou['workName']=work_msg[i]['positionName']
            lagou['company']=work_msg[i]['companyFullName']
            lagou['maxSalary']=work_msg[i]['salary'].split("-")[1]
            lagou['minSalary']=work_msg[i]['salary'].split("-")[0]
            lagou['experience']=work_msg[i]['workYear']
            lagou['educational']=work_msg[i]['education']
            yield lagou
            pass

        if self.pn<20:
            print(self.pn)
            self.pn+=1
            time.sleep(3)#用多个爬虫，不同的ip地址去爬不同页的数据然后整合
            yield scrapy.FormRequest(url=self.url, formdata={"first": self.first, "pn": str(self.pn), "kd": self.kd},
                                     headers=self.headers, cookies=self.cookies_msg, callback=self.parse)
