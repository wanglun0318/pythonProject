import pymysql

# 建立数据库连接
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345',
                             database='MyDB',
                             charset='utf8')
try:
    # 创建游标对象
    with connection.cursor() as cursor:
        # 执行SQL操作
        sql = 'select max(userid) from user'
        cursor.execute(sql)

        # 提取结果集
        row = cursor.fetchone()

        if row is not None:
            print('最大用户ID：{0}'.format(row[0]))
            print(row[0])

        # with 代码块结束  关闭游标
finally:
    # 关闭数据连接
    connection.close()
