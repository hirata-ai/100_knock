#!/usr/bin/python
#-*-coding:utf-8-*-
import sys

print "graph sample{"
for line in open(sys.argv[1]):
    line = line.strip()
    words = line.split("\t")
    print "\t"+"\""+words[1]+"\" -- \""+words[2]+"\""
print "}"
