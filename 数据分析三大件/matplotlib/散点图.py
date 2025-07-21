import random

from matplotlib import pyplot as plt

#  设置字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题
font = {'family': 'SimHei', 'size': 20, 'weight': 'bold'}
plt.rc('font', family="SimHei", weight="bold")

# 读取数据
y_1 = [random.randint(10,30) for i in range(20)]  # 生成20个10到30之间的随机数
y_2 = [random.randint(5,25) for i in range(20)]  # 生成20个10到30之间的随机数
x_1 = range(1, 21)
x_2 = range(41,61)

# 设置图形大小 这里的label就是图例显示的值
plt.figure(figsize=(20,8),dpi=120)
plt.scatter(x_1, y_1, label='三月份', color='r')
plt.scatter(x_2, y_2, label='四月份', color='g')

#调整x轴和y轴的刻度
plt.title('气温变化图', fontproperties=font, fontsize=30)
plt.xlabel('日期 单位(日)')
plt.ylabel('气温 单位(℃)')
_x = list(x_1) + list(x_2)
_xticks_labels = ['3月{}日'.format(i) for i in x_1]
_xticks_labels += ['4月{}日'.format(i-40) for i in x_2]
plt.legend(loc='best', prop=font)
plt.xticks(_x[::3], _xticks_labels[::3], rotation=45, fontproperties=font)
plt.savefig('2020年3月和4月气温变化图.png')

plt.show()
