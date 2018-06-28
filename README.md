# tf-suspect-domains-example

Based on the outstanding work by:

https://medium.com/slalom-engineering/detecting-malicious-requests-with-keras-tensorflow-5d5db06b4f28

https://csirtgadgets.com/commits/2018/6/9/phishing-predictions-with-deep-learning-and-tensorflow

```bash
$ mkvirtualenv tf
$ pip install pandas tensorflow keras
$ time bash rebuild.sh
Using TensorFlow backend.
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
embedding_1 (Embedding)      (None, 255, 32)           1280
_________________________________________________________________
dropout_1 (Dropout)          (None, 255, 32)           0
_________________________________________________________________
lstm_1 (LSTM)                (None, 128)               82432
_________________________________________________________________
dropout_2 (Dropout)          (None, 128)               0
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 129
=================================================================
Total params: 83,841
Trainable params: 83,841
Non-trainable params: 0
_________________________________________________________________
None
Train on 27140 samples, validate on 9047 samples
Epoch 1/3
2018-06-28 12:00:46.329387: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
27140/27140 [==============================] - 64s 2ms/step - loss: 0.6195 - acc: 0.6618 - val_loss: 0.4532 - val_acc: 0.7954
Epoch 2/3
27140/27140 [==============================] - 63s 2ms/step - loss: 0.4753 - acc: 0.7798 - val_loss: 0.3749 - val_acc: 0.8363
Epoch 3/3
27140/27140 [==============================] - 63s 2ms/step - loss: 0.4182 - acc: 0.8138 - val_loss: 0.3565 - val_acc: 0.8407
12063/12063 [==============================] - 6s 519us/step
Model Accuracy: 84.60%

real	3m18.579s
user	13m14.356s
sys	    4m59.391s



$ bash test.sh
google.com: 0.268851
g00gle.com: 0.644312
paypal.com: 0.462150
secure-paypal.com: 0.854046
securitymywindowspcsystem.info: 0.963942
bank.wellsbankingsecurelogin.com: 0.946198
apple-gps-tracker.xyz: 0.957657

```
