import Levenshtein
import json
words = []
with open('Oxford_Dictionary.txt','r') as f:
    for i in f.readlines():
        word = i.split('\t')[0]
        print word
        words.append(word)
confusion_set = {}
for word in words:
    confusion_set[word] = []
    # print word
    # print 11
    for word_ in words:
        # if Levenshtein.distance(word,word_) == 1:
        #     confusion_set[word].append(word_)
        if Levenshtein.distance(word,word_) == 2:
            confusion_set[word].append(word_)

with open('Confusion_set.json','w') as f:
    json.dump(confusion_set,f)
