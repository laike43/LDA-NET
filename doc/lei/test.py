from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans
from stop_words import get_stop_words
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

import jieba
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def test_d(corpus):
    cv = CountVectorizer()
    cv_fit = cv.fit_transform(corpus)

    print(cv.get_feature_names())
    print(cv_fit.toarray())
    VM = cv_fit.toarray()
    print(cv_fit.toarray().sum(axis=0))

    X, labels_true = make_blobs(n_samples=750, centers=VM, cluster_std=0.4,
                                random_state=0)

    X = StandardScaler().fit_transform(X)

    ##############################################################################
    # Compute DBSCAN
    db = DBSCAN(eps=0.3, min_samples=10).fit(X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    print('Estimated number of clusters: %d' % n_clusters_)
    print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
    print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
    print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
    print("Adjusted Rand Index: %0.3f"
          % metrics.adjusted_rand_score(labels_true, labels))
    print("Adjusted Mutual Information: %0.3f"
          % metrics.adjusted_mutual_info_score(labels_true, labels))
    print("Silhouette Coefficient: %0.3f"
          % metrics.silhouette_score(X, labels))

    ##############################################################################
    # Plot result
    import matplotlib.pyplot as plt

    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = 'k'

        class_member_mask = (labels == k)

        xy = X[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)

        xy = X[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=6)

    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()



def  kw_keanms(corpus):
    vectorizer = CountVectorizer()

    # 计算个词语出现的次数

    X = vectorizer.fit_transform(corpus)

    # 获取词袋中所有文本关键词

    word = vectorizer.get_feature_names()
    print('word')
    print(word)

    # print (X.toarray())

    transformer = TfidfTransformer()

    print('transformer')
    print(transformer)
    # 将词频矩阵X统计成TF-IDF值

    tfidf = transformer.fit_transform(X)
    print('tfidf')
    # 查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重
    print(tfidf)
    print('toarry')
    print(tfidf.toarray())
    tfidf_weight = tfidf.toarray()
    print("****************************************************************************************")

    print(tfidf_weight)

    num_clusters = 5

    km = KMeans(n_clusters=num_clusters, n_jobs=2)

    km.fit(tfidf)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
    clusters = km.labels_.tolist()
    print(km.cluster_centers_)

    for index, label in enumerate(km.labels_, 1):
        print("index: {}, label: {}".format(index, label))

    # 样本距其最近的聚类中心的平方距离之和，用来评判分类的准确度，值越小越好
    # k-means的超参数n_clusters可以通过该值来评估
    print("inertia: {}".format(km.inertia_))

    result = km.fit_predict(tfidf)

    print("Predicting result: ", result)

    # 简单打印结果
    r1 = pd.Series(km.labels_).value_counts()  # 统计各个类别的数目
    r2 = pd.DataFrame(km.cluster_centers_)  # 找出聚类中心
    r = pd.concat([r2, r1], axis=1)  # 横向连接（0是纵向），得到聚类中心对应的类别下的数目
    print(r)

    tsne = TSNE(n_components=2)
    print("计算权重")
    decomposition_data = tsne.fit_transform(tfidf_weight)

    x = []
    y = []

    for i in decomposition_data:
        x.append(i[0])
        y.append(i[1])
    print("##########################################################################################################3")
    print(y)
    print(x)
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes()
    plt.scatter(x, y, c=km.labels_, marker="*")
    plt.xticks(())
    plt.yticks(())

    plt.show()
    plt.savefig('./sample.png', aspect=1)

stop_words = get_stop_words('en')
def str_spit(str_i):
    str = ''
    str_i_tmp = str_i.strip().split(' ')
    for i in str_i_tmp:
        if len(i) > 5:
            if  not i in stop_words:
                str = str+' ' +i
    list_s = str.split(' ')
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    if len(list_s) < 4:
        str_r =''
    else:
        str_list = sorted(list_s)
        print(str_list)
        str_r =''
        for j in str_list:
            str_r = str_r +' '+j
    print(str_r)
    return str_r
with open('kw_sender','r') as f:
    corpus = []
    num =0
    for i in f.readlines():
        print(i)
        str_i = i.split(':')
        print(str_i[0])
        print(str_i[1])
        str = str_spit(str_i[1])
        if str != '':
            corpus.append(str)
        print('处理完成的',str)
        print(num)
        if num == 100:
            break
        num =num +1
print(corpus)
kw_keanms(corpus)
#test_d(corpus)
'''
vectorizer = CountVectorizer()

#计算个词语出现的次数

X = vectorizer.fit_transform(corpus)

#获取词袋中所有文本关键词

word = vectorizer.get_feature_names()
print(word)

#print (X.toarray())

transformer = TfidfTransformer()

print (transformer)

#将词频矩阵X统计成TF-IDF值

tfidf = transformer.fit_transform(X)

#查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重
print(tfidf)
print (tfidf.toarray())
tfidf_weight = tfidf.toarray()
print("****************************************************************************************")

print(tfidf_weight)



num_clusters = 5

km = KMeans(n_clusters=num_clusters,n_jobs=2)


km.fit(tfidf)
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
clusters = km.labels_.tolist()
print(km.cluster_centers_)

for index, label in enumerate(km.labels_, 1):
    print("index: {}, label: {}".format(index, label))

# 样本距其最近的聚类中心的平方距离之和，用来评判分类的准确度，值越小越好
# k-means的超参数n_clusters可以通过该值来评估
print("inertia: {}".format(km.inertia_))

result = km.fit_predict(tfidf)

print ("Predicting result: ", result)





#简单打印结果
r1 = pd.Series(km.labels_).value_counts() #统计各个类别的数目
r2 = pd.DataFrame(km.cluster_centers_) #找出聚类中心
r = pd.concat([r2, r1], axis = 1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
print(r)

tsne = TSNE(n_components=2)
decomposition_data = tsne.fit_transform(tfidf_weight)

x = []
y = []

for i in decomposition_data:
    x.append(i[0])
    y.append(i[1])
print("##########################################################################################################3")
print(y)
print(x)
fig = plt.figure(figsize=(10, 10))
ax = plt.axes()
plt.scatter(x, y, c=km.labels_, marker="*")
plt.xticks(())
plt.yticks(())
plt.show()
#plt.savefig('./sample.png', aspect=1)


'''





