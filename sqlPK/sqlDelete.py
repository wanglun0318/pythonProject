import pymysql


# 查询最大用户ID
def read_max_userid():
    # 建立数据库连接
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='12345',
                                 database='MyDB',
                                 charset='utf8')

    try:
        with connection.cursor() as cursor:
            sql = 'select max(userid) from user'
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is not None:
                print('最大id: {0}'.format(row[0]))
                return row[0]
    finally:
        connection.close()


# 建立数据库连接
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345',
                             database='MyDB',
                             charset='utf8')

# 查询最大值
maxid = read_max_userid()

try:
    # 创建游标对象
    with connection.cursor() as cursor:
        # 执行sql操作
        sql = 'delete from user where userid = %s'
        afc = cursor.execute(sql, (maxid))
        print('影响的数据行数：{0}'.format(afc))
        # 提交 数据库事务
        connection.commit()
    # with代码块结束 关闭游标
except pymysql.DatabaseError:
    # 回滚数据库事务
    connection.rollback()
finally:
    # 关闭数据库
    connection.close()
