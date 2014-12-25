#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import re
r1 = re.compile(u"[亜-熙]+（[A-Z]+）")
r2 = re.compile(u"[亜-熙]+\([A-Z]+\)")
for line in open(sys.argv[1]):
    line = line.decode("utf-8")
    line = line.strip()
    m = r1.search(line)
    n = r2.search(line)
    if m != None:
        print m.group(0).encode("utf-8")
    if n != None:
        print n.group(0).encode("utf-8")
