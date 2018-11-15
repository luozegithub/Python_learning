from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import GridSearchCV


def RandomForest():
    """
       决策树对泰坦尼克号进行预测生死
       :return: None
       """

    # 获取数据
    titan = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    # pclass age sex survived

    # 处理数据，找出特征值和目标值
    x = titan[['pclass', 'age', 'sex']]
    y = titan['survived']
    print(x.info())
    # age       633 non-null float64
    x['age'].fillna(x['age'].mean(), inplace=True)

    # 分割数据集到训练集合测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 进行处理（特征工程）特征-》类别-》one_hot编码
    dict = DictVectorizer(sparse=False)
    x_train = dict.fit_transform(x_train.to_dict(orient='records'))
    print(dict.get_feature_names())
    x_test = dict.fit_transform(x_test.to_dict(orient='records'))
    # print(x_train)

    rf = RandomForestClassifier()
    param = {"n_estimators": [120, 200, 300, 500, 800, 1200], "max_depth": [5, 8, 15, 25, 30]}
    gc = GridSearchCV(rf,param_grid=param,cv=2)
    gc.fit(x_train, y_train)
    print("准确率：", gc.score(x_test, y_test))
    print("查看选择的参数模型：", gc.best_params_)


if __name__ == '__main__':
    RandomForest()
