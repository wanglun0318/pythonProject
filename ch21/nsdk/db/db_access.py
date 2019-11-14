# coding=utf-8
import pymysql

def insert_hisq_data(row):
    # 在股票历史价格表中传入数据
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='12345',
                                 database='nasdaq',
                                 charset='utf8')

    try:
        with connection.cursor() as cursor:
            sql = 'insert into historicalquote ' \
                      '(HDate,Open,High,Low,Close,Volume,Symbol)' \
                      ' values (%(Date)s,%(Open)s,%(High)s,%(Low)s,%(Close)s,%(Volume)s,%(Symbol)s)'
            affectedcount = cursor.execute(sql, row)  # 绑定sql语句并执行
            print('影响行数；{0}'.format(affectedcount))
            # 提交数据库事务
            connection.commit()
    except pymysql.DatabaseError as error:
        # 回滚 事务
        connection.rollback()
        print(error)
    finally:
        # 关闭数据库
        connection.close()