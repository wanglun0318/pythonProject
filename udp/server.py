import socket  # 服务器


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建UDP socket对象
s.bind(('', 8888))   # 绑定端口和IP
print('服务器启动.......')

# 从客户端接收数据
data, client_address = s.recvfrom(1024)  # recvfrom(1024)接收数据，设置接收虽大字节数
print('从客户端接收消息：{0}'.format(data.decode()))

# 给客户端发送数据
s.sendto('你好'.encode(), client_address)

# 释放资源
s.close()
