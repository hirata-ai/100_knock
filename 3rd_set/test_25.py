#!/usr/bin/python
#-*-coding:utf-8-*-
import sys

for line in open(sys.argv[1]):
    line = line.strip()
    print line + "\t" + line.lower()
