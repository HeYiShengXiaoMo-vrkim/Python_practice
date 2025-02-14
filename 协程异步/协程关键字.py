"""
协程常用于IO密集型的任务,协程是单线程,所以不需要考虑线程安全问题
协程的本质是单线程下,由用户自己控制一个任务遇到IO阻塞了就切换另外一个任务去执行,以此来提升效率
协程的本质是通过单线程来实现多任务的切换+保存状态
"""

"""
1. 理解yield的工作原理
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo() # 先得到一个生成器g,此时函数并没有执行
print(next(g)) # 直到调用next(g)，foo函数才开始执行，遇到yield时，foo函数就返回一个4，然后“暂停”
print("*"*20)
print(next(g)) # 从刚才的next(g)的位置开始执行，此时执行赋值操作,但是右边已经没有值了(yeild返回了),所以赋值为none
"""

"""
2. yield简单实现协程(A和B交替执行)
import time
def A():
    while True:
        print("starting...")
        print("Task A")
        yield
        time.sleep(2)
def B(c):
    while True:
        print("starting...")
        print("Task B")
        c.__next__()  # 这个和next(c)是一样的
        time.sleep(2)

if __name__ == '__main__':
    a = A()
    B(a)
"""

"""
3. send()和next()的区别
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo() # 先得到一个生成器g,此时函数并没有执行
print(next(g)) # 直到调用next(g)，foo函数才开始执行，遇到yield时，foo函数就返回一个4，然后“暂停”
print("*"*20)
print(g.send(g)) # send()将上一次yield返回值4，赋值给res，然后继续执行，遇到yield时，foo函数就返回一个4，然后“暂停”，这样就解决了下面打印函数打印的值为none的问题
"""

"""
# 创建task
import time, asyncio
now = lambda : time.time()
# 通过async关键字定义一个协程,该协程不能直接运行,需要将协程加入到事件循环中
async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x) # 异步调用asyncio.sleep(X)
    return 'Done after {}s'.format(x)
# 得到当前时间
start = now()
#得到一个协程对象
coroutine = do_some_work(2)
#创建一个事件循环对象
loop = asyncio.get_event_loop() # 创建事件循环
#将协程加入到事件循环中,并启动事件循环
loop.run_until_complete(coroutine) # 将协程对象加入到事件循环中
print('TIME: ', now() - start)
"""

# 绑定回调
import time, asyncio
now = lambda : time.time()
# 通过async关键字定义一个协程,该协程不能直接运行,需要将协程加入到事件循环中
async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)
def callback(future):
    print('callback future:', future.result())
# 得到当前时间
start = now()
# 得到一个协程对象
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine, loop=loop)
task.add_done_callback(callback)
loop.run_until_complete(task)
print('TIME: ', now() - start)