import sqlite3

con = sqlite3.connect('sqlite.db')
cur = con.cursor()

def changeData():
    try:
        # 执行sql创建表
        updateData = 'update t_person set pname=? where pno=?'
        cur.execute(updateData,('小张', 1)) # 修改第一个人的名字
        # 提交事物
        con.commit()
        print('修改成功')
    except Exception as e:
        print(e)
        print("修改失败")
        con.rollback()
    finally:
        if con:
            cur.close()
            con.close()

if __name__ == '__main__':
    changeData()