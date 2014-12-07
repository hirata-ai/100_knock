#!/usr/bin/python
#-*-coding:utf-8-*-
from test_54 import *
import sys

chunk_list = chunk_module(sys.argv[1])
for sent in chunk_list:
    for i in range(len(sent)):
        if sent[i].dst != "-1":
            print sent[i].no
            a = ""
            b = ""
            noun = 0
            verb = 0
            for j in sent[i].morph:
                if j.surface != "、" and j.surface != "。":
                    a += j.surface
                if j.pos == "名詞" and j.pos1 != "非自立":
                    noun = 1
            if noun == 0:
                continue
            for k in sent[int(sent[i].dst)].morph:
                if k.surface != "、" and k.surface != "。":
                    b += k.surface
                if k.pos in "動詞" and k.pos1 != "非自立":
                    verb = 1
            if verb == 0:
                continue
            print a + "\t" + b
