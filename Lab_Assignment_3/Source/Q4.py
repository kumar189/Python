import nltk
from nltk import pos_tag, ne_chunk
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
import re
from nltk.tokenize import RegexpTokenizer
from nltk import FreqDist
#opens and reads file
f= open('file')
Words=f.read()
#break the file into tokens
St=sent_tokenize(Words)
#replaces special charecters with spaces
Words=Words.replace('.','').replace(',','')

tokens= nltk.word_tokenize(Words)
#lemmatizes the given input
lemmatizer=WordNetLemmatizer()
print [lemmatizer.lemmatize(t) for t in tokens ]
words=[]
#tokens is given as input and pos_tag function is applied to get the output
sent = pos_tag(tokens)
for s in sent:
    #removes all verbs with pos tag VB
    if(s[1]!='VB'):
        print s
        words.append(s[0])
wordfreq = []
#used for calculating word frequency
wordfreq = [words.count(p) for p in words]
#prints the words with their frequency count
print(dict(zip(words,wordfreq)))
fdist = FreqDist(words)
#returns top 5 repeated words in file
freq= fdist.most_common(5)
print freq
repeated_words=[]
for q in freq:
    repeated_words.append(q[0])
print repeated_words
str=[]
#used for getting all the sentences with the most repeated words and prints the sentences
for s in St:
    if(any(map(lambda word: word in s,repeated_words))):
        print s
# re.findall(r"([^.]*?"+re.escape(t)+r"[^.]*\.)",St)
# for t in repeated_words:
#     print [re.findall(r"([^.]*?" + re.escape(t) + r"[^.]*\.)", St)]
#     for s in St.split('.'):
#         if t in s:
#             str.append(s)
#             St.remove(s)
#
# print str


# top_words = sorted(words.iteritems(), cmp=sort_items, reverse=True)[:N]
# for w in words:
#     wordfreq.append(words.count(w))
# print("Pairs\n" + str(zip(words, wordfreq)))