from matplotlib import pyplot as plt

font = {'family': 'LiSu',
        'weight': 'bold',
        'size': '16'}
plt.rc('font', **font)  # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）

plt.figure(figsize=(20, 8), dpi=80)
interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]

plt.bar(range(len(quantity)), quantity, width=1)
# 设置x轴刻度
_x = [i-0.5 for i in range(13)]
_xtick_labels = interval+[150]
plt.xticks(_x, _xtick_labels)
plt.grid()
plt.show()
