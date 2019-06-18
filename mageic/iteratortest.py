"""
    迭代是重复反馈过程的活动，其目的通常是为了接近并到达所需的目标或结果。每一次对过程的重复
被称为异常“迭代”，而每一次迭代得到的结果会被用来作为下一次的迭代的初始值
迭代器就是实现了__next__()方法的对象，用于遍历容器中的数据

__iter__(self)  定义当迭代容器中的元素的行为
__next__() 让对象可以通过next(实例名)访问下一个元素
"""

import datetime as dt


class LeapYear:
    def __init__(self):
        self.now = dt.date.today().year  # 获取当前年份

    def isLeapYear(self, year):
        if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        while not self.isLeapYear(self.now):
            self.now -= 1
        temp = self.now
        self.now -= 1
        return temp


leapYears = LeapYear()
for i in leapYears:
    if i >= 2000:
        print(i)
    else:
        break
