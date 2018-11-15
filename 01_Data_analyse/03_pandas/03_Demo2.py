import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
font = {
    'family': 'LiSu',
    'weight': 'bold',
    'size': '16'
}
plt.rc('font', **font)

""" original_publication_year   9979 non-null float64
    对出版年月做聚合，首先 先去除空项，drapna会去除多余的项，所以我们不采用该方法
    我们使用pd.notnull  pandas的布尔索引
    我们得到Series，因为聚合的时候所使用的publication_year为
    整数类型，所以无法使用分片。只用字符类型才支持分片[:20]
"""

def demo1():
    publication_year = df[pd.notnull(df["original_publication_year"])].groupby(by='original_publication_year').count()["title"].sort_values(ascending=False)
    _x = list(publication_year.index)[:20]
    _y = list(publication_year.values)[:20]
    plt.barh(_x,_y,0.3,color='orange')
"""
    计算不同年份评分的平均值
 """
def demo2():
    publication_year = df[pd.notnull(df["original_publication_year"])]
    data1 = publication_year.groupby(by='original_publication_year')[
        "average_rating"].mean()
    print(data1)
    plt.plot(range(len(data1.index)),data1.values,color='orange')
    plt.xticks(range(len(data1.index))[::10],data1.index[::10].astype(np.int),rotation=45)
df = pd.read_csv('../data/books.csv')

plt.figure(figsize=(20, 12), dpi=80)
demo2()
plt.grid()
plt.show()
