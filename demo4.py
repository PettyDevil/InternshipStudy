class Student:
    '''
    无参构造方法
    Student(){

    }
    '''
    #private String name
    def __init__(self,name,age,gender):#通过参数的默认值做重载效果
        #this.name=name
        self.__name=name   #普通字段,在普通子段之前加上__,就会变成私有化的
        if 100>age>0:
            self.__age=age
        else:
            self.__age=18
        self.__gender=gender
        print("qqqqqqqqq")
    #构造方法的重载：让构造方法多样化，声明对象时可以有选择性的去使用不同的构造方法   python没有重载
    #模仿java做getter和setter方法
    # def getAge(self):
    #     return self.__age
    # def setAge(self,age):
    #     self.__age=age

    #python解决私有化问题
    @property   #定义属性的getter方法
    def name(self):
        print("name的getter方法被执行")
        return self.__name
    @name.setter   #定义属性的setter方法
    def name(self,name):
        print("name的setter方法被执行")
        self.__name=name

    @property
    def  age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if 100>age>0:
            self.__age=age
        else:
            self.__age=18

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self,gender):
        self.gender=gender


    def speak(self):#对象方法:只能由对象自己去调用，类对象不可以调用的
        print("wwwwwwww")

    @classmethod
    def eat(cls):#类方法：能够被对象和类本身调用    相当于java中加了static的方法
        print("eeeeeeeeee")  #可以调用类中的某些东西

    @staticmethod
    def introduce():#静态方法：能够被对象和类本身调用
        print("hahhhahahahahahhaahhaah")    #一般不能调用任何属性或方法

#获取对象
#Student stu=new Student()    构造方法（默认系统会给）
stu=Student("呵呵",2000,"男")    #构造方法
# stu.speak()
# stu.eat()
# stu.introduce()

#获取私有化子段的捷径
#print(stu._Student__age)#不建议用，违背了程序的安全性
# stu.setAge(30)
# print(stu.getAge())
stu.name="嘻嘻"   #赋值时python会自动调用改属性的setter方法
print(stu.name)   #当没有赋值时python会自动调用该属性的getter方法
# print(stu.name)
# s1=Student("嘻嘻",20,"女")
# print(s1.name)
#Student.speak()
# Student.eat()
# Student.introduce()