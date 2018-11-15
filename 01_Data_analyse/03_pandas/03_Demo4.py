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
cate_list = [i[0] for i in temp_list]
df['cate'] = cate_list
print(df.groupby(by='cate').count()['title'])