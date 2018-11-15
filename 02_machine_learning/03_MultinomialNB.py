from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report


def naivebayes():
    news = fetch_20newsgroups(subset='all')
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)

    tf = TfidfVectorizer()
    x_train = tf.fit_transform(x_train)
    x_test = tf.transform(x_test)
    # print(x_train.toarray())
    # print(tf.get_feature_names())

    mlt = MultinomialNB(alpha=1.0)
    mlt.fit(x_train, y_train)
    y_predict = mlt.predict(x_test)

    print("预测的文章类别为：", y_predict)
    print("准确率为：", mlt.score(x_test, y_test))
    print("每个类别的精确率和召回率：",
          classification_report(y_test, y_predict, target_names=news.target_names))


if __name__ == '__main__':
    naivebayes()
