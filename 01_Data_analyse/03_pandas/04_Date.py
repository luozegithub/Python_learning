import pandas as pd
import numpy as np
print(pd.date_range(start='20180901',end='20181031',freq='D'))
print(pd.date_range(start='20180901',periods=10,freq='D'))
print(pd.date_range(start='20180901',end='20181031',freq='2D'))

index = pd.date_range(start='20180101',periods=10)
df = pd.DataFrame(np.random.rand(10),index=index)
print(df)

