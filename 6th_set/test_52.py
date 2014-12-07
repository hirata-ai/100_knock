#!/usr/bin/python
#-*-coding:utf-8-*-

import sys

class Morph:
    def __init__(self,word,base,pos,pos1):
        self.surface = word
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

morphs = []
for line in open(sys.argv[1]):
    line = line.strip()
    if line[0:2] != "* " and line != "EOS":
        (word,feature) = line.split("\t")
        features = feature.split(",")
        morph = Morph(word,features[6],features[0],features[1])
        morphs.append(morph) 
    if line == "EOS":
        for morph in morphs:
            print morph.base
        morphs = []
        continue

#if __name__ == "__main__":
#    import sys

