import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
font = {
    'family': 'LiSu',
    'weight': 'bold',
    'size': '16'
}
plt.rc('font', **font)

df = pd.read_csv('../data/911.csv')
"""获取分类"""
temp_list = df['title'].str.split(': ').tolist()
cate_list = list(set([i[0] for i in temp_list]))
# print(cate_list)
"""构造带有分类的数组
    参照demo4，我们给df添加一列 cate属性，填充的值为cate_list 不需要去重的结果，
    这样我们就可以使用groupby方法，count统计得到最终的结果
"""
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=cate_list)
for cate in cate_list:
    zeros_df[cate][df['title'].str.contains(cate)] = 1
sum_ret = zeros_df.sum(axis=0)
print(sum_ret)