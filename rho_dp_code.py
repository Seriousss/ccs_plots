import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 定义参数
a = 0.14
b = 0.457
mu = 1.2
rho = 0.294
# 定义横坐标范围
x = np.linspace(1, 4, 300)
y = np.linspace(0, 3, 300)
# 计算纵坐标值
y_orange = 1 - b - a * x
y_blue = (norm.cdf(-(np.log(x) / mu) + mu / 2)) - (x * norm.cdf(-(np.log(x) / mu) - mu / 2))
y_red = 1 / (rho*(x ** 3))

# 绘图
plt.plot(x, y_orange, color='orange', label='Orange Line', linewidth=2)
plt.plot(x, y_blue, color='blue', label='Blue Line', linewidth=2)
plt.plot(x, y_red, color='red', label='Red Line', linewidth=2)

# 添加标题和图例
# plt.title('Plot of Three Lines')


# 设置坐标轴范围
plt.xlim(1, 4)
plt.ylim(0, 0.45)

# 显示图形
# plt.show()
plt.savefig('plot.svg', format='svg')

