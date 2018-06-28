#!/bin/bash

set -e

rm -rf tmp
mkdir tmp

cat data/whitelist.txt | python build.py --good > tmp/whitelist.csv
cat data/blacklist.txt | python build.py > tmp/blacklist.csv
cat whitelist.csv blacklist.csv | gshuf > tnp/training.csv
python train.py
