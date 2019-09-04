import socket   # 服务器


HOST = ''
PORT = 8888

f_name = 'timg_copy.jpg'  # 定义上传图片名字

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))   # 绑定IP和端口
    s.listen(10)  # 监听端口
    print('服务器启动...........')

    while True:
        with s.accept()[0] as conn:  # 等待客户端连接
            # 创建字节序列对象列表，作为接收数据的缓冲区
            buffer = []
            while True:  # 反复接收数据
                data = conn.recv(1024)
                if data:
                    # 接收的数据添加到缓冲区
                    buffer.append(data)
                else:
                    # 没有接收到数据则退出
                    break
            # 将接收到的字节序列对象合并为一个字节序列对象
            b = bytes().join(buffer)   # bytes()创建一个空字节，join(buffer)可以将buffer连接起来
            with open(f_name, 'wb') as f:  # 以写入模式打开二进制本地文件，将上传数据写入文件中
                f.write(b)

            print('服务器接收完成')


