#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
for line in open(sys.argv[1]):
    line = line.strip()
    words = line.split()
    for i in words:
        if i[0]=="@":
            if i[-1] == ":":
                print i[:-1]
            else:
                print i
