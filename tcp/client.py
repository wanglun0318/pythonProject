import socket   # 客户端


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个socket对象
# 连接服务器
s.connect(('127.0.0.1', 8888))  # 127.0.0.1是远程服务器IP或者主机名，8888是远程服务端口

# 给服务器端发送数据
s.send(b'Hello')  # 在字符串前面加b可以将字符串转换为字节序列，这种方法只适合ASCII字符串


# 从服务器端接收数据
data = s.recv(1024)
print('从服务器端接收到的消息：{0}'.format(data.decode()))

while data.decode() != '结束':
    information_client = input('请输入：')
    s.send(information_client.encode())

    # 从服务器端接收数据
    data = s.recv(1024)
    print('从服务器端接收到的消息：{0}'.format(data.decode()))
else:
    s.send('结束'.encode())

# 释放资源
s.close()
