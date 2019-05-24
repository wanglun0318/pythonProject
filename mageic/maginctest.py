import time as t
# 记录指定变量的读取和修改操作，并将记录一级触发时间保存到文件

class MyDes:
    def __init__(self, name=None, value=None):
        self.present = 0
        self.lasted = []
        self.name = name
        self.value = value
        self.unit = ["年", "月", "天", "小时", "分钟", "秒"]
        self.prompt = ""
        self.filename = "record.txt"

    def gain_time(self):
        self.present = t.localtime()  # 获取当前时间
        for index in range(6):
            temp = self.present[index]
            self.lasted.append(temp)
            self.prompt += str(self.lasted[index]) + self.unit[index]

        return self.prompt

    def __get__(self, instance, owner):
        self.prompt = MyDes().gain_time()
        print("{0}变量与北京时间{1}被读取,{0} =".format(self.name, self.prompt), end=" ")
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write("{0}变量与北京时间{1}被读取,{0} = {2}\n".format(self.name, self.prompt, str(self.value)))
        return self.value

    def __set__(self, instance, value):
        self.prompt = MyDes().gain_time()
        print("{0}变量与北京时间{1}被修改,{0} =".format(self.name, self.prompt), end=" ")
        self.value = value
        print(self.value)
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write("{0}变量与北京时间{1}被修改,{0} = {2}\n".format(self.name, self.prompt, str(self.value)))


class Test:
    x = MyDes("x", 10)
    y = MyDes("y", 8.8)


test = Test()
print(test.x)
print(test.y)
test.x = 123
test.y = "wo ai you"


