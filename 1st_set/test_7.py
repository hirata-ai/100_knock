#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys

address = set()
for line in open(sys.argv[1]):
    words = line.split("\t")
    address.add(words[0])
print len(address)

# cut -f 1 <address.txt |sort | uniq |wc -l で確認
