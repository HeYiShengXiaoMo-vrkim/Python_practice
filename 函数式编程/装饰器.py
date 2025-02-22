# 装饰器
import time
def writeLog(func):
    try:
        f = open('log.txt', 'a')
        f.write(func.__name__)
        f.write('\t')
        f.write(time.asctime())
        f.write('\n')
    except Exception as e:
        print(e)
    finally:
        f.close()
# 不修改源代码的基础上，添加日志工能
def func_out(func):
    def func_in():
        # 调用添加日志的方法
        writeLog(func)
        func()
    return func_in
@func_out
def fun1():
    print('fun1')
@func_out
def fun2():
    print('fun2')
fun1()
fun2()

def fun_out(func):
    def func_in(x, y):
        func(x,y)
    return fun_out
@fun_out
def test(a, b):
    print(a, b)
test(10, 20)