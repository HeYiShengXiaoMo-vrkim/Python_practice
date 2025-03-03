import random
import matplotlib.pyplot as plt

# 设置字体
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 更改默认字体为 "SimHei"
plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题
font = {'family': 'SimHei', 'size': 20, 'weight': 'bold'}
plt.rc('font', family="SimHei", weight="bold")

# 设置图形大小
photo = plt.figure(figsize=(44,22),dpi=120)

# 设置横坐标
a = [random.randint(20, 35) for i in range(120)]
b = [a[i] + random.uniform(-3, 3) for i in range(120)]  # 添加随机波动
x = range(0, 120, 1)  # 当a和x大小不一样时会报错

# 将x轴的刻度标签设置为中文
_x = list(x)
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]  # 将11点的刻度标签添加到列表中
# rotation=45 旋转45度，fontsize=20 字体大小
plt.xticks(_x[::3], _xtick_labels[::3], rotation=45, fontsize=20)

# 设置 y 轴的范围
_y = list(a)
_ytrick_labels = [i for i in range(20, 36)]
plt.yticks(_ytrick_labels)

# 设置标题和坐标轴标签
plt.title("10点到12点气温变化折线图", fontsize=20)
plt.xlabel('时间 单位(min)', fontsize=20)
plt.ylabel('温度 单位(℃)', fontsize=20)

# 绘制折线图
plt.grid(alpha=0.56)  # 添加网格线,alpha设置透明度
# 对于linestyle，supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

plt.plot(x, a, label="平均气温", color='g', linestyle='--', linewidth=5, alpha=0.75)  # 绘制第一个折线图
plt.plot(x, b, label="随机波动")  # 绘制第二个折线图

# 添加图例
plt.legend(loc="best", fontsize=20)  # loc="best" 自动选择最佳位置
# 绘制折线统计图1.py
# 保存图片并展示
plt.savefig("10点后每分钟气温.svg")  # 保存要在show前面
plt.show()
