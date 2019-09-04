import socket   # 服务器


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个socket对象
s.bind(('', 8888))  # 绑定本机IP(ip为空，系统会自动分配可用的本机IP)和端口
s.listen()   # 监听本机8888端口
print('服务器启动......')

# 等待客户端连接
conn, address = s.accept()  # 使用accept()方法阻塞程序，等待客户端连接，返回二元组（conn接受对象，address接受客户端地址）
# 客户端连接成功
print(address)  # 打印IP

# 从客户端接受数据
data = conn.recv(1024)  # 参数1024是设置一次接收的最大字节
print('从客户端接收到的消息是：{0}'.format(data.decode()))

while data.decode() != '结束':

    # 给客户端发送数据
    information_server = input('请输入：')
    conn.send(information_server.encode())

    data = conn.recv(1024)  # 参数1024是设置一次接收的最大字节
    print('从客户端接收到的消息是：{0}'.format(data.decode()))
else:
    conn.send('结束'.encode())

# 释放资源
conn.close()
s.close()
