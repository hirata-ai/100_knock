#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
for line in open(sys.argv[1]):
    line = line.strip()
    words = line.split()
    for i in words:
        if "@" in i:
            print i
