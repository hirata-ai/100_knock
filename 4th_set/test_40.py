#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from kyotocabinet import *

db = DB()

# open the database
if not db.open("medline_db.kch", DB.OREADER):
    print >>sys.stderr, "open error: " + str(db.error())

score = 1
for line in sys.stdin:
    line = line.strip()
    words = line.split(" ")
    for i in range(len(words)-1):
        word = "%s\t%s" % (words[i],words[i+1])
        if word in db:
            score *= db[word]
        else:
            score *= 0
    print score
