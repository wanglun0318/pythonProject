# coding=utf-8

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name=None):
        super().__init__(name=name)

    # 线程体函数
    def run(self):
        # 当前线程对象
        t = threading.current_thread()
        for n in range(5):
            # 当前线程名
            print('第{0}次执行线程{1}'.format(n, t.name))
            # 休眠
            time.sleep(1)
        print('线程{0}执行完成'.format(t.name))


# 主函数
def main():
    # 创建线程对象t1
    t1 = MyThread()
    # 启动线程
    t1.start()

    # 创建线程对象t2
    t2 = MyThread()
    # 启动线程
    t2.start()


if __name__ == '__main__':
    main()
