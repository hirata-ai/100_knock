#!/usr/bin/python
# -*- coding:utf-8 -*-

def sortword(imput):
    from collections import defaultdict
    addr = defaultdict(int)
    for line in imput:
        line = line.strip()
        addr[line] += 1
    for k,v in sorted(addr.items(),key=lambda x:x[1],reverse=True):
        print k,v

if __name__ == "__main__":
    import sys
    lines = []
    for line in open(sys.argv[1]):
        lines.append(line)
    sortword(lines)
