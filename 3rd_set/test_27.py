#!/usr/bin/python
#-*-coding:utf-8-*-
#importするファイルの名前の最初が数字だと良くない。
import sys
from test import *

if __name__ == "__main__":
    lines = []
    for line in open(sys.argv[1]):
        lines.append(line)
    sortword(lines) 
