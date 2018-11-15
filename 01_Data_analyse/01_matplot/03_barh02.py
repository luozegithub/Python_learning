from matplotlib import pyplot as plt
font = {'family': 'LiSu',
        'weight': 'bold',
        'size': '16'}
plt.rc('font', **font)  # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）

plt.figure(figsize=(20,8),dpi=80)

a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_14 = [2358,399,2358,362]
b_15 = [12357,156,2045,168]
b_16 = [15746,312,4497,319]
bar_width = 0.2
x_14=range(len(a))
x_15=[i+bar_width for i in x_14]
x_16=[i+bar_width for i in x_15]


plt.barh(x_14,b_14,bar_width,label="9月14日")
plt.barh(x_15,b_15,bar_width,label="9月15日")
plt.barh(x_16,b_16,bar_width,label="9月16日")

plt.yticks(range(len(a)),a)
plt.legend()
plt.grid()
plt.show()