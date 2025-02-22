""""
import queue
from multiprocessing import Queue

q = Queue(3)

try:
    q.put("消息1", timeout=1)
    q.put("消息2", timeout=1)
    q.put("消息3", timeout=1)
except queue.Full:
    print("队列已满，无法添加更多消息")
"""

"""
进程 
- 进程 = multiprocessing。Process(target, args, kwargs, name) 创建进程实体对象
- class name(进程) 创建进程类
- 进程.start() 启动进程
- 进程.join(timeout) 等待进程结束,以及设置超时时间
"""

# 1.进程的创建使用multiprocessing模块，支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。
import multiprocessing as mp
import time
# 5.使用类创建进程
class Worker(mp.Process):
    def __init__(self, interval):
        mp.Process.__init__(self)
        self.interval = interval
    def run(self):
        print("子进程开始执行")
        time.sleep(self.interval)
        print("子进程结束执行")

def printName(name, age, times, **kwargs):
    for i in range(times):
        print("进程开始的时间：{}", time.ctime())
        print("My name is {name} and I am {age} years old.".format(name=name, age=age))
        print(kwargs)
        time.sleep(0.5)

if __name__ == '__main__':
    print("父进程运行")
    # 2.使用multiprocessing头文件的Process类创建进程对象
    p = mp.Process(target=printName, args=("小张", 14, 10), kwargs={'m':3}, name="fun1") # 这里target后面直接函数名就好了，不用加括号,args后面要加逗号
    p2 = Worker(2)
    print('子进程开始运行')
    p.start()
    p2.start()
    p2.join()
    p.join(3) # 3. 等待子进程结束(括号里的是超时退出)
    # 4.获取进程的id和名称
    print('子进程id:', p.pid, p2.pid, end='\n')
    print('子进程名称:', p.name, p2.name)
    print('子进程是否存活:', p.is_alive(), p2.is_alive())

    print("进程结束")
