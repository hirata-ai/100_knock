#/usr/bin/python
# -*- coding:utf-8 -*-
import sys

addr = []
for line in open(sys.argv[1]):
    words = line.split("\t")
    addr.append(words)

for add in sorted(addr,key=lambda x:(x[1],x[0]),reverse=True):
    add[1] = add[1].strip()
    print("%s\t%s"%(add[0],add[1]))
