from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error,classification_report
import pandas as pd
import numpy as np

def logistic():
    """
        逻辑回归做二分类进行癌症预测（根据细胞的属性特征）
        :return: NOne
        """
    # 构造列标签名字
    column = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
              'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli',
              'Mitoses', 'Class']

    data = pd.read_csv(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
        names=column)
    # print(data.head(2))
    # print(data['Class'].unique())

    #对缺失值进行处理
    data = data.replace(to_replace='?',value=np.nan)
    data = data.dropna()
    # print(column[1:10])
    # 进行数据的分割
    x_train, x_test, y_train, y_test = train_test_split(data[column[1:10]], data[column[10]], test_size=0.25)

    # 进行标准化处理
    std = StandardScaler()
    std.fit_transform(x_train)
    std.transform(x_test)
 # 逻辑回归预测
    lg = LogisticRegression(penalty='l2',C=1.0)
    lg.fit(x_train,y_train)
    print(lg.coef_)
    y_predict = lg.predict(x_test)
    print("准确率：", lg.score(x_test, y_test))
    print('召回率:',classification_report(y_test,y_predict,labels=[2,4],target_names=['良性','恶性']))

if __name__ == '__main__':
    logistic()


