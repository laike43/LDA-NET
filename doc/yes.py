import nltk
nltk.download('brown')
from nltk.corpus import stopwords
from nltk.corpus import brown
import numpy as np
 
#分词
text = "Sentiment analysis is a challenging subject in machine learning.\
 People express their emotions in language that is often obscured by sarcasm,\
  ambiguity, and plays on words, all of which could be very misleading for \
  both humans and computers.".lower()
text_list = nltk.word_tokenize(text)
#去掉标点符号
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
text_list = [word for word in text_list if word not in english_punctuations]
#去掉停用词
stops = set(stopwords.words("english"))
text_list = [word for word in text_list if word not in stops]
print(text_list)
t = nltk.pos_tag(text_list)
#print(t)
brown_taged= nltk.corpus.brown.tagged_words()
print(brown_taged)