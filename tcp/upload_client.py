import socket  # 客户端


HOST = '127.0.0.1'
POST = 8888
f_name = 'timg.jpg'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, POST))  # 连接远程服务器

    with open(f_name, 'rb') as f:  # 以只读模式打开二进制本文件
        b = f.read()
        s.sendall(b)
        print('客户端上传完成.！！！！！')
