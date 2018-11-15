import numpy as np
from matplotlib import pyplot as plt
us_file_path = '../data/youtube_video_data/US_video_data_numbers.csv'
uk_file_path = "../data/youtube_video_data/GB_video_data_numbers.csv"
t_us = np.loadtxt(us_file_path, delimiter=',', dtype=np.int)
t_uk = np.loadtxt(uk_file_path, delimiter=',', dtype=np.int)

zeros_data = np.zeros((t_us.shape[0],1))
ones_data = np.ones((t_uk.shape[0],1))
print(t_us.shape,t_uk.shape)

t_us = np.hstack((t_us,zeros_data))
t_uk = np.hstack((t_uk,ones_data))
print(t_us.shape,t_uk.shape)

# random 随机生成整数 和 浮点数
print(np.random.randint(1,10,(2,3)))
print(np.random.uniform(1,10,(2,3)))


