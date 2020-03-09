
b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
c = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

f=[6,2,2,5,0,3,5,1,4,6,2,4]
r=[5,1,2,5,0,3,5,1,4,6,2,4]
y,m=input("请输入日期，中间用空格隔开如2020 2\n").split()
# print(type(y),m)
y=int(y)
m=int(m)
y1=y%100
y2=((y1//4)+y1)%7
# print(y2)
i=1
if ((y%100==0 and y%400==0) or (y%100!=0 and y%4==0)):
    m1=r[m-1]
    t = (y2 + m1 + 1) % 7
    s=c[m-1]
else:
    m1=f[m-1]
    t = (y2 + m1 + 1) % 7
    s=c[m-1]
    pass
# print(m1)
t=(y2+m1+1)%7
# print(t)
print("     %d年%d月"%(y,m))
print("一 二 三 四 五 六 日")
if t==0:
    for i in range(6):
        print("   ",end="")
        pass
    print(" 1")
    for j in range(s-1):
        print("%2d"%(j+2),end=" ")
        if (j+1)%7==0:
            print(" ")
    pass
else:
    l=0
    for i in range(t-1):
        l+=1
        print("  ",end=" ")
        pass
    for j in range(8-t):
        l+=1
        print("%2d"%(j+1),end=" ")
        pass
    # print(8-t,l,'sadsadsa')
    for k in range(9-t,s+1):
        if l%7==0:
            print(" ")
        print("%2d"%k,end=" ")
        l+=1
        pass
    pass