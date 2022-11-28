#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys
import re
filename = 0
index = 0
for line in sys.stdin:
    if index == 0:
        line = line.strip().split(',')[0]
        filename = line
        index+=1;
    else:
        line = re.sub(r'\W+',' ',line.strip())
        words = line.split()

        for word in words:
            print('{}\t{}\t{}'.format(word,1,filename))