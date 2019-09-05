import socket  # 客户端


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 服务器地址
server_address = ('127.0.0.1', 8888)

# 给服务器发送数据
s.sendto(b'hello', server_address)

# 从服务器端接收数据
data, _ = s.recvfrom(1024)
print('从服务器接收消息：{0}'.format(data.decode()))

# 释放资源
s.close()
