# _*_ coding=utf-8 _*_


import pymysql

# 1连接
db = pymysql.connect(host='localhost', user='root', password='123', port=3306, db='spiders')
cursor = db.cursor()
# cursor.execute('select version()')
# data = cursor.fetchone()
# print('Version:',data)
# cursor.execute('create database spiders default character set utf8')
# cursor.execute('SHOW DATABASES')
# cursor.execute('USE spiders')
# data2 = cursor.fetchall()
# print(data2)
# cursor.close()

# 2创建表
# cursor.execute('USE spiders')
# sql = """CREATE TABLE students(id VARCHAR(255),name VARCHAR(255) NOT NULL ,age INT NOT NULL ,PRIMARY KEY(id))"""
# cursor.execute(sql)

# 3插入数据
# sid = '2001'
# user = 'Rain'
# age = 20
#
# sql = 'INSERT INTO students(sid,name,age) VALUES(%s,%s,%s)'
# try:
#     cursor.execute(sql, (sid, user, age))
#     db.commit()
# except:
#     db.rollback()

# 4动态插入数据（推荐）
# data = {
#     'sid': "2002",
#     'name': "Alex",
#     'age': 22
# }
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s'] * len(data))
# print(','.join(['%s']*3))
# print(data.keys())
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
# try:
#     if cursor.execute(sql,tuple(data.values())):
#         print('successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()

# 5更新数据：主键存在则更新，主键不存在则插入
# data = {
#     'sid': '2001',
#     'name': 'Bob',
#     'age': 25
# }
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s'] * len(data))
# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
#                                                                                      values=values)
# update = ','.join([' {key}=%s '.format(key=key) for key in data])  # 注意key左右需要有空格来隔开update
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values()) * 2):   # 这里元祖变成双倍
#         print('successful')
#         db.commit()
# except Exception as e:
#     print('failed：', e)
#     db.rollback()

# 6查询数据
sql = 'select * from students where age>20'
try:
    cursor.execute(sql)
    print('count:', cursor.rowcount)
    one = cursor.fetchone()
    print('one:', one)
    # 回在游标当前位置向后匹配所有，上面调用过fetchone，所有这次匹配到剩下的2条数据
    results = cursor.fetchall()
    print(results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except Exception as e:
    print("Failed:", e)

# 循环获取所有数据，而不是一次性取出所有的数据
res = cursor.fetchone()
while res:
    print('Res:', res)
    res = cursor.fetchone()

# 7删除数据，修改数据的操作都需要使用commit()进行生效
table = 'students'
condition = 'age < 25'
sql2 = 'delete from {table} where {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql2)
    db.commit()
except Exception as e:
    print('Error', e)
    db.rollback()
