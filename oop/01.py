
"""
定义一个学生类
"""


# 定义一个类，用来描述学生
class PythonStudent():
    name = "月夜"
    age = 19
    course = "python"


# 定一个学生行为的方法，注意缩进层级
    def doHomework(self):

        print("在做作业，是个好好孩子呢......")
# 推荐在函数末尾使用return语句
        return None

# 构造函数
    def __init__(self):
        self.name = "aaaa"
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "bbbbbb"
    age = 90

# 实例化一个学生


student1 = PythonStudent()
print(student1.name)
print(student1.age)

student1.doHomework()

# 此时 系统会默认把a作为第一个参数传入函数
a = PythonStudent()
a.say()

# 此时self被a替换
PythonStudent.say(a)

# 同样可以把PythonStudent作为参数传入
PythonStudent.say(PythonStudent)

# 此时传入的是类实例B,因为B具有name和age不会报错,此时利用了鸭子模型
PythonStudent.say(B)

