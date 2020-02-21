

from sklearn.decomposition import PCA
from sklearn.cluster import Birch
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from gensim import corpora,models

def  kw_keanms(corpus):
    '''
    tfidf = models.TfidfModel(corpus)
    corpusTfidf = tfidf[corpus]
    '''
    vectorizer = CountVectorizer()

    # 计算个词语出现的次数

    X = vectorizer.fit_transform(corpus)

    # 获取词袋中所有文本关键词

    word = vectorizer.get_feature_names()

    print('我的特政',word)

    # print (X.toarray())

    transformer = TfidfTransformer()

    print(transformer)

    # 将词频矩阵X统计成TF-IDF值

    tfidf = transformer.fit_transform(X)

    # 查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重
    print(tfidf)
    print(tfidf.toarray())
    tfidf_weight = tfidf.toarray()
    print("****************************************************************************************")

    print(tfidf_weight)

    num_clusters = 3

    km = KMeans(n_clusters=num_clusters, n_jobs=2)

    km.fit(tfidf_weight)

    print(3*'sdffffffffffff')

    clusterer = Birch(threshold=0.5, branching_factor=50, n_clusters=12, compute_labels=True, copy=True)
    clusterer.fit_predict(tfidf)


cop = [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1)], [(3, 1), (8, 2), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1)]]
kw_keanms(cop)