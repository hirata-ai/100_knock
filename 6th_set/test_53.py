#!/usr/bin/python
#-*-coding:utf-8-*-

class Morph:
    def __init__(self,word,base,pos,pos1):
        self.surface = word
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

class Chunk:
    def __init__(self,morphs,dst,srcs):
        self.morph = morphs
        self.dst   = dst
        self.srcs  = srcs 

if __name__ == "__main__":
    import sys
    morphs = []
    index = []
    srcs = []
    chunks = []
    for line in open(sys.argv[1]):
        line = line.strip()
        if line == "EOS":
            chunk = Chunk(morphs,dst,srcs)
            chunks.append(chunk)
            #chunks =[]
            index = []
            srcs = []
            morphs = []
        if line[0:2] == "* ":
            if len(morphs) != 0:
                chunk = Chunk(morphs,dst,srcs)
                chunks.append(chunk)
            words = line.split()
            srcs = []
            no = words[1]                   #文節番号
            dst = words[2][:-1]             #係り先番号
            index.append((words[1],dst))
            if len(index) != 0:
                for i in index:
                    if i[1] == no:
                        srcs.append(i[0])
            
        elif line[0:2] != "* " and line != "EOS":
            (word,feature) = line.split()
            features = feature.split(",")
            morph = Morph(word,features[6],features[0],features[1])
            morphs.append(morph)

    for chunk in chunks:
        print chunk.dst
