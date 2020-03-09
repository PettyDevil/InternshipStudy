#数据类型：数字（整数、小数、复数） 字符串 列表  元组  字典
#流程结构：顺序、选择if-elif-else  、循环while  for-in
#函数与oop ： 继承和封装
#对txt操作：os
#对excel操作：xlwt、xlrd、xlutils
#对mysql操作：pymysql

#两个小时之内交代码：获取2019-12月、2020年1月、2020年2月份
#txt文档、excel表格、mysql表数据
import requests
import xlwt
import os
import pymysql
from bs4 import BeautifulSoup
#发送请求得到我想要的数据

allMsg=[]#整体数据列表
fileName=""
def getData(url):
    response=requests.get(url)
    #获取网站的解码方式
    data=response.content.decode("gb2312")
    #print(response.encoding)
    #解析获取的内容：正则（json 第一）、xpath（第二）、html（xlml）效率最低
    html=BeautifulSoup(data,'html.parser')
    #找到对应的节点模块
    global fileName
    weatherData=html.find_all("tr")
    for i in weatherData[1:]:
        #通过text属性拿到所有的文本信息
        oneData=[]
        ls=i.text.split()
        fileName=ls[0][:8]
        oneData.append(ls[0])#添加日期
        oneData.append(ls[1]+ls[2])#天气状况
        oneData.append("-".join(ls[3:6:2]))
        oneData.append("/".join(ls[6:8]))
        allMsg.append(oneData)

url="http://www.tianqihoubao.com/lishi/wuhan/month/201912.html"
url1="http://www.tianqihoubao.com/lishi/wuhan/month/202001.html"
url2="http://www.tianqihoubao.com/lishi/wuhan/month/202002.html"
getData(url)
getData(url1)
getData(url2)


#txt
try:
    with open("output/"+fileName+".txt",'w',encoding="utf-8") as fp:
        fp.writelines("时间\t\t\t天气状况\t气温\t风力风向\n")
        for i in allMsg:
            fp.writelines("{}\t{}\t{}\t{}\n".format(i[0],i[1],i[2],i[3]))
            pass
except Exception as e:
    print("发生错误%s" %e)


#excel
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
    for j in  range(len(allMsg[i])):
        sheet.write(i+1,j,allMsg[i][j])
wb.save("output/"+fileName+".xls")



#mysql
conn=pymysql.connect(host="localhost",port=3306,database="test",user="root",password="123456",charset="utf8")
cursor=conn.cursor()
sql="show tables"
cursor.execute(sql)#执行sql语句
for i in cursor.fetchall():
    if i[0]=="weather":
        break
else:
    sql="create table weather(wid int primary key AUTO_INCREMENT,calander varchar(20),tianqi varchar(20),qiwen varchar(20),fengli varchar(20))CHARACTER SET utf8;"
    cursor.execute(sql)
    cursor.close()

try:
    with conn.cursor() as cursor1:
        sql="insert into weather(calander,tianqi,qiwen,fengli) values (%s,%s,%s,%s)"
        for i in allMsg:
            cursor1.execute(sql,i)
        conn.commit()
except Exception as e:
    print("插入出现错误%s" %e)
    conn.rollback()
finally:
    conn.close()

#csv 一次性将数据装到csv文件