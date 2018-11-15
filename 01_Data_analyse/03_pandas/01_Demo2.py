import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
"""
电影类型
"""
file_path = '../data/IMDB-Movie-Data.csv'
df = pd.read_csv(file_path)

temp_list = df["Genre"].str.split(',').tolist()
genre_list = list(set([i for j in temp_list for i in j]))
# print(len(genre_list),genre_list)

zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)
# print(zeros_df.shape)   #(1000, 20)

# 赋值 
for i in range(df.shape[0]):
    zeros_df.loc[i, temp_list[i]] = 1
df_sum = zeros_df.sum(axis=0)
genre_count = df_sum.sort_values()
_x = genre_count.index
_y = genre_count.values
print(len(_x))

plt.figure(figsize=(20,8),dpi=80)

# 离散化 x 需要用先使用range替代x，然后在对应替换xticks
plt.bar(range(len(_x)),_y,width=0.3,color='orange')
plt.xticks(range(len(_x)),_x)
plt.grid()
plt.show()

