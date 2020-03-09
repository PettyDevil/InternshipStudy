import xlwt
import pymysql
import requests
from bs4 import BeautifulSoup
import os

url = "http://www.tianqihoubao.com/lishi/wuhan/month/"

lis = []
wb = xlwt.Workbook()


def Write_excel(tag_trs):
    tag_trs = tag_trs
    i = 0
    sheet = wb.add_sheet("天气%s" % month)
    for tag_tr in tag_trs:
        j = 0
        date = tag_tr.td.a
        if date != None:
            print(date.string.replace(" ", ""), "!!!!")
            date = date.string.replace(" ", "")
            tds = tag_tr.find_all('td')
            sheet.write(i, j, date)
            for td in tds:
                j += 1
                data = td.string
                data = str(data).replace(" ", "")
                print(data)
                sheet.write(i, j, data)
                pass
            i += 1
            print(type(tds))
        else:
            print("date为None！！！")
    wb.save('天气/tianqi.xls')


def Write_mysql(tag_trs):
    conn = pymysql.connect(host="localhost", port=3306, database="mysql", user="root", password="998506",
                           charset="utf8")
    cursor = conn.cursor()
    sql = "show tables"
    cursor.execute(sql)  # 执行sql语句
    for i in cursor.fetchall():
        if i[0] == "tianqi":
            break
    else:
        sql = "create table tianqi(sid int primary key AUTO_INCREMENT,date varchar(20),wea varchar(20),tem varchar (20),wind varchar(20))CHARACTER SET utf8;"
        cursor.execute(sql)
        cursor.close()
    # 往表中插入
    try:
        with conn.cursor() as cursor1:
            # mysql的时间转换函数 str_to_date(%s,'%Y-%m-%d %h:%M:%s')
            for tag_tr in tag_trs:
                list = []
                date0 = tag_tr.td.a
                if date0 != None:
                    date0 = date0.string.replace(" ", "").replace("\n", "").replace("\r", "")
                    print(date0 + "!!!!")
                    tds = tag_tr.find_all('td')
                    list.append(str(date0))
                    for td in tds:
                        data = td.string
                        if data == None:
                            print("data无数据！")
                            continue
                        else:
                            data = td.string
                            data = str(data).replace(" ", "").replace("\n", "").replace("\r", "")
                            print(data)
                            list.append(data)
                        pass
                    print(list)
                    sql = "insert into tianqi (date,wea,tem,wind) values (%s,%s,%s,%s)"
                    cursor1.execute(sql, [list[0], list[1], list[2], list[3]])
                    conn.commit()  # 事务的提交
                else:
                    print("date为None！！！")
    except Exception as e:
        print("出现错误%s" % e)
        conn.rollback()  # 事务的回滚
    finally:
        cursor1.close()
        conn.close()
        pass
    pass


def Write_txt(tag_trs):
    file_tianqi = open("%s%s.txt" % (file_path, month), "w", 1, encoding="utf-8")
    file_tianqi.write("日期         天气状况         气温         风力风向\n")
    for tag_tr in tag_trs:
        list = []
        date0 = tag_tr.td.a
        if date0 != None:
            date0 = date0.string.replace(" ", "").replace("\n", "").replace("\r", "")
            print(date0 + "!!!!")
            tds = tag_tr.find_all('td')
            list.append(str(date0))
            for td in tds:
                data = td.string
                if data == None:
                    print("data无数据！")
                    continue
                else:
                    data = td.string
                    data = str(data).replace(" ", "").replace("\n", "").replace("\r", "")
                    print(data)
                    list.append(data)
                pass
            print(list)
            all = list[0] + "  " + list[1] + "  " + list[2] + "  " + list[3] + "\n"
            file_tianqi.write(all)
        else:
            print("数据为None！！！")
    file_tianqi.close()
    pass


def Get_tianqi_mulu_context(url, month, header):
    requests_02 = requests.get(url=url, data=header)
    if requests_02.status_code == 200:
        requests_02.encoding = "gb2312"
        context_data = requests_02.text
        soup = BeautifulSoup(context_data, "html.parser")
        # tianqi_context = soup.find("table",attrs={"class":"b"}).get_text()
        tianqi_context = soup.find("table", attrs={"class": "b"})
        tag_trs = tianqi_context.find_all("tr")
        print("天气数目为：", len(tag_trs))
        Write_excel(tag_trs)  # 写入excel
        Write_mysql(tag_trs)  # 写入mysql
        Write_txt(tag_trs)  # 写入txt
        print('------------操作成功！--------------')
    else:
        print("网络访问失败：请求码：%d - 请检查网址" % requests_02.status_code);
        pass


def Get_tianqi_html(url, month, header):
    requests_01 = requests.get(url=url, data=header)
    print("网络请求的返回码：", requests_01.status_code)
    if requests_01.status_code == 200:
        print("当前网页的编码格式:", requests_01.encoding)
        requests_01.encoding = "gb2312"
        data = requests_01.text
        file_tianqi = open("%s%s.html" % (file_path, month), "w", 1)
        file_tianqi.write(data)
        file_tianqi.close()
        print("已经保存到本地文件中。")

        pass
    else:
        print("网络访问失败：请求码：%d - 请检查网址" % requests_01.status_code);
        pass

    pass


if __name__ == "__main__":
    print("==========进入程序=============")
    print("欢迎使用Python爬虫V.10版本")
    print("目前本软件只支持：http://www.tianqihoubao.com/weather/top/wuhan.html网站天气")
    months = ['201912', '202001', '202002']
    """
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36
    """
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"};
    file_path = "C:\/Users\/92381\/Desktop\/InternshipStudy\/天气\/"
    # print(file_path)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        pass
    for month in months:
        urls = url + str(month) + '.html'
        print("天气地址为：", urls)
        #     Get_tianqi_html(urls,str(month),header)
        Get_tianqi_mulu_context(urls, str(month), header)
    pass
