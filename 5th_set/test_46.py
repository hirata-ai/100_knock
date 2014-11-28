#!/usr/bin/python
#-*-coding:utf-8-*-

def noun_chain(input_data):
    noun = []
    noun_list = []
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
            if mecab["pos"] == u"名詞":
                noun.append(mecab["surface"])
            else:
                if len(noun) >= 2:
                    #print "\t".join(noun)
                    noun_list.append("\t".join(noun))
                noun = []
        else:
            noun = []
    return(noun_list)

if __name__ == "__main__":
    import sys
    noun = noun_chain(sys.argv[1])
    for line in noun:
        print line
