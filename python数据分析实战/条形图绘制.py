import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题
font = {'family': 'SimHei', 'size': 20, 'weight': 'bold'}
plt.rc('font', family="SimHei", weight="bold")

# 设置数据
a = ['2019年\n', '2020年\n', '2021年', '2022年']
b = [10, 20, 30, 40]

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

#  plt.bar(a, b, color='red', width=0.5)
plt.xlabel('年份 单位(年)')
plt.ylabel('销量 单位(万件)')
plt.title('某品牌手机销量统计')
# 竖着的条形图这么玩
plt.bar(range(len(a)), b, color='red', width=0.3)
# 横着的条形图这么玩
#plt.barh(range(len(a)), b, color='red', height=0.3)
plt.xticks(range(len(a)), a, rotation=45)
plt.show()

