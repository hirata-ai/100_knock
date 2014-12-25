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

    return(sents)
    #for i in range(len(sents)):
    #    for j in range(len(sents[i])):
    #        print sents[i][j]

def noun_choice(sents):
    for sent in sents:
        noun_phrase = {}
        noun_phrase["phrase"] = ""
        noun_phrase["hpos"] = ""
        noun_phrase["fpos"] = ""
        noun_phrase["p_pos"] = ""
        noun_phrase["p_word"] = ""
        noun_phrase["m_pos"] = ""
        noun_phrase["pos_no"] = 0
        no = 0
        for token in sent:
            if token["chunk"] == "B-NP":
                if noun_phrase["phrase"] != "":
                    (articles,w_o,fw,hw) = article(noun_phrase["phrase"])
                    print sent[noun_phrase["pos_no"]]["w"]
                    print "# " + noun_phrase["phrase"]
                    print articles + " w[-1]=" + sent[noun_phrase["pos_no"]]["pos"] + " fw=" + fw +" fpos=" + noun_phrase["fpos"] + " w[0]=" + w_o.replace(" ","_") + " fw|fpos=" + fw + "|" + noun_phrase["fpos"] + " hw=" + hw + " hw|hpos=" + hw + "|" + noun_phrase["hpos"] + " pos[+1]=" + noun_phrase["p_pos"] + " hpos=" + noun_phrase["hpos"] + " pos[-1]=" + noun_phrase["m_pos"] + " w[+1]=" + noun_phrase["p_word"]
                noun_phrase["phrase"] = token["w"]
                noun_phrase["hpos"] = token["pos"]
                if no != 0:
                    noun_phrase["m_pos"] = sent[no-1]["pos"]
                if no+1 != len(sent):
                    noun_phrase["p_pos"] = sent[no+1]["pos"]
                    noun_phrase["p_word"] = sent[no+1]["w"]
                if token["w"] != "the" and token["w"] != "a" and token["w"] != "an":
                    noun_phrase["fpos"] = token["pos"]
                else:
                    noun_phrase["fpos"] = sent[no+1]["pos"]
                if no != 0:
                        noun_phrase["pos_no"] = no-1

            if token["chunk"] == "I-NP":
                noun_phrase["hpos"] = token["pos"]
                noun_phrase["phrase"] = noun_phrase["phrase"] + " " + token["w"]
                if no+1 != len(sent):
                    noun_phrase["p_pos"] = sent[no+1]["pos"]
                    noun_phrase["p_word"] = sent[no+1]["w"]

            no += 1
        if noun_phrase["phrase"] != "":
            (articles,w_o,fw,hw) = article(noun_phrase["phrase"])
            print "# " + noun_phrase["phrase"]
            print articles + " w[-1]=" + sent[noun_phrase["pos_no"]]["pos"] + " fw=" + fw +" fpos=" + noun_phrase["fpos"] + " w[0]=" + w_o .replace(" ","_")+ " fw|fpos=" + fw + "|" + noun_phrase["fpos"] + " hw=" + hw + " hw|hpos=" + hw + "|" + noun_phrase["hpos"] + " pos[+1]=" + noun_phrase["p_pos"] + " hpos=" + noun_phrase["hpos"] + " pos[-1]=" + noun_phrase["m_pos"] + " w[+1]=" + noun_phrase["p_word"]
 

def article(phrases):
    article_type = ""
    if " " in phrases:
        phrase = phrases.split(" ")
        if phrase[0] == "the":
            article_type = "THE"
        elif phrase[0] == "a":
            article_type = "A"
        elif phrase[0] == "an":
            article_type = "AN"
        else:
            article_type = "NONE"
        w_o = " ".join(phrase[1:])
        hw = phrase[len(phrase)-1]
        fw = phrase[1]
        return(article_type,w_o,fw,hw)
    else:
        article_type = "NONE"
        return(article_type,phrases,phrases,phrases)

if __name__ == "__main__":
    import sys
    sents = chunk(sys.argv[1])
    noun_choice(sents)
