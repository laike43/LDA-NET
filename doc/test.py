import nltk
#nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
t = wordnet_lemmatizer.lemmatize('dogs')
print(t)
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()
a = wordnet_lemmatizer.lemmatize('dogs')
print(a)

text = 'That U.S.A.poster-print costs$12.40...'

pattern =r'''
    (?x) #set flag to allow verbose regexps
    ([A-Z]\.)+ #abbreviations, e.g. U.S.A.
    | \w+(-\w+)* #words with optional internal hyphens  
    | \$?\d+(\.\d+)?%? #currency and percentages,e.g. $12.40,82%
    | \.\.\. #ellipsis
    | [][.,;"'?():-_`] #these are separate tokens
        '''
nltk.regexp_tokenize(text, pattern)