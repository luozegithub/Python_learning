from matplotlib import pyplot as plt

font = {'family': 'LiSu',
        'weight': 'bold',
        'size': '16'}
plt.rc('font', **font)  # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）
plt.figure(figsize=(20, 8), dpi=80)
x = range(11, 31)
y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

plt.plot(x, y_1, label='自己', color='cyan')
plt.plot(x, y_2, label='同学', color='r')
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_labels)
plt.grid(0.4)
plt.legend(loc='upper left')
plt.show()
