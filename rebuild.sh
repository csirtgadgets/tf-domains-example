#!/bin/bash

set -e

cat data/whitelist2.txt | python build.py --good > whitelist.csv
cat data/blacklist.txt | python build.py > blacklist.csv
cat whitelist.csv blacklist.csv | gshuf > training.csv
python train.py
