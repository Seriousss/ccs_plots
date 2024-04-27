import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['axes.linewidth'] = 3

# 定义参数
a = 0.58
b = 0.19
mu = 0.63
rho = 4.1
# 定义横坐标范围
x = np.linspace(0.4, 4, 300)
y_orange = 1 - b - a * x
y_blue = (norm.cdf(-(np.log(x) / mu) + mu / 2)) - (x * norm.cdf(-(np.log(x) / mu) - mu / 2))
y_red = 1 / (rho*(x ** 3))
y_yellow = 1 / (rho*(x ** 2))
y_green = np.full_like(x, 0.03)  # 使用与 x 相同长度的数组，并填充为 0.05
fig = plt.figure(figsize=(5.5, 5.5))
# 绘图
plt.plot(x, y_orange, color='black', linewidth=3.5)
plt.plot(x, y_blue, color='blue', linewidth=3.5)
plt.plot(x, y_red, color=(1.0, 0.725, 0.173), linestyle='--', linewidth=3)

plt.plot(x, y_green, color='black', linestyle=':', linewidth=3.5)  # 添加 linestyle 参数
plt.plot(x, y_yellow, color=(1.0, 0.725, 0.173), linestyle='-.', linewidth=3.5)
# 添加标题和图例
# plt.title('Plot of Three Lines')
intersection_x = x[np.argmin(np.abs(y_yellow - y_green))]
intersection_y = y_yellow[np.argmin(np.abs(y_yellow - y_green))]
intersection_x1 = x[np.argmin(np.abs(y_blue - y_green))]
intersection_y1 = y_blue[np.argmin(np.abs(y_blue - y_green))]
intersection_x2 = x[np.argmin(np.abs(y_red - y_green))]
intersection_y2= y_red[np.argmin(np.abs(y_red - y_green))]
plt.plot(intersection_x2, intersection_y2, marker='o', markersize=6, color=(1.0, 0.725, 0.173))

# plt.plot(intersection_x2+0.3, 0.03, marker='o', markersize=6, color='black')
# plt.text(intersection_x2+0.23 , -0.018, r' $e^{\epsilon_c}$', fontsize=14,color='black')
# plt.plot([intersection_x2+0.3, intersection_x2+0.3], [0.03, -0.013], color='black', linestyle='--',linewidth=3)
# plt.text(intersection_x2-0.05 , -0.026, r' $e^{\xi_1^{*}}$', fontsize=23,color=(1.0, 0.725, 0.173),fontweight='bold',font='Times New Roman')
plt.plot([intersection_x2, intersection_x2], [intersection_y2, -0.013], color=(1.0, 0.725, 0.173), linestyle='--',linewidth=3.5)
plt.plot(intersection_x1, intersection_y1, marker='o', markersize=6, color='blue')
# plt.text(intersection_x1-0.05 , -0.026, r' $e^{\epsilon^*}$', fontsize=23,color='blue',fontweight='bold',font='Times New Roman')
plt.plot([intersection_x1, intersection_x1], [intersection_y1, -0.013], color='blue', linestyle='--',linewidth=3.5)
# 在交点处添加标注
plt.plot(intersection_x, intersection_y, marker='o', markersize=6, color=(1.0, 0.725, 0.173))
# plt.text(intersection_x-0.05 , -0.026, r' $e^{\xi_2^{*}}$', fontsize=23,color=(1.0, 0.725, 0.173),fontweight='bold',font='Times New Roman')
plt.plot([intersection_x, intersection_x], [intersection_y, -0.013], color=(1.0, 0.725, 0.173), linestyle='--',linewidth=3.5)
# plt.plot(intersection_x2+0.66, 0.03, marker='o', markersize=6, color='black')
# plt.text(intersection_x2+0.59 , -0.018, r' $e^{\epsilon_c}$', fontsize=14,color='black')
# plt.plot([intersection_x2+0.66, intersection_x2+0.66], [0.03, -0.013], color='black', linestyle='--',linewidth=3)
# linestyleplt.legend(fontsize=16)
plt.text(3.23, -0.019, r' $e^{\epsilon}$', fontsize=23,color='black',fontweight='bold')
# 设置坐标轴范围
plt.xlim(0.87, 3.2)
plt.ylim(0,0.3)
plt.ylabel(r'$\delta$', fontsize=23,fontweight='bold')
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
plt.xticks([])
plt.yticks([])
plt.tight_layout()
# 显示图形
# plt.show()
plt.savefig('plot.svg', format='svg')
