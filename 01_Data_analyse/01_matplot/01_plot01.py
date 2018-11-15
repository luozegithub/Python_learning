import random

from matplotlib import pyplot as plt

font = {'family': 'LiSu',
        'weight': 'bold',
        'size': '16'}
plt.rc('font', **font)  # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）

plt.figure(figsize=(20, 8), dpi=80)

random.seed(1)
x = range(120)
y = [random.randint(20, 35) for i in range(120)]

plt.xlabel('时间')
plt.ylabel('温度 单位（摄氏度）')
plt.title('10点到12点每分钟的气温变化情况')
plt.plot(x, y)
# alpha 透明度 0-1
plt.grid(alpha=0.4)

_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(x[::10], _xtick_labels[::10], rotation=45)
plt.yticks(range(min(y), max(y)))
plt.savefig('./b.svg')
plt.show()
