#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import re
r = re.compile(u"[ぁ-んァ-ヴ]")
for line in open(sys.argv[1]):
    line = line.strip()
    if "RT" in line:
        (word,RT) = line.split("RT",1)
        print RT
