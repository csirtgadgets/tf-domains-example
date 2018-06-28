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
embedding_1 (Embedding)      (None, 255, 32)           1280
_________________________________________________________________
dropout_1 (Dropout)          (None, 255, 32)           0
_________________________________________________________________
lstm_1 (LSTM)                (None, 64)                24832
_________________________________________________________________
dropout_2 (Dropout)          (None, 64)                0
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 65
=================================================================
Total params: 26,177
Trainable params: 26,177
Non-trainable params: 0
_________________________________________________________________
None
Train on 27140 samples, validate on 9047 samples
Epoch 1/3
27140/27140 [==============================] - 273s 10ms/step - loss: 0.5120 - acc: 0.7460 - val_loss: 0.3662 - val_acc: 0.8395
Epoch 2/3
27140/27140 [==============================] - 268s 10ms/step - loss: 0.4000 - acc: 0.8283 - val_loss: 0.3562 - val_acc: 0.8432
Epoch 3/3
27140/27140 [==============================] - 268s 10ms/step - loss: 0.3759 - acc: 0.8397 - val_loss: 0.3373 - val_acc: 0.8574
12063/12063 [==============================] - 18s 1ms/step
Model Accuracy: 85.44%
(tf) h:tf-domains-example wes$ bash test.sh
Using TensorFlow backend.
google.com: 0.292872
g00gle.com: 0.707535
paypal.com: 0.571224
secure-paypal.com: 0.900945
securitymywindowspcsystem.info: 0.969256
bank.wellsbankingsecurelogin.com: 0.915325
apple-gps-tracker.xyz: 0.983738


```
