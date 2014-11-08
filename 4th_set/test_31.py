#!/usr/bin/python
#-*-coding:utf-8-*-

# echo "Christmas ferns"| python test_31.py inflection.table.txt で実行

def inflection_dic(input_file):
    from collections import defaultdict
    inflection = {}
    freq = defaultdict(int)
    for line in open(input_file):
        words = line.split("|")
        freq[words[0]]+=1
        if words[0] not in inflection:
            inflection[words[0]] = [(words[1],words[3],words[6])]
        else:
            inflection[words[0]].append((words[1],words[3],words[6]))
    return(inflection)

def print_inflection(inflection):
    for i in inflection:
        print i,inflection[i]

def print_inflectionword(word,inflection):
    print word,inflection[word]

if __name__ == "__main__":
    import sys
    inflection = inflection_dic(sys.argv[1])
    for word in sys.stdin:
        word = str(word)
        word = word.strip()
        #print_inflection(inflection)
        print_inflectionword(word,inflection)
