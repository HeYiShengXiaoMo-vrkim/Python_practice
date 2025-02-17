import asyncio
import time

from docutils.nodes import pending

"""
# Python实现并发
now = lambda : time.time()
async def do_some_works(x):
    print("waiting :", x)
    await asyncio.sleep(x)
    return 'Done after {} seconds'.format(x)

start = now()
# 1. 创建task
coroutine1 = do_some_works(1)
coroutine2 = do_some_works(2)
coroutine3 = do_some_works(3)
tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]
# 2. 创建循环
loop = asyncio.get_event_loop()
# 3. 将task加入到循环中
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task ret: ', task.result())
print('TIME: ', now() - start)
"""
now = lambda : time.time()
async def do_some_works(x):
    print("waiting :", x)
    await asyncio.sleep(x)
    return 'Done after {} seconds'.format(x)
async def main():
    coroutine1 = do_some_works(1)
    coroutine2 = do_some_works(2)
    coroutine3 = do_some_works(3)
    tasks =[
        asyncio.ensure_future(coroutine1), # 这里是将coroutine1封装成一个future对象,并将其加入到事件循环中等待执行,future对象代表一个异步操作的结果,可以用来跟踪携程的执行状态
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    dones, pending = await asyncio.wait(tasks) #这行代码的主要功能是并发地运行 tasks 列表中的所有异步任务，并等待这些任务完成。asyncio.wait 是一个协程函数，它会阻塞当前协程，直到所有传入的任务（tasks 列表中的 Future 或 Task 对象）完成或者达到指定的超时时间。
    for task in dones:
        print('Task ret: ', task.result())
start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print('TIME: ', now() - start)