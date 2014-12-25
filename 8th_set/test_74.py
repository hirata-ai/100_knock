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
        noun_phrase = ""
        for token in sent:
            if token["chunk"] == "B-NP":
                if noun_phrase != "":
                    articles = article(noun_phrase)
                    print "# " + noun_phrase
                    print articles
                noun_phrase = token["w"]
            if token["chunk"] == "I-NP":
                noun_phrase = noun_phrase + " " + token["w"]
        if noun_phrase != "":
            articles = article(noun_phrase)
            print "# " + noun_phrase
            print articles

def article(phrases):
    if " " in phrases:
        phrase = phrases.split(" ")
        if phrase[0] == "the":
            return("THE")
        if phrase[0] == "a":
            return("A")
        if phrase[0] == "an":
            return("AN")

if __name__ == "__main__":
    import sys
    sents = chunk(sys.argv[1])
    noun_choice(sents)
