import sqlite3

con = sqlite3.connect('sqlite.db')
cur = con.cursor()

def deleteData(idnumber):
    delete_data = 'delete from t_person where pno = ?'
    try:
        cur.execute(delete_data, [idnumber])
        con.commit()
        print("删除成功")
        return True
    except Exception as e:
        print(e)
        con.rollback()
        return False
    finally:
        # 关闭游标
        cur.close()
        con.close()

if __name__ == '__main__':
    deleteData(2)