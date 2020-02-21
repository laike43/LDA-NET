
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
import nltk
import os

from os import path


def  run(path):
    
    kw = []
    s= ''
    with open(path, 'r') as f:
        print()
        for i in f.readlines():
            if i[0] == '所':
                continue
            s =s + i.strip()

    kw.append(s)
      
    corpus = kw

     
    tfidf_model = TfidfVectorizer()
    tfidf_matrix = tfidf_model.fit_transform(corpus)
    word_dict=tfidf_model.get_feature_names()
    #print(word_dict)
    #print(tfidf_matrix)
    weight=tfidf_matrix.toarray()
    #print(weight)
    sender ={}
    for t,word in enumerate(word_dict):
        #print(t,word)
        sender[word] = weight[0][t]
    #print(sender)
    g = sorted(sender.items(),key=lambda x: x[1], reverse=True)
    token = []
    for i in g:
        token.append(i[0])
   
    st = nltk.pos_tag(token)
    print('字符前五',path)
    keyword =''
    for i in st[:6]:
        if i[1] == 'NN' or i[1] == 'CC' :
            keyword = keyword + ' ' + i[0]

    print(keyword)




if __name__ == "__main__":
    path = 'data/'
    for root,dirs,files in os.walk(path): 
        for file in files:
            file_path =  os.path.join(root,file)
            run(file_path)

    

