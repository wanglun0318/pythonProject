"""
__getattr__(self, name)
    定义当用户试图获取一个不存在的属性时的行为

__getattribute__（self, name)
    定义当该类的属性被访问时的行为

__setattr__(self, name, value)
    定义当一个属性被设置时的行为

__delattr__（self, name)
    定义当一个属性被删除时的行为

super()函数是用于调用父类的一个方法
    是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
但是如果使用多继承，会涉及到查找顺序（MRO）,重复调用等种种问题
MRO就是类的方法解析顺序表，其实也就是继承父类方法是的顺序表
super()方法的语法：
    super（type[, object-or-type]）

避免无限递归的两种解决办法：
def __setattr__(self, name, value):
    self.__dict__[name] = value + 1

def __setattr__（self, name, value）
    super().__setattr__ = value + 1
"""


class Counter:
    def __init__(self):
        super().__setattr__("counter", 0)

    def __setattr__(self, key, value):
        super().__setattr__("counter", self.counter + 1)
        super().__setattr__(key, value)

    def __delattr__(self, item):
        super().__setattr__("counter", self.counter - 1)
        super().__delattr__(item)


c = Counter()
c.x = 1
print(c.counter)
c.y = 1
c.z = 1
print(c.counter)
del c.x
print(c.counter)
