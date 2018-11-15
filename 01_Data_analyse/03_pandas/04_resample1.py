# 911数据中不同月份电话次数
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
font = {
    'family':'LiSu',
    'weight':'bold',
    'size':'15'
}
plt.rc('font',**font)
"""
    重采样（resample），从一个频率转换为另一个频率
    降采样，升采样
"""
df = pd.read_csv('../data/911.csv')
# print(df.info())
# print(df['timeStamp'])
"""
    将时间字符串类型转换为我们timeStamp类型，
    同时设置为索引
    方便我们df.resample('M')
"""
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
# inplace 原地进行修改
df.set_index('timeStamp', inplace=True)
# .count计算完成后，我们选取一列没有缺失的即可
count_by_month = df.resample('M').count()['title']
print(count_by_month)

_x = count_by_month.index
_y = count_by_month.values

_x = [i.strftime('%Y-%m-%d') for i in _x]
plt.figure(figsize=(20,12),dpi=80)
plt.plot(range(len(_x)),_y,label='911数据中不同月份电话次数')
plt.xticks(range(len(_x)),_x,rotation = 45)
plt.grid()
plt.legend()
plt.show()

