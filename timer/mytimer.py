import time as t


class MyTimer:
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.lasted = []
        self.prompt = "未开始计时"
        self.unit = ["年", "月", "天", "小时", "分钟", "秒"]
        self.borrow = [0, 12, 31, 24, 60, 60]

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    # 开始计时
    def start(self):
        self.begin = t.localtime()  # 获取当前时间
        self.prompt = "提示：请先调用 stop()停止计时"
        print("计时开始！")

    # 停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用start()开始计时")
        else:
            self.end = t.localtime()
            self._calc()
            print("停止计时！")

    # 定义私有方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了："
        for index in range(6):
            temp = self.end[index] - self.begin[index]
            # 低位不够减，需向高位借位
            if temp < 0:
                # 测试高位是否有得借，没得借的话再向更高位借......
                i = 1
                while self.lasted[index-i] < 1:
                    self.lasted[index-i] += self.borrow[index-i] - 1
                    self.lasted[index-i-1] -= 1
                    i += 1

                self.lasted.append(self.borrow[index] + temp)
                self.lasted[index-1] -= 1
            else:
                self.lasted.append(temp)

        # 由于高位随时会被借位，所以打印放在最后
        for index in range(6):
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])

        # 为下一轮做准备，重置变量
        self.begin = 0
        self.end = 0


count = 0
while not "关闭" == input("计时器（开始/关闭）："):
    count += 1
    t1 = MyTimer()
    if input("第{0}次计时，是否开始：".format(count)):
        t1.start()

    if input("是否结束计时："):
        t1.stop()

    print("第{0}次计时,{1}".format(count, t1))
    print("=================================================================================")
else:
    print("已关闭计时器！")
    exit()  # 关闭程序
