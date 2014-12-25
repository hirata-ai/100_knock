#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import re

r1 = re.compile(".+ly")
r2 = re.compile(".+ness")
for line in sys.stdin:
    line = line.strip()
    if r1.match(line) or r2.match(line):
        print line
