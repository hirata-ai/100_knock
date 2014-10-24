#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import re
r = re.compile("[亜-煕]+県.+市")
for line in open(sys.argv[1]):
    m = r.search(line)
    if m != None:
        print m.group(0)
