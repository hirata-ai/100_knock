#!/usr/bin/python
#-*-coding:utf-8-*-

def base_verb(input_data):
    base_list = []
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
                #print mecab["base"]
                base_list.append(mecab["base"])
    return(base_list)

if __name__ == "__main__":
    import sys
    base_list = base_verb(sys.argv[1])
    for line in base_list:
        print line
