# coding=utf-8


"""爬取纳斯达克股票数据"""
import urllib.request
import hashlib
from db.db_access import insert_hisq_data
import datetime
import os
import json

# url = 'https://www.nasdaq.com/symbol/aapl/historical#.UWdnJBDMhHk'
# url = 'https://api.nasdaq.com/api/quote/AAPL/historical?assetclass=stocks&fromdate=2019-10-14&limit=18&todate=2019-11-14'
curr_time = datetime.datetime.now()
shijian = curr_time - datetime.timedelta(days=31)
url = 'https://api.nasdaq.com/api/quote/AAPL/historical?assetclass=stocks&fromdate={0}&limit=18&todate={1}'.format(shijian.date(), curr_time.date())


def validateUpdate(html):
    """验证数据是否更新，更新返回True，未更新返回False"""
    # 创建md5对象
    md5obj = hashlib.md5()
    md5obj.update(html.encode(encoding='utf-8'))  # update()方法对传入的数据进行md5运算
    md5code = md5obj.hexdigest()    # hexdigest()方法返回一个十六字节的md5码
    print(md5code)

    old_md5code = ''
    f_name = 'md5.txt'

    if os.path.exists(f_name):   #如果文件存在则读取文件内容
        with open(f_name, 'r', encoding='utf-8') as f:
            old_md5code = f.read()

    if md5code == old_md5code:
        print('数据没有更新')
        return False
    else:
        # 把新的md5码写入文件
        with open(f_name, 'w', encoding='utf-8') as f:
            f.write(md5code)
        print('数据更新')
        return True


req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    date = response.read()
    html = date.decode()
    if validateUpdate(html):  # 调用md5方法验证是否更新
        d = json.loads(html)  # 使用json解析数据
        stock = d["data"]["tradesTable"]["rows"]
        print(stock)

        
        data = []
        df = '%m/%d/%Y'
        for i in stock:
            # print(i)
            fields = {}
            fields['Date'] = datetime.datetime.strptime(i['date'], df)
            fields['Open'] = float(i['open'].replace('$', ''))
            fields['High'] = float(i['high'].replace('$', ''))
            fields['Low'] = float(i['low'].replace('$', ''))
            fields['Close'] = float(i['close'].replace('$', ''))
            fields['Volume'] = int(i['volume'].replace(',', ''))
            # print(fields)
            data.append(fields)

        print(data)
        for row in data:
            row['Symbol'] = 'AAPL'
            print(row)
            insert_hisq_data(row)







