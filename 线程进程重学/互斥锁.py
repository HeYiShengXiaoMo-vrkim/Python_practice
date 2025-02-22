import threading
import time

"""
# 互斥锁
- threading.lock() 实体，创建一个锁对象
- lock.acquire()上锁
- lock.release()解锁
"""

# 创建一个锁对象
lock1 = threading.Lock()
lock2 = threading.Lock()
lock3 = threading.Lock()
lock1.acquire()
lock2.acquire()

class Task1(threading.Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print("----Task1----")
                time.sleep(0.5)
                lock1.release()

class Task2(threading.Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print("----Task2----")
                time.sleep(0.5)
                lock2.release()

class Task3(threading.Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print("----Task3----")
                time.sleep(0.5)
                lock3.release()

if __name__ == '__main__':
    t1 = Task1()
    t2 = Task2()
    t3 = Task3()
    t1.start()
    t2.start()
    t3.start()
