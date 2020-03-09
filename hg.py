# 数据类型：数字（整数、小数、复数）字符串 列表 元组 字典
# 流程结构：顺序、选择if-elif-else、循环while for-in
# 函数与oop：继承和封装
# 对txt操作：os
# 对excel操作：xlwt、xlrd、xlutils
# 对mysql操作：pymysql

import requests
import os
import xlwt
from bs4 import BeautifulSoup
import pymysql
# 发送请求得到我想要的数据
url = "http://www.tianqihoubao.com/lishi/wuhan/month/202001.html"
response = requests.get(url)
# print(response.headers)
# print(response.encoding)
# print(response.cookies)
# print(response.content)
# 获取网站的解码方式
data=response.content.decode("gb2312")
# print(response.encoding)
# 解析获取的内容：正则（json第一）、xpath（效率第二）、html（xlml）效率最低
html=BeautifulSoup(data,'html.parser')
# print(html)
# 找到对应的节点模块
weatherData=html.find_all("tr")
allMsg=[]   # 整体数据列表
fileName=""
for i in weatherData[1:]:
    # 通过text属性拿到所有的文本信息
    oneData=[]
    ls=i.text.split()
    fileName=ls[0][:8]
    oneData.append(ls[0])# 添加日期
    oneData.append(ls[1]+ls[2]) # 天气状况
    oneData.append("-".join(ls[3:6:2]))
    oneData.append("/".join(ls[6:8]))
    allMsg.append(oneData)
print(allMsg)
print(fileName)
# txt
try:
    with open("output/"+fileName+"txt","w",encoding="utf-8") as fp:
        fp.writelines("时间\t天气状况\t气温\t风力风向\n")
        for i in allMsg:
            fp.writelines("{}\t{}\t{}\t{}\n".format(i[0],i[1],i[2],i[3]))
            pass
except Exception as e:
    print("发生错误%s"%e)


# excel
wb=xlwt.Workbook()
sheet=wb.add_sheet("{}的数据".format(fileName))
style=xlwt.XFStyle()
font=xlwt.Font()
font.bold=True
style.font=font
msg=["时间","天气状况","气温","风力风向"]
for i in range(len(msg)):
    sheet.write(0,i,msg[i],style)
for i in range(len(allMsg)):
    for j in range(len(allMsg[i])):
        sheet.write(i+1,j,allMsg[i][j])
wb.save("output/"+fileName+".xls")



# mysql
conn=pymysql.connect(host="localhost",port=3306,database="test",user="root",password="998506",charset="utf8")
cursor=conn.cursor()
