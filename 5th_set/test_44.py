#!/usr/bin/python
#-*-coding:utf-8-*-

def base_form(input_data):
    form_list = []
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
            if mecab["pos1"] == u"サ変接続":
                #print mecab["serface"]
                form_list.append(mecab["surface"])
    return(form_list)

if __name__ == "__main__":
    import sys
    form_list = base_form(sys.argv[1])
    if form_list != None:
        for line in form_list:
            print line
