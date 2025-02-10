import time
import threading

# 3. 线程之间共享全局变量
globalNumber = 10

# 4. 使用互斥锁规范化管理全局数据
lock = threading.Lock()

# 5. 通过local变量将全局变量私有化
local = threading.local()

def func1(name, nowtime):
    global globalNumber
    print("{0}函数开始执行,时间{1}".format(name, nowtime))
    time.sleep(1)
    print("{}函数执行完毕".format(name))

def func2(name, nowtime):
    global globalNumber
    print("{0}函数开始执行,时间{1}".format(name, nowtime))
    time.sleep(1)
    print("{}函数执行完毕".format(name))

def func3(name, nowtime):
    global globalNumber
    """
    在两个线程上都调用上锁的办法，则这两个线程会先后上锁，如果一方上锁，
    另一方就只能等待先上锁的线程运行结束后继续。
    ！-- 小心死锁 -- ！ 
    """
    lock.acquire()  # 上锁
    for i in range(100000):
        globalNumber += 1
    lock.release()  # 解锁
    print("{}函数执行完毕".format(name))
    print("globalNumber的值为：", globalNumber)

class MyThread(threading.Thread):
    def __init__(self, name, nowtime):
        super().__init__()
        self.name = name
        self.nowtime = nowtime
    def run(self):
        print("{0}函数开始执行,时间{1}".format(self.name, self.nowtime))
        time.sleep(1)
        print("{}函数执行完毕".format(self.name))

def process_student():
    # 获取当前线程关联的name
    student_name = local.name
    print("线程名称为:%s, 学生姓名为:%s" % (threading.current_thread().name, student_name))

def process_thread(name):
    # 绑定ThreadLocal的name
    local.name = name
    process_student()

if __name__ == '__main__':
    # 1. 正常调用
    t1 = threading.Thread(target=func1, args=('thread-1', time.ctime()))
    t2 = threading.Thread(target=func2, args=('thread-2', time.ctime()))
    # 2. 使用继承类调用
    t3 = MyThread('thread-3', time.ctime())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("end")

    t3 = threading.Thread(target=process_thread, args=('张三',), name='Thread-A')
    t4 = threading.Thread(target=process_thread, args=('李四',), name='Thread-B')
    t3.start()
    t4.start()
    t3.join()
    t4.join()