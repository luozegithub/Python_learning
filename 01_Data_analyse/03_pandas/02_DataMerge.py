import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((2,4)),columns=list("abcd"),index=["A","B"])
df2 = pd.DataFrame(np.zeros((3,3)),columns=list("xyz"),index=["A","B","C"])

print(df1)
print(df2)
print(df1.join(df2))
# inner以左边为标准，类似leftjoin，join 行维度的合并,找到on条件相同的行，做笛卡尔积
# outer列维度的合并是 merge,以on指定的维度为基准，内连接完成后，剩余的行填充NaN,how 属性 有left,right,inner,outer
"""
     a    b    c    d
A  1.0  1.0  1.0  1.0
B  1.0  1.0  1.0  1.0
   f  a  x
0  0  1  2
1  3  1  5
2  6  7  8
     a    b    c    d  f  x
0  1.0  1.0  1.0  1.0  0  2
1  1.0  1.0  1.0  1.0  3  5
2  1.0  1.0  1.0  1.0  0  2
3  1.0  1.0  1.0  1.0  3  5
4  7.0  NaN  NaN  NaN  6  8
"""
# df3 = pd.DataFrame(np.arange(9).reshape((3,3)),columns=list("fax"))
# df3['a'][1]=1
# print(df1)
# print(df3)
# print(df1.merge(df3,on='a'))
# print(df1.merge(df3,on='a',how='outer'))

