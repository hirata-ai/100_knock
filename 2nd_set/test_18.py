#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import re
r = re.compile(u".{3}市")
for line in open(sys.argv[1]):
    line = line.decode("utf-8")
    m = r.search(line)
    if m != None:
        print m.group(0).encode("utf-8")
