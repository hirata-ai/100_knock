#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from collections import defaultdict
import math

contexts = defaultdict(dict)
for line in sys.stdin:
    line = line.strip()
    (noun,context) = line.split("\t")
    if not contexts[noun].has_key(context):
        contexts[noun][context] = 1
    else:
        contexts[noun][context] += 1
for i in contexts:
    n = 0
    for j in contexts[i]:
        n += contexts[i][j]*contexts[i][j]
        #print i,j,contexts[i][j],n
    a = i + "\t"
    for j in contexts[i]:
        #print i,j,float(contexts[i][j])/float(n)
        a += j + ":" + str(math.sqrt(float(contexts[i][j]*float(contexts[i][j])))/math.sqrt(float(n))) + "\t"
    print a + "\n"
