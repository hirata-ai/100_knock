#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import re
r = re.compile(r".+さん")
for line in open(sys.argv[1]):
    line = line.strip()
    m = r.search(line)
    if m != None:
        print m.group(0)
