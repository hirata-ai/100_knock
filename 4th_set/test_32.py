#!/usr/bin/python
# -*-coding:utf-8 -*-
from test_31 import *
import marshal

def marshaldic(input_data):
    inflection = inflection_dic(input_data)
    f = open("inflection_dump.bin","w")
    marshal.dump(inflection,f)

if __name__ == "__main__":
    import sys
    marshaldic(sys.argv[1])
