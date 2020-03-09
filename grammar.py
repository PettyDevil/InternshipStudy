import keyword
# int aaa=10 静态数据类型语言 基于JIT即时编译
# var aaa=10 动态数据类型语言 基于GIL
aaa=10.0# pypy进行加速 JIT
bbb=111
ccc=-3
print(type(aaa))
print(keyword.kwlist)
msg='''dadaddada
        dadsdssd
        qdqwd
        dwqdd
    '''
'''
多行注释
'''
swd='sdasdasd'
print(swd[0:6])  # 切片[起始位置：截至位置，不包含（默认是结尾下标+1）：步长]
print(swd[3::2]) # 步长

# 字符串的模板化     格式化%s 将输出的内容转化为字符串 %d、%.2f
ms='我叫{0:s}，今年{1:d}岁'   # 或者%s、%d
# print(ms.format("菜鸡","hh"))
# ms='我叫菜鸡'
print(ms.format("渣渣",22))
# strip剪切   spilt分割

hh='aaa  bb  cc  ddd'
c=hh.split("  ")
print(c,'yuguy')

flag=False # 做判断 bool False->0 True->1
# flag=None # 空类型（有且只有一个）


print(flag+ccc)
print(bool(ccc))

# 字符串的拼接 + 和数字拼接之前一般要先把数字转化为字符串str
print(hh+str(ccc))

print(False and True) # 短路运算
print(True or False)

if(1>2):  # 或者if 1>2
    print("2222")
    # if():
elif 2>1:
    print("11111")
else:
    print("33333")
    pass

# while True:

# 死循环   ：遵从三大要素：循环必须要有循环初量、循环的判断表达式、循环增量
i=0
while i<6:
    i += 1
    if i==4:
        print("休息一下")
        continue # 跳过本次循环，直接执行下一次
    else:
        print("小明正在跑第%s圈" %i)


# i=5
# while i>0:
#     print("小明正在跑第%s圈" %i)
#     i-=1

num=input("请输入：")
print(num)





