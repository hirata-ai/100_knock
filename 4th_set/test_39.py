#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
from kyotocabinet import *

db = DB()
# open the database
if not db.open("medline_db.kch", DB.OWRITER | DB.OCREATE):
    print >>sys.stderr, "open error: " + str(db.error())

for line in open(sys.argv[1]):
    line = line.strip()
    (prob,words) = line.split("\t",1)
    prob = float(prob)
    db[words] = prob

