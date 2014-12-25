#!/usr/bin/python
#-*-coding:utf-8-*-

#echo "AA" |python test_33.py inflection_dump.bin   で実行

def load_dic(input_data):
    import marshal
    inflection_dic = marshal.load(open(input_data))
    print "load complete"
    return(inflection_dic)

if __name__ == "__main__":
    import sys
    inflection_dic = load_dic(sys.argv[1])
    for word in sys.stdin:
        word = word.strip()
        if word in inflection_dic:
            if len(inflection_dic[word]) >= 3:
                print word,inflection_dic[word]
