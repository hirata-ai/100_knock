#!/usr/bin/python
#-*-coding:utf-8-*-
from test_54 import *
import sys

chunk_list = chunk_module(sys.argv[1])
for sent in chunk_list:
    for i in range(len(sent)):
        nouns = []
        #print sent[i].dst
        for j in sent[i].morph:
            if j.pos == "名詞":
                nouns.append(j.surface)
                #print j.surface
            else:
                if len(nouns) > 1:
                    print "".join(nouns)
                nouns = []
        if len(nouns) > 1:
            print "".join(nouns)
                #a += j.surface
        #for k in sent[int(sent[i].dst)].morph:
        #    if k.pos != "記号":
        #        b += k.surface
