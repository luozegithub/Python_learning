from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import pandas as pd


def decision():
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
    # 用决策树进行预测
    dec = DecisionTreeClassifier()
    #
    dec.fit(x_train, y_train)
    #
    # # 预测准确率
    print("预测的准确率：", dec.score(x_test, y_test))
    #
    # # 导出决策树的结构
    # 安装graphviz dot -Tpdf tree.dot -o desiciontree.pdf
    export_graphviz(dec, out_file="./tree.dot",
                    feature_names=['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'female', 'male'])


if __name__ == '__main__':
    decision()
