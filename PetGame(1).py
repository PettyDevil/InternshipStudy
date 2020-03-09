#宠物类
class Pet:
    def __init__(self,name,health,love=20):
        self.__name=name
        self.__health=health
        self.__love=love

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name

    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self,health):
        self.__health=health

    @property
    def love(self):
        return self.__love
    @love.setter
    def love(self,love):
        self.__love=love

    def introduce(self):
        print("我的名字叫{},我的健康值是{},我的主人的亲密度是{}".format(self.name,self.__health,self.love))

    def eatFood(self):
        print("")

class Dog(Pet):
    def __init__(self,name,health,types):
        super().__init__(name,health)
        self.__types=types

    @property
    def types(self):
        return self.__types
    @types.setter
    def types(self,types):
        self.__types=types

    def introduce(self):
        print("我的名字叫{},我的健康值是{},我的主人的亲密度是{},我的品种是{}".format(self.name,self.health,self.love,self.types))

    def eatFood(self):
        self.health+=8
        print("吃狗粮，健康值+8")

class Penguin(Pet):
    def __init__(self,name,health,gender):
        super().__init__(name,health)
        self.__gender=gender

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self,gender):
        self.__gender=gender

    def introduce(self):
        print("我的名字叫{},我的健康值是{},我的主人的亲密度是{},我的性别是{}".format(self.name,self.health,self.love,self.gender))

    def eatFood(self):
        self.health+=7
        print("吃小鱼，健康值+7")

class Panda(Pet):
    def __init__(self,name,health,weight):
        super().__init__(name,health)
        self.__weight=weight
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self,weight):
        self.__weight=weight

    def introduce(self):
        print("我的名字叫{},我的健康值是{},我的主人的亲密度是{},体重为{}".format(self.name,self.health,self.love,self.weight))

    def eatFood(self):
        self.health+=3
        print("吃苹果，健康值+3")

ps=[]

while True:
    print("1.领养宠物")
    print("2.喂养宠物")
    print("3.和宠物玩耍")
    id=int(input("请输入您要使用的功能编号："))
    if id==1:
        print("欢迎您来到宠物店")
        name=input("请输入您要领养的宠物名称")
        no=int(input("请输入要领养的宠物类型(1.狗  2.企鹅  3.熊猫)"))
        p=""
        if no==1:
            type=""
            num=int(input("请输入要领养的狗品种（1.拉布拉多  2.雪纳瑞）"))
            if num==1:
                type="拉布拉多"
            else:
                type="雪纳瑞"
            health=int(input("请输入健康值"))
            p=Dog(name,health,type)
        elif no==2:
            gender=input("请输入企鹅的性别")
            health = int(input("请输入健康值"))
            p=Penguin(name,health,gender)
        elif no==3:
            weight=input("请输入熊猫的体重")
            health = int(input("请输入健康值"))
            p=Panda(name,health,weight)
        ps.append(p)
    elif id==2:
        # print("名称\t健康值\t亲密度\t其他属性")
        # for i in ps:
        #     str=""
        #     #判断原始类型
        #     if isinstance(i,Dog):
        #         str=i.types
        #     elif isinstance(i,Penguin):
        #         str=i.gender
        #     elif isinstance(i,Panda):
        #         str=i.weight
        #     print("{}\t\t{}\t\t{}\t{}".format(i.name,i.health,i.love,str))
        for i in ps:
            i.introduce()
        na=input("请输入您要喂养的宠物名称")
        for i in ps:
            if i.name==na:
                na.eatFood()
                break
        else:
            print("您输入的宠物名称不存在！！")
    elif id==3:
        print("fdfds")
