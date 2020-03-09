print("欢迎您来到宠物店")
dic={}
pet=[]
dic["亲密度"]=0
class Animal:
    def __init__(self):

        h=input("请输入宠物的健康值（1到100之间）：")
        h=int(h)
        if 100>=h>=0:
            dic["健康值"]=h
        else:
            print("健康值应该在0和100之间，默认值是60")
            dic["健康值"]=60

    @classmethod
    def intimacy(cls):
        behavior=int(input())
        if behavior == 1:
            for temp in pet:
                if temp["健康值"]<0:
                    print("宠物健康值为负，无法进行该操作")
                else:
                    if temp["亲密度"]>=100:
                        temp["亲密度"] =100
                    else:
                        temp["亲密度"]=temp["亲密度"]+5
                    temp["健康值"]=temp["健康值"]+5
        elif behavior == 2:
            for temp in pet:
                if temp["亲密度"]>=100:
                    temp["亲密度"] =100
                else:
                    temp["亲密度"]=temp["亲密度"]+5
                temp["健康值"]=temp["健康值"]-10




class Dog(Animal):
    def __init__(self):
        super().__init__()
        while(True):
            k = input("请选择狗的品种：（1、聪明的拉布拉多犬2、酷酷的雪纳瑞）")
            if(k=='1'):
                dic["种类"]="聪明的拉布拉多犬"
                break
            elif(k=='2'):
                dic["种类"]="酷酷的雪纳瑞"
                break
            else:
                print("输入有误！请重新输入！")



class Penguin(Animal):
    def __init__(self):
        super().__init__()
        while(True):
            k = input("请选择企鹅的品种：（1、北极企鹅2、南极企鹅）")
            if(k=='1'):
                dic["种类"]="北极企鹅"
                break
            elif(k=='2'):
                dic["种类"]="南极企鹅"
                break
            else:
                print("输入有误！请重新输入！")


while(True):
    dic["昵称"] = input("请输入要领养宠物的名字或按3退出：")
    dic["类型"] = input("请选择要领养的宠物类型：（1、狗狗2、企鹅）")
    if dic["类型"]=='1':
        d=Dog()
        pet.append(dic)
        print("以下是你的宠物")
        print("宠物名称\t\t\t种类\t\t\t健康值\t\t\t亲密度")
        for temp in pet:
            print("%s%16s%16s%16s" % (temp["昵称"], temp["种类"], temp["健康值"], temp["亲密度"]))
            while True:
                print("选择下面功能\n与宠物互动请按1\n退出宠物系统请按2")
                p = int(input())
                if p == 1:
                    for temp in pet:
                        if "聪明的拉布拉多犬" == temp["种类"] or temp["种类"] == "酷酷的雪纳瑞":
                            print("1.与你的狗狗玩接飞盘游戏，健康值-10，亲密度+5\n2.让你的狗狗休息，健康值+5，亲密度+1")
                            Dog.intimacy()
                    print("玩游戏后宠物属性\n")
                    print("宠物名称\t\t\t种类\t\t\t健康值\t\t\t亲密度")
                    for temp in pet:
                        print("%s%16s%16s%16s" % (temp["昵称"], temp["种类"], temp["健康值"], temp["亲密度"]))
                elif p==2:
                    break

    if dic["类型"] == '2':
        d = Penguin()
        pet.append(dic)
        print("以下是你的宠物")
        print("宠物名称\t\t\t种类\t\t\t健康值\t\t\t亲密度")
        for temp in pet:
            print("%s%16s%16s%16s" % (temp["昵称"], temp["种类"], temp["健康值"], temp["亲密度"]))
            while True:
                print("选择下面功能\n与宠物互动请按1\n退出宠物系统请按2")
                p = int(input())
                if p == 1:
                    for temp in pet:
                        if "北极企鹅" == temp["种类"] or temp["种类"] == "南极企鹅":
                            print("1.与你的企鹅滑雪，健康值-10，亲密度+5\n2.让你的企鹅休息，健康值+5，亲密度+1")
                            Dog.intimacy()
                    print("玩游戏后宠物属性\n")
                    print("宠物名称\t\t\t种类\t\t\t健康值\t\t\t亲密度")
                    for temp in pet:
                        print("%s%16s%16s%16s" % (temp["昵称"], temp["种类"], temp["健康值"], temp["亲密度"]))
                elif p == 2:
                    break

    elif dic["类型"] == '3':
        break