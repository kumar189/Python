with open('testfile') as fn: #opening a file named testfile which has data
    data = fn.read()
fn.closed

input_str= data.replace('(','').replace(')','').replace('.','').replace('"','').replace(',','').replace("'",'')
wordlist=[]
# input string is split and stored into a list
wordlist= input_str.lower().split()

wordfreq={}
for w in wordlist:
    #every word is compared and stored in wordlist if it is not or counter of word is incremented
    if w not in wordfreq:
        wordfreq[w] = 1
    else:
        wordfreq[w] += 1
# words and their frequency are printed
print(w,wordfreq)


