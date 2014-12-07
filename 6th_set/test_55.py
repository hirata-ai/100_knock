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
            for j in sent[i].morph:
                if j.pos != "記号":
                    a += j.surface
            for k in sent[int(sent[i].dst)].morph:
                if k.pos != "記号":
                    b += k.surface
            print a + "\t" + b
