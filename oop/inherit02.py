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