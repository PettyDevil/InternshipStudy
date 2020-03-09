import os
#系统控制
folder_name="output"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

#文件操作txt
#java: fileInputStream 文件输入流（读）  FileOutputStream文件输出流（写）   字节
#fileReader fileWiter  字符流必须关（刷新通道）
#字节-》字符

#python读写文件操作是一致     打开文件的方式有区别
#通过文件操作去创建一个文件，并且写入
file_name="demo.txt"
#mode='w' 先清空文件再去往里面写入内容
fp=open(folder_name+"/"+file_name,'w',encoding="utf-8")
#write()写一个字符串
fp.write("qqqqqqqqqqq\n")
#fp.write("wwwwwwwwwwww")
data=["这是第{}条数据\n".format(i+1) for i in range(10)]
fp.writelines(data)
fp.close()#开启了管道流，耗费资源

# with open(folder_name+"/"+file_name,'r') as fp: 自动释放资源

#读取文件数据
fp1=open(folder_name+"/"+file_name,'r',encoding="utf-8")
print(fp1.read(9))#换行符也会读
fp1.seek(0,0)#将指针调到开头
str=fp1.readline()#读整一行
while ""!=str:
    print(str)
    str=fp1.readline()

#指针 读取的位置fp1.seek(0,0开头  1当前位置  2最后的位置)
fp1.seek(0,0)
#读全部数据
print(fp1.readlines())
fp1.close()

#追加文件
fp2=open(folder_name+"/"+file_name,'a',encoding="utf-8")
fp2.write("hasnfsjank")
fp2.close()


#修改文件
#先读取全部的数据，然后找到列表中对应的位置进行替换，最后一次性全部写入