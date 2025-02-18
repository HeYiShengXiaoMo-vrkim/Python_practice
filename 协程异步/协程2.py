import asyncio
import time

"""
- await asyncio.gather(*tasks) 是一个协程函数，用于并发地运行 tasks 列表中的所有异步任务，并等待这些任务完成。asyncio.gather() 是一个协程函数，它会阻塞当前协程，直到所有传入的任务（tasks 列表中的 Future 或 Task 对象）完成或者达到指定的超时时间。
- await asyncio.wait(tasks) 和 await asyncio.gather(*tasks) 的区别在于，asyncio.wait() 函数返回两个集合：dones 和 pending。dones 集合包含已经完成的任务，pending 集合包含未完成的任务。而 asyncio.gather() 函数返回一个列表，其中包含所有任务的结果。
- asyncio.as_completed(tasks): # 处理一组异步任务。这个函数会返回一个迭代器，迭代器会按照任务完成的顺序产生结果asyncio.as_completed 已经是一种高效处理异步任务的方式，它能让我们在任务完成后立即处理结果，无需等待所有任务都完成

"""

"""
# 8. Python实现并发
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

"""
9. Python异步任务并发执行及结果收集示例代码
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
    dones, pending = await asyncio.wait(tasks) # 这行代码的主要功能是并发地运行 tasks 列表中的所有异步任务，并等待这些任务完成。asyncio.wait 是一个协程函数，它会阻塞当前协程，直到所有传入的任务（tasks 列表中的 Future 或 Task 对象）完成或者达到指定的超时时间。
    for task in dones:
        print('Task ret: ', task.result())
start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print('TIME: ', now() - start)
"""

"""
9. asyncio.gather()创建协程对象
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
    # 加 * 对task进行解包操作，* 会把 tasks 列表里的每个元素都解包出来，作为独立的参数传递给 asyncio.gather 函数。
    results = await asyncio.gather(*tasks) # 这里使用了 asyncio.gather() 函数来并发地运行 tasks 列表中的所有异步任务，并等待这些任务完成。asyncio.gather() 是一个协程函数，它会阻塞当前协程，直到所有传入的任务（tasks 列表中的 Future 或 Task 对象）完成或者达到指定的超时时间。
    for task in results:
        print('Task ret: ', task.result())
start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print('TIME: ', now() - start)
"""

"""
10. 使用asyncio.as_completed()函数
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
    for task in asyncio.as_completed(tasks): # NEW 处理一组异步任务。这个函数会返回一个迭代器，迭代器会按照任务完成的顺序产生结果
        result = await task # 使用 await 关键字等待这个已完成的任务返回结果，并将结果赋值给 result 变量
        print('Task ret: ', result)
        
start = now()
loop = asyncio.get_event_loop()
done = loop.run_until_complete(main())
print('TIME: ', now() - start)
"""

"""
11. task的列表封装在main函数中,协程停止

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
    dones, pending = await asyncio.wait(tasks) # 这行代码的主要功能是并发地运行 tasks 列表中的所有异步任务，并等待这些任务完成。asyncio.wait 是一个协程函数，它会阻塞当前协程，直到所有传入的任务（tasks 列表中的 Future 或 Task 对象）完成或者达到指定的超时时间。
    for task in dones:
        print('Task ret: ', task.result())
start = now()
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(main())
try:
    loop.run_until_complete(task)
except  KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())
    print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()