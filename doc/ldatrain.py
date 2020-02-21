from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from gensim import corpora,models
from sqlconnect import Sqldata
from fileop import Fileop
import nltk
import datetime
import gensim
import logging





#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
start = datetime.datetime.now()
tokenizer =RegexpTokenizer(r'\w+')
#tokenizer =RegexpTokenizer(r'\w+|\$[\d\.]+|\S+')

stop_words = get_stop_words('en')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

class Model_lda(object):
    def __init__(self):
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.stop_words = get_stop_words('en')
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def train(self,i):
        mail_list = Sqldata().sql_conn(i)
        body = mail_list[0][0][0]
        sender = mail_list[1][0][0]
        # 全部小写
        body1=body.lower()
        # 用句号作为分割符，可加入逗号改进
        body2=body1.split('.')
        body1=[]
        texts=[]
        for body in body2:
        #  分词
            token = tokenizer.tokenize(body)
        # 去除停用词
            stop_tokens=[]
            for j in token:
                if not j in stop_words:
                    stop_tokens.append(j)
            #  提炼词干
            stemmed=[]

            st = nltk.pos_tag(stop_tokens)
            
            for j in st:
                
                #print(lemmatizer.lemmatize(word=j[0],pos=j[1]))
                stemmed.append(lemmatizer.lemmatize(word=j[0]))
                #print('stem:',stemmed)
                #stemmed.append(stemmer.stem(j))
            #  将文件合成二维矩阵
                
            texts.append(stemmed)
        #print(texts)
       # 词频统计
        dictionary = corpora.Dictionary(texts)
        corpus = []
       # print('dict',dictionary)
        for j in texts:
            corpus.append(dictionary.doc2bow(j))

     #   print('corpus',corpus)
    # 调整语料中不同词的词频，将那些在所有文档中都出现的高频词的词频降低
        tfidf = models.TfidfModel(corpus)
        corpusTfidf = tfidf[corpus]
      #  print(tfidf)

    #未使用多核心，可改
        try:
            #ldamodel=gensim.models.LdaMulticore(corpusTfidf,num_topics=1,id2word = dictionary)
            ldamodel=gensim.models.LdaModel(corpusTfidf,num_topics=1,id2word = dictionary)
            #pathgen = './gensimodel/1.model'
            #ldamodel.save(pathgen)
            print("正在处理原始数据......")
            print(ldamodel.print_topics(num_topics=1, num_words=3))
        except:
            pass
        lda_words=ldamodel.show_topics(num_topics=1, num_words=3)
        Model_lda().words_op(i,lda_words,sender)

    def words_op(self,id,ldamodel,sender):
        topic = ldamodel
        data = topic[0][1]
        dat = data.split('+')
        strl =''
        kw =[]
        pd =[]
        for i in dat:
            top_str = (i.split('*'))
            tmp=top_str[1].strip()
            kw.append(tmp.strip('\"'))
            pd.append(top_str[0])
        Sqldata().sql_insert(id,kw,pd,sender)

