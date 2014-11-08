#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
words = []
for line in open(sys.argv[1]):
    line = line.strip()
    words.append(line)

for i in range(len(words)):
    if i != len(words)-1:
        print words[i] + "\t" + words[i+1]
