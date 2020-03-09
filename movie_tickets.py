import xlwt
import pymysql
import requests
from bs4 import BeautifulSoup
import os


file_path = "C:\/Users\/92381\/Desktop\/InternshipStudy\/电影排行\/"
if not os.path.exists(file_path):
    os.makedirs(file_path)
    pass
url = "http://58921.com/alltime/2019"
response = requests.get(url)
print(response.encoding)
data=response.content.decode("utf-8")
html=BeautifulSoup(data,'html.parser')
# print(html)
# movie = open("%s%s.html" % (file_path, 'movie_tickets'), "w",encoding='ISO-8859-1')
# movie.write(data)
# movie.close()
# print("已经保存到本地文件中。")
ticketsData=html.find_all("td")
# print(ticketsData)
allMsg=[]   # 整体数据列表
k=0
oneData=[]
for i in ticketsData[0:]:
    # print(i.string)
    ls=i.string
    if ls != None:
        # print(ls,'!!!!!!')
        oneData.append(ls)
        k+=1
        if k%8 == 0:
            allMsg.append(oneData)
            oneData = []
        else:
            continue
        pass
    else:
        ls=i.img["src"]
        oneData.append(ls)
        k+=1
        # print(ls)
print(allMsg)


# excel
wb=xlwt.Workbook()
sheet=wb.add_sheet("2019年内地电影票房总排行榜")
style=xlwt.XFStyle()
font=xlwt.Font()
font.bold=True
style.font=font
msg=["年度排名","历史排名","电影名称","总票房","总人次","总场次","上映年份","操作"]
for i in range(len(msg)):
    sheet.write(0,i,msg[i],style)
for i in range(len(allMsg)):
    for j in range(len(allMsg[i])):
        sheet.write(i+1,j,allMsg[i][j])
wb.save("电影排行/2019年内地电影票房总排行榜.xls")
print("excel操作成功！")


# mysql
conn=pymysql.connect(host="localhost",port=3306,database="mysql",user="root",password="998506",charset="UTF8MB4")
cursor=conn.cursor()
sql="show tables"
cursor.execute(sql)#执行sql语句
for i in cursor.fetchall():
    if i[0]=="movie_tickets":
        break
else:
    sql="create table movie_tickets(wid int primary key AUTO_INCREMENT,yearank varchar(20),hisrank varchar(20),moviename varchar(20),alltick varchar(200),allper varchar(20),allsess varchar(20),playear varchar (20),options varchar (20))CHARACTER SET utf8;"
    cursor.execute(sql)
    cursor.close()
try:
    with conn.cursor() as cursor1:
        sql = "insert into movie_tickets(yearank,hisrank,moviename,alltick,allper,allsess,playear,options) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        for i in allMsg:
            cursor1.execute(sql, i)
        conn.commit()
except Exception as e:
    print("插入出现错误%s" % e)
    conn.rollback()
finally:
    conn.close()
print("mysql操作成功！")