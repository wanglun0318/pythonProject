# coding=utf-8


import threading
import time

# 线程停止变量
isrunning = True


# 线程体函数
def thread_body():
    while isrunning:
        # 线程开始工作
        print('下载中...')
        # 线程休眠
        time.sleep(5)
    print('执行完成！')


# 主函数
def main():
    # 创建线程对象
    t1 = threading.Thread(target=thread_body)
    # 启动线程
    t1.start()
    # 从键盘接收指令
    command = input('请输入停止指令：')
    if command == '停止':
        global isrunning
        isrunning = False


if __name__ == '__main__':
    main()
