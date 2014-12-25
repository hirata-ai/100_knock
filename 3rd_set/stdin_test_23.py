#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import re

for line in sys.stdin:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        print word
    print ""
