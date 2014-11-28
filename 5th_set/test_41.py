#!/usr/bin/python
#-*-coding:utf-8-*-

def mecab_dic(input_file):
    sentences = []
    sentence = []
    for line in open(input_file):
        mecab = {}
        line = line.strip()
        line = line.decode("utf-8")
        if line != "EOS":
            (word,morphs) = line.split("\t")
            morph  = morphs.split(",")
            #print word
            mecab["surface"] = word
            mecab["base"]    = morph[6]
            mecab["pos"]     = morph[0]
            mecab["pos1"]    = morph[1]
            sentence.append(mecab)

        else:
            sentence.append(mecab)
            sentences.append(sentence)
            sentence = []
    print sentences

if __name__ == "__main__":
    import sys
    mecab_dic(sys.argv[1])
