#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
for line in open(sys.argv[1]):
    words = line.split(".")
    for i in words:
        print i+(".")
