import numpy as np
import random

t1 = np.array([1,2,3])
print(t1,t1.dtype)

t2 = np.arange(10)
print(t2)

##numpy中的bool类型
t5 = np.array([1,1,0,1,0,0],dtype=bool)
print(t5)
print(t5.dtype)

#调整数据类型
t6 = t5.astype("int8")
print(t6)
print(t6.dtype)

t7 = np.array([random.random() for i in range(10)])
print(t7,t7.dtype)

t8 = np.round(t7,2)
print(t8,t8.dtype)

t9 = np.arange(24).reshape((4,6))
# flatten() 有返回值，不覆盖初始值
print(t9.reshape(t9.shape[0]*t9.shape[1],))
print(t9.flatten())
print(t9)

"""数组进行计算的时候有三种情况
    1.数字和数组进行计算，广播机制
    2.数组与数组进行计算，当数组shape相同的时候，对应位置进行计算
                        当shape不同的时候，找到某一个维度（列/行，广播原则），进行计算    
"""
