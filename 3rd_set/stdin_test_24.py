#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import re

r = re.compile("[!-/:-@≠\[-`{-~]")
for line in sys.stdin:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if r.match(word[-1]):
            print word[:-1] + "\n" + word[-1]
        else:
            print word
    print ""
