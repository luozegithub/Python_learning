from gensim.models import Word2Vec

en_wiki_word2vec_model = Word2Vec.load('wiki.zh.text.model')

testwords = ['有','数学']
for i in range(5):
    res = en_wiki_word2vec_model.most_similar(testwords[i])
    print (testwords[i])
    print (res)