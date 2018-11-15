from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(message)s',level=logging.INFO)

raw_sentences = ["the quick brown fox jumps over the lazy dogs",'yoyoyo you go home now to sleep']

sentences = [s.split() for s in raw_sentences]
print(sentences)

# min_count 在不同的预料集中，我们对于基准词频的需求也是不一样的，例如在较大的预料集中，我们希望忽略那些只出现过一两次的单词，一般而言取0~100比较合适

# size参数 主要用来设置神经网络的层数，默认值是100，更大的层次设置意味着更多的输入数据，不过也能提升整体的准确度
model = word2vec.Word2Vec(sentences,min_count=1)
print(model.similarity('dogs','you'))