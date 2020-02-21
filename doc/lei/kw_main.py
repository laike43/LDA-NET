from sqlconnect import Sqldata
from sklearn.decomposition import PCA
from fileop import Fileop
import datetime
import logging
from stop_words import get_stop_words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans
from multiprocessing import Manager,Process,Lock
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

import jieba
import matplotlib.pyplot as plt
from multiprocessing import Pool
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
xunhuan =400
def test(corpus):
    print(corpus)

def matrixPCA(weight, dimension):
    pca = PCA(n_components=dimension)  # 初始化PCA
    pcaMatrix = pca.fit_transform(weight)  # 返回降维后的数据
    print("降维之前的权重维度：", weight.shape)
    print("降维之后的权重维度：", pcaMatrix.shape)
    return pcaMatrix
def  kw_keanms(corpus):
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
    #weightPCA = matrixPCA(tfidf_weight, dimension=20)
    print("****************************************************************************************")

    print(tfidf_weight)

    num_clusters = 4

    km = KMeans(n_clusters=num_clusters, n_jobs=2)

    km.fit(tfidf_weight)
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
    # plt.savefig('./sample.png', aspect=1)
    return  result
def saveResult(data,y,name):
    y = y.reshape((len(data), 1))
    print(data)
    print(len(data))
    for i in range(12):
        str_num = str(i)
        filename = './data2/result' + str_num + '.txt'  # 文件名
        with open(filename, 'w', encoding='utf8') as fr:
            for j in range(len(data)):
                try:
                    if y[j] == i:
                        print(y[j],'y[j',data[j])
                        strLine = ''.join(data[j])
                        fr.write(strLine)
                        fr.write('\n')
                        fr.write('所属邮箱:')
                        ename = ''.join(name[j])
                        fr.write(ename)
                        fr.write('\n')
                except:
                    pass
            fr.close()
def str_spit(str_i):
    str = ''
    str_i_tmp = str_i.strip().split(' ')
    for i in str_i_tmp:
        if len(i) > 3:
            if not i in stop_words:
                str = str + ' ' + i
    list_s = str.split(' ')
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    if len(list_s) < 3:
        str_r = ''
    else:
        #str_list = sorted(list_s)
        str_list = list_s
        print(str_list)
        str_r = ''
        for j in str_list:
            str_r = str_r + ' ' + j
    print(str_r)
    return str_r
def  kw_str(i):

    return sender_kw


#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


#start = datetime.datetime.now()
count = Sqldata().kw_num()
print(count)
count =count[0][0]


stop_words = get_stop_words('en')
sender_kw ={}

for i in range(xunhuan):
    print("ssdfsdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
    data = Sqldata().sql_kw(i)
    print("第%s条:", i)
    sender = data[3]
    kw = data[0] + ' ' + data[1] + ' ' + data[2]

    if sender in sender_kw.keys():
        kw = sender_kw[sender] + ' ' + kw
        sender_kw[sender] = kw
    sender_kw[sender] = kw


print(sender_kw)

kw_sender = {}
for i in sender_kw.items():
    kw_tmp = set()
    t = i[1].split(' ')
    for j in t:
        kw_tmp.add(j)
        str =''
        for k in kw_tmp:
            str = k +' '+ str
    kw_sender[i[0]]=str



print(kw_sender)

'''

with open('kw_sender','a') as f:
    for i in kw_sender.items():
        sender = i[0]
        data = i[1]
        f.write(sender)
        f.write(':')
        f.write(data)
        f.write('\n')
'''
corpus = []
for i in kw_sender.values():
    print(i)
    #t = str_spit(i);i=t

    corpus.append(i)

print(corpus)
print(len(corpus))

kw_keanms(corpus)

print('all done')
















