# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanItem


class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider' #爬虫主程序名称
    allowed_domains = ['douban.com']  #主域名
    start_urls = ['https://movie.douban.com/top250'] #爬取的地址，地址可以有多个
    #请求头
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    #初始化请求对象
    def start_requests(self):
        #对请求对象设置参数
        #装饰器  自动创建一个序列（并把后面得到数据放入序列）
        yield scrapy.Request(url=self.start_urls[0],callback=self.parse,headers=self.headers)

    #转化：将得到的整体数据（requests.get(url)）转化为想要得到的数据
    def parse(self, response):
        #解析整体数据
        movie_data=response.xpath("//div[@class='item']")
        for i in movie_data:#将单页的数据爬取完毕
            movie=DoubanItem()
            movie['rank']=i.xpath("div[@class='pic']/em/text()").extract()
            movie['name']=i.xpath("div[@class='info']/div[@class='hd']/a/span[1]/text()").extract()
            movie['socre']=i.xpath("div[@class='info']/div[@class='bd']/div[@class='star']/span[2]/text()").extract()
            movie['commentNum']=i.xpath("div[@class='info']/div[@class='bd']/div[@class='star']/span[4]/text()").extract()
            movie['firstComment']=i.xpath("div[@class='info']/div[@class='bd']/p[@class='quote']/span/text()").extract()
            yield movie
            pass

        #获取下一页的链接
        nextpage=response.xpath("span[@class='next']/a/@href")
        if nextpage:#不为空时证明有下一页的链接
            url=response.urljoin(nextpage[0].extract())#将获取到的字符串转换为url对象
            yield scrapy.Request(url,self.parse)

