# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 15:33
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : 24.sqllite数据库的使用.py
# @Software: PyCharm
import sqlite3

'''
sqllite是一个小型的数据库，python3后的版本就自动支持了该数据库
'''

'''
1.在数据库中添加表
'''
# # 1.打开并创建数据库
# connect = sqlite3.connect('test.db')
# # 2.获取操作数据库的游标
# cursor = connect.cursor()
# # 3.定义sql语句
# sql = '''
# create table user
#         (id integer not null primary key autoincrement,
#          name text not null,
#          age int not null ,
#          salary real,
#          address char(50)
#         );
# '''
# # 4.执行sql语句
# cursor.execute(sql)
# # 5.提交事务
# connect.commit()
# # 6.关闭数据库
# connect.close()

'''
2.向表中添加数据
'''
# connect = sqlite3.connect('test.db')
# cursor = connect.cursor()
# sql1 = '''
# insert into user (name,age,salary,address)
# values('张三',32,25.23,'北京')
# '''
#
# sql2 = '''
# insert into user (name,age,salary,address)
# values('李四',32,25.23,'北京')
# '''
#
# cursor.execute(sql1)
# cursor.execute(sql2)
# connect.commit()
# connect.close()

'''
3.查找表中的数据
'''
# connect = sqlite3.connect('test.db')
# cursor = connect.cursor()
#
# sql = '''
# select id,name,age,salary,address from user
# '''
# result = cursor.execute(sql)
# # 输出查询的结果
# for temp in result:
#     print('id = ',temp[0])
#     print('name = ',temp[1])
#     print('age = ',temp[2])
#     print('salary = ',temp[3])
#     print('address = ',temp[4],'\n')
#
# connect.commit()
# connect.close()
