# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanItem

class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'  # 爬虫主程序名称
    allowed_domains = ['douban.com']  # 主域名（可以删掉）
    start_urls = ['https://movie.douban.com/top250'] # 爬取的地址，这是个列表，可以有多个地址
    # 请求头
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}


    # 初始化请求对象
    def start_requests(self):
        # 对请求对象设置参数
        # 装饰器  自动创建一个序列（并把后面得到的数据放入序列）
        yield scrapy.Request(url=self.start_urls[0],callback=self.parse,headers=self.headers)

    # parse（转化），将得到的整体数据（requests.get(url).content）转化为想要得到的数据
    def parse(self, response):
        # 解析整体数据
        # name=response.xpath("//div[@class='item']/div[@class='info']/div[@class='hd']/a/span[1]/text()").extract()
        # print(name)
        # print(response.body)
        movie_data=response.xpath("//div[@class='item']")
        for i in movie_data:
            movie=DoubanItem()
            movie['rank']=i.xpath("div[@class='pic']/em/text()").extract()
            movie['name']=i.xpath("div[@class='info']/div[@class='hd']/a/span[1]/text()").extract()
            movie['socre']=i.xpath("div[@class='info']/div[@class='bd']/div[@class='star']/span[2]/text()").extract()
            movie['commentNum']=i.xpath("div[@class='info']/div[@class='bd']/div[@class='star']/span[4]/text()").extract()
            movie['firstComment']=i.xpath("div[@class='info']/div[@class='bd']/p[@class='quote']/span/text()").extract()
            movie['picPath']=i.xpath("div[@class='pic']/a/img/@src")
            yield movie  # 创造一个序列（列表、元组、字典）
        pass

        # 获取下一页的链接
        print("!@!@$#$@#$!@$!@!@$!#$#$@#%#$^%$$^&Y$&%&^%^%*^&*^")
        nextpage = response.xpath("//span[@class='next']/a/@href")
        print(nextpage,"124234546576655443233234565765434233435467")
        if nextpage:  # 不为空时证明有下一页的链接
            url = response.urljoin(nextpage[0].extract())  # 将获取到的字符串转换为url对象
            print(url,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            yield scrapy.Request(url=url, callback=self.parse,headers=self.headers)
