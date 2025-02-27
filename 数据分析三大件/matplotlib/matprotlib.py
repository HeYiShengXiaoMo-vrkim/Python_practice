import matplotlib.pyplot as plt
import numpy as np
# 三天中三部电影的票房变化
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
real_names = ['千与千寻', '玩具总动员', '黑衣人']
real_num1 = [5453, 7548, 6578]
real_num2 = [1842, 1935, 2198]
real_num3 = [1080, 2142, 985]
# 生成x 第一天 第二天 第三天
x = np.arange(len(real_names))
x_labels = ['第{}天'.format(i+1) for i in range(len(real_names))]
# 绘制柱形图 设置柱的宽度
width = 0.3
plt.bar(x, real_num1, color='g', width=width, label=real_names[0])
plt.bar([i+width for i in x], real_num2, color='r', width=width, label=real_names[1])
plt.bar([i+2*width for i in x], real_num3, color='b', width=width, label=real_names[2])
# 修改x坐标
plt.xticks([i+width for i in x], x_labels)
# 添加图例
plt.legend(loc='upper right')
# 添加标题
plt.title('三天的票房数')
plt.savefig('photo.jpg')
plt.show()