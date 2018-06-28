#!/usr/bin/env python

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import os
import json
import optparse
from keras.models import load_model
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from pprint import pprint

from constants import MAX_STRING_LEN, MODEL, WEIGHTS, BATCH_SIZE


def predict(i):
    tokenizer = Tokenizer(filters='\t\n', char_level=True, lower=True)

    word_dict_file = os.path.join('build/word-dict.json')

    with open(word_dict_file) as F:
        txt = F.read()

    txt = json.loads(txt)
    tokenizer.word_index = txt

    seq = tokenizer.texts_to_sequences(i)
    i_processed = sequence.pad_sequences(seq, maxlen=MAX_STRING_LEN)

    model = load_model(MODEL)
    model.load_weights(WEIGHTS)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    prediction = model.predict(i_processed, batch_size=BATCH_SIZE)

    for idx, v in enumerate(i):
        print("%s: %f" % (v, prediction[idx]))


if __name__ == '__main__':
    parser = optparse.OptionParser()
    options, args = parser.parse_args()

    if args[0] is not None:
        predict(args[0].split(','))
