import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
#  设置字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题
font = {'family': 'SimHei', 'size': 20, 'weight': 'bold'}
plt.rc('font', family="SimHei", weight="bold")

plt.style.use('_mpl-gallery')

# Make data
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

# 添加轴标签和标题
ax.set_xlabel('X 轴', fontsize=12)
ax.set_ylabel('Y 轴', fontsize=12)
ax.set_zlabel('Z 轴 (sin(R))', fontsize=12)
ax.set_title('3D 正弦波形图', fontsize=14, fontweight='bold')

# 设置更好的观察角度
ax.view_init(elev=30, azim=45)

# 添加颜色条
mappable = ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues, alpha=0.8)
plt.colorbar(mappable, shrink=0.5, aspect=10)
plt.show()
# 保存图像
plt.savefig('3d_waveform.png', dpi=300)