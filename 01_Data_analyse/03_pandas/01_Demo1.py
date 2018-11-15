import pandas as pd
import numpy as np
"""
我们计算平均评价，以及导演人数等信息
Director              1000 non-null object
Rating                1000 non-null float64
"""
file_path = '../data/IMDB-Movie-Data.csv'
df = pd.read_csv(file_path)

print(df.shape)  # (1000, 12)
print(df.info())

print(df["Rating"].mean())
print(len(set(df["Director"].tolist())))
# unique()方法 去重,<class 'numpy.ndarray'>
print(len(df["Director"].unique()))

print(df["Actors"].head(5))
# 获取演员的人数
temp_actors_list = df["Actors"].str.split(', ').tolist()
actors_list = [i for j in temp_actors_list for i in j]
print(actors_list)
print(len(set(actors_list)))







