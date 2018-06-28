# tf-phishing-example

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
embedding_1 (Embedding)      (None, 255, 255)          10200
_________________________________________________________________
dropout_1 (Dropout)          (None, 255, 255)          0
_________________________________________________________________
lstm_1 (LSTM)                (None, 128)               196608
_________________________________________________________________
dropout_2 (Dropout)          (None, 128)               0
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 129
=================================================================
Total params: 206,937
Trainable params: 206,937
Non-trainable params: 0
_________________________________________________________________
None
Train on 27140 samples, validate on 9047 samples
Epoch 1/3
27140/27140 [==============================] - 588s 22ms/step - loss: 0.4016 - acc: 0.8198 - val_loss: 0.3427 - val_acc: 0.8597
Epoch 2/3
27140/27140 [==============================] - 587s 22ms/step - loss: 0.3302 - acc: 0.8574 - val_loss: 0.3198 - val_acc: 0.8624
Epoch 3/3
27140/27140 [==============================] - 587s 22ms/step - loss: 0.3116 - acc: 0.8676 - val_loss: 0.3047 - val_acc: 0.8760
12063/12063 [==============================] - 40s 3ms/step
Model Accuracy: 86.89%

real	30m5.305s
user	90m56.160s
sys	26m50.120s


$ bash test.sh
Using TensorFlow backend.
google.com: 0.195869
g00gle.com: 0.727469
paypal.com: 0.456698
secure-paypal.com: 0.905234
securitymywindowspcsystem.info: 0.997279
bank.wellsbankingsecurelogin.com: 0.739096
apple-gps-tracker.xyz: 0.992589


```
