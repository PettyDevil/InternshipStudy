import abc
class A(metaclass=abc.ABCMeta):#抽象类
    def test1(self):
        print("A")

    @abc.abstractclassmethod
    def demo(self):
        pass

class B(A):
    def test1(self):
        print("B")

class C:
    def test(self):
        print("C")

class D(B,C):
    def test1(self):
        print("D")

d=D() #深度继承
d.test()


#抽象类