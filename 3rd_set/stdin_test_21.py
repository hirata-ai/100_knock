#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
for line in sys.stdin:
    line = line.strip()
    sent = line.split(".")
    for i in sent:
        print i+(".")
