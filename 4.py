#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
col1 = []
col2 = []
f = open("restore.txt","w")
for line in open(sys.argv[1]):
    line = line.strip()
    col1.append(line)

for line in open(sys.argv[2]):
    line = line.strip()
    col2.append(line)

for line3 in zip(col1,col2):
    line = "\t".join(line3)
    f.write("%s\n" % line)
