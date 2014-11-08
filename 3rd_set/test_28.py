#!/usr/bin/python
#-*-coding:utf-8-*-

if __name__ == "__main__":
    import sys
    import glob
    from test import *
    words = []
    lines = []
    f = open("result.txt","w")
    for line in open(sys.argv[1]):
        line = line.strip()
        words.append(line)
    for i in range(len(words)):
        if i != len(words)-1:
            #print words[i] +"\t" + words[i+1]
            #f.write("%s\t%s\n"%(words[i],words[i+1]))
            lines.append("%s\t%s\n"%(words[i],words[i+1]))
    sortword(lines)
