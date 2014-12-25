#!/usr/bin/python
#-*-coding:utf-8-*-
import argparse 
from test_42 import *
from test_43 import *
from test_44 import *
from test_45 import *
from test_46 import *

def print_list(text):
    if text != None:
        for line in text:
            print line

parser = argparse.ArgumentParser(description="Choice 42-46")
parser.add_argument("-v","--verb")    #(42)
parser.add_argument("-b","--base")    #(43)
parser.add_argument("-n","--noun")    #(44)
parser.add_argument("-o","--AofB")    #(45)
parser.add_argument("-c","--chain")   #(46)
options,args = parser.parse_args()
if options.verb != None:
    verb_list = verb_picup(options.verb)
    print_list(verb_list)
if options.base != None:
    base_list = base_verb(options.base)
    print_list(base_list)
if options.noun != None:
    form_list = base_form(options.noun)
    print_list(form_list)
if options.AofB != None:
    pair_list = of_pair(options.AofB)
    print_list(pair_list)
if options.chain != None:
    chain_list = noun_chain(options.chain)
    freq_count(chain_list)
