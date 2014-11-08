#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import re

for line in open(sys.argv[1]):
    line = line.strip()
    words = line.split(" ")
    for word in words:
        print word
