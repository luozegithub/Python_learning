import pandas as pd
import numpy as np

df = pd.read_csv('../data/starbucks_store_worldwide.csv')
# print(df.info())
# print(df.head(1))
grouped = df.groupby(by='Country')
# type DataFrameGroupBy
# print(grouped)
"""遍历DataFrameGroupby,i为分组的key，value为具体的数据"""
# for i,j in grouped:
#     print(i,'\n',j)
#     break
"""默认count()会对每一列都进行都会count，我们"""
# country_count = grouped.count()
# country_count  type  Series
country_count = grouped["Brand"].count()
# print(type(df[df["Country"]=="US"]["Brand"]))
# print('美国的数量为：',country_count["US"])
# print('中国的数量为：',country_count["CN"])

"""统计中国每个省店铺的数量"""
China_data = df[df["Country"]=='CN']
China_Province_data = China_data.groupby(by='State/Province').count()["Brand"]
# print(China_Province_data)
# for i,j in China_Province_data:
#     print(i,'\n',j)
#     break

"""对某几列进行分组，以下两种方法等同"""
# result = df.groupby(by=["Country","State/Province"]).count()["Brand"]
result = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(result)
"""复合索引"""

# print(result["AE"]["AJ"])
# print(result.index)
"""如果我们想要返回的类型为DataFrame，只需要如下操作,我们想要取某行的数据的时候，
就不能像series那样，只能使用loc方法。
"""
result = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()

# result = df.groupby(by=["Country","State/Province"]).count()[["Brand"]]


test1 = pd.DataFrame({'a':range(7),'b':range(7,0,-1),'c':['one','one','one','two','two','two','two'],'d':list('hjklmno')})
print(test1)
"""swaplevel() Methon"""
print(test1.set_index(['c','d']))
print(test1.set_index(['d','c']).swaplevel())

