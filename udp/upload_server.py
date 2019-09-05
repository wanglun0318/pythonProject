import socket  # 服务器


HOST = '127.0.0.1'
POST = 8888

f_name = '666_copy.txt'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, POST))
    print('服务器启动....')

    # 创建字节序列对象列表，作为接收数据的缓冲区
    buffer = []
    while True:  # 反复接收数据
        data, _ = s.recvfrom(1024)
        if data:
            flag = data.decode()  # 解码数据包
            if flag == 'bye':   # 判断是否为bye字符串
                break
            buffer.append(data)
        else:
            # 没有接收到数据，进入下次循环继续接收
            continue
    # 将接收的字节序列对象列表合并为一字节序列对象
    b = bytes().join(buffer)
    with open(f_name, 'w') as f:
        f.write(b.decode())

    print('接收完成......')