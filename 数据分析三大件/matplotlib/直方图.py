# 数据分组
# 只有未经历过处理的原始数据才能画直方图
# 1. 100以内数据分5-12组，2.组数 = 极数/组距
from matplotlib import pyplot as plt
plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题
font = {'family': 'SimHei', 'size': 20, 'weight': 'bold'}
plt.rc('font', family="SimHei", weight="bold")  # 设置全局字体为SimHei

a = [131, 98, 125, 131, 124, 139, 135, 128, 138, 134, 135, 136, 126, 127, 105, 134, 125, 116, 123, 119, 133, 112, 114, 122, 109, 120, 129, 126, 110, 109, 121, 122, 120, 103, 118, 112, 126, 129, 127, 105, 99, 131, 134, 124, 119, 106, 117, 127, 121, 130, 125, 126, 111, 113, 119, 120, 123, 119, 114, 122, 109, 123, 116, 111, 117, 114, 124, 119, 113, 128, 125, 120, 114, 122, 109, 123, 116, 126, 111, 113, 119, 113, 122, 120, 113, 126, 111, 110, 116, 117, 139, 112, 125, 121, 122, 113, 127, 121, 130, 119, 113, 128, 125, 120, 120, 113, 122, 109, 123, 116, 126, 116, 117]

# 计算组数
d = 9  # 组数
num_bins = (max(a) - min(a)) // d + 1# 组数 = 极数/组距
print(num_bins)
print(max(a) - min(a))
print(max(a))
plt.figure(figsize=(20, 8), dpi=80) # 设置画布大小和分辨率

# 设置x轴的刻度
plt.xticks(range(min(a), max(a) + d, d)) # range(min(a), max(a) + d, d) 生成一个从min(a)到max(a) + d的序列，步长为d

# 绘制网格
plt.grid(linestyle='--', alpha=0.5) # linestyle='--' 设置线型为虚线，alpha=0.5 设置透明度为0.5

# 绘制直方图
plt.hist(a, num_bins, density=1, facecolor="blue", edgecolor="black", alpha=0.7)
plt.show()