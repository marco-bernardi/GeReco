# Test Data

## Static gestures 

## data set rock, paper, ...
Test loss:0.49700918793678284, Test accuracy:0.7083333134651184

Modello con lr=0.003 e dropout=0.2:
Test loss:0.4362185001373291, Test accuracy:0.75

-hagrid ridotto (contesto del corpo)
Test loss:0.25240442156791687, Test accuracy:0.9074074029922485

Modello con lr=0.003 e dropout=0.2:
Test loss:0.3453475832939148, Test accuracy:0.9074074029922485


-hagrid ridotto con none + cartelle delle gesture effettive
Modello con lr=0.003 e dropout=0.2:
Test loss:0.20843610167503357, Test accuracy:0.876447856426239

- training e validation random data augmentation, test su hagrid ridotto con none + cartelle delle gesture effettive
Modello con lr=0.003 e dropout=0.2:
Test loss:0.2519017457962036, Test accuracy:0.8610038757324219

Modello con lr=0.005 e dropout=0.2:
Test loss:0.2519017457962036, Test accuracy:0.85

Modello con lr=0.01 e dropout=0.2:
Test loss:0.3023953437805176, Test accuracy:0.8571428656578064

learning_rate=0.003, export_dir="exported_model_2", epochs=10, gamma=3
Test loss:0.3023953437805176, Test accuracy:0.8571428656578064

learning_rate=0.003, export_dir="exported_model_2", epochs=10, batch_size=6 dropout_rate=0.2
Test loss:0.23528344929218292, Test accuracy:0.8532818555831909]

- training random data augmentation, validation e test su hagrid ridotto con none + cartelle delle gesture effettive

learning_rate=0.003, export_dir="exported_model_2", epochs=10, batch_size=6 dropout_rate=0.2
Test loss:0.1824459731578827, Test accuracy:0.8803088665008545 	-> THE BEST 

### Training on Hagrid dataset with 1000 examples per label + 1000 data augmentation per label = 2000 examples per label

**Model config:**
```
hparams = gesture_recognizer.HParams(learning_rate=0.001,export_dir="exported_model_2", epochs=15, shuffle=True, batch_size=16, gamma=3)
model_options = gesture_recognizer.ModelOptions(dropout_rate=0.1,layer_widths=[256, 128])
```

**Training results:**

```
Model: "model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 hand_embedding (InputLayer  [(None, 128)]             0         
 )                                                               
                                                                 
 batch_normalization (Batch  (None, 128)               512       
 Normalization)                                                  
                                                                 
 re_lu (ReLU)                (None, 128)               0         
                                                                 
 dropout (Dropout)           (None, 128)               0         
                                                                 
 custom_gesture_recognizer_  (None, 256)               33024     
 0 (Dense)                                                       
                                                                 
 batch_normalization_1 (Bat  (None, 256)               1024      
 chNormalization)                                                
                                                                 
 re_lu_1 (ReLU)              (None, 256)               0         
                                                                 
 dropout_1 (Dropout)         (None, 256)               0         
                                                                 
 custom_gesture_recognizer_  (None, 128)               32896     
 1 (Dense)                                                       
                                                                 
 batch_normalization_2 (Bat  (None, 128)               512       
 chNormalization)                                                
                                                                 
 re_lu_2 (ReLU)              (None, 128)               0         
                                                                 
 dropout_2 (Dropout)         (None, 128)               0         
                                                                 
 custom_gesture_recognizer_  (None, 6)                 774       
 out (Dense)                                                     
                                                                 
=================================================================
Total params: 68742 (268.52 KB)
Trainable params: 67718 (264.52 KB)
Non-trainable params: 1024 (4.00 KB)
_________________________________________________________________
None
Epoch 1/15
425/425 [==============================] - 13s 25ms/step - loss: 0.2912 - categorical_accuracy: 0.7694 - val_loss: 0.1842 - val_categorical_accuracy: 0.8298 - lr: 0.0010
Epoch 2/15
425/425 [==============================] - 10s 24ms/step - loss: 0.2192 - categorical_accuracy: 0.8074 - val_loss: 0.1803 - val_categorical_accuracy: 0.8592 - lr: 9.9000e-04
Epoch 3/15
425/425 [==============================] - 8s 19ms/step - loss: 0.1986 - categorical_accuracy: 0.8193 - val_loss: 0.1771 - val_categorical_accuracy: 0.8615 - lr: 9.8010e-04
Epoch 4/15
425/425 [==============================] - 10s 22ms/step - loss: 0.2004 - categorical_accuracy: 0.8191 - val_loss: 0.1750 - val_categorical_accuracy: 0.8533 - lr: 9.7030e-04
Epoch 5/15
425/425 [==============================] - 10s 24ms/step - loss: 0.1864 - categorical_accuracy: 0.8284 - val_loss: 0.1612 - val_categorical_accuracy: 0.8521 - lr: 9.6060e-04
Epoch 6/15
425/425 [==============================] - 9s 22ms/step - loss: 0.1792 - categorical_accuracy: 0.8379 - val_loss: 0.1569 - val_categorical_accuracy: 0.8568 - lr: 9.5099e-04
Epoch 7/15
425/425 [==============================] - 8s 19ms/step - loss: 0.1772 - categorical_accuracy: 0.8321 - val_loss: 0.1673 - val_categorical_accuracy: 0.8545 - lr: 9.4148e-04
Epoch 8/15
425/425 [==============================] - 10s 24ms/step - loss: 0.1774 - categorical_accuracy: 0.8365 - val_loss: 0.1575 - val_categorical_accuracy: 0.8674 - lr: 9.3207e-04
Epoch 9/15
425/425 [==============================] - 10s 24ms/step - loss: 0.1635 - categorical_accuracy: 0.8450 - val_loss: 0.1541 - val_categorical_accuracy: 0.8674 - lr: 9.2274e-04
Epoch 10/15
425/425 [==============================] - 10s 23ms/step - loss: 0.1639 - categorical_accuracy: 0.8450 - val_loss: 0.1620 - val_categorical_accuracy: 0.8638 - lr: 9.1352e-04
Epoch 11/15
425/425 [==============================] - 10s 24ms/step - loss: 0.1600 - categorical_accuracy: 0.8482 - val_loss: 0.1551 - val_categorical_accuracy: 0.8732 - lr: 9.0438e-04
Epoch 12/15
425/425 [==============================] - 8s 19ms/step - loss: 0.1658 - categorical_accuracy: 0.8428 - val_loss: 0.1540 - val_categorical_accuracy: 0.8732 - lr: 8.9534e-04
Epoch 13/15
425/425 [==============================] - 10s 24ms/step - loss: 0.1627 - categorical_accuracy: 0.8438 - val_loss: 0.1514 - val_categorical_accuracy: 0.8685 - lr: 8.8638e-04
Epoch 14/15
425/425 [==============================] - 10s 24ms/step - loss: 0.1609 - categorical_accuracy: 0.8466 - val_loss: 0.1485 - val_categorical_accuracy: 0.8756 - lr: 8.7752e-04
Epoch 15/15
425/425 [==============================] - 8s 20ms/step - loss: 0.1517 - categorical_accuracy: 0.8529 - val_loss: 0.1513 - val_categorical_accuracy: 0.8732 - lr: 8.6875e-04
```

**Test results:**

Test loss:0.12592071294784546, Test accuracy:0.8873239159584045

---

**Model config:**

```
hparams = gesture_recognizer.HParams(learning_rate=0.001, export_dir="exported_model_2", epochs=15, shuffle=True, batch_size=32, gamma=3)
model_options = gesture_recognizer.ModelOptions(dropout_rate=0.1, layer_widths=[256, 128])
```

**Training results:**

```
Epoch 1/15
214/214 [==============================] - 10s 39ms/step - loss: 0.1162 - categorical_accuracy: 0.8770 - val_loss: 0.1572 - val_categorical_accuracy: 0.8778 - lr: 0.0010
Epoch 2/15
214/214 [==============================] - 7s 31ms/step - loss: 0.1128 - categorical_accuracy: 0.8791 - val_loss: 0.1584 - val_categorical_accuracy: 0.8731 - lr: 9.9000e-04
Epoch 3/15
214/214 [==============================] - 8s 36ms/step - loss: 0.1088 - categorical_accuracy: 0.8877 - val_loss: 0.1592 - val_categorical_accuracy: 0.8673 - lr: 9.8010e-04
Epoch 4/15
214/214 [==============================] - 9s 40ms/step - loss: 0.1101 - categorical_accuracy: 0.8870 - val_loss: 0.1579 - val_categorical_accuracy: 0.8708 - lr: 9.7030e-04
Epoch 5/15
214/214 [==============================] - 7s 30ms/step - loss: 0.1104 - categorical_accuracy: 0.8855 - val_loss: 0.1585 - val_categorical_accuracy: 0.8673 - lr: 9.6060e-04
Epoch 6/15
214/214 [==============================] - 8s 38ms/step - loss: 0.1084 - categorical_accuracy: 0.8886 - val_loss: 0.1624 - val_categorical_accuracy: 0.8685 - lr: 9.5099e-04
Epoch 7/15
214/214 [==============================] - 7s 32ms/step - loss: 0.1078 - categorical_accuracy: 0.8883 - val_loss: 0.1617 - val_categorical_accuracy: 0.8731 - lr: 9.4148e-04
Epoch 8/15
214/214 [==============================] - 8s 36ms/step - loss: 0.1078 - categorical_accuracy: 0.8911 - val_loss: 0.1590 - val_categorical_accuracy: 0.8731 - lr: 9.3207e-04
Epoch 9/15
214/214 [==============================] - 8s 38ms/step - loss: 0.1068 - categorical_accuracy: 0.8890 - val_loss: 0.1577 - val_categorical_accuracy: 0.8766 - lr: 9.2274e-04
Epoch 10/15
214/214 [==============================] - 6s 30ms/step - loss: 0.1065 - categorical_accuracy: 0.8905 - val_loss: 0.1584 - val_categorical_accuracy: 0.8696 - lr: 9.1352e-04
Epoch 11/15
214/214 [==============================] - 6s 29ms/step - loss: 0.1074 - categorical_accuracy: 0.8871 - val_loss: 0.1605 - val_categorical_accuracy: 0.8719 - lr: 9.0438e-04
Epoch 12/15
214/214 [==============================] - 7s 30ms/step - loss: 0.1062 - categorical_accuracy: 0.8868 - val_loss: 0.1575 - val_categorical_accuracy: 0.8789 - lr: 8.9534e-04
Epoch 13/15
214/214 [==============================] - 8s 37ms/step - loss: 0.1040 - categorical_accuracy: 0.8880 - val_loss: 0.1569 - val_categorical_accuracy: 0.8731 - lr: 8.8638e-04
Epoch 14/15
214/214 [==============================] - 8s 38ms/step - loss: 0.1034 - categorical_accuracy: 0.8871 - val_loss: 0.1577 - val_categorical_accuracy: 0.8766 - lr: 8.7752e-04
Epoch 15/15
214/214 [==============================] - 7s 30ms/step - loss: 0.1019 - categorical_accuracy: 0.8879 - val_loss: 0.1602 - val_categorical_accuracy: 0.8754 - lr: 8.6875e-04
```

**Test results:**

Test loss:0.14583705365657806, Test accuracy:0.8987194299697876

---

**Model config:**

```
hparams = gesture_recognizer.HParams(learning_rate=0.0002, export_dir="exported_model_2", epochs=40, shuffle=True, batch_size=64)
model_options = gesture_recognizer.ModelOptions(dropout_rate=0.2, layer_widths=[1024, 512, 256, 128, 64])
```

**Training results:**

```
Epoch 1/40
107/107 [==============================] - 14s 100ms/step - loss: 0.6720 - categorical_accuracy: 0.6253 - val_loss: 0.5107 - val_categorical_accuracy: 0.7322 - lr: 2.0000e-04
Epoch 2/40
107/107 [==============================] - 10s 92ms/step - loss: 0.3751 - categorical_accuracy: 0.7802 - val_loss: 0.3911 - val_categorical_accuracy: 0.7625 - lr: 1.9800e-04
Epoch 3/40
107/107 [==============================] - 8s 75ms/step - loss: 0.3317 - categorical_accuracy: 0.8021 - val_loss: 0.3487 - val_categorical_accuracy: 0.7870 - lr: 1.9602e-04
Epoch 4/40
107/107 [==============================] - 10s 96ms/step - loss: 0.3116 - categorical_accuracy: 0.8068 - val_loss: 0.3082 - val_categorical_accuracy: 0.8137 - lr: 1.9406e-04
Epoch 5/40
107/107 [==============================] - 8s 73ms/step - loss: 0.2965 - categorical_accuracy: 0.8135 - val_loss: 0.2984 - val_categorical_accuracy: 0.8126 - lr: 1.9212e-04
Epoch 6/40
107/107 [==============================] - 13s 119ms/step - loss: 0.2840 - categorical_accuracy: 0.8183 - val_loss: 0.2870 - val_categorical_accuracy: 0.8114 - lr: 1.9020e-04
Epoch 7/40
107/107 [==============================] - 8s 77ms/step - loss: 0.2771 - categorical_accuracy: 0.8214 - val_loss: 0.2866 - val_categorical_accuracy: 0.8149 - lr: 1.8830e-04
Epoch 8/40
107/107 [==============================] - 10s 97ms/step - loss: 0.2585 - categorical_accuracy: 0.8259 - val_loss: 0.2853 - val_categorical_accuracy: 0.8161 - lr: 1.8641e-04
Epoch 9/40
107/107 [==============================] - 10s 95ms/step - loss: 0.2583 - categorical_accuracy: 0.8249 - val_loss: 0.2719 - val_categorical_accuracy: 0.8184 - lr: 1.8455e-04
Epoch 10/40
107/107 [==============================] - 8s 71ms/step - loss: 0.2564 - categorical_accuracy: 0.8324 - val_loss: 0.2726 - val_categorical_accuracy: 0.8172 - lr: 1.8270e-04
Epoch 11/40
107/107 [==============================] - 10s 95ms/step - loss: 0.2481 - categorical_accuracy: 0.8348 - val_loss: 0.2687 - val_categorical_accuracy: 0.8265 - lr: 1.8088e-04
Epoch 12/40
107/107 [==============================] - 10s 96ms/step - loss: 0.2526 - categorical_accuracy: 0.8306 - val_loss: 0.2635 - val_categorical_accuracy: 0.8231 - lr: 1.7907e-04
Epoch 13/40
107/107 [==============================] - 8s 74ms/step - loss: 0.2405 - categorical_accuracy: 0.8353 - val_loss: 0.2610 - val_categorical_accuracy: 0.8289 - lr: 1.7728e-04
Epoch 14/40
107/107 [==============================] - 10s 91ms/step - loss: 0.2319 - categorical_accuracy: 0.8411 - val_loss: 0.2627 - val_categorical_accuracy: 0.8335 - lr: 1.7550e-04
Epoch 15/40
107/107 [==============================] - 11s 97ms/step - loss: 0.2352 - categorical_accuracy: 0.8338 - val_loss: 0.2572 - val_categorical_accuracy: 0.8393 - lr: 1.7375e-04
Epoch 16/40
107/107 [==============================] - 8s 73ms/step - loss: 0.2332 - categorical_accuracy: 0.8404 - val_loss: 0.2514 - val_categorical_accuracy: 0.8277 - lr: 1.7201e-04
Epoch 17/40
107/107 [==============================] - 12s 110ms/step - loss: 0.2253 - categorical_accuracy: 0.8423 - val_loss: 0.2521 - val_categorical_accuracy: 0.8359 - lr: 1.7029e-04
Epoch 18/40
107/107 [==============================] - 11s 98ms/step - loss: 0.2359 - categorical_accuracy: 0.8341 - val_loss: 0.2486 - val_categorical_accuracy: 0.8289 - lr: 1.6859e-04
Epoch 19/40
107/107 [==============================] - 11s 98ms/step - loss: 0.2259 - categorical_accuracy: 0.8402 - val_loss: 0.2477 - val_categorical_accuracy: 0.8289 - lr: 1.6690e-04
Epoch 20/40
107/107 [==============================] - 10s 96ms/step - loss: 0.2154 - categorical_accuracy: 0.8443 - val_loss: 0.2427 - val_categorical_accuracy: 0.8382 - lr: 1.6523e-04
Epoch 21/40
107/107 [==============================] - 8s 72ms/step - loss: 0.2203 - categorical_accuracy: 0.8451 - val_loss: 0.2453 - val_categorical_accuracy: 0.8370 - lr: 1.6358e-04
Epoch 22/40
107/107 [==============================] - 10s 96ms/step - loss: 0.2169 - categorical_accuracy: 0.8464 - val_loss: 0.2449 - val_categorical_accuracy: 0.8335 - lr: 1.6195e-04
Epoch 23/40
107/107 [==============================] - 8s 75ms/step - loss: 0.2167 - categorical_accuracy: 0.8474 - val_loss: 0.2428 - val_categorical_accuracy: 0.8428 - lr: 1.6033e-04
Epoch 24/40
107/107 [==============================] - 10s 90ms/step - loss: 0.2182 - categorical_accuracy: 0.8454 - val_loss: 0.2408 - val_categorical_accuracy: 0.8382 - lr: 1.5872e-04
Epoch 25/40
107/107 [==============================] - 10s 97ms/step - loss: 0.2146 - categorical_accuracy: 0.8486 - val_loss: 0.2394 - val_categorical_accuracy: 0.8347 - lr: 1.5714e-04
Epoch 26/40
107/107 [==============================] - 10s 91ms/step - loss: 0.2099 - categorical_accuracy: 0.8494 - val_loss: 0.2363 - val_categorical_accuracy: 0.8405 - lr: 1.5556e-04
Epoch 27/40
107/107 [==============================] - 11s 101ms/step - loss: 0.2120 - categorical_accuracy: 0.8487 - val_loss: 0.2370 - val_categorical_accuracy: 0.8382 - lr: 1.5401e-04
Epoch 28/40
107/107 [==============================] - 10s 92ms/step - loss: 0.2052 - categorical_accuracy: 0.8524 - val_loss: 0.2348 - val_categorical_accuracy: 0.8347 - lr: 1.5247e-04
Epoch 29/40
107/107 [==============================] - 10s 90ms/step - loss: 0.2113 - categorical_accuracy: 0.8490 - val_loss: 0.2333 - val_categorical_accuracy: 0.8428 - lr: 1.5094e-04
Epoch 30/40
107/107 [==============================] - 8s 75ms/step - loss: 0.2047 - categorical_accuracy: 0.8528 - val_loss: 0.2331 - val_categorical_accuracy: 0.8428 - lr: 1.4943e-04
Epoch 31/40
107/107 [==============================] - 11s 100ms/step - loss: 0.2084 - categorical_accuracy: 0.8484 - val_loss: 0.2346 - val_categorical_accuracy: 0.8405 - lr: 1.4794e-04
Epoch 32/40
107/107 [==============================] - 9s 83ms/step - loss: 0.2074 - categorical_accuracy: 0.8509 - val_loss: 0.2284 - val_categorical_accuracy: 0.8498 - lr: 1.4646e-04
Epoch 33/40
107/107 [==============================] - 10s 89ms/step - loss: 0.1988 - categorical_accuracy: 0.8595 - val_loss: 0.2311 - val_categorical_accuracy: 0.8510 - lr: 1.4500e-04
Epoch 34/40
107/107 [==============================] - 11s 97ms/step - loss: 0.2042 - categorical_accuracy: 0.8512 - val_loss: 0.2299 - val_categorical_accuracy: 0.8405 - lr: 1.4355e-04
Epoch 35/40
107/107 [==============================] - 9s 81ms/step - loss: 0.2000 - categorical_accuracy: 0.8567 - val_loss: 0.2289 - val_categorical_accuracy: 0.8475 - lr: 1.4211e-04
Epoch 36/40
107/107 [==============================] - 10s 96ms/step - loss: 0.1965 - categorical_accuracy: 0.8529 - val_loss: 0.2291 - val_categorical_accuracy: 0.8417 - lr: 1.4069e-04
Epoch 37/40
107/107 [==============================] - 8s 73ms/step - loss: 0.1983 - categorical_accuracy: 0.8537 - val_loss: 0.2257 - val_categorical_accuracy: 0.8487 - lr: 1.3928e-04
Epoch 38/40
107/107 [==============================] - 11s 96ms/step - loss: 0.1944 - categorical_accuracy: 0.8538 - val_loss: 0.2331 - val_categorical_accuracy: 0.8370 - lr: 1.3789e-04
Epoch 39/40
107/107 [==============================] - 11s 97ms/step - loss: 0.1946 - categorical_accuracy: 0.8572 - val_loss: 0.2310 - val_categorical_accuracy: 0.8475 - lr: 1.3651e-04
Epoch 40/40
107/107 [==============================] - 10s 92ms/step - loss: 0.1948 - categorical_accuracy: 0.8575 - val_loss: 0.2278 - val_categorical_accuracy: 0.8475 - lr: 1.3515e-04
```
-> no overfitting ma non buone performance

**Test results:**
Test loss:0.19374984502792358, Test accuracy:0.8742724061012268

## Training on Hagrid dataset with 1500 examples per label + 500 data augmentation per label (25%) = 2000 examples per label

**Model config 1:**
```
hparams = gesture_recognizer.HParams(learning_rate=0.0002, export_dir="exported_model_2", epochs=40, shuffle=True, batch_size=64)
model_options = gesture_recognizer.ModelOptions(dropout_rate=0.2, layer_widths=[1024, 512, 256, 128, 64])
```

**Training result:**
```
Epoch 1/40
117/117 [==============================] - 17s 105ms/step - loss: 0.7058 - categorical_accuracy: 0.6227 - val_loss: 0.3863 - val_categorical_accuracy: 0.8047 - lr: 2.0000e-04
Epoch 2/40
117/117 [==============================] - 12s 105ms/step - loss: 0.3587 - categorical_accuracy: 0.7970 - val_loss: 0.2775 - val_categorical_accuracy: 0.8471 - lr: 1.9800e-04
Epoch 3/40
117/117 [==============================] - 12s 99ms/step - loss: 0.3154 - categorical_accuracy: 0.8231 - val_loss: 0.2447 - val_categorical_accuracy: 0.8609 - lr: 1.9602e-04
Epoch 4/40
117/117 [==============================] - 10s 85ms/step - loss: 0.2908 - categorical_accuracy: 0.8257 - val_loss: 0.2266 - val_categorical_accuracy: 0.8662 - lr: 1.9406e-04
Epoch 5/40
117/117 [==============================] - 12s 97ms/step - loss: 0.2752 - categorical_accuracy: 0.8364 - val_loss: 0.2135 - val_categorical_accuracy: 0.8684 - lr: 1.9212e-04
Epoch 6/40
117/117 [==============================] - 12s 101ms/step - loss: 0.2650 - categorical_accuracy: 0.8380 - val_loss: 0.2085 - val_categorical_accuracy: 0.8694 - lr: 1.9020e-04
Epoch 7/40
117/117 [==============================] - 11s 94ms/step - loss: 0.2553 - categorical_accuracy: 0.8372 - val_loss: 0.1985 - val_categorical_accuracy: 0.8726 - lr: 1.8830e-04
Epoch 8/40
117/117 [==============================] - 11s 86ms/step - loss: 0.2518 - categorical_accuracy: 0.8407 - val_loss: 0.1961 - val_categorical_accuracy: 0.8737 - lr: 1.8641e-04
Epoch 9/40
117/117 [==============================] - 12s 102ms/step - loss: 0.2388 - categorical_accuracy: 0.8446 - val_loss: 0.1926 - val_categorical_accuracy: 0.8737 - lr: 1.8455e-04
Epoch 10/40
117/117 [==============================] - 12s 98ms/step - loss: 0.2379 - categorical_accuracy: 0.8436 - val_loss: 0.1914 - val_categorical_accuracy: 0.8747 - lr: 1.8270e-04
Epoch 11/40
117/117 [==============================] - 10s 84ms/step - loss: 0.2324 - categorical_accuracy: 0.8442 - val_loss: 0.1910 - val_categorical_accuracy: 0.8832 - lr: 1.8088e-04
Epoch 12/40
117/117 [==============================] - 12s 100ms/step - loss: 0.2307 - categorical_accuracy: 0.8496 - val_loss: 0.1844 - val_categorical_accuracy: 0.8822 - lr: 1.7907e-04
Epoch 13/40
117/117 [==============================] - 12s 101ms/step - loss: 0.2265 - categorical_accuracy: 0.8462 - val_loss: 0.1835 - val_categorical_accuracy: 0.8790 - lr: 1.7728e-04
Epoch 14/40
117/117 [==============================] - 12s 98ms/step - loss: 0.2237 - categorical_accuracy: 0.8482 - val_loss: 0.1826 - val_categorical_accuracy: 0.8769 - lr: 1.7550e-04
Epoch 15/40
117/117 [==============================] - 12s 100ms/step - loss: 0.2150 - categorical_accuracy: 0.8515 - val_loss: 0.1803 - val_categorical_accuracy: 0.8854 - lr: 1.7375e-04
Epoch 16/40
117/117 [==============================] - 12s 99ms/step - loss: 0.2126 - categorical_accuracy: 0.8530 - val_loss: 0.1802 - val_categorical_accuracy: 0.8811 - lr: 1.7201e-04
Epoch 17/40
117/117 [==============================] - 12s 100ms/step - loss: 0.2121 - categorical_accuracy: 0.8539 - val_loss: 0.1839 - val_categorical_accuracy: 0.8779 - lr: 1.7029e-04
Epoch 18/40
117/117 [==============================] - 12s 101ms/step - loss: 0.2156 - categorical_accuracy: 0.8522 - val_loss: 0.1781 - val_categorical_accuracy: 0.8800 - lr: 1.6859e-04
Epoch 19/40
117/117 [==============================] - 12s 101ms/step - loss: 0.2152 - categorical_accuracy: 0.8512 - val_loss: 0.1757 - val_categorical_accuracy: 0.8747 - lr: 1.6690e-04
Epoch 20/40
117/117 [==============================] - 13s 106ms/step - loss: 0.2113 - categorical_accuracy: 0.8508 - val_loss: 0.1771 - val_categorical_accuracy: 0.8769 - lr: 1.6523e-04
Epoch 21/40
117/117 [==============================] - 12s 105ms/step - loss: 0.2072 - categorical_accuracy: 0.8568 - val_loss: 0.1785 - val_categorical_accuracy: 0.8737 - lr: 1.6358e-04
Epoch 22/40
117/117 [==============================] - 13s 108ms/step - loss: 0.2050 - categorical_accuracy: 0.8554 - val_loss: 0.1723 - val_categorical_accuracy: 0.8843 - lr: 1.6195e-04
Epoch 23/40
117/117 [==============================] - 12s 101ms/step - loss: 0.2053 - categorical_accuracy: 0.8556 - val_loss: 0.1732 - val_categorical_accuracy: 0.8800 - lr: 1.6033e-04
Epoch 24/40
117/117 [==============================] - 12s 105ms/step - loss: 0.2039 - categorical_accuracy: 0.8554 - val_loss: 0.1682 - val_categorical_accuracy: 0.8822 - lr: 1.5872e-04
Epoch 25/40
117/117 [==============================] - 12s 101ms/step - loss: 0.2025 - categorical_accuracy: 0.8578 - val_loss: 0.1710 - val_categorical_accuracy: 0.8896 - lr: 1.5714e-04
Epoch 26/40
117/117 [==============================] - 17s 141ms/step - loss: 0.1952 - categorical_accuracy: 0.8568 - val_loss: 0.1696 - val_categorical_accuracy: 0.8854 - lr: 1.5556e-04
Epoch 27/40
117/117 [==============================] - 12s 99ms/step - loss: 0.1987 - categorical_accuracy: 0.8572 - val_loss: 0.1700 - val_categorical_accuracy: 0.8715 - lr: 1.5401e-04
Epoch 28/40
117/117 [==============================] - 10s 85ms/step - loss: 0.1965 - categorical_accuracy: 0.8594 - val_loss: 0.1656 - val_categorical_accuracy: 0.8843 - lr: 1.5247e-04
Epoch 29/40
117/117 [==============================] - 12s 95ms/step - loss: 0.1969 - categorical_accuracy: 0.8602 - val_loss: 0.1716 - val_categorical_accuracy: 0.8822 - lr: 1.5094e-04
Epoch 30/40
117/117 [==============================] - 12s 101ms/step - loss: 0.1970 - categorical_accuracy: 0.8610 - val_loss: 0.1671 - val_categorical_accuracy: 0.8907 - lr: 1.4943e-04
Epoch 31/40
117/117 [==============================] - 12s 102ms/step - loss: 0.1957 - categorical_accuracy: 0.8616 - val_loss: 0.1649 - val_categorical_accuracy: 0.8885 - lr: 1.4794e-04
Epoch 32/40
117/117 [==============================] - 14s 111ms/step - loss: 0.1966 - categorical_accuracy: 0.8583 - val_loss: 0.1653 - val_categorical_accuracy: 0.8896 - lr: 1.4646e-04
Epoch 33/40
117/117 [==============================] - 13s 106ms/step - loss: 0.1959 - categorical_accuracy: 0.8630 - val_loss: 0.1625 - val_categorical_accuracy: 0.8885 - lr: 1.4500e-04
Epoch 34/40
117/117 [==============================] - 12s 103ms/step - loss: 0.1912 - categorical_accuracy: 0.8655 - val_loss: 0.1614 - val_categorical_accuracy: 0.8885 - lr: 1.4355e-04
Epoch 35/40
117/117 [==============================] - 12s 100ms/step - loss: 0.1918 - categorical_accuracy: 0.8654 - val_loss: 0.1638 - val_categorical_accuracy: 0.8832 - lr: 1.4211e-04
Epoch 36/40
117/117 [==============================] - 10s 85ms/step - loss: 0.1874 - categorical_accuracy: 0.8630 - val_loss: 0.1643 - val_categorical_accuracy: 0.8864 - lr: 1.4069e-04
Epoch 37/40
117/117 [==============================] - 12s 101ms/step - loss: 0.1854 - categorical_accuracy: 0.8667 - val_loss: 0.1653 - val_categorical_accuracy: 0.8875 - lr: 1.3928e-04
Epoch 38/40
117/117 [==============================] - 11s 91ms/step - loss: 0.1900 - categorical_accuracy: 0.8616 - val_loss: 0.1598 - val_categorical_accuracy: 0.8960 - lr: 1.3789e-04
Epoch 39/40
117/117 [==============================] - 12s 97ms/step - loss: 0.1854 - categorical_accuracy: 0.8651 - val_loss: 0.1634 - val_categorical_accuracy: 0.8928 - lr: 1.3651e-04
Epoch 40/40
117/117 [==============================] - 12s 102ms/step - loss: 0.1864 - categorical_accuracy: 0.8662 - val_loss: 0.1603 - val_categorical_accuracy: 0.8907 - lr: 1.3515e-04
```

**Test result:**
Test loss:0.16634710133075714, Test accuracy:0.889713704586029 

**Observations:** it does not overfit => good

**Model config 2:**
```
hparams = gesture_recognizer.HParams(learning_rate=0.0002, export_dir="exported_model_2", epochs=30, shuffle=True, batch_size=64)
model_options = gesture_recognizer.ModelOptions(dropout_rate=0.1, layer_widths=[1024, 512, 256, 128, 64])
```

**Training results:**
```
Epoch 1/30
117/117 [==============================] - 18s 110ms/step - loss: 0.3929 - categorical_accuracy: 0.7774 - val_loss: 0.3819 - val_categorical_accuracy: 0.8462 - lr: 2.0000e-04
Epoch 2/30
117/117 [==============================] - 12s 105ms/step - loss: 0.2532 - categorical_accuracy: 0.8446 - val_loss: 0.2124 - val_categorical_accuracy: 0.8727 - lr: 1.9800e-04
Epoch 3/30
117/117 [==============================] - 11s 91ms/step - loss: 0.2328 - categorical_accuracy: 0.8486 - val_loss: 0.1804 - val_categorical_accuracy: 0.8802 - lr: 1.9602e-04
Epoch 4/30
117/117 [==============================] - 13s 106ms/step - loss: 0.2259 - categorical_accuracy: 0.8524 - val_loss: 0.1663 - val_categorical_accuracy: 0.8759 - lr: 1.9406e-04
Epoch 5/30
117/117 [==============================] - 12s 103ms/step - loss: 0.2139 - categorical_accuracy: 0.8550 - val_loss: 0.1656 - val_categorical_accuracy: 0.8855 - lr: 1.9212e-04
Epoch 6/30
117/117 [==============================] - 11s 91ms/step - loss: 0.2063 - categorical_accuracy: 0.8578 - val_loss: 0.1625 - val_categorical_accuracy: 0.8823 - lr: 1.9020e-04
Epoch 7/30
117/117 [==============================] - 12s 102ms/step - loss: 0.2048 - categorical_accuracy: 0.8622 - val_loss: 0.1629 - val_categorical_accuracy: 0.8865 - lr: 1.8830e-04
Epoch 8/30
117/117 [==============================] - 12s 103ms/step - loss: 0.1988 - categorical_accuracy: 0.8657 - val_loss: 0.1655 - val_categorical_accuracy: 0.8834 - lr: 1.8641e-04
Epoch 9/30
117/117 [==============================] - 12s 103ms/step - loss: 0.1946 - categorical_accuracy: 0.8647 - val_loss: 0.1609 - val_categorical_accuracy: 0.8855 - lr: 1.8455e-04
Epoch 10/30
117/117 [==============================] - 12s 100ms/step - loss: 0.1874 - categorical_accuracy: 0.8679 - val_loss: 0.1599 - val_categorical_accuracy: 0.8812 - lr: 1.8270e-04
Epoch 11/30
117/117 [==============================] - 12s 101ms/step - loss: 0.1890 - categorical_accuracy: 0.8651 - val_loss: 0.1597 - val_categorical_accuracy: 0.8855 - lr: 1.8088e-04
Epoch 12/30
117/117 [==============================] - 12s 100ms/step - loss: 0.1880 - categorical_accuracy: 0.8661 - val_loss: 0.1607 - val_categorical_accuracy: 0.8834 - lr: 1.7907e-04
Epoch 13/30
117/117 [==============================] - 12s 103ms/step - loss: 0.1812 - categorical_accuracy: 0.8718 - val_loss: 0.1594 - val_categorical_accuracy: 0.8855 - lr: 1.7728e-04
Epoch 14/30
117/117 [==============================] - 14s 115ms/step - loss: 0.1819 - categorical_accuracy: 0.8694 - val_loss: 0.1525 - val_categorical_accuracy: 0.8897 - lr: 1.7550e-04
Epoch 15/30
117/117 [==============================] - 12s 103ms/step - loss: 0.1785 - categorical_accuracy: 0.8711 - val_loss: 0.1521 - val_categorical_accuracy: 0.8897 - lr: 1.7375e-04
Epoch 16/30
117/117 [==============================] - 12s 103ms/step - loss: 0.1782 - categorical_accuracy: 0.8731 - val_loss: 0.1532 - val_categorical_accuracy: 0.8855 - lr: 1.7201e-04
Epoch 17/30
117/117 [==============================] - 12s 100ms/step - loss: 0.1744 - categorical_accuracy: 0.8779 - val_loss: 0.1511 - val_categorical_accuracy: 0.8865 - lr: 1.7029e-04
Epoch 18/30
117/117 [==============================] - 10s 84ms/step - loss: 0.1713 - categorical_accuracy: 0.8767 - val_loss: 0.1549 - val_categorical_accuracy: 0.8865 - lr: 1.6859e-04
Epoch 19/30
117/117 [==============================] - 12s 103ms/step - loss: 0.1727 - categorical_accuracy: 0.8742 - val_loss: 0.1541 - val_categorical_accuracy: 0.8865 - lr: 1.6690e-04
Epoch 20/30
117/117 [==============================] - 12s 102ms/step - loss: 0.1696 - categorical_accuracy: 0.8769 - val_loss: 0.1534 - val_categorical_accuracy: 0.8876 - lr: 1.6523e-04
Epoch 21/30
117/117 [==============================] - 12s 102ms/step - loss: 0.1684 - categorical_accuracy: 0.8755 - val_loss: 0.1548 - val_categorical_accuracy: 0.8887 - lr: 1.6358e-04
Epoch 22/30
117/117 [==============================] - 12s 99ms/step - loss: 0.1667 - categorical_accuracy: 0.8738 - val_loss: 0.1524 - val_categorical_accuracy: 0.8918 - lr: 1.6195e-04
Epoch 23/30
117/117 [==============================] - 11s 88ms/step - loss: 0.1694 - categorical_accuracy: 0.8757 - val_loss: 0.1483 - val_categorical_accuracy: 0.8897 - lr: 1.6033e-04
Epoch 24/30
117/117 [==============================] - 12s 103ms/step - loss: 0.1684 - categorical_accuracy: 0.8755 - val_loss: 0.1509 - val_categorical_accuracy: 0.8918 - lr: 1.5872e-04
Epoch 25/30
117/117 [==============================] - 12s 104ms/step - loss: 0.1631 - categorical_accuracy: 0.8834 - val_loss: 0.1537 - val_categorical_accuracy: 0.8971 - lr: 1.5714e-04
Epoch 26/30
117/117 [==============================] - 12s 103ms/step - loss: 0.1607 - categorical_accuracy: 0.8806 - val_loss: 0.1569 - val_categorical_accuracy: 0.8855 - lr: 1.5556e-04
Epoch 27/30
117/117 [==============================] - 12s 102ms/step - loss: 0.1639 - categorical_accuracy: 0.8767 - val_loss: 0.1563 - val_categorical_accuracy: 0.8908 - lr: 1.5401e-04
Epoch 28/30
117/117 [==============================] - 12s 104ms/step - loss: 0.1616 - categorical_accuracy: 0.8782 - val_loss: 0.1527 - val_categorical_accuracy: 0.8929 - lr: 1.5247e-04
Epoch 29/30
117/117 [==============================] - 12s 104ms/step - loss: 0.1598 - categorical_accuracy: 0.8777 - val_loss: 0.1504 - val_categorical_accuracy: 0.8918 - lr: 1.5094e-04
Epoch 30/30
117/117 [==============================] - 12s 95ms/step - loss: 0.1590 - categorical_accuracy: 0.8799 - val_loss: 0.1561 - val_categorical_accuracy: 0.8918 - lr: 1.4943e-04
```

**Test results:**
Test loss:0.15926462411880493, Test accuracy:0.890774130821228

**Model config 3:**
```
hparams = gesture_recognizer.HParams(learning_rate=0.0002, export_dir="exported_model_2", epochs=30, shuffle=True, batch_size=128)
model_options = gesture_recognizer.ModelOptions(dropout_rate=0.1, layer_widths=[1024, 512, 256, 128, 64])
```

**Training results:**
```
Epoch 1/30
58/58 [==============================] - 16s 195ms/step - loss: 0.4731 - categorical_accuracy: 0.7371 - val_loss: 0.6240 - val_categorical_accuracy: 0.7953 - lr: 2.0000e-04
Epoch 2/30
58/58 [==============================] - 11s 193ms/step - loss: 0.2659 - categorical_accuracy: 0.8477 - val_loss: 0.4076 - val_categorical_accuracy: 0.8335 - lr: 1.9800e-04
Epoch 3/30
58/58 [==============================] - 13s 222ms/step - loss: 0.2440 - categorical_accuracy: 0.8537 - val_loss: 0.2902 - val_categorical_accuracy: 0.8653 - lr: 1.9602e-04
Epoch 4/30
58/58 [==============================] - 11s 190ms/step - loss: 0.2260 - categorical_accuracy: 0.8584 - val_loss: 0.2367 - val_categorical_accuracy: 0.8674 - lr: 1.9406e-04
Epoch 5/30
58/58 [==============================] - 11s 190ms/step - loss: 0.2158 - categorical_accuracy: 0.8580 - val_loss: 0.2105 - val_categorical_accuracy: 0.8706 - lr: 1.9212e-04
Epoch 6/30
58/58 [==============================] - 11s 177ms/step - loss: 0.2123 - categorical_accuracy: 0.8622 - val_loss: 0.1943 - val_categorical_accuracy: 0.8780 - lr: 1.9020e-04
Epoch 7/30
58/58 [==============================] - 11s 191ms/step - loss: 0.2044 - categorical_accuracy: 0.8636 - val_loss: 0.1868 - val_categorical_accuracy: 0.8812 - lr: 1.8830e-04
Epoch 8/30
58/58 [==============================] - 11s 175ms/step - loss: 0.2028 - categorical_accuracy: 0.8596 - val_loss: 0.1846 - val_categorical_accuracy: 0.8791 - lr: 1.8641e-04
Epoch 9/30
58/58 [==============================] - 11s 187ms/step - loss: 0.1964 - categorical_accuracy: 0.8673 - val_loss: 0.1802 - val_categorical_accuracy: 0.8823 - lr: 1.8455e-04
Epoch 10/30
58/58 [==============================] - 11s 190ms/step - loss: 0.1866 - categorical_accuracy: 0.8727 - val_loss: 0.1813 - val_categorical_accuracy: 0.8812 - lr: 1.8270e-04
Epoch 11/30
58/58 [==============================] - 9s 155ms/step - loss: 0.1914 - categorical_accuracy: 0.8665 - val_loss: 0.1749 - val_categorical_accuracy: 0.8844 - lr: 1.8088e-04
Epoch 12/30
58/58 [==============================] - 11s 188ms/step - loss: 0.1887 - categorical_accuracy: 0.8672 - val_loss: 0.1780 - val_categorical_accuracy: 0.8770 - lr: 1.7907e-04
Epoch 13/30
58/58 [==============================] - 11s 180ms/step - loss: 0.1848 - categorical_accuracy: 0.8689 - val_loss: 0.1732 - val_categorical_accuracy: 0.8844 - lr: 1.7728e-04
Epoch 14/30
58/58 [==============================] - 9s 153ms/step - loss: 0.1783 - categorical_accuracy: 0.8754 - val_loss: 0.1716 - val_categorical_accuracy: 0.8887 - lr: 1.7550e-04
Epoch 15/30
58/58 [==============================] - 13s 220ms/step - loss: 0.1808 - categorical_accuracy: 0.8731 - val_loss: 0.1716 - val_categorical_accuracy: 0.8855 - lr: 1.7375e-04
Epoch 16/30
58/58 [==============================] - 11s 186ms/step - loss: 0.1781 - categorical_accuracy: 0.8751 - val_loss: 0.1677 - val_categorical_accuracy: 0.8876 - lr: 1.7201e-04
Epoch 17/30
58/58 [==============================] - 11s 190ms/step - loss: 0.1767 - categorical_accuracy: 0.8715 - val_loss: 0.1714 - val_categorical_accuracy: 0.8865 - lr: 1.7029e-04
Epoch 18/30
58/58 [==============================] - 9s 155ms/step - loss: 0.1752 - categorical_accuracy: 0.8770 - val_loss: 0.1664 - val_categorical_accuracy: 0.8961 - lr: 1.6859e-04
Epoch 19/30
58/58 [==============================] - 10s 163ms/step - loss: 0.1710 - categorical_accuracy: 0.8773 - val_loss: 0.1675 - val_categorical_accuracy: 0.8929 - lr: 1.6690e-04
Epoch 20/30
58/58 [==============================] - 11s 186ms/step - loss: 0.1765 - categorical_accuracy: 0.8700 - val_loss: 0.1648 - val_categorical_accuracy: 0.8908 - lr: 1.6523e-04
Epoch 21/30
58/58 [==============================] - 15s 258ms/step - loss: 0.1700 - categorical_accuracy: 0.8739 - val_loss: 0.1651 - val_categorical_accuracy: 0.8887 - lr: 1.6358e-04
Epoch 22/30
58/58 [==============================] - 11s 183ms/step - loss: 0.1701 - categorical_accuracy: 0.8781 - val_loss: 0.1640 - val_categorical_accuracy: 0.8897 - lr: 1.6195e-04
Epoch 23/30
58/58 [==============================] - 11s 190ms/step - loss: 0.1669 - categorical_accuracy: 0.8772 - val_loss: 0.1630 - val_categorical_accuracy: 0.8834 - lr: 1.6033e-04
Epoch 24/30
58/58 [==============================] - 10s 162ms/step - loss: 0.1684 - categorical_accuracy: 0.8762 - val_loss: 0.1617 - val_categorical_accuracy: 0.8918 - lr: 1.5872e-04
Epoch 25/30
58/58 [==============================] - 10s 167ms/step - loss: 0.1649 - categorical_accuracy: 0.8812 - val_loss: 0.1620 - val_categorical_accuracy: 0.8908 - lr: 1.5714e-04
Epoch 26/30
58/58 [==============================] - 11s 189ms/step - loss: 0.1586 - categorical_accuracy: 0.8813 - val_loss: 0.1599 - val_categorical_accuracy: 0.8982 - lr: 1.5556e-04
Epoch 27/30
58/58 [==============================] - 10s 154ms/step - loss: 0.1636 - categorical_accuracy: 0.8794 - val_loss: 0.1622 - val_categorical_accuracy: 0.8950 - lr: 1.5401e-04
Epoch 28/30
58/58 [==============================] - 13s 219ms/step - loss: 0.1668 - categorical_accuracy: 0.8786 - val_loss: 0.1652 - val_categorical_accuracy: 0.8918 - lr: 1.5247e-04
Epoch 29/30
58/58 [==============================] - 11s 185ms/step - loss: 0.1584 - categorical_accuracy: 0.8824 - val_loss: 0.1641 - val_categorical_accuracy: 0.8940 - lr: 1.5094e-04
Epoch 30/30
58/58 [==============================] - 9s 153ms/step - loss: 0.1617 - categorical_accuracy: 0.8803 - val_loss: 0.1628 - val_categorical_accuracy: 0.8929 - lr: 1.4943e-04
```

**Test results:**
Test loss:0.1385858952999115, Test accuracy:0.9004237055778503 => the best

## Training on Hagrid dataset with 1400 examples per label + 600 data augmentation per label (30%) = 2000 examples per label

**Model config:**
```
hparams = gesture_recognizer.HParams(learning_rate=0.0002, export_dir="exported_model_2", epochs=40, shuffle=True, batch_size=64)
model_options = gesture_recognizer.ModelOptions(dropout_rate=0.2, layer_widths=[1024, 512, 256, 128, 64])
```

**Training result:**
```
Epoch 1/40
115/115 [==============================] - 17s 107ms/step - loss: 0.6327 - categorical_accuracy: 0.6428 - val_loss: 0.4143 - val_categorical_accuracy: 0.7462 - lr: 2.0000e-04
Epoch 2/40
115/115 [==============================] - 12s 98ms/step - loss: 0.3519 - categorical_accuracy: 0.7989 - val_loss: 0.2772 - val_categorical_accuracy: 0.8218 - lr: 1.9800e-04
Epoch 3/40
115/115 [==============================] - 12s 105ms/step - loss: 0.3042 - categorical_accuracy: 0.8167 - val_loss: 0.2489 - val_categorical_accuracy: 0.8423 - lr: 1.9602e-04
Epoch 4/40
115/115 [==============================] - 13s 113ms/step - loss: 0.2867 - categorical_accuracy: 0.8258 - val_loss: 0.2459 - val_categorical_accuracy: 0.8456 - lr: 1.9406e-04
Epoch 5/40
115/115 [==============================] - 12s 104ms/step - loss: 0.2685 - categorical_accuracy: 0.8355 - val_loss: 0.2375 - val_categorical_accuracy: 0.8499 - lr: 1.9212e-04
Epoch 6/40
115/115 [==============================] - 12s 105ms/step - loss: 0.2638 - categorical_accuracy: 0.8322 - val_loss: 0.2312 - val_categorical_accuracy: 0.8553 - lr: 1.9020e-04
Epoch 7/40
115/115 [==============================] - 14s 121ms/step - loss: 0.2500 - categorical_accuracy: 0.8367 - val_loss: 0.2256 - val_categorical_accuracy: 0.8585 - lr: 1.8830e-04
Epoch 8/40
115/115 [==============================] - 12s 104ms/step - loss: 0.2415 - categorical_accuracy: 0.8417 - val_loss: 0.2243 - val_categorical_accuracy: 0.8564 - lr: 1.8641e-04
Epoch 9/40
115/115 [==============================] - 12s 105ms/step - loss: 0.2402 - categorical_accuracy: 0.8401 - val_loss: 0.2234 - val_categorical_accuracy: 0.8553 - lr: 1.8455e-04
Epoch 10/40
115/115 [==============================] - 12s 106ms/step - loss: 0.2379 - categorical_accuracy: 0.8406 - val_loss: 0.2172 - val_categorical_accuracy: 0.8585 - lr: 1.8270e-04
Epoch 11/40
115/115 [==============================] - 12s 106ms/step - loss: 0.2305 - categorical_accuracy: 0.8423 - val_loss: 0.2156 - val_categorical_accuracy: 0.8596 - lr: 1.8088e-04
Epoch 12/40
115/115 [==============================] - 12s 107ms/step - loss: 0.2209 - categorical_accuracy: 0.8484 - val_loss: 0.2135 - val_categorical_accuracy: 0.8585 - lr: 1.7907e-04
Epoch 13/40
115/115 [==============================] - 12s 104ms/step - loss: 0.2223 - categorical_accuracy: 0.8505 - val_loss: 0.2163 - val_categorical_accuracy: 0.8607 - lr: 1.7728e-04
Epoch 14/40
115/115 [==============================] - 12s 97ms/step - loss: 0.2179 - categorical_accuracy: 0.8520 - val_loss: 0.2151 - val_categorical_accuracy: 0.8575 - lr: 1.7550e-04
Epoch 15/40
115/115 [==============================] - 12s 106ms/step - loss: 0.2167 - categorical_accuracy: 0.8524 - val_loss: 0.2090 - val_categorical_accuracy: 0.8629 - lr: 1.7375e-04
Epoch 16/40
115/115 [==============================] - 11s 89ms/step - loss: 0.2031 - categorical_accuracy: 0.8590 - val_loss: 0.2065 - val_categorical_accuracy: 0.8683 - lr: 1.7201e-04
Epoch 17/40
115/115 [==============================] - 12s 102ms/step - loss: 0.2086 - categorical_accuracy: 0.8503 - val_loss: 0.2033 - val_categorical_accuracy: 0.8639 - lr: 1.7029e-04
Epoch 18/40
115/115 [==============================] - 11s 90ms/step - loss: 0.2095 - categorical_accuracy: 0.8548 - val_loss: 0.2051 - val_categorical_accuracy: 0.8650 - lr: 1.6859e-04
Epoch 19/40
115/115 [==============================] - 12s 99ms/step - loss: 0.2123 - categorical_accuracy: 0.8557 - val_loss: 0.2028 - val_categorical_accuracy: 0.8672 - lr: 1.6690e-04
Epoch 20/40
115/115 [==============================] - 12s 107ms/step - loss: 0.2048 - categorical_accuracy: 0.8558 - val_loss: 0.2060 - val_categorical_accuracy: 0.8661 - lr: 1.6523e-04
Epoch 21/40
115/115 [==============================] - 12s 100ms/step - loss: 0.2077 - categorical_accuracy: 0.8549 - val_loss: 0.2027 - val_categorical_accuracy: 0.8672 - lr: 1.6358e-04
Epoch 22/40
115/115 [==============================] - 17s 148ms/step - loss: 0.2045 - categorical_accuracy: 0.8579 - val_loss: 0.2072 - val_categorical_accuracy: 0.8672 - lr: 1.6195e-04
Epoch 23/40
115/115 [==============================] - 12s 104ms/step - loss: 0.1971 - categorical_accuracy: 0.8630 - val_loss: 0.2047 - val_categorical_accuracy: 0.8661 - lr: 1.6033e-04
Epoch 24/40
115/115 [==============================] - 11s 87ms/step - loss: 0.2001 - categorical_accuracy: 0.8575 - val_loss: 0.2022 - val_categorical_accuracy: 0.8693 - lr: 1.5872e-04
Epoch 25/40
115/115 [==============================] - 12s 107ms/step - loss: 0.1923 - categorical_accuracy: 0.8588 - val_loss: 0.2028 - val_categorical_accuracy: 0.8618 - lr: 1.5714e-04
Epoch 26/40
115/115 [==============================] - 12s 104ms/step - loss: 0.1976 - categorical_accuracy: 0.8577 - val_loss: 0.2032 - val_categorical_accuracy: 0.8596 - lr: 1.5556e-04
Epoch 27/40
115/115 [==============================] - 12s 102ms/step - loss: 0.1999 - categorical_accuracy: 0.8567 - val_loss: 0.2004 - val_categorical_accuracy: 0.8618 - lr: 1.5401e-04
Epoch 28/40
115/115 [==============================] - 13s 108ms/step - loss: 0.1912 - categorical_accuracy: 0.8683 - val_loss: 0.2022 - val_categorical_accuracy: 0.8661 - lr: 1.5247e-04
Epoch 29/40
115/115 [==============================] - 12s 104ms/step - loss: 0.1908 - categorical_accuracy: 0.8647 - val_loss: 0.1983 - val_categorical_accuracy: 0.8704 - lr: 1.5094e-04
Epoch 30/40
115/115 [==============================] - 14s 123ms/step - loss: 0.1874 - categorical_accuracy: 0.8625 - val_loss: 0.2024 - val_categorical_accuracy: 0.8629 - lr: 1.4943e-04
Epoch 31/40
115/115 [==============================] - 12s 104ms/step - loss: 0.1883 - categorical_accuracy: 0.8635 - val_loss: 0.1975 - val_categorical_accuracy: 0.8683 - lr: 1.4794e-04
Epoch 32/40
115/115 [==============================] - 12s 104ms/step - loss: 0.1880 - categorical_accuracy: 0.8621 - val_loss: 0.1968 - val_categorical_accuracy: 0.8629 - lr: 1.4646e-04
Epoch 33/40
115/115 [==============================] - 12s 102ms/step - loss: 0.1898 - categorical_accuracy: 0.8606 - val_loss: 0.2004 - val_categorical_accuracy: 0.8650 - lr: 1.4500e-04
Epoch 34/40
115/115 [==============================] - 12s 106ms/step - loss: 0.1825 - categorical_accuracy: 0.8671 - val_loss: 0.1974 - val_categorical_accuracy: 0.8650 - lr: 1.4355e-04
Epoch 35/40
115/115 [==============================] - 12s 97ms/step - loss: 0.1849 - categorical_accuracy: 0.8648 - val_loss: 0.1959 - val_categorical_accuracy: 0.8650 - lr: 1.4211e-04
Epoch 36/40
115/115 [==============================] - 13s 108ms/step - loss: 0.1893 - categorical_accuracy: 0.8643 - val_loss: 0.2015 - val_categorical_accuracy: 0.8618 - lr: 1.4069e-04
Epoch 37/40
115/115 [==============================] - 14s 117ms/step - loss: 0.1809 - categorical_accuracy: 0.8660 - val_loss: 0.1967 - val_categorical_accuracy: 0.8650 - lr: 1.3928e-04
Epoch 38/40
115/115 [==============================] - 12s 102ms/step - loss: 0.1799 - categorical_accuracy: 0.8697 - val_loss: 0.1946 - val_categorical_accuracy: 0.8672 - lr: 1.3789e-04
Epoch 39/40
115/115 [==============================] - 12s 106ms/step - loss: 0.1852 - categorical_accuracy: 0.8640 - val_loss: 0.1971 - val_categorical_accuracy: 0.8639 - lr: 1.3651e-04
Epoch 40/40
115/115 [==============================] - 12s 106ms/step - loss: 0.1774 - categorical_accuracy: 0.8712 - val_loss: 0.1956 - val_categorical_accuracy: 0.8672 - lr: 1.3515e-04
```

**Test result:**
Test loss:0.191091850399971, Test accuracy:0.8748651742935181

## Training on Hagrid dataset with 1300 examples per label + 700 data augmentation per label (35%) = 2000 examples per label

**Model config:**
```
hparams = gesture_recognizer.HParams(learning_rate=0.0002, export_dir="exported_model_2", epochs=40, shuffle=True, batch_size=64)
model_options = gesture_recognizer.ModelOptions(dropout_rate=0.2, layer_widths=[1024, 512, 256, 128, 64])
```

**Training result:**
```
Epoch 1/40
113/113 [==============================] - 16s 107ms/step - loss: 0.6309 - categorical_accuracy: 0.6369 - val_loss: 0.4034 - val_categorical_accuracy: 0.8020 - lr: 2.0000e-04
Epoch 2/40
113/113 [==============================] - 12s 102ms/step - loss: 0.3530 - categorical_accuracy: 0.7886 - val_loss: 0.2784 - val_categorical_accuracy: 0.8273 - lr: 1.9800e-04
Epoch 3/40
113/113 [==============================] - 13s 113ms/step - loss: 0.3044 - categorical_accuracy: 0.8099 - val_loss: 0.2279 - val_categorical_accuracy: 0.8482 - lr: 1.9602e-04
Epoch 4/40
113/113 [==============================] - 13s 109ms/step - loss: 0.2867 - categorical_accuracy: 0.8227 - val_loss: 0.2198 - val_categorical_accuracy: 0.8526 - lr: 1.9406e-04
Epoch 5/40
113/113 [==============================] - 10s 86ms/step - loss: 0.2677 - categorical_accuracy: 0.8252 - val_loss: 0.2082 - val_categorical_accuracy: 0.8559 - lr: 1.9212e-04
Epoch 6/40
113/113 [==============================] - 12s 102ms/step - loss: 0.2586 - categorical_accuracy: 0.8314 - val_loss: 0.2011 - val_categorical_accuracy: 0.8581 - lr: 1.9020e-04
Epoch 7/40
113/113 [==============================] - 12s 104ms/step - loss: 0.2553 - categorical_accuracy: 0.8316 - val_loss: 0.1919 - val_categorical_accuracy: 0.8559 - lr: 1.8830e-04
Epoch 8/40
113/113 [==============================] - 12s 104ms/step - loss: 0.2411 - categorical_accuracy: 0.8388 - val_loss: 0.1918 - val_categorical_accuracy: 0.8658 - lr: 1.8641e-04
Epoch 9/40
113/113 [==============================] - 12s 101ms/step - loss: 0.2473 - categorical_accuracy: 0.8337 - val_loss: 0.1859 - val_categorical_accuracy: 0.8658 - lr: 1.8455e-04
Epoch 10/40
113/113 [==============================] - 12s 105ms/step - loss: 0.2367 - categorical_accuracy: 0.8368 - val_loss: 0.1866 - val_categorical_accuracy: 0.8735 - lr: 1.8270e-04
Epoch 11/40
113/113 [==============================] - 12s 104ms/step - loss: 0.2329 - categorical_accuracy: 0.8424 - val_loss: 0.1836 - val_categorical_accuracy: 0.8724 - lr: 1.8088e-04
Epoch 12/40
113/113 [==============================] - 10s 86ms/step - loss: 0.2292 - categorical_accuracy: 0.8399 - val_loss: 0.1822 - val_categorical_accuracy: 0.8713 - lr: 1.7907e-04
Epoch 13/40
113/113 [==============================] - 12s 103ms/step - loss: 0.2256 - categorical_accuracy: 0.8457 - val_loss: 0.1810 - val_categorical_accuracy: 0.8702 - lr: 1.7728e-04
Epoch 14/40
113/113 [==============================] - 12s 105ms/step - loss: 0.2268 - categorical_accuracy: 0.8439 - val_loss: 0.1796 - val_categorical_accuracy: 0.8735 - lr: 1.7550e-04
Epoch 15/40
113/113 [==============================] - 12s 102ms/step - loss: 0.2213 - categorical_accuracy: 0.8439 - val_loss: 0.1766 - val_categorical_accuracy: 0.8823 - lr: 1.7375e-04
Epoch 16/40
113/113 [==============================] - 12s 104ms/step - loss: 0.2214 - categorical_accuracy: 0.8438 - val_loss: 0.1805 - val_categorical_accuracy: 0.8845 - lr: 1.7201e-04
Epoch 17/40
113/113 [==============================] - 12s 104ms/step - loss: 0.2161 - categorical_accuracy: 0.8494 - val_loss: 0.1737 - val_categorical_accuracy: 0.8922 - lr: 1.7029e-04
Epoch 18/40
113/113 [==============================] - 12s 104ms/step - loss: 0.2153 - categorical_accuracy: 0.8497 - val_loss: 0.1748 - val_categorical_accuracy: 0.8889 - lr: 1.6859e-04
Epoch 19/40
113/113 [==============================] - 12s 103ms/step - loss: 0.2163 - categorical_accuracy: 0.8479 - val_loss: 0.1721 - val_categorical_accuracy: 0.8889 - lr: 1.6690e-04
Epoch 20/40
113/113 [==============================] - 10s 84ms/step - loss: 0.2120 - categorical_accuracy: 0.8493 - val_loss: 0.1745 - val_categorical_accuracy: 0.8779 - lr: 1.6523e-04
Epoch 21/40
113/113 [==============================] - 12s 102ms/step - loss: 0.2107 - categorical_accuracy: 0.8523 - val_loss: 0.1741 - val_categorical_accuracy: 0.8845 - lr: 1.6358e-04
Epoch 22/40
113/113 [==============================] - 12s 107ms/step - loss: 0.2074 - categorical_accuracy: 0.8494 - val_loss: 0.1718 - val_categorical_accuracy: 0.8834 - lr: 1.6195e-04
Epoch 23/40
113/113 [==============================] - 12s 102ms/step - loss: 0.2034 - categorical_accuracy: 0.8584 - val_loss: 0.1663 - val_categorical_accuracy: 0.8911 - lr: 1.6033e-04
Epoch 24/40
113/113 [==============================] - 10s 86ms/step - loss: 0.2026 - categorical_accuracy: 0.8518 - val_loss: 0.1698 - val_categorical_accuracy: 0.8856 - lr: 1.5872e-04
Epoch 25/40
113/113 [==============================] - 12s 104ms/step - loss: 0.2055 - categorical_accuracy: 0.8514 - val_loss: 0.1686 - val_categorical_accuracy: 0.8845 - lr: 1.5714e-04
Epoch 26/40
113/113 [==============================] - 12s 105ms/step - loss: 0.2011 - categorical_accuracy: 0.8522 - val_loss: 0.1695 - val_categorical_accuracy: 0.8889 - lr: 1.5556e-04
Epoch 27/40
113/113 [==============================] - 17s 152ms/step - loss: 0.2019 - categorical_accuracy: 0.8566 - val_loss: 0.1719 - val_categorical_accuracy: 0.8911 - lr: 1.5401e-04
Epoch 28/40
113/113 [==============================] - 12s 104ms/step - loss: 0.2017 - categorical_accuracy: 0.8523 - val_loss: 0.1666 - val_categorical_accuracy: 0.8889 - lr: 1.5247e-04
Epoch 29/40
113/113 [==============================] - 12s 103ms/step - loss: 0.1967 - categorical_accuracy: 0.8579 - val_loss: 0.1683 - val_categorical_accuracy: 0.8889 - lr: 1.5094e-04
Epoch 30/40
113/113 [==============================] - 13s 111ms/step - loss: 0.1994 - categorical_accuracy: 0.8520 - val_loss: 0.1663 - val_categorical_accuracy: 0.8867 - lr: 1.4943e-04
Epoch 31/40
113/113 [==============================] - 13s 111ms/step - loss: 0.1957 - categorical_accuracy: 0.8561 - val_loss: 0.1688 - val_categorical_accuracy: 0.8867 - lr: 1.4794e-04
Epoch 32/40
113/113 [==============================] - 12s 103ms/step - loss: 0.1981 - categorical_accuracy: 0.8583 - val_loss: 0.1657 - val_categorical_accuracy: 0.8889 - lr: 1.4646e-04
Epoch 33/40
113/113 [==============================] - 12s 103ms/step - loss: 0.1956 - categorical_accuracy: 0.8580 - val_loss: 0.1653 - val_categorical_accuracy: 0.8823 - lr: 1.4500e-04
Epoch 34/40
113/113 [==============================] - 13s 114ms/step - loss: 0.1920 - categorical_accuracy: 0.8581 - val_loss: 0.1646 - val_categorical_accuracy: 0.8845 - lr: 1.4355e-04
Epoch 35/40
113/113 [==============================] - 12s 101ms/step - loss: 0.1979 - categorical_accuracy: 0.8569 - val_loss: 0.1652 - val_categorical_accuracy: 0.8801 - lr: 1.4211e-04
Epoch 36/40
113/113 [==============================] - 12s 108ms/step - loss: 0.1896 - categorical_accuracy: 0.8587 - val_loss: 0.1603 - val_categorical_accuracy: 0.8900 - lr: 1.4069e-04
Epoch 37/40
113/113 [==============================] - 11s 99ms/step - loss: 0.1888 - categorical_accuracy: 0.8609 - val_loss: 0.1653 - val_categorical_accuracy: 0.8911 - lr: 1.3928e-04
Epoch 38/40
113/113 [==============================] - 10s 86ms/step - loss: 0.1900 - categorical_accuracy: 0.8592 - val_loss: 0.1660 - val_categorical_accuracy: 0.8823 - lr: 1.3789e-04
Epoch 39/40
113/113 [==============================] - 12s 100ms/step - loss: 0.1849 - categorical_accuracy: 0.8631 - val_loss: 0.1640 - val_categorical_accuracy: 0.8878 - lr: 1.3651e-04
Epoch 40/40
113/113 [==============================] - 12s 105ms/step - loss: 0.1870 - categorical_accuracy: 0.8645 - val_loss: 0.1654 - val_categorical_accuracy: 0.8878 - lr: 1.3515e-04
```

