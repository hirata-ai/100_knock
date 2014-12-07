#!/usr/bin/python
#-*-coding:utf-8-*-

#53とほぼ同じ

def chunk_module(input_data):
    class Morph:
        def __init__(self,word,base,pos,pos1):
            self.surface = word
            self.base    = base
            self.pos     = pos
            self.pos1    = pos1

    class Chunk:
        def __init__(self,morphs,no,dst,srcs):
            self.morph = morphs
            self.dst   = dst
            self.srcs  = srcs 
            self.no    = no
            #print self.dst
     
    morphs = []
    index = []
    srcs = []
    chunks = []
    chunk_sentence = []
    for line in open(input_data):
        line = line.strip()
        if line == "EOS":
            chunk = Chunk(morphs,no,dst,srcs)
            chunks.append(chunk)
            chunk_sentence.append(chunks)
            chunks =[]
            index = []
            srcs = []
            morphs = []
        if line[0:2] == "* ":
            if len(morphs) != 0:
                chunk = Chunk(morphs,no,dst,srcs)
                chunks.append(chunk)
            words = line.split()
            srcs = []
            morphs = []
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
    return(chunk_sentence)

if __name__ == "__main__":
    import sys
    a = chunk_module(sys.argv[1])
    print a
