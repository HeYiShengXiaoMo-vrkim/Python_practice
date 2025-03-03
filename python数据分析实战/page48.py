from matplotlib import pyplot as plt

plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题
font = {'family': 'SimHei', 'size': 20, 'weight': 'bold'}
plt.rc('font', family="SimHei", weight="bold")  # 设置全局字体为黑体

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]

plt.bar(range(len(interval)), quantity, width=1) # 绘制柱状图

# 设置x轴刻度
_x = [i-0.5 for i in range(len(interval))]
_x_interval = interval
plt.xticks(_x, _x_interval)


plt.xlabel('时间间隔（天）')  # 设置x轴标签
plt.ylabel('数量')  # 设置y轴标签
plt.title('客户流失数量与时间间隔的关系')  # 设置图表标题
plt.figure(figsize=(20, 6), dpi=80)  # 设置图表大小
plt.show()  # 显示图表