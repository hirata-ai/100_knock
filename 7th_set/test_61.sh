#!/bin/bash

for i in data/*
do
        a=`basename ${i}`
		cabocha -f1 $i > cabocha_data/$a
done
