#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys

add = {}
i = 1
N = int(sys.argv[2])
for line in open(sys.argv[1]):
    line = line.strip()
    add[i] = line
    i += 1

for a in range(len(add)-N,len(add)):
    print add[a]
