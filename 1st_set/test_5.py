#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
i = int(sys.argv[2])
a = 0
for line in open(sys.argv[1]):
    line = line.strip()
    print line
    a += 1
    if a == i:
        break
