# 1. 绝对值
print('-10的绝对值是: ',abs(-10))

# 2. map映射
def f(x):
    return x * x
"""
# 第一种表示方式
L = []
for i in range(10):
    L.append(f(i)) # 这里将f函数作用到循环的每一个i上并加入到L列表中
print(L)

# 第二种表示方式
L = map(f, range(10))
print(list(L))

# 第三种表示方式
L = map(lambda X: x * x,range(10))
print(list(L))
"""

"""
# 将列表中元素全部转化为字符串
L = list(map(str, [1,2,3,4,5,6,7,8,9]))
print(L)
"""

# 3. reduce: 实现累加
from functools import reduce
def add(x, y):
    return x + y
sum = reduce(add, range(10))
print(sum) # 打印0-9的累加和

# 4. filter : 过滤列表
def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(10)))
print(L) # 打印0-9的奇数列表

# 5. stored : 排序
storer1 = sorted([1, 2, 3,4,5,6,7,8,9], key=abs, reverse=True) # 参数的意思是将列表中的元素按照绝对值进行排序,并且倒序输出
# key = lambda x:x.age可以对目标进行age的排序
print(storer1)

# 6. 闭包
"""
def func_out(num1):
    def func_in(num2):
        return num1 / num2 # 这里的num1是10，num2是20
    return func_in
f = func_out(10)
result = f(20)
print(result) # 闭包的意思是将函数作为返回值返回,并且在函数中可以使用外部的变量
"""
# 使用闭包求两点之间的距离
import math
def getDisOut(x1, y1):
    def getDisIn(x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return getDisIn
getDisIn = getDisOut(1,2)
result = getDisIn(2,5)
print('(1,2)到(2,5)的距离是',result)