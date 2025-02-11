import sqlite3

# 创建对数据库的连接
con = sqlite3.connect('sqlite.db')
# 获取游标
cur = con.cursor()

# 2. 插入数据方法（一条）
def insert(name,age,sex,birthday,address):
    try:
        # 执行sql创建表
        sql2 = 'insert into t_person(pname, age, sex, birthday, address) values(?, ?, ?, ?, ?)'
        cur.execute(sql2, (name, age, sex, birthday, address))
        con.commit()
        print('插入成功')
        return True
    except Exception as e:
        print(e)
        print('插入失败')
        con.rollback() # 回滚, 撤销上一次操作
        return False
    """
        finally:
        # 关闭游标
        cur.close()
        # 关闭连接
        con.close()
    """
def multiInsert():
    try:
        # 执行sql创建表
        sql2 = 'insert into t_person(pname, age, sex, birthday, address) values(?,?,?,?,?)'
        cur.executemany(sql2, [('张三', 18, '男', '2000-01-01', '北京'), ('李四', 19, '女', '2001-01-01', '上海'), ('王五', 20, '男', '2002-01-01', '广州'), ('赵六', 21, '女', '2003-01-01', '深圳'), ('钱七', 22, '男', '2004-01-01', '杭州'), ('孙八', 23, '女', '2005-01-01', '武汉'), ('周九', 24, '男', '2006-01-01', '南京'), ('吴十', 25, '女', '2007-01-01', '天津'), ('郑十一', 26, '男', '2008-01-01', '重庆'), ('冯十二', 27, '女', '2009-01-01', '西安'), ('陈十三', 28, '男', '2010-01-01', '成都'), ])
        con.commit()
        print('插入成功')
        return True
    except Exception as e:
        print(e)
        print('插入失败')
        con.rollback() # 回滚, 撤销上一次操作
        return False
    """
        finally:
        # 关闭游标
        cur.close()
        con.close()
    """
if __name__ == '__main__':
    # insert('张三', 18, '男', '2000-01-01', '北京')
    multiInsert()