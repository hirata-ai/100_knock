#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
word_count = 0
for line in open(sys.argv[1]):
    word_count += 1
print word_count
