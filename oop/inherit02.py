# 继承语法
# 在python中，任何类都有一个共同的父类叫object


class person():
    name = "NoName"
    age  = 0
    def sleep(self):
        print("sleep.............")


# 父类写在括号内

class teacher(person):
    def make_test(self):
        pass


t = teacher()
print(t.name)

# 构造函数的概念

class Dog():

    # __init__ 就是构造函数
    # 每次实例化的时候，第一次被调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print("这是一只狗")

# 实例化的时候，括号内的参数自动跟构造函数参数匹配
kaka = Dog()

# 多继承的例子
# 子类可以直接拥有父类的属性和方法
class Fish():
    def __init__(self,name):
        self.name = name

    def swim(self):
        print("i am swimming.............")


class Bird():
    def __init__(self,name):
        self.name = name

    def fly(self):
        print("i am fly............")


class Person():
    def __init__(self,name):
        self.name = name

    def work(self):
        print("working..........")


# 多继承例子
class SuperMan(Person,Bird,Fish):
    def __init__(self,name):
        self.name = name


s = SuperMan("yueyue")
s.fly()
s.swim()


class Student():
    def __init__(self, name):
        self.name = name

    def __gt__(self, other):
        print("{0}会比{1}大吗?".format(self.name, other.name))
        return self.name > self.name

# 字符串的比较规则


stu1 = Student("one")
stu2 = Student("two")

print(stu1 > stu2)
