class Student:
    '''
    无参构造方法
    Student(){


    }
    '''
    # private String name
    def __init__(self,name,age,gender): # 通过参数的默认值做重载效果
        # this.name=name
        self.__name=name  # 普通字段，在普通字段之前加上__，就会变成私有化
        if 100>age>0:
            self.__age=age
        else:
            self.__age=18
        self.gender=gender
        print("sdfasdas")
        # java构造方法的重载：让构造方法多样化，声明对象时可以有选择性的去使用不同的构造方法   python没有重载，只有覆盖
    # def __init__(self):
    #     print("dsdvdsvdsv")


    def getAge(self):
        return  self.__age

    def setAge(self,age):
        self.__age=age


    # python解决私有化问题\
    @property    # 定义属性
    def name(self):  # 定义属性的getter方法
        print("name的getter方法被运行")
        return self.name()
    @name.setter  # 定义属性的setter方法
    def name(self,name):
        print("name的setter方法被运行")
        self.__name=name

    def speak(self):  # 对象方法:只能由对象自己去调用，类对象不可以调用
        print("cdcacadacasdas")


    @classmethod
    def eat(cls):  # 类方法：能够被对象和类本身调用     相当于java中加了static的方法
        print("wwweewrwere")  # 可以调用类中的某些东西

    @staticmethod
    def introduce(): # 静态方法：能够被对象和类本身调用
        print("dkdsbfkdsjhufjksdhkfjhdskfhkejhfkjewh")  # 一般不能调用任何属性或方法


# 获取对象
# Student stu = new Student()
stu=Student("呵呵",18,'男')  # 构造方法
# stu.speak()
# stu.eat()
# # stu.name="哈哈"
# print(stu.name)
# s1=Student("嘻嘻",20,'女')
# print(s1.name)
# # s2=Student()
# Student.eat()
# Student.introduce()
# 获取私有化字段的捷径
# print(stu._Student__age)  # 不建议用，违背了程序的安全性
# stu.setAge(30)
# print(stu.getAge())
stu.name="嘻嘻"  # 赋值时python会自动调用该属性的setter方法
print(stu.name)

# stu.age=2000
# print(stu.age)