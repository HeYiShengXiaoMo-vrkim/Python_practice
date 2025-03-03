import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题
font = {'family': 'SimHei', 'size': 20 , 'weight': 'bold'}
plt.rc('font',family = "SimHei", weight = "bold")

a = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y = [1, 3, 2, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 0]

x = range(11,31)  # 这里如果x轴的刻度是11到30，那么a的长度应该是20
plt.figure(figsize=(20, 12), dpi=120)   # 设置图表大小

plt.xticks(x)   # 设置x轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_labels)   # 设置x轴刻度标签

plt.title('交女朋友实验')   # 设置图表标题
plt.xlabel('岁数 单位(岁)')   # 设置x轴标签
plt.ylabel('女朋友数量 单位(个)')   # 设置y轴标签
plt.plot(x, a, label = "库课")   # 绘制折线图
plt.plot(x, y, label = "麻瓜疼")   # 绘制折线图
plt.legend()   # 显示图例
plt.savefig('交女朋友实验.png')   # 保存图表
plt.show()   # 显示图表