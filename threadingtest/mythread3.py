# coding=utf-8


import threading
import time


class TicketDB:
    def __init__(self):
        # 机票数量
        self.ticket_count = 5

    # 获取当前机票数量
    def get_ticket_count(self):
        return self.ticket_count

    # 销售机票
    def sell_ticket(self):
        # 线程休眠 阻塞当前线程，模拟等待用户付款
        time.sleep(1)
        print('第{0}号票，已经售出'.format(self.ticket_count))
        self.ticket_count -= 1


# 创建TicketDB对象
db = TicketDB()
# 创建lock对象
lock = threading.Lock()


# 线程体
def thread1_body():
    global db, lock  # 声明为全局变量
    while True:
        lock.acquire()
        curr_ticket_count = db.get_ticket_count()
        # 查询是否有票
        if curr_ticket_count > 0:
            db.sell_ticket()
        else:
            lock.release()
            break
        lock.release()
        time.sleep(1)


def thread2_body():
    global db, lock
    while True:
        lock.acquire()
        curr_ticket_count = db.get_ticket_count()
        # 查询是否有票
        if curr_ticket_count > 0:
            db.sell_ticket()
        else:
            lock.release()
            break
        lock.release()
        time.sleep(1)


# 主函数
def main():
    # 创建线程对象
    t1 = threading.Thread(target=thread1_body)
    t1.start()

    t2 = threading.Thread(target=thread2_body)
    t2.start()


if __name__ == '__main__':
    main()
