#!/usr/bin/python
#-*-coding:utf-8-*-
def tfidfscore():
    import glob
    import sys
    import math
    from collections import defaultdict
    freq = defaultdict(int) 
    freq_doc = {}
    df = defaultdict(int)
    file_no = 0
    tfidf = {}
    for i in glob.glob("noun_data/*.n"):
        file_no += 1
        for line in open(i):
            line = line.strip()
            freq[line] += 1
            freq_doc[line] = 1
        for j in freq_doc:
            df[j] += 1    
        freq_doc = {}
    for k in freq:
        idf = float(math.log(file_no/df[k],2))
        tfidf[k] = freq[k]*idf
        #print k,freq[k]*idf,freq[k],df[k]
    return(tfidf,freq,df)
    #for k,v in sorted(df.items(),key=lambda x:x[1]):
    #    print k,v
    #print file_no

if __name__ == "__main__":
    (tfidf,freq,df) = tfidfscore()
    for i in tfidf:
        print i,tfidf[i],freq[i],df[i]
