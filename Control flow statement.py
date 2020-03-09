data=list(range(10))  # 决定生成的数值的上限，下线为默认的0
print(data)
data=list(range(1,10)) # 以第一个数字作为下限，以第二个数字作为上限
print(data)
data=list(range(1,10,3))
print(data)
# range当生成的序列很长时，内存消耗会很大
# python2.0 xrange(0,10)每次生成的值会及时销毁，3的range不会

for i in range(0,10):
    print(i)
    pass


for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}\t".format(i,j,i*j),end="")
        pass
    print("")
    pass


for i in range(5):
    print(i)
    if i==4:
        break
else:  # 当循环执行完毕时会自动运行，除非在for循环中使用break关键字
    print("addadsdf")
# try-catch-finally


# 序列类型
# 元组tuple，能够保存多个数据，整体不可变，但不是绝对的不可变
msg=10,"aaa","qwer",323,list(range(3))
print(msg)
# 通过下标取值，下标从0开始
print(msg[1]) # 元组下标不可越界
print(type(msg))
# msg[0]=20 不可更改
msg[len(msg)-1][1]=3
print(msg)
# msg[len(msg)-1]=list("qweee")
# 通过位置取值
# a,b,c,d,e=msg
# print(c)
a,b,*c=msg
print(c)
a,b,*_=msg # 只取元组的第一个和第二个，其他都不要



# 列表list 可变
data=["sdsd","asd",53,121,None]
print(data[0])
data[0]='wqe'
print(data)
# 分片
print(data[:3]) # 也就是[0:3]
print(data[:len(data):2])
# 列表的赋值
ta=data  # 赋地址
ta=data[:]
ta[2]=35
print(data)
data.append(list("9873")) # 追加一个值
print(data)
data.extend("7987")  # 拼接列表
print(data)
data.pop()
print(data)
# 字典{键:值,}   键必须是不可变数据类数字、字符串、元组、小数      可变数据类型：列表、字典
h=[i for i in range(10)]
dic={"a":"b",1:"c","d":56,"e":h,"f":list(range(5))}
# 通过键来取值，如果键不存在
print(dic["e"])
# 赋值
dic["a"]="qwer"
print(dic)
# 增加新的值    用新的键来对应新的值
dic["g"]="hhhhh"
print(dic)


