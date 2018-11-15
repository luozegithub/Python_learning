import numpy as np
from matplotlib import pyplot as plt
us_file_path = '../data/youtube_video_data/US_video_data_numbers.csv'
t = np.loadtxt(us_file_path, delimiter=',', dtype=np.int)
comment = t[:,-1]
comment=comment[comment<=5000]
print(comment.max(),comment.min())# 4995 0
dis = 100
num_bins = (comment.max()-comment.min())//dis
plt.figure(figsize=(20,8),dpi=80)
plt.hist(comment,num_bins)
plt.xticks(range(min(comment),max(comment)+dis,dis),rotation =90)
plt.show()