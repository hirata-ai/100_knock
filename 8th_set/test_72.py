#!/usr/bin/python
#-*-coding:utf-8-*-
import sys

def chunk(imput_data):
    sent = []
    sents = []
    for line in open(sys.argv[1]):
        token = {}
        line = line.strip()
        if line != "":
            words = line.split("\t")
            token["w"] = words[0]
            token["lem"] = words[1]
            token["pos"] = words[2]
            token["chunk"] = words[3]
            sent.append(token)
        elif line == "":
            sents.append(sent)
            sent = []
    for i in range(len(sents)):
        for j in range(len(sents[i])):
            print sents[i][j]

if __name__ == "__main__":
    import sys
    chunk(sys.argv[1])
