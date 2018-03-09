import re, collections
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk import pos_tag,ne_chunk
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from operator import itemgetter
from nltk import ngrams



#summarize a text file
with open("scscs.txt", "r") as f:
    plv = f.readlines()
print("lines", plv)
vv= ''
#Multi file into single string
for m in plv:
    vv= vv + m
print(vv)
#tokenized words
vv_word = word_tokenize(vv)
vv_sent = sent_tokenize(vv)

#-	apply lemmatization on the remaining words
lemmatizer = WordNetLemmatizer()
vv_lemma = []
for wordd in vv_word:
    fr_lema = lemmatizer.lemmatize(wordd.lower())
    vv_lemma.append(fr_lema)

print("\n -----------lemmet----------  ")
print(vv_lemma)
fr_pos = pos_tag(vv_lemma)

print("--------------BI-------------")

n = 2
grrm=[]
bigrams = ngrams(vv_lemma, n)
for grmm in bigrams:
    grrm.append(grmm)
print(grrm)
sss = " ".join(str(x) for x, y in fr_pos)
ss1s = word_tokenize(sss)
print("--------word  frequency----------")
fdi = nltk.FreqDist(grrm)
to = fdi.most_common()
to_fi = fdi.most_common(5)

thope=sorted(to, key=itemgetter(0))
print(thope)
print('---------word freq with count--------')
print(to_fi)
senttt = sent_tokenize(vv)
reppsp = []


for cdcd in senttt:
    for wordd, w1 in grrm:
        for ((c,m), l) in to_fi:
            if (wordd, w1 == c, m):
                reppsp.append(cdcd)  # the most common words
print ("\n top five Bigrams")
print(max(reppsp, key=len))