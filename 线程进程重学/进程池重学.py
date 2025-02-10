import time
import multiprocessing as mp

def func1(msg): # 进程池函数体
    print("start:", msg)
    time.sleep(3)
    print("end:", msg)

def write(q):
    for i in "abc": # 向队列中写入数据
        print("开始写入,时间为: {}".format(time.ctime()))
        q.put(i)
        time.sleep(1)

def read(q):
    for i in range(q.qsize()): # 读取队列中的数据
        print("开始读取,时间为: {}".format(time.ctime()))
        if not q.empty():
            print(q.get())
            time.sleep(1)
        else:
            print("队列为空")
            break

if __name__ == "__main__":
    # 1. 创建进程池
    pool = mp.Pool(processes = 3)
    for i in range(10):
        msg = "hello %d" %(i)
        # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        pool.apply_async(func1, (msg,))
    pool.close() # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    pool.join()

    # 2. Queue是多进程安全的队列,可以使用Queue实现多进程之间的数据传递
    q = mp.Queue(3)
    q.put("消息1")
    q.put("消息2")
    q.put("消息3")
    print(q.full())
    # 写入时需要判断消息队列是否已满
    if not q.full():
        # queue拥有两个参数,block用于标注是否处于阻塞状态，timeout用于标注阻塞状态的等待时间
        q.put("消息4", True, 2) # 当队列满时，等待2秒后再写入
    # 读取时也要先判断消息队列是否为空
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get())

    # 3.使用Queue队列实现进程间通信
    p3 = mp.Queue()
    pw = mp.Process(target=write, args=(p3,)) # args传递的p3是一个队列
    pr = mp.Process(target=read, args=(p3,)) # args传递的p3是一个队列
    # 启动进程
    pw.start()
    pr.start()
    pr.join()
    pw.join()
    print("end")