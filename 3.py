#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
f1 = open("col1.txt","w")
f2 = open("col2.txt","w")

for line in open(sys.argv[1]):
    (col1,col2) = line.split("\t")
    f1.write("%s\n" % col1)
    f2.write("%s" % col2)
