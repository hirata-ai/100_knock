#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from collections import defaultdict

def cal_probability(medline_text,bigram_file):
    word = defaultdict(int)
    bi_gram = {}
    for line in open(medline_text):
        line = line.strip()
        word[line] += 1
        
    for line in open(bigram_file):
        line = line.strip()
        words = line.split("\t",1)
        bi_gram[words[1]] = words[0]

    for i in bi_gram:
        uni = i.split("\t")
        prob = float(bi_gram[i])/word[uni[0]]
        print str(prob) + "\t" + i

if __name__ == "__main__":
    cal_probability(sys.argv[1],sys.argv[2])
