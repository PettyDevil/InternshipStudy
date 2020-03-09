import os
folder_name="output"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
file_name = "zl.txt"
m = []
d = []
n = []
c1={1:600,2:500,3:300}
c2={1:800,2:1500}
c3=50
dic1={1:"别克商务舱GL8",2:"宝马550i",3:"别克林荫大道"}
dic2={1:"<=16座",2:">16座"}
if __name__ == '__main__':
    print("欢迎来到汽车租赁系统！")
    s=0
    s1=0
    s2=0
    s3=0
    fp = open(folder_name + "/" + file_name, 'w', encoding="utf-8")
    while True:
        i=input("1、轿车\n2、客车\n3、卡车\n4、查询当前花费\n5、结算\n请输入您要租赁的车型或结算：")
        if i=='1':
            m1=int(input("请输入您要租赁的车型：1、别克商务舱GL8 2、宝马550i 3、别克林荫大道"))
            d1=int(input("请输入您要租赁的天数："))
            n1 = int(input("请输入您要租赁的数量："))
            m.append(m1)
            d.append(d1)
            n.append(n1)
            s1+=d1*c1[m1]*n1
            data = ["租赁轿车型号{}，共{}辆，租用{}天，花费{}元\n".format(dic1[m1],n1,d1,s1)]
            fp.writelines(data)
        elif i=='2':
            m2 = int(input("请输入您要租赁的车型：1、<=16座 2、>16座"))
            d2=int(input("请输入您要租赁的天数："))
            n2 = int(input("请输入您要租赁的数量："))
            m.append(m2)
            d.append(d2)
            n.append(n2)
            s2 += d2 * c2[m2] * n2
            data = ["租赁客车型号{}，共{}辆，租用{}天，花费{}元\n".format(dic2[m2], n2, d2, s2)]
            fp.writelines(data)
        elif i=='3':
            m3=int(input("请输入您的卡车吨位："))
            d3=int(input("请输入您要租赁的天数："))
            n3 = int(input("请输入您要租赁的数量："))
            m.append(m3)
            d.append(d3)
            n.append(n3)
            s3 += d3 * c3*m3 * n1
            data = ["租赁卡车吨位{}吨，共{}辆，租用{}天，花费{}元\n".format(m3, n3, d3, s3)]
            fp.writelines(data)
        elif i=='4':
            s=s1+s2+s3
            print("目前共花费{}元".format(s))
            continue
        elif i=='5':
            s = s1 + s2 + s3
            print("您本次花费共计{}元".format(s))
            print("感谢使用租赁系统，欢迎下次光临！")
            data=["共计花费{}元".format(s)]
            fp.writelines(data)
            fp.close()
            break
        else:
            print("您输入的序号有误，请从新输入！")
            continue