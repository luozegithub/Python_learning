import numpy as np

# us_file_path = './data/youtube_video_data/US_video_data_numbers.csv'
# t1 = np.loadtxt(us_file_path, delimiter=',', dtype=np.int)
# # unpack 转置
# t2 = np.loadtxt(us_file_path, delimiter=',', dtype=np.int, unpack=1)
# print(t2)
# split
# 不连续的列t1[[row],[col]]
# print(t1[1:,:])
# 选取多个不相邻的点，选出来的结果为 （0,0） （2,1） （2,3）
# c = t2[[0, 2, 2], [0, 1, 3]]
# print(c)

# np中的转置的另外3中方法
# t3 = np.arange(24).reshape(4, 6)
# numpy中的布尔索引
# t3[t3 > 10] = 9
# print(t3)

# numpy中的三元运算符,结果作为返回值。不对ndarray做改变
# np.where(t3 <= 8, 0, 1)
# print(np.where(t3 <= 8, np.nan,np.inf ))

# clip 裁剪
# print(t3.clip(3,4))
# print(t3.transpose())
# print(t3.T)
# print(t3.swapaxes(0,1))

# nan inf 都是float类型的变量，没有两个相等的nan，所以我们可以使用以下方法统计ndarray中nan的个数
# t = np.arange(24,dtype=float).reshape((4,6))
# t[:,1] = np.nan
# print(np.count_nonzero(t!=t))
# axis =  1/0 行/列,指定row col 则按照指定的计算，否则是全局。
# print(t)
# print('*'*20)
# print('sum:',t.sum(axis=0))
# print('mean:',t.mean(axis=0))
# print('median',np.median(t,axis=0))
# print('max:',t.max(axis=0))
# print('min',t.min(axis=0))
#  print('argmax:',t.argmax(axis=0))
# print('argmin',t.argmin(axis=0))
# print('ptp(极值)',t.ptp(axis=1))
# print('std（标准差）',t.std(axis=0))

# 数组的拼接
x1 = np.arange(12).reshape((3,4))
x2 = np.arange(12,24).reshape((3,4))
# vstack(vertically) hstack(horizontally)
print(np.vstack((x1,x2)))
print(np.hstack((x1,x2)))

# 交换,列同样的道理
print(x1)
x1[[1,2],:] = x1[[2,1],:]
print(x1)
