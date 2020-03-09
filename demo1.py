print("************欢迎来到宠物店**************")
dictionary={}
dictionary["name"] = input("请问你的宠物取一个名字")
value = 0
dictionary["value"] = 0
class animal():
    def __init__(self):
        typeanimal = int(input("请选择宠物类型：1、狗狗；2、企鹅"))
        if typeanimal == 1:
            typedog = int(input("请选择狗的品种：1、聪明的拉布拉多犬；2、酷酷的雪纳瑞"))
            if typedog == 1:
                typedog ="聪明的拉布拉多犬"
                dictionary["type"]=typedog
                print("恭喜你获得了一只聪明的拉布拉多犬")
            elif typedog == 2:
                typedog ="酷酷的雪纳瑞"
                dictionary["type"] = typedog
                print("恭喜你获得了一只酷酷的雪纳瑞")
        elif typeanimal == 2:
            typepenguin = int(input("请选择企鹅的品种：1、迷你的小企鹅；2、胖胖的大企鹅"))
            if typepenguin == 1:
                typepenguin ="迷你的小企鹅"
                dictionary["type"] = typepenguin
                print("恭喜你获得了一只迷你的小企鹅")
            elif typepenguin== 2:
                typepenguin ="胖胖的大企鹅"
                dictionary["type"] = typepenguin
                print("恭喜你获得了一只胖胖的大企鹅")
        while True:
            health = int(input("请输入宠物的健康值0—100之间"))
            if 0<=health<=100:
                dictionary["health"]= health
                break
            else:
                print("输入错误，请重新输入")
    def intimacy(self):

        pass

    @classmethod
    def allshow(cls):
        print("宠物名称\t\t\t种类\t\t\t健康值\t\t\t亲密度")
        for temp in pet:
            print("%s%16s%16s%16s" % (temp["name"], temp["type"], temp["health"], temp["value"]))


class dog(animal):
    # def __init__(self):
    #     super().__init__()
    @classmethod
    def intimacy(cls):

        play=int(input())
        if play == 1:
            for temp in pet:
                if temp["health"]<10:
                    print("无法执行该操作，否则宠物死亡")
                else:
                    if temp["value"]>=100:
                        temp["value"] =100
                    else:
                        temp["value"]=temp["value"]+5
                    temp["health"]=temp["health"]+5
        elif play == 2:
            for temp in pet:
                if temp["value"]>=100:
                    temp["value"] =100
                else:
                    temp["value"]=temp["value"]+5
                temp["health"]=temp["health"]-10




class punguin(dog):
    def __init__(self):
        super().__init__()

A=animal()
pet=[]
pet.append(dictionary)
print("\n")
print("以下是你的宠物")
dog.allshow()
print("\n")
while True:
    print("选择下面功能\n与宠物互动请按1\n退出宠物系统请按2")
    p = int(input())
    if p==1:
        for temp in pet:
            if "聪明的拉布拉多犬"== temp["type"]or temp["type"]=="酷酷的雪纳瑞":
                print("1.与你的狗狗玩接飞盘游戏，健康值-10，亲密度+5\n2.让你的狗狗休息，健康值+5，亲密度+1")
                dog.intimacy()
            else:
                print("1.与你的企鹅竞走比赛，健康值-10，亲密度+5\n2.让你的企鹅休息，健康值+5，亲密度+1")
                punguin.intimacy()
        print("玩游戏后宠物属性\n")
        dog.allshow()
    elif p==2:
        break
    else:
        print("输入错误，请重新输入")



