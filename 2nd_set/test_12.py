#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
tweet_list = []
tweet = ""
for line in open(sys.argv[1]):
    line = line.decode("utf-8")
    if line != "\n":
        line = line.strip()
        tweet += line
    elif line == "\n":
        tweet_list.append(tweet)
        tweet = ""
for i in tweet_list:
    if u"なう" in i:
        print i.encode("utf-8")
