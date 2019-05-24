import os
import pickle


class MyDes:
    saved = []

    def __init__(self, name = None):
        self.name = name
        self.filename = self.name + ".pkl"

    def __get__(self, instance, owner):
        if self.name not in MyDes.saved:
            raise AttributeError("{0}属性还没有赋值！".format(self.name))

        with open(self.filename, "rb") as f:
            value = pickle.load(f)

        return value

    def __set__(self, instance, value):
        with open(self.filename, "wb") as f:
            pickle.dump(value, f)
            MyDes.saved.append(self.name)

    def __delete__(self, instance):
        os.remove(self.filename)
        MyDes.saved.remove(self.name)


class Test:
    x = MyDes("x")
    y = MyDes("y")


test = Test()
test.x = 123
del test.x
