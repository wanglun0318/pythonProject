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
        # 执行sql操作
        sql = 'update user set name = %s where userid = %s'
        afc = cursor.execute(sql, ('Tony', 3))
        print('影响的数据行数：{0}'.format(afc))
        # 提交数据库事务
        connection.commit()
    # with代码块结束  关闭游标
except pymysql.DatabaseError as e:
    # 回滚数据库事务
    connection.rollback()
    print(e)
finally:
    # 关闭数据库连接
    connection.close()
