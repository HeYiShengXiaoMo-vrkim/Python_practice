"""
桌面数据库SQLite     关系型数据库MySQL

"""

import sqlite3
# 创建一个数据库
con = sqlite3.connect('sqlite.db')
# 创建一个游标
cur = con.cursor()
# SQL语句创建表
sql2 = 'create table t_person(pno INTEGER PRIMARY KEY AUTOINCREMENT, pname varchar(30) NOT NULL, age INTEGER NOT NULL, sex varchar(10) NOT NULL, birthday DATE NOT NULL, address varchar(100))'

# 1. 这是一个建表过程
try:
    cur.execute(sql2)
except Exception as e:
    print(e)
    print('建表失败')

