# dbm(DataBaseManager)数据库是最简单的NoSQL数据库，不需要安装，直接通过键值对数据存储
"""
dbm.open(file, flag='r')
参数file是数据库文件名，包括路径；flag是文件打开方式，
flag取值说明：
    r：以只读方式打开现有数据库，这是默认值
    w：以读写方式打开现有数据库
    c：以读写方式打开数据库，如果数据库不存在则创建
    n：始终创建一个新的空的数据库，打开方式为读写

"""


import dbm


with dbm.open('mydb', 'c') as db:
    db['name'] = 'tony'   # 更新数据
    print(db['name'].decode())   # 取出数据

    age = int(db.get('age', b'18').decode())  # 取出数据
    print(age)

    if 'age' in db:           # 判断是否存在age数据
        db['age'] = '19'       # 或者 b'20'
        age1 = int(db.get('age', b'18').decode())  # 取出数据
        print(age1)

    print(22222)
    del db['name']      # 删除name数据