**Test result:**
Test loss:0.1935928463935852, Test accuracy:0.8800880312919617

## Training on Hagrid dataset with 1200 examples per label + 800 data augmentation per label (40%) = 2000 examples per label

**Model config:**
```
hparams = gesture_recognizer.HParams(learning_rate=0.0002, export_dir="exported_model_2", epochs=40, shuffle=True, batch_size=64)
model_options = gesture_recognizer.ModelOptions(dropout_rate=0.2, layer_widths=[1024, 512, 256, 128, 64])
```

**Training result:**
```
Epoch 1/40
111/111 [==============================] - 23s 165ms/step - loss: 0.6920 - categorical_accuracy: 0.6270 - val_loss: 0.4293 - val_categorical_accuracy: 0.7774 - lr: 2.0000e-04
Epoch 2/40
111/111 [==============================] - 12s 110ms/step - loss: 0.3710 - categorical_accuracy: 0.7890 - val_loss: 0.3196 - val_categorical_accuracy: 0.8076 - lr: 1.9800e-04
Epoch 3/40
111/111 [==============================] - 12s 110ms/step - loss: 0.3352 - categorical_accuracy: 0.8056 - val_loss: 0.2629 - val_categorical_accuracy: 0.8333 - lr: 1.9602e-04
Epoch 4/40
111/111 [==============================] - 12s 109ms/step - loss: 0.3125 - categorical_accuracy: 0.8125 - val_loss: 0.2534 - val_categorical_accuracy: 0.8389 - lr: 1.9406e-04
Epoch 5/40
111/111 [==============================] - 13s 111ms/step - loss: 0.2980 - categorical_accuracy: 0.8178 - val_loss: 0.2408 - val_categorical_accuracy: 0.8434 - lr: 1.9212e-04
Epoch 6/40
111/111 [==============================] - 12s 108ms/step - loss: 0.2829 - categorical_accuracy: 0.8208 - val_loss: 0.2282 - val_categorical_accuracy: 0.8490 - lr: 1.9020e-04
Epoch 7/40
111/111 [==============================] - 12s 109ms/step - loss: 0.2741 - categorical_accuracy: 0.8242 - val_loss: 0.2258 - val_categorical_accuracy: 0.8490 - lr: 1.8830e-04
Epoch 8/40
111/111 [==============================] - 14s 121ms/step - loss: 0.2722 - categorical_accuracy: 0.8229 - val_loss: 0.2194 - val_categorical_accuracy: 0.8468 - lr: 1.8641e-04
Epoch 9/40
111/111 [==============================] - 12s 110ms/step - loss: 0.2601 - categorical_accuracy: 0.8295 - val_loss: 0.2189 - val_categorical_accuracy: 0.8490 - lr: 1.8455e-04
Epoch 10/40
111/111 [==============================] - 12s 107ms/step - loss: 0.2568 - categorical_accuracy: 0.8326 - val_loss: 0.2139 - val_categorical_accuracy: 0.8501 - lr: 1.8270e-04
Epoch 11/40
111/111 [==============================] - 11s 97ms/step - loss: 0.2553 - categorical_accuracy: 0.8321 - val_loss: 0.2118 - val_categorical_accuracy: 0.8546 - lr: 1.8088e-04
Epoch 12/40
111/111 [==============================] - 12s 105ms/step - loss: 0.2515 - categorical_accuracy: 0.8305 - val_loss: 0.2047 - val_categorical_accuracy: 0.8546 - lr: 1.7907e-04
Epoch 13/40
111/111 [==============================] - 12s 108ms/step - loss: 0.2442 - categorical_accuracy: 0.8345 - val_loss: 0.2120 - val_categorical_accuracy: 0.8568 - lr: 1.7728e-04
Epoch 14/40
111/111 [==============================] - 11s 99ms/step - loss: 0.2422 - categorical_accuracy: 0.8376 - val_loss: 0.2006 - val_categorical_accuracy: 0.8568 - lr: 1.7550e-04
Epoch 15/40
111/111 [==============================] - 12s 109ms/step - loss: 0.2479 - categorical_accuracy: 0.8346 - val_loss: 0.1988 - val_categorical_accuracy: 0.8557 - lr: 1.7375e-04
Epoch 16/40
111/111 [==============================] - 18s 156ms/step - loss: 0.2413 - categorical_accuracy: 0.8384 - val_loss: 0.1984 - val_categorical_accuracy: 0.8557 - lr: 1.7201e-04
Epoch 17/40
111/111 [==============================] - 12s 107ms/step - loss: 0.2314 - categorical_accuracy: 0.8401 - val_loss: 0.2088 - val_categorical_accuracy: 0.8535 - lr: 1.7029e-04
Epoch 18/40
111/111 [==============================] - 12s 108ms/step - loss: 0.2294 - categorical_accuracy: 0.8392 - val_loss: 0.1995 - val_categorical_accuracy: 0.8546 - lr: 1.6859e-04
Epoch 19/40
111/111 [==============================] - 13s 112ms/step - loss: 0.2283 - categorical_accuracy: 0.8421 - val_loss: 0.1942 - val_categorical_accuracy: 0.8523 - lr: 1.6690e-04
Epoch 20/40
111/111 [==============================] - 12s 109ms/step - loss: 0.2263 - categorical_accuracy: 0.8405 - val_loss: 0.1944 - val_categorical_accuracy: 0.8579 - lr: 1.6523e-04
Epoch 21/40
111/111 [==============================] - 12s 106ms/step - loss: 0.2267 - categorical_accuracy: 0.8452 - val_loss: 0.1996 - val_categorical_accuracy: 0.8523 - lr: 1.6358e-04
Epoch 22/40
111/111 [==============================] - 14s 122ms/step - loss: 0.2204 - categorical_accuracy: 0.8450 - val_loss: 0.1877 - val_categorical_accuracy: 0.8602 - lr: 1.6195e-04
Epoch 23/40
111/111 [==============================] - 13s 111ms/step - loss: 0.2238 - categorical_accuracy: 0.8478 - val_loss: 0.1933 - val_categorical_accuracy: 0.8591 - lr: 1.6033e-04
Epoch 24/40
111/111 [==============================] - 12s 107ms/step - loss: 0.2174 - categorical_accuracy: 0.8516 - val_loss: 0.1919 - val_categorical_accuracy: 0.8523 - lr: 1.5872e-04
Epoch 25/40
111/111 [==============================] - 11s 102ms/step - loss: 0.2172 - categorical_accuracy: 0.8480 - val_loss: 0.1891 - val_categorical_accuracy: 0.8591 - lr: 1.5714e-04
Epoch 26/40
111/111 [==============================] - 12s 109ms/step - loss: 0.2135 - categorical_accuracy: 0.8485 - val_loss: 0.1809 - val_categorical_accuracy: 0.8613 - lr: 1.5556e-04
Epoch 27/40
111/111 [==============================] - 12s 106ms/step - loss: 0.2161 - categorical_accuracy: 0.8480 - val_loss: 0.1850 - val_categorical_accuracy: 0.8613 - lr: 1.5401e-04
Epoch 28/40
111/111 [==============================] - 14s 121ms/step - loss: 0.2179 - categorical_accuracy: 0.8480 - val_loss: 0.1908 - val_categorical_accuracy: 0.8591 - lr: 1.5247e-04
Epoch 29/40
111/111 [==============================] - 12s 105ms/step - loss: 0.2132 - categorical_accuracy: 0.8512 - val_loss: 0.1986 - val_categorical_accuracy: 0.8579 - lr: 1.5094e-04
Epoch 30/40
111/111 [==============================] - 10s 88ms/step - loss: 0.2091 - categorical_accuracy: 0.8537 - val_loss: 0.1879 - val_categorical_accuracy: 0.8613 - lr: 1.4943e-04
Epoch 31/40
111/111 [==============================] - 12s 105ms/step - loss: 0.2139 - categorical_accuracy: 0.8494 - val_loss: 0.1917 - val_categorical_accuracy: 0.8591 - lr: 1.4794e-04
Epoch 32/40
111/111 [==============================] - 12s 106ms/step - loss: 0.2121 - categorical_accuracy: 0.8494 - val_loss: 0.1866 - val_categorical_accuracy: 0.8647 - lr: 1.4646e-04
Epoch 33/40
111/111 [==============================] - 12s 106ms/step - loss: 0.2082 - categorical_accuracy: 0.8535 - val_loss: 0.1902 - val_categorical_accuracy: 0.8613 - lr: 1.4500e-04
Epoch 34/40
111/111 [==============================] - 12s 103ms/step - loss: 0.2045 - categorical_accuracy: 0.8530 - val_loss: 0.1923 - val_categorical_accuracy: 0.8691 - lr: 1.4355e-04
Epoch 35/40
111/111 [==============================] - 10s 90ms/step - loss: 0.2061 - categorical_accuracy: 0.8539 - val_loss: 0.1882 - val_categorical_accuracy: 0.8624 - lr: 1.4211e-04
Epoch 36/40
111/111 [==============================] - 12s 106ms/step - loss: 0.2036 - categorical_accuracy: 0.8529 - val_loss: 0.1907 - val_categorical_accuracy: 0.8647 - lr: 1.4069e-04
Epoch 37/40
111/111 [==============================] - 11s 95ms/step - loss: 0.2075 - categorical_accuracy: 0.8519 - val_loss: 0.1913 - val_categorical_accuracy: 0.8647 - lr: 1.3928e-04
Epoch 38/40
111/111 [==============================] - 11s 99ms/step - loss: 0.2067 - categorical_accuracy: 0.8522 - val_loss: 0.1883 - val_categorical_accuracy: 0.8613 - lr: 1.3789e-04
Epoch 39/40
111/111 [==============================] - 12s 109ms/step - loss: 0.2077 - categorical_accuracy: 0.8511 - val_loss: 0.1915 - val_categorical_accuracy: 0.8591 - lr: 1.3651e-04
Epoch 40/40
111/111 [==============================] - 13s 114ms/step - loss: 0.2016 - categorical_accuracy: 0.8552 - val_loss: 0.1868 - val_categorical_accuracy: 0.8624 - lr: 1.3515e-04
```

