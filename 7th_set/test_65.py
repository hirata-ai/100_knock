#!/usr/bin/python
#-*-coding:utf-8-*-
from test_54 import *
import sys
import glob

nouns_100 = []
for line in sys.stdin:
    line = line.strip()
    nouns_100.append(line)

for i in glob.glob("cabocha_data/*"):
    chunk_list = chunk_module(i)
    for sent in chunk_list:
        for j in range(len(sent)):
            nouns = []
            #print sent[i].dst
            for k in sent[j].morph:
                if k.pos == "名詞":
                    nouns.append(k.surface)
                    #print j.surface
                else:
                    if len(nouns) > 1:
                        a = "".join(nouns)
                        if a in nouns_100:
                            #print a,sent[int(sent[j].dst)].morph
                            for b in sent[int(sent[j].dst)].morph:
                                if b.pos == "名詞" or b.pos == "動詞" or b.pos == "形容詞":
                                    print a + "\t-> " + b.base
                            for c in sent[j].srcs:
                                for d in sent[int(c)].morph:
                                    if b.pos == "名詞" or b.pos == "動詞" or b.pos == "形容詞":
                                        print a + "\t <- " + d.base
                    nouns = []
            if len(nouns) > 1:
                a = "".join(nouns)
                if a in nouns_100:
                    for i in sent[int(sent[j].dst)].morph:
                        if b.pos == "名詞" or b.pos == "動詞" or b.pos == "形容詞":
                            print a + "\t-> " + b.base
