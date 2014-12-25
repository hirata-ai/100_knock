#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from collections import defaultdict

def count_freq(input_data):
    word_freq = defaultdict(int)
    for line in input_data:
        line = line.strip()
        word_freq[line] += 1
    for i in word_freq:
        print str(word_freq[i]) +"\t"+ i

if __name__ == "__main__":
    lines = sys.stdin
    count_freq(lines)
