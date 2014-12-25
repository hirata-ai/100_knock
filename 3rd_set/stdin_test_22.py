#!/usr/bin/python
#-*-coding:utf-8-*-
#re.splitで.→スペースでsplitしてから大文字判別
import sys
import re

r = re.compile("[A-Z]")
for line in sys.stdin:
    line = line.strip()
    if line != "":
        sent=re.split("\. ",line[:-1])
        for i in sent:
            if r.match(i[0]):
                print i + "."
