from matplotlib import pyplot as plt
font = {'family': 'LiSu',
        'weight': 'bold',
        'size': '16'}
plt.rc('font', **font)  # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）

plt.figure(figsize=(20,8),dpi=80)

a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊"]

b=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]

plt.barh(range(len(a)),b,0.3,color='orange',label='10月票房统计')
plt.xticks(range(60)[::5])
plt.yticks(range(len(a)),a)

plt.xlabel("票房")
plt.ylabel("电影名称")
plt.title("本月票房统计")

plt.legend()
plt.grid(0.4)
plt.show()