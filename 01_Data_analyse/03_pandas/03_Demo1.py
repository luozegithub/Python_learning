import pandas as pd
from matplotlib import pyplot as plt
font = {
    'family':'LiSu',
    'weight':'bold',
    'size':'16'
}
plt.rc('font',**font)
def demo1():
    data1 = df.groupby(by='Country').count()["Store Number"].sort_values(ascending=False)[:10]
    print(data1)
    plt.bar(range(len(data1.index)), data1.values)
    plt.xticks(range(len(data1.index)), data1.index)
    plt.title("不同国家店铺的数量")
def demo2():
    data1 = df[df["Country"]=='CN'].groupby(by='City').count()["Store Number"].sort_values(ascending=False)[:20]
    print(data1)
    # plt.bar(range(len(data1.index)), data1.values,width=0.3,color='orange')
    plt.barh(range(len(data1.index)), data1.values,0.3,color='orange',label='China')
    # plt.xticks(range(len(data1.index)), data1.index)
    plt.yticks(range(len(data1.index)), data1.index)
    plt.title("中国不同城市店铺的数量")

df = pd.read_csv('../data/starbucks_store_worldwide.csv')
plt.figure(figsize=(20, 8), dpi=80)
# demo1()
demo2()
plt.grid()
plt.legend()
plt.show()
