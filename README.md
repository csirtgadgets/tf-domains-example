# tf-phishing-example

Based on the outstanding work by:

https://medium.com/slalom-engineering/detecting-malicious-requests-with-keras-tensorflow-5d5db06b4f28

https://csirtgadgets.com/commits/2018/6/9/phishing-predictions-with-deep-learning-and-tensorflow

```bash
$ mkvirtualenv tf
$ pip install pandas tensorflow keras
$ time python train.py --file data.csv

Using TensorFlow backend.
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
embedding_1 (Embedding)      (None, 2083, 32)          2112
_________________________________________________________________
dropout_1 (Dropout)          (None, 2083, 32)          0
_________________________________________________________________
lstm_1 (LSTM)                (None, 64)                24832
_________________________________________________________________
dropout_2 (Dropout)          (None, 64)                0
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 65
=================================================================
Total params: 27,009
Trainable params: 27,009
Non-trainable params: 0
_________________________________________________________________
None
Train on 35129 samples, validate on 11710 samples
2018-06-09 10:10:30.992495: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
Epoch 1/3
35129/35129 [==============================] - 815s 23ms/step - loss: 0.4950 - acc: 0.7581 - val_loss: 0.3881 - val_acc: 0.8201
Epoch 2/3
35129/35129 [==============================] - 870s 25ms/step - loss: 0.3833 - acc: 0.8324 - val_loss: 0.3333 - val_acc: 0.8523
Epoch 3/3
35129/35129 [==============================] - 825s 23ms/step - loss: 0.3452 - acc: 0.8495 - val_loss: 0.3025 - val_acc: 0.8653
15613/15613 [==============================] - 57s 4ms/step
Model Accuracy: 86.99%

real	43m2.124s
user	131m15.837s
sys	42m0.835s

$ python predict.py http://raganinfotech.com/ow/adb/0016dc3e2b506150a88aebc589eb12f9
[0.9533803]

$ python predict.py http://dvxtmac.com/home/Validation/login.php?cmd=login_submit
[0.48320338]

$ ./predict.py https://google.com
[0.69641]

$ ./predict.py https://google.com/about-us
[0.03857325]

```
