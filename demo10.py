import requests
from bs4 import BeautifulSoup

url="http://58921.com/alltime/2019"
response=requests.get(url)
#gbk  gb2312  utf-8  中文编码
data=response.content.decode("utf-8")
html=BeautifulSoup(data,"html.parser")#速度很慢，容错率不错   lxml
allMsg=html.find_all("tr")

for i in allMsg[1:]:#表头信息去掉
    tdList=list(i.children)#拿到单个tr的所有子节点td
    yearOrder=tdList[0].text
    lishiOrder=tdList[1].text
    movieName=tdList[2].text
    yearStr=tdList[3].text
