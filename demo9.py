import pymysql

#jdbc 加载驱动  连接  操作preparedstatement  关闭
conn=pymysql.connect(host="localhost",port=3306,database="test",user="root",password="998506",charset="utf8")
#创建表之前先查询要创建的表存不存在
#通过连接游标对象
cursor=conn.cursor()
sql="show tables"
cursor.execute(sql)#执行sql语句
for i in cursor.fetchall():
    if i[0]=="student":
        break
else:
    sql="create table student(sid int primary key AUTO_INCREMENT,sname varchar(20),gender varchar(3),age int,address varchar(20))CHARACTER SET utf8;"
    cursor.execute(sql)
    cursor.close()

#往表中插入
try:
    with conn.cursor() as cursor1:
        sql="insert into student (sname,gender,age,address) values (%s,%s,%s,%s)"
        cursor1.execute(sql,["哈哈","男",18,"湖北武汉"])
        #事务 --》DML操作（增加、修改、删除）    事务的提交   事务的回滚
        conn.commit()#事务的提交
        #mysql的时间转换函数 str_to_date(%s,'%Y-%m-%d %h:%M:%s')
except Exception as e:
    print("出现错误%s" %e)
    conn.rollback()#事务的回滚
finally:
    cursor1.close()
    conn.close()
