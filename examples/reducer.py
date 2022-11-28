#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys
from collections import OrderedDict

word = None
wordcount = {}

for line in sys.stdin:
    line = line.strip()
    word, count, filename = line.split('\t')

    if word in wordcount:
        matrix = wordcount[word]
        if filename in matrix:
            count = matrix[filename]
            matrix.update({filename:int(count)+1})
            wordcount.update({word:matrix})
        else:         
            matrix.update({filename:int(count)})
            wordcount.update({word:matrix})
    else:
        matrix = {filename: int(count)}
        wordcount.update({word:matrix})


wordcount = OrderedDict(sorted(wordcount.items()))

for x in wordcount:
    print(x,'|',str(wordcount[x]))