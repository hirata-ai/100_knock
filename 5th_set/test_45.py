#!/usr/bin/python
#-*-coding:utf-8-*-

def of_pair(input_data):
    sent = []
    sent_list = []
    for line in open(input_data):  #mecabにかけた文章を入力
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
            sent.append((mecab["surface"],mecab["pos"]))
        elif line == "EOS":
            for i in range(len(sent)-2):
                if sent[i][1] == u"名詞" and sent[i+1][0] == u"の" and sent[i+2][1] == u"名詞":
                    a = sent[i][0].encode("utf-8")+"\t"+sent[i+1][0].encode("utf-8")+"\t"+sent[i+2][0].encode("utf-8")
                    #print a
                    sent_list.append(a)
            sent = []
    return(sent_list)

if __name__ =="__main__":
    import sys
    sent = of_pair(sys.argv[1])
    for line in sent:
        print line
