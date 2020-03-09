import pymysql
# jdbc 加载驱动 链接 操作preparedstatement 关闭
conn=pymysql.connect(host="localhost",port=3306,database="mysql",user="root",password="998506",charset="utf8")
# 创建表之前先要查询要创建的表存在不存在
# 通过链接游标对象
cursor=conn.cursor()
sql="show tables"
cursor.execute(sql) # 执行sql语句
print(type(cursor.fetchall()))