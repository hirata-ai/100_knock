#!/usr/bin/python
#-*-coding:utf-8-*-
from test_54 import *
import sys

chunk_list = chunk_module(sys.argv[1])
for sent in chunk_list:
    for i in range(len(sent)):
        if len(sent[i].srcs) > 1:
            print sent[i].srcs
            b = ""
            for j in sent[i].morph:
                b += j.surface
            print b + "\n"
            for src in sent[i].srcs:
                a = ""
                for k in sent[int(src)].morph:
                    a += k.surface
                print a
