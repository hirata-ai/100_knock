from test_63 import *
import re

r = re.compile("[0-9]")
(tfidf,freq,df) = tfidfscore()
n = 0
for i,j in sorted(tfidf.items(),key=lambda x:x[1],reverse=True):
    if r.search(i) == None:
        n += 1
        print i
    if n >= 100:
        break
