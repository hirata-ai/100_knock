#!/bin/bash

path=$(pwd)
path="${path}/cabocha_data/*"
#echo ${path}
for filepath in ${path}
do
		filename=$(basename $filepath)
		output="noun_data/${filename}.n"
		#echo ${output}
		python test_62.py ${filepath} > ${output}
done
