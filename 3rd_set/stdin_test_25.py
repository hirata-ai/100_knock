#!/usr/bin/python
#-*-coding:utf-8-*-
import sys

for line in sys.stdin:
    line = line.strip()
    print line + "\t" + line.lower()
