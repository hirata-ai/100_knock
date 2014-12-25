#!/bin/bash

path=$(pwd)
path="${path}/data/e*"
#echo ${path}
for filepath in ${path}
	do
			filename=$(basename $filepath .txt)
			output1="22_${filename}.txt"
			output2="${filename}_genia.txt"
			a="genia_data/${output1}"
			echo ${a}
			#python test_22.py ${filepath} > "genia_data/${output1}"
			
	done
