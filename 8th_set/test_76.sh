#!/bin/bash

for i in genia_data/*;
do 
    python test_75.py $i > learning_data/`basename $i`;
done
