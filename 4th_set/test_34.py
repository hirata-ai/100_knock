#!/usr/bin/python
#-*-coding:utf-8-*-

def load_dic(input_data,medline_txt):
    import marshal
    inflection_dic = marshal.load(open(input_data))
    for line in open(medline_txt):
        line = line.strip()
        words = line.split("\t")
        for word in words:
            if word not in inflection_dic:
                print word

if __name__ == "__main__":
    import sys
    load_dic(sys.argv[1],sys.argv[2])
