import matplotlib.pyplot as plt

# 假设我们有一系列的点对
x = [1, 2, 3]
y = [1, 2, 3]

# 绘制点
plt.plot(x, y, 'o-')

# 添加箭头
for i in range(len(x) - 1):
    plt.annotate("", xy=(x[i+1], y[i+1]), xytext=(x[i], y[i]),
                 arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()