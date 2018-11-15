import numpy as np

"""跟之前的那种使用另一个变量，不改变本身值的不同，
在np中，你取出任意一个split，给另一个变量，对其进行操作，都会影响到本身。
a=b
a=b[:,] view操作，数据变化是一致的 
在这里我们使用a=b.copy()
"""


def fill_ndarray_nan(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]
        if np.count_nonzero(temp_col != temp_col):
            temp_col[temp_col != temp_col] = temp_col[temp_col == temp_col].mean()


if __name__ == '__main__':
    t1 = np.arange(12).reshape((3, 4)).astype(np.float)
    print(t1)
    print('argmax:', t1.argmax(axis=0))
    print('argmin', t1.argmin(axis=0))
    t1[1, 2:] = np.nan
    fill_ndarray_nan(t1)
    print(t1)
