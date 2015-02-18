#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IELTS Writing Essay Creator
# License: Apache

import random, re, phrases

__version__ = 'v0.1.0.1 Alpha'
__author__ = 'Will Skywalker'


class Essay:
    def __init__(self):
        self.text = ''

    def __str__(self):
        return self.text

    def addSentence(self, sentence):
        self.text += sentence.getText().rstrip() + " "


class Sentence:
    def __init__(self, pos, keyword, number, kind='b', expression='n'):
        self.pos = pos
        self.text = ''
        self.keyword = str(keyword)
        self.number = str(number)
        self.kind = kind
        if pos == 0:
            self.kind += 'p'
        self.expression = expression

    def createSummary(first, second):
        pass

    def getPos(self):
        return self.pos

    def getKind(self):
        return self.kind

    def getText(self):
        if self.kind[0] == 'b':
            self.text = str(random.choice(phrases.phrasesBegin_b)).capitalize()+' '+self.keyword+' '\
                        +str(random.choice(phrases.wordsProvide))+' '+self.number+'% '\
                        +'of the total value.'
        elif self.kind[0] == 'c':
            self.text = self.number+r'% of the '+str(random.choice(phrases.wordsTotal))+' '\
                        +str(random.choice(phrases.wordsNumber))+' is '\
                        +str(random.choice(phrases.wordsProvideParticiple))+' by '+self.keyword+'.'



        if self.kind[-1] == 'p':
            self.text = self.text.rstrip('.')
            self.text += ', ' + str(random.choice(phrases.subordinateClause))
        return self.text



# class Data:
#     def __init__(self, name, percent):
#         self.name = name
#         self.percent = percent

#     def getName(self):
#         return self.name

#     def getPercent(self):
#         return self.percent



def main():
    dataList = list()
    sentenceList = list()
    for i in range(int(raw_input('Enter the number of datas:'))):
        dataList.append({raw_input('Enter its name:'): raw_input('Enter its percentage:')})
    dataList.sort(key=lambda dic: float(dic.values()[0]), reverse=True)
    for i in range(len(dataList)):
        if i == 0:
            sentenceList.append(Sentence(i, dataList[i].keys()[0], dataList[i].values()[0], kind=random.choice(['b', 'c'])))
        elif sentenceList[i-1].getKind()[0] == 'b':
            sentenceList.append(Sentence(i, dataList[i].keys()[0], dataList[i].values()[0], kind='c'))
        else:
            sentenceList.append(Sentence(i, dataList[i].keys()[0], dataList[i].values()[0]))
    for s in sentenceList:
        newEssay.addSentence(s)

    print newEssay



    

if __name__ == '__main__':
    print 'IETLS Writing Essay Creator', __version__, '\n'
    newEssay = Essay()
    main()
