#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from collections import defaultdict
word_freq = defaultdict(int)
for line in open(sys.argv[1]):
    line = line.strip()
    word_freq[line] += 1
for i in word_freq:
    print str(word_freq[i]) +"\t"+ i
