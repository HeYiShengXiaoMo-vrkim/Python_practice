"""
协程常用于IO密集型的任务,协程是单线程,所以不需要考虑线程安全问题
协程的本质是单线程下,由用户自己控制一个任务遇到IO阻塞了就切换另外一个任务去执行,以此来提升效率
协程的本质是通过单线程来实现多任务的切换+保存状态
"""

"""
- 1.yield
- 2.send()
- 3.next()
- 4.c.__next__()
- 5.await asyncio.sleep(x)
- 6.asyncio.get_event_loop()
- 7.loop.run_until_complete(coroutine)
- 8.asyncio.ensure_future(coroutine, loop=loop)
- 9.loop.create_task(coroutine)
"""

"""
1. 理解yield的工作原理
def foo():
    print("starting...")
    while True:
        res = yield 4 # 1.NEW
        print("res:",res)
g = foo() # 先得到一个生成器g,此时函数并没有执行
print(next(g)) # 直到调用next(g)，foo函数才开始执行，遇到yield时，foo函数就返回一个4，然后“暂停”
print("*"*20)
print(next(g)) # 从刚才的next(g)的位置开始执行，此时执行赋值操作,但是右边已经没有值了(yeild返回了),所以赋值为none
"""

"""
# 2. yield简单实现协程(A和B交替执行)
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
        c.__next__()  # 2.NEW 这个和next(c)是一样的
        time.sleep(2)

if __name__ == '__main__':
    a = A() # 得到一个生成器a
    B(a) # 最后a,b交替进行,先执行a,然后执行b,然后再执行a,然后再执行b,以此类推
"""


"""
# 3. send()和next()的区别
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo() # 先得到一个生成器g,此时函数并没有执行
print(next(g)) # 直到调用next(g)，foo函数才开始执行，遇到yield时，foo函数就返回一个4，然后“暂停”
print("*"*20)
print(g.send(g)) # 3.NEW send()将上一次yield返回值4，赋值给res，然后继续执行，遇到yield时，foo函数就返回一个4，然后“暂停”，这样就解决了下面打印函数打印的值为none的问题
"""

"""
# 4. 绑定回调 : 可以在异步任务执行完毕后,绑定一个回调函数,该回调函数会在异步任务执行完毕后被调用
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
# 1. 得到一个协程对象
coroutine = do_some_work(2)
# 2. 创建循环体
loop = asyncio.get_event_loop()
# 3. asyncio.ensure_future 提供了一个统一的接口，无论传入的是协程对象还是其他可等待对象（如 Future），都能正确处理。这使得代码更加简洁和易于维护。
task = asyncio.ensure_future(coroutine, loop=loop) # 封装coroutine为一个task对象，task是future子类，表示一个异步操作的结果，跟踪事件循环中被调度执行
# 4. 绑定回归函数
task.add_done_callback(callback) # 为这个task对象绑定一个回调函数，无论task对象是否被取消，都会执行回调函数
# 5. 执行循环体
loop.run_until_complete(task)
print('TIME: ', now() - start)
"""

"""
# 5. task.result(): 这里用同步的编码方式写异步,避免回调
# 当存在多个异步操作，并且一个操作依赖于另一个操作的结果时，使用回调函数会导致代码嵌套层级过深，形成所谓的“回调地狱”
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

"""
# 6. task的使用 : 没有绑定回调函数的部分
import time,asyncio

now = lambda : time.time()
async def do_some_work(x):
    print("Waiting for:", x)
    return 'Done after {}s'.format(x)

start = now()
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine) # NEW 使用 loop.create_task 可以将协程对象封装成 Task 对象，方便事件循环对其进行调度和管理，从而实现异步编程。这种方式可以提高程序的性能，特别是在处理多个 I/O 密集型任务时。
loop.run_until_complete(task)
print('Task ret: ', task.result())
print('TIME: ', now() - start)
"""

"""
# 7. 封装协程函数
import time
import asyncio
now = lambda : time.time()
async def do_some_works(x):
    print("waiting: ", x)
    await asyncio.sleep(x) # 异步调用asyncio.sleep(),相比于time.sleep(),不会阻塞主线程
    return "Done after {}s".format(x)

start = now() # 保存开始时间
coroutine = do_some_works(2) # 创建协程对象
loop = asyncio.get_event_loop() # 创建时间循环对象
task = asyncio.ensure_future(coroutine) # 将协程封装为一个task对象
loop.run_until_complete(task) # 开始循环
print("Task ret", task.result()) # 获取协程返回值
print('TIME: ', now() - start)
"""

