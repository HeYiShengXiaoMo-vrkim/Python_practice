import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题
font = {'family': 'SimHei', 'size': 20, 'weight': 'bold'}
plt.rc('font', family="SimHei", weight="bold")  # 设置全局字体为黑体

#  设置坐标轴样例
a = ['2017', '2018', '2019', '2020', '2021']
b_1 = [100, 200, 300, 400, 500]
b_2 = [50, 150, 250, 350, 450]
b_3 = [20, 120, 220, 320, 420]

# 设置图形大小
plt.figure(figsize=(20, 6), dpi=80)

# 对于多个条形，我们需要将其进行偏转
x_2 = list(range(len(a)))
x_3 = [i + 0.2 for i in x_2]
x_1 = [i - 0.2 for i in x_2]

# 设置图形标题
plt.bar(x_1, b_1, width=0.2, label='2017年')
plt.bar(x_2, b_2, width=0.2, label='2018年')
plt.bar(x_3, b_3, width=0.2, label='2019年')

plt.xticks(x_2,a)
plt.title('2017-2021年销量对比图')

plt.xlabel('年份(年)')
plt.ylabel('销量(万件)')
plt.legend(loc='upper left')
plt.show()
