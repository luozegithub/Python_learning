#
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
font = {
    'family':'LiSu',
    'weight':'bold',
    'size':'15'
}
plt.rc('font',**font)

data1 = pd.read_csv('../data/PM2.5/BeijingPM20100101_20151231.csv')
print(data1.info())
"""将分开的时间字符串通过periodIndex方法转换为pandas中的时间类型"""
peroid  = pd.PeriodIndex(year = data1['year'],month =data1['month'],day=data1['day'],hour=data1['hour'],freq='H')
data1['datatime'] = peroid
# 保持怀疑态度，这里转化为了object类型，并不是timestamp类型
data1.set_index('datatime',inplace=True)
# print(data1.info())
print(data1.shape)

data1 = data1.resample('7D').mean()
"""处理PM_US Post 为nan的项，在这里我们选择删除该行数据"""
data_US = data1['PM_US Post'].dropna()
_x =data_US.index
_y = data_US.values
_x = [i.strftime('%Y-%m-%d') for i in _x]
plt.plot(range(len(_x)),_y)
plt.xticks(range(0,len(_x),10),list(_x)[::10],rotation=45)

plt.figure(figsize=(20,12 ),dpi=80)
plt.show()