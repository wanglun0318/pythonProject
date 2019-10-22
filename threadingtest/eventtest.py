# coding=utf-8


import threading
import time

event = threading.Event()


class Stack:
    def __init__(self):
        # 堆栈指针 初始值为0
        self.pointer = 0
        # 堆栈有5个数字控件
        self.data = [-1, -1, -1, -1, -1]

    # 压栈方法
    def push(self, c):
        global event
        # 堆栈已满，不能压栈
        while self.pointer == len(self.data):
            # 等待其他线程把数据出栈
            event.wait()
        # 通知其他线程把数据 出栈
        event.set()
        # 数据压栈
        self.data[self.pointer] = c
        # 指针向上移动
        self.pointer += 1

    # 出栈方法
    def pop(self):
        global event
        # 堆栈无数据，不能出栈
        while self.pointer == 0:
            # 等待其他线程把数据压栈
            event.wait()
        # 通知其他线程压栈
        event.set()
        # 指针向下移动
        self.pointer -= 1
        data = self.data[self.pointer]
        # 数据出栈
        return data


# 创建堆栈对象
stack = Stack()


# 生存者线程体函数
def producer_thread_body():
    global stack
    # 产生10个数字
    for i in range(0, 10):
        # 把数字压栈
        stack.push(i)
        print('生产：{0}'.format(i))
        # 每产生一个数字，线程就睡眠
        time.sleep(1)


# 消费者线程体函数
def consumer_thread_body():
    global stack
    # 从堆栈中读取数字
    for i in range(0, 10):
        x = stack.pop()
        print('消费： {0}'.format(x))
        # 每产生一个数字，线程就睡眠
        time.sleep(1)


# 主函数
def main():
    # 创建生存者对象
    producer = threading.Thread(target=producer_thread_body)
    producer.start()

    # 创建消费者对象
    consumer = threading.Thread(target=consumer_thread_body)
    consumer.start()


if __name__ == '__main__':
    main()
