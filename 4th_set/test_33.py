#!/usr/bin/python
#-*-coding:utf-8-*-

#echo "AA" |python test_33.py inflection_dump.txt   で実行

def load_dic(input_data,word):
    import marshal
    inflection_dic = marshal.load(open(input_data))
    #for line in open(medline_txt):
    #    line = line.strip()
    #    words = line.split("\t")
    #    for word in words:
    #        if word in inflection_dic:
    #            print word,inflection_dic[word]
    if word in inflection_dic:
        print word,inflection_dic[word]
    else:
        print word
        print "error"

if __name__ == "__main__":
    import sys
    for word in sys.stdin:
        word = word.strip()
        load_dic(sys.argv[1],word)