**Test result:**
Test loss:0.1770118623971939, Test accuracy:0.8724831938743591

## Training on Hagrid dataset with 1600 examples per label + 400 data augmentation per label (20%) = 2000 examples per label

**Model config:**
```
hparams = gesture_recognizer.HParams(learning_rate=0.0002, export_dir="exported_model_2", epochs=40, shuffle=True, batch_size=64)
model_options = gesture_recognizer.ModelOptions(dropout_rate=0.2, layer_widths=[1024, 512, 256, 128, 64])
```

**Training result:**
```
Epoch 1/40
120/120 [==============================] - 23s 145ms/step - loss: 0.6151 - categorical_accuracy: 0.6585 - val_loss: 0.3470 - val_categorical_accuracy: 0.8210 - lr: 2.0000e-04
Epoch 2/40
120/120 [==============================] - 13s 104ms/step - loss: 0.3408 - categorical_accuracy: 0.8122 - val_loss: 0.2200 - val_categorical_accuracy: 0.8658 - lr: 1.9800e-04
Epoch 3/40
120/120 [==============================] - 13s 103ms/step - loss: 0.2979 - categorical_accuracy: 0.8301 - val_loss: 0.1855 - val_categorical_accuracy: 0.8793 - lr: 1.9602e-04
Epoch 4/40
120/120 [==============================] - 13s 107ms/step - loss: 0.2782 - categorical_accuracy: 0.8315 - val_loss: 0.1711 - val_categorical_accuracy: 0.8928 - lr: 1.9406e-04
Epoch 5/40
120/120 [==============================] - 13s 103ms/step - loss: 0.2594 - categorical_accuracy: 0.8387 - val_loss: 0.1623 - val_categorical_accuracy: 0.8991 - lr: 1.9212e-04
Epoch 6/40
120/120 [==============================] - 13s 106ms/step - loss: 0.2528 - categorical_accuracy: 0.8419 - val_loss: 0.1599 - val_categorical_accuracy: 0.9022 - lr: 1.9020e-04
Epoch 7/40
120/120 [==============================] - 13s 111ms/step - loss: 0.2466 - categorical_accuracy: 0.8482 - val_loss: 0.1585 - val_categorical_accuracy: 0.9001 - lr: 1.8830e-04
Epoch 8/40
120/120 [==============================] - 13s 107ms/step - loss: 0.2431 - categorical_accuracy: 0.8413 - val_loss: 0.1535 - val_categorical_accuracy: 0.9043 - lr: 1.8641e-04
Epoch 9/40
120/120 [==============================] - 12s 100ms/step - loss: 0.2351 - categorical_accuracy: 0.8461 - val_loss: 0.1570 - val_categorical_accuracy: 0.8897 - lr: 1.8455e-04
Epoch 10/40
120/120 [==============================] - 13s 105ms/step - loss: 0.2329 - categorical_accuracy: 0.8510 - val_loss: 0.1542 - val_categorical_accuracy: 0.8949 - lr: 1.8270e-04
Epoch 11/40
120/120 [==============================] - 12s 102ms/step - loss: 0.2270 - categorical_accuracy: 0.8496 - val_loss: 0.1508 - val_categorical_accuracy: 0.8876 - lr: 1.8088e-04
Epoch 12/40
120/120 [==============================] - 13s 108ms/step - loss: 0.2234 - categorical_accuracy: 0.8521 - val_loss: 0.1512 - val_categorical_accuracy: 0.9001 - lr: 1.7907e-04
Epoch 13/40
120/120 [==============================] - 16s 128ms/step - loss: 0.2185 - categorical_accuracy: 0.8513 - val_loss: 0.1493 - val_categorical_accuracy: 0.9053 - lr: 1.7728e-04
Epoch 14/40
120/120 [==============================] - 13s 104ms/step - loss: 0.2170 - categorical_accuracy: 0.8521 - val_loss: 0.1472 - val_categorical_accuracy: 0.9053 - lr: 1.7550e-04
Epoch 15/40
120/120 [==============================] - 13s 105ms/step - loss: 0.2113 - categorical_accuracy: 0.8576 - val_loss: 0.1454 - val_categorical_accuracy: 0.9032 - lr: 1.7375e-04
Epoch 16/40
120/120 [==============================] - 13s 104ms/step - loss: 0.2143 - categorical_accuracy: 0.8585 - val_loss: 0.1441 - val_categorical_accuracy: 0.9022 - lr: 1.7201e-04
Epoch 17/40
120/120 [==============================] - 11s 86ms/step - loss: 0.2034 - categorical_accuracy: 0.8561 - val_loss: 0.1424 - val_categorical_accuracy: 0.9053 - lr: 1.7029e-04
Epoch 18/40
120/120 [==============================] - 12s 100ms/step - loss: 0.2052 - categorical_accuracy: 0.8570 - val_loss: 0.1394 - val_categorical_accuracy: 0.9147 - lr: 1.6859e-04
Epoch 19/40
120/120 [==============================] - 13s 103ms/step - loss: 0.2074 - categorical_accuracy: 0.8585 - val_loss: 0.1463 - val_categorical_accuracy: 0.9022 - lr: 1.6690e-04
Epoch 20/40
120/120 [==============================] - 17s 144ms/step - loss: 0.2003 - categorical_accuracy: 0.8611 - val_loss: 0.1403 - val_categorical_accuracy: 0.9022 - lr: 1.6523e-04
Epoch 21/40
120/120 [==============================] - 13s 105ms/step - loss: 0.1964 - categorical_accuracy: 0.8668 - val_loss: 0.1420 - val_categorical_accuracy: 0.9084 - lr: 1.6358e-04
Epoch 22/40
120/120 [==============================] - 13s 104ms/step - loss: 0.1967 - categorical_accuracy: 0.8613 - val_loss: 0.1367 - val_categorical_accuracy: 0.9126 - lr: 1.6195e-04
Epoch 23/40
120/120 [==============================] - 12s 101ms/step - loss: 0.1959 - categorical_accuracy: 0.8600 - val_loss: 0.1377 - val_categorical_accuracy: 0.9084 - lr: 1.6033e-04
Epoch 24/40
120/120 [==============================] - 13s 106ms/step - loss: 0.1985 - categorical_accuracy: 0.8579 - val_loss: 0.1386 - val_categorical_accuracy: 0.9147 - lr: 1.5872e-04
Epoch 25/40
120/120 [==============================] - 13s 105ms/step - loss: 0.1913 - categorical_accuracy: 0.8664 - val_loss: 0.1338 - val_categorical_accuracy: 0.9116 - lr: 1.5714e-04
Epoch 26/40
120/120 [==============================] - 13s 107ms/step - loss: 0.1947 - categorical_accuracy: 0.8583 - val_loss: 0.1352 - val_categorical_accuracy: 0.9136 - lr: 1.5556e-04
Epoch 27/40
120/120 [==============================] - 13s 110ms/step - loss: 0.1936 - categorical_accuracy: 0.8628 - val_loss: 0.1357 - val_categorical_accuracy: 0.9084 - lr: 1.5401e-04
Epoch 28/40
120/120 [==============================] - 12s 102ms/step - loss: 0.1910 - categorical_accuracy: 0.8642 - val_loss: 0.1356 - val_categorical_accuracy: 0.9105 - lr: 1.5247e-04
Epoch 29/40
120/120 [==============================] - 15s 120ms/step - loss: 0.1884 - categorical_accuracy: 0.8654 - val_loss: 0.1359 - val_categorical_accuracy: 0.9043 - lr: 1.5094e-04
Epoch 30/40
120/120 [==============================] - 18s 148ms/step - loss: 0.1917 - categorical_accuracy: 0.8626 - val_loss: 0.1339 - val_categorical_accuracy: 0.9126 - lr: 1.4943e-04
Epoch 31/40
120/120 [==============================] - 13s 108ms/step - loss: 0.1884 - categorical_accuracy: 0.8669 - val_loss: 0.1315 - val_categorical_accuracy: 0.9105 - lr: 1.4794e-04
Epoch 32/40
120/120 [==============================] - 13s 110ms/step - loss: 0.1871 - categorical_accuracy: 0.8661 - val_loss: 0.1344 - val_categorical_accuracy: 0.9095 - lr: 1.4646e-04
Epoch 33/40
120/120 [==============================] - 15s 123ms/step - loss: 0.1836 - categorical_accuracy: 0.8687 - val_loss: 0.1337 - val_categorical_accuracy: 0.9105 - lr: 1.4500e-04
Epoch 34/40
120/120 [==============================] - 14s 111ms/step - loss: 0.1856 - categorical_accuracy: 0.8699 - val_loss: 0.1349 - val_categorical_accuracy: 0.9147 - lr: 1.4355e-04
Epoch 35/40
120/120 [==============================] - 12s 95ms/step - loss: 0.1869 - categorical_accuracy: 0.8668 - val_loss: 0.1379 - val_categorical_accuracy: 0.9116 - lr: 1.4211e-04
Epoch 36/40
120/120 [==============================] - 13s 104ms/step - loss: 0.1819 - categorical_accuracy: 0.8661 - val_loss: 0.1344 - val_categorical_accuracy: 0.9074 - lr: 1.4069e-04
Epoch 37/40
120/120 [==============================] - 13s 110ms/step - loss: 0.1796 - categorical_accuracy: 0.8717 - val_loss: 0.1310 - val_categorical_accuracy: 0.9095 - lr: 1.3928e-04
Epoch 38/40
120/120 [==============================] - 13s 105ms/step - loss: 0.1813 - categorical_accuracy: 0.8701 - val_loss: 0.1322 - val_categorical_accuracy: 0.9084 - lr: 1.3789e-04
Epoch 39/40
120/120 [==============================] - 13s 104ms/step - loss: 0.1800 - categorical_accuracy: 0.8687 - val_loss: 0.1331 - val_categorical_accuracy: 0.9136 - lr: 1.3651e-04
Epoch 40/40
120/120 [==============================] - 13s 105ms/step - loss: 0.1793 - categorical_accuracy: 0.8695 - val_loss: 0.1353 - val_categorical_accuracy: 0.9084 - lr: 1.3515e-04
```

**Test result:**
Test loss:0.17035436630249023, Test accuracy:0.8772112131118774

## Dynamic gestures
- mano destra, da destra a sinistra: cancella un carattere

