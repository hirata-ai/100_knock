#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from collections import defaultdict

context = {}
cluster = []
for line in open(sys.argv[1]):
    line = line.strip()
    (score,words) = line.split("\t",1)
    context[words] = score
    word = words.split("\t")
    for i in word:
        if i not in cluster:
            cluster.append((i,))

for i in context:
    if len(cluster) > 1:
        a = max(context.items(),key=lambda x:x[1])[0]
        words = a.split("\t")
        for j in range(len(cluster)):
            n = 0
            for k in range(len(cluster[j])):
                for l in words:
                    if cluster[j][k] in l:
                        if n == 0:
                            new_cluster = cluster[j]
                            no_1 = j
                            n += 1
                        else:
                            new_cluster += cluster[j]
                            no_2 = j
            #print no_2
            #cluster.pop(no_0)
            #cluster.pop(no_2)
            #cluster.append(new_cluster)
        context[a] = 0
    elif len(cluster) == 1:
        break
print len(cluster)
