#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import re

r = re.compile("[!-/:-@≠\[-`{-~]")
for line in open(sys.argv[1]):
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if r.match(word[-1]):
            print word[:-1] + "\n" + word[-1]
        else:
            print word
