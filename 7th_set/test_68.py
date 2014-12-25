#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from collections import defaultdict

vector = defaultdict(dict)
for line in open(sys.argv[1]):
    line = line.strip()
    if line != "":
        (word,contexts) = line.split("\t",1)
        context = contexts.split("\t")
        for i in context:
            (text,score) = i.split(":")
            #print score
            vector[word][text] = score
word = []
result = {}
for i in vector:
    word.append(i)
    for j in vector:
        if j not in word:
            score = 0
            for k in vector[i]:
                if k in vector[j]:
                    #print vector[i][k],vector[j][k]
                    score += float(vector[i][k])*float(vector[j][k])
            if score >= 0.6:
                a = i+"\t"+j
                result[a] = str(score)
                #print str(score) + "\t" + str(i) + "\t" + str(j)
for i,j in sorted(result.items(),key=lambda x:x[1],reverse=True):
    print j + "\t" + i
