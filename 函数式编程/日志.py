import time
def writeLog(func):
    try:
        f = open('log.txt','a')
        f.write(func.__name__)
        f.write('\t')
        f.write(time.asctime())
        f.write('\n')
    except Exception as e:
        print(e.args)
    finally:
        f.close()
def func1():
    writeLog(func1)
    print('功能1')
def func2():
    writeLog(func2)
    print('功能2')
func1()
func2()