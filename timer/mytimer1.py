import time as t


class MyTimer:
    def __init__(self):
        self.prompt = "为开始计时！"
        self.lasted = 0.0
        self.begin = 0
        self.end = 0
        self.default_timer = t.perf_counter  # 返回计时器的精准时间

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self, other):
        result = self.lasted + other.lasted
        prompt = "总共运行了{0}秒".format(result)
        return prompt

    # 开始计时
    def start(self):
        self.begin = self.default_timer()  # 返回当前进程CPU的时间总和
        self.prompt = "提示：请先调用stop()停止计时！"
        print("计时开始...........")

    # 停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用start()开始计时！")
        else:
            self.end = self.default_timer()
            self._calc()
            print("计时结束！")

    # 内部方法 计算运行时间
    def _calc(self):
        self.lasted = self.end - self.begin
        self.prompt = "总共运行了{0}秒".format(self.lasted)

        # 为下一轮计时初始化变量
        self.begin = 0
        self.end = 0

    # 设置计时器
    def set_timer(self, timer):
        if timer == "process_time":
            self.default_timer = t.process_time
        elif timer == "perf_counter":
            self.default_timer = t.perf_counter
        else:
            print("输入无效，请输入 per_counter 或 process_time")


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