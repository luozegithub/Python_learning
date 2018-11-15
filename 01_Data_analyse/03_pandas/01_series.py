import pandas as pd
import numpy as np
import string
# t = pd.Series([1,2,3])
# print(t,type(t))
# dict = {
#     'name':'zhangsan',
#     'age':23,
#     'position':'China'
# }
# t1 = pd.Series(dict)
# print(t1,type(t1))
# for index in t1.index:
#     print(index)
# print(t1.values)

t =pd.DataFrame(np.arange(12).reshape(3,4),index=list(string.ascii_lowercase[:3]),columns=list(string
.ascii_uppercase[-4:]))
print(t)
# print(t.head())
# print(t.info())
# print(t.describe())
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.ascii_letters)
"""笛卡尔积,与之前numpy之中的有点差别"""
print(t.loc[['a','b'],['W','X']])
print(t.loc[['a','b']])
"""pd中的loc方法中的切片，会取到右边的值(ioc不会)，与普通的切片有一点不同，需要注意"""
print(t.loc['a':'c','W':'Y'])
"""iloc   loc  一个是根据数字作为索引，另一个是根据字符串作为索引"""
t.iloc[1:,:2]=np.nan
print(t)

print(t['W'])