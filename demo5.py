#java中的继承：提高代码的复用性以及维护性,单一继承

class A:#父类、超类、基类
    def __init__(self,a):
        self.a=a

    def test(self):
        print("a的test方法被执行")

class B(A):
    def __init__(self,a,b):#子类构造方法调用父类的构造方法来获取父类的属性
        super().__init__(a) #调用父类的构造方法
        self.b=b

    def test(self):#python中的方法重写
        print("b的test方法被执行")


demo=B("1","2")
demo.test()
print(demo.a)

#python中类分为两种：新式类、普通类
#继承体系的区别：广式继承、深度继承