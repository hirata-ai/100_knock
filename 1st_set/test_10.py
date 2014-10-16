#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
from collections import defaultdict

addr = defaultdict(int)
for line in open(sys.argv[1]):
    line = line.strip()
    addr[line] += 1
for k,v in sorted(addr.items(),key=lambda x:x[1],reverse=True):
    print k,v
