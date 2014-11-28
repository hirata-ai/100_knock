#!/usr/bin/python
#-*-coding:utf-8-*-

def verb_picup(input_data):
    verb_list = []
    for line in open(input_data):
        mecab = {}
        line = line.strip()
        line = line.decode("utf-8")
        if line != "EOS":
            (word,morph) = line.split("\t")
            words = morph.split(u",")
            mecab["surface"] = word
            mecab["base"] = words[6]
            mecab["pos"] = words[0]
            mecab["pos1"] = words[1]
            if mecab["pos"] == u"動詞":
                verb_list.append(mecab["surface"])
                print mecab["surface"]
    return(verb_list)

if __name__ == "__main__":
    import sys
    verb_picup(sys.argv[1])
