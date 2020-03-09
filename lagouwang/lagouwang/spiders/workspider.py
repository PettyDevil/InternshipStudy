# -*- coding: utf-8 -*-
import scrapy
import requests
import time

class WorkspiderSpider(scrapy.Spider):
    name = 'workspider'
    allowed_domains = ['lagou.com']
    url="https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
             "Referer":"https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
             "Accept": "application/json,text/javascript,*/*;q=0.01"}
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

    def parse(self, response):
        print(response.body)
        pass
#https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false