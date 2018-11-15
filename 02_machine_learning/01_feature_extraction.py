import jieba
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler, StandardScaler,Imputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
"""对字典进行特征抽取"""

""" 初始化DictVectorizer()sparse默认位True，
    使用sparse，节约内存，方便读取处理，
    False的时候，使用ndarray存储
"""


def dictvec():
    dict = DictVectorizer()
    # one-hot 编码，将类别型特征进行转化
    data = dict.fit_transform(
        [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30}])
    print(data.toarray())
    print(dict.get_feature_names())
    print(dict.inverse_transform(data))
    return None


def textvec():
    text = CountVectorizer()
    """基于text的fit_transform，需要提前分词，然后统计文章中出现了哪些词语（set集合），
       过滤掉单个字母，生成sparse矩阵，使用toarray方法，生成ndarray数组。然后可以根据
       生成的数组，计算tf-idf
     """
    data = text.fit_transform(["人生 苦短，我 喜欢 喜欢 python", "人生 漫长，不用 python"])
    print(text.get_feature_names())
    print(type(data.toarray()))


def cutword():
    con1 = jieba.cut("今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。")
    con2 = jieba.cut("我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。")
    con3 = jieba.cut("如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。")
    c1 = ' '.join(con1)
    c2 = ' '.join(con2)
    c3 = ' '.join(con3)
    return c1, c2, c3


def hanzivec():
    c1, c2, c3 = cutword()
    print(c1, c2, c3)
    cv = CountVectorizer()
    data = cv.fit_transform([c1, c2, c3])
    print(cv.get_feature_names())
    print(data.toarray())


"""
    因为上面使用的基于text的CountVectorizer，并没有过滤停用词表，
    所以可能会出现一些问题，一些没有意义的词会影响到我们对于主题的判定，
    所以我们引入tf-idf(词语的重要程度)
"""


def tfidfvec():
    c1, c2, c3 = cutword()
    tf = TfidfVectorizer()
    data = tf.fit_transform([c1, c2, c3])
    print(tf.get_feature_names())
    print(data.toarray())


def guiyi():
    """
    当多个特征同等重要的时候，我们需要对特征进行归一化处理，因为公式中依赖于max，min，所以
    归一受异常点的影响，特定场景下，最大值最小值是变化的，这时鲁棒性较差，只适合传统精确数据场景
    """
    mm = MinMaxScaler(feature_range=(2, 3))
    data = mm.fit_transform([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])
    print(data)

def stand():
    """
    取代归一化,使用标准化，通过标准化，使得
    均值为0，标准差为1。
    :return:
    """
    std = StandardScaler()
    data = std.fit_transform([[1., -1., 3.], [2., 4., 2.], [4., 6., -1.]])
    print(data)
    print(std.mean_)

def imputer():
    """通过sklearn
     来处理缺失值，缺失值的类型必须是np.nan"""
    im = Imputer(missing_values='NaN',strategy='mean',axis=0)
    data = im.fit_transform([[1, 2], [np.nan, 3], [7, 6]])
    print(data)


def var():
    """特征选择（过滤式 VarianceThreshold）：删除方差为 0 的列。"""
    var = VarianceThreshold(threshold=0.0)
    data = var.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])
    print(data)

def pca():
    pca = PCA(n_components=0.9)
    data = pca.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])
    print(data)


if __name__ == '__main__':
    dictvec()
    # textvec()
    # cutword()
    # hanzivec()
    # tfidfvec()
    # guiyi()
    # stand()
    # imputer()
    # var()
    # pca()