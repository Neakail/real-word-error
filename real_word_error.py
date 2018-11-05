import json
import nltk
import time

class zhencijiucuo:

    def __init__(self):
        with open('Confusion_set_process.json') as f:
            self.confusion_set = json.load(f)

        with open('qianci.json') as f:
            self.qianci = json.load(f)

        with open('houci.json') as f:
            self.houci = json.load(f)


    def jiucuo(self,text):
        recommend = []
        text_sentences = nltk.sent_tokenize(text)
        for sentence in text_sentences:
            sentence_index = text_sentences.index(sentence)
            words = nltk.word_tokenize(sentence)
            words.insert(0, '<BEG>')
            words.append('<END>')

            for i in xrange(1, len(words) - 1):
                word = words[i]
                last_word = words[i - 1]
                next_word = words[i + 1]
                if word in self.confusion_set:
                    houxuanci = self.confusion_set[word]
                    if last_word in self.houci and next_word not in self.qianci:
                        if word in self.houci[last_word]:
                            count = self.houci[last_word][word]
                        else:
                            count = 1
                        temp_word_ = {}
                        for each_houxuanci in houxuanci:
                            if each_houxuanci in self.houci[last_word]:
                                if self.houci[last_word][each_houxuanci] > count:
                                    temp_word_[each_houxuanci] = self.houci[last_word][each_houxuanci]


                        if len(temp_word_) != 0:
                            recommend_ = {}
                            temp_word = []
                            if len(temp_word_) <= 3:
                                for each_word in temp_word_:
                                    temp_word.append(each_word)
                            else:
                                temp_word_ = sorted(temp_word_.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
                                print temp_word_
                                temp_word.append(temp_word_[0][0])
                                temp_word.append(temp_word_[1][0])
                                temp_word.append(temp_word_[1][0])

                            recommend_['sentence_index'] = sentence_index
                            recommend_['word_index'] = i-1
                            recommend_['word'] = word
                            recommend_['true_word'] = temp_word
                            recommend.append(recommend_)

                    elif last_word not in self.houci and next_word in self.qianci:
                        if word in self.qianci[next_word]:
                            count = self.qianci[next_word][word]
                        else:
                            count = 1
                        temp_word_ = {}
                        for each_houxuanci in houxuanci:
                            if each_houxuanci in self.qianci[next_word]:
                                if self.qianci[next_word][each_houxuanci] > count:
                                    temp_word_[each_houxuanci] = self.houci[last_word][each_houxuanci]

                        if len(temp_word_) != 0:
                            temp_word = []
                            recommend_ = {}
                            if len(temp_word_) <= 3:
                                for each_word in temp_word_:
                                    temp_word.append(each_word)
                            else:
                                temp_word_ = sorted(temp_word_.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
                                print temp_word_
                                temp_word.append(temp_word_[0][0])
                                temp_word.append(temp_word_[1][0])
                                temp_word.append(temp_word_[1][0])

                            recommend_['sentence_index'] = sentence_index
                            recommend_['word_index'] = i - 1
                            recommend_['word'] = word
                            recommend_['true_word'] = temp_word
                            recommend.append(recommend_)

                    elif last_word in self.houci and next_word in self.qianci:

                        if word in self.houci[last_word]:
                            count = self.houci[last_word][word]
                        else:
                            count = 1

                        if word in self.qianci[next_word]:
                            count += self.qianci[next_word][word]
                        else:
                            count += 1

                        temp_word_ = {}
                        for each_houxuanci in houxuanci:
                            sorce = 0
                            if each_houxuanci in self.qianci[next_word]:
                                sorce += self.qianci[next_word][each_houxuanci]
                            if each_houxuanci in self.houci[last_word]:
                                sorce += self.houci[last_word][each_houxuanci]
                            if sorce > count:
                                temp_word_[each_houxuanci] = sorce

                        if len(temp_word_) != 0:
                            temp_word = []
                            recommend_ = {}
                            if len(temp_word_) <= 3:
                                for each_word in temp_word_:
                                    temp_word.append(each_word)
                            else:
                                temp_word_ = sorted(temp_word_.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
                                print temp_word_
                                temp_word.append(temp_word_[0][0])
                                temp_word.append(temp_word_[1][0])
                                temp_word.append(temp_word_[1][0])

                            recommend_['sentence_index'] = sentence_index
                            recommend_['word_index'] = i - 1
                            recommend_['word'] = word
                            recommend_['true_word'] = temp_word
                            recommend.append(recommend_)
                else:
                    pass


        return recommend


jiu = zhencijiucuo()
start = time.time()
text = "I'm very happi. I want to write a deary. We will hake a meeting."
for i in jiu.jiucuo(text):
    print i
end = time.time()
print end-start