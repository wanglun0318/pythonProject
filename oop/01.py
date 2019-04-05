
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

# 实例化一个学生


student1 = PythonStudent()
print(student1.name)
print(student1.age)

student1.doHomework()
