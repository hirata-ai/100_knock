#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from stemming.porter2 import stem

for line in open(sys.argv[1]):
    line = line.strip()
    words = line.split("\t")
    print line + "\t" + stem(words[1])
