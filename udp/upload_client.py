import socket  # 客户端


HOST = '127.0.0.1'
POST = 8888
f_name = '666.txt'

# 服务器 地址
server_address = (HOST, POST)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    with open(f_name, 'r') as f:
        while True:  # 反复从文件中读取数据
            data = f.read(1024)
            if data:
                # 发送数据
                s.sendto(data.encode(), server_address)
            else:
                # 发送结束标志
                s.sendto(b'bye', server_address)
                # 文件中可读取的数据则退出
                break
        print('客户端上传完成。')
