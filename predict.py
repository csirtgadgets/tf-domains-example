#!/usr/bin/env python

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import sys
import os
import json
import pandas
import optparse
from keras.models import Sequential, load_model
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from pprint import pprint

BATCH_SIZE = os.getenv('TF_BATCHSIZE', 32)


def predict(log_entry):
    # tokenizer = Tokenizer(filters='\t\n', char_level=True)
    tokenizer = Tokenizer(filters='\t\n', char_level=True, lower=True, split='.')

    word_dict_file = os.path.join('build/word-dict.json')

    with open(word_dict_file) as F:
        txt = F.read()

    txt = json.loads(txt)
    tokenizer.word_index = txt

    seq = tokenizer.texts_to_sequences(log_entry)
    max_log_length = 255
    log_entry_processed = sequence.pad_sequences(seq, maxlen=max_log_length)

    model = load_model('model.h5')
    model.load_weights('weights.h5')
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    prediction = model.predict(log_entry_processed, batch_size=BATCH_SIZE)

    for idx, v in enumerate(log_entry):
        print("%s: %f" % (v, prediction[idx]))


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file', action="store", dest="file", help="data file")
    options, args = parser.parse_args()

    if options.file is not None:
        csv_file = options.file
    else:
        csv_file = 'training.csv'

    if args[0] is not None:
        predict(args[0].split(','))
