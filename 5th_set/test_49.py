#!/usr/bin/python
#-*-coding:utf-8-*-
from optparse import OptionParser
from test_42 import *
from test_43 import *
from test_44 import *
from test_45 import *
from test_46 import *

def freq_count(text):
    from collections import defaultdict
    import matplotlib.pyplot as plt
    freq = defaultdict(int)
    value_freq = defaultdict(int)
    a = []
    if text != None:
        for line in text:
            freq[line] += 1
        
        for i in freq:
            a.append(freq[i])
        plt.hist(a,bins=100,range=(0,50))
        plt.savefig("output_49.png")
        plt.show()

parser = OptionParser()
parser.add_option("-v","--verb")    #(42)
parser.add_option("-b","--base")    #(43)
parser.add_option("-n","--noun")    #(44)
parser.add_option("-o","--AofB")    #(45)
parser.add_option("-c","--chain")   #(46)
options,args = parser.parse_args()
if options.verb != None:
    verb_list = verb_picup(options.verb)
    freq_count(verb_list)
if options.base != None:
    base_list = base_verb(options.base)
    freq_count(base_list)
if options.noun != None:
    form_list = base_form(options.noun)
    freq_count(form_list)
if options.AofB != None:
    pair_list = of_pair(options.AofB)
    freq_count(pair_list)
if options.chain != None:
    chain_list = noun_chain(options.chain)
    freq_count(chain_list)
