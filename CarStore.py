import os

class MotoviCar:
    def __init__(self,price,day):
        self.__price=price
        self.__day=day

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,price):
        self.__price=price

    @property
    def day(self):
        return self.__day
    @day.setter
    def day(self,day):
        self.__day=day

    def intro(self):
        return

class Car(MotoviCar):
    def __init__(self,price,day,types):
        super().__init__(price,day)
        self.__types=types

    @property
    def types(self):
        return self.__types
    @types.setter
    def types(self,types):
        self.__types=types

    def intro(self):
        str="{}\t{}\t{}\t{}\n".format(self.types,self.price,self.day,self.price*self.day)
        return str

class Bus(MotoviCar):
    def __init__(self,price,day,seatCount):
        super().__init__(price,day)
        self.__seatcount=seatCount

    @property
    def seatcount(self):
        return self.__seatcount
    @seatcount.setter
    def seatcount(self,seatcount):
        self.__seatcount=seatcount

    def intro(self):
        str="{}\t{}\t{}\t{}\n".format(self.seatcount,self.price,self.day,self.price*self.day)
        return str

cs=[]

while True:
    print("1.租赁汽车")
    print("2.打印小票")
    id=int(input("请输入功能编号："))
    if id==1:
        num=int(input("可租赁车型包含：1.轿车  2.巴士"))
        if num==1:
            no=int(input("请选择不同品牌的汽车（1.别克商务GL8  2.宝马550i  3.别克林荫大道）"))
            types=""
            price=0
            if no==1:
                types="别克商务GL8"
                price=600
            elif no==2:
                types="宝马550i"
                price=500
            elif no==3:
                types="别克林荫大道"
                price=300
            day=int(input("请输入租赁的天数："))
            c=Car(price,day,types)
            cs.append(c)
        elif num==2:
            no=int(input("请选择巴士的车型（1.座位<=16    2.座位>16）"))
            seatcount=""
            price=0
            if no==1:
                seatcount="座位<=16"
                price=500
            elif no==2:
                seatcount="座位>16"
                price=800
            day = int(input("请输入租赁的天数："))
            b=Bus(price,day,seatcount)
            cs.append(b)
    elif id==2:
        # print("车型\t单价\t租赁天数\t小计")
        # for i in cs:
        #     if isinstance(i,Car):
        #         print("{}\t{}\t{}\t{}".format(i.types,i.price,i.day,i.price*i.day))
        #     else:
        #         print("{}\t{}\t{}\t{}".format(i.seatcount,i.price,i.day,i.price*i.day))
        ss=[]
        for i in cs:
            ss.append(i.intro())
        folder_name="output"
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        file_name="xiaopiao.txt"
        with open(folder_name+"/"+file_name,'w',encoding="utf-8") as fp:
            fp.writelines(ss)

