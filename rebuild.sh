#!/bin/bash

set -e

rm -rf tmp
mkdir tmp

cat data/whitelist.txt | python build.py --good > tmp/whitelist.csv
cat data/blacklist.txt | python build.py > tmp/blacklist.csv
cat tmp/whitelist.csv tmp/blacklist.csv | gshuf > tmp/training.csv
time python train.py
