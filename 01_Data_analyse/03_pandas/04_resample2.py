# 911数据中不同月份不同电话类型次数
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
font = {
    'family':'LiSu',
    'weight':'bold',
    'size':'15'
}
plt.rc('font',**font)

df = pd.read_csv('../data/911.csv')
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

"""添加列，根据电话内容分组"""
temp_list = df['title'].str.split(': ').tolist()
cate_list = [i[0] for i in temp_list]
df['cate'] = cate_list
df.set_index('timeStamp',inplace=True)

plt.figure(figsize=(20, 12), dpi=80)
for group_name,group_data in df.groupby(by='cate'):
    count_by_month = group_data.resample('M').count()['title']
    _x = count_by_month.index
    _y = count_by_month.values

    _x = [i.strftime('%Y-%m-%d') for i in _x]
    plt.plot(range(len(_x)), _y, label=group_name)
plt.xticks(range(len(_x)), _x, rotation=45)
plt.grid()
plt.legend()
plt.show()

