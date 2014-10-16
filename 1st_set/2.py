#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
f = open("1-2_result.txt","w")
for line in open(sys.argv[1]):
    line = line.strip()
    line = line.replace("\t"," ")
    f.write("%s\n" % line)
