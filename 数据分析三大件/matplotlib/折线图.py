from matplotlib import pyplot as plt
# 设置图片大小
photo = plt.figure(figsize=(10, 6), dpi=80)  # 创建画布

# 设置x轴和y轴数据
x = range(2, 26, 2)  # 生成x轴数据
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]  # 生成y轴数据
plt.title('Scores of Math')  # 设置标题
plt.xticks(x)  # 设置x轴刻度 可以使用plt.xticks(range(2, 26, 2))来设置刻度，利用步长设置稀疏程度
plt.yticks(y)  # 设置y轴刻度

plt.plot(x, y)  # 绘制折线图
plt.savefig('photo.svg')  # 保存图片
plt.show()  # 显示图形