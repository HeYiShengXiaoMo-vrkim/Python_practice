# 导入sqlite3模块
import sqlite3

from sympy.simplify.hyperexpand import try_lerchphi

# 连接到数据库
con = sqlite3.connect('sqlite.db')
# 获取游标
cur = con.cursor()

# 1. 查询所有数据
def query_all():
    # 执行sql查询语句
    sql = 'select * from t_person'
    cur.execute(sql)
    try:
        person_list = cur.fetchall()
        # print(person_list)
        # 遍历
        for person in person_list:
            print(person)
    except Exception as e:
        print(e)
        print('查询失败')

# 2. 查询一条数据
def query_one(preson_name):
    # 执行sql创建表
    sql = 'select * from t_person where pname = ?'
    try:
        cur.execute(sql, [preson_name])
        # 获取一条数据
        person = cur.fetchone()
        print(person)
    except Exception as e:
        print(e)
        print('查询失败')

if __name__ == '__main__':
    query_all()
    query_one('孙八')