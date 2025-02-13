# Static gestures 

## Training on Hagrid dataset with 1000 examples per label + 1000 data augmentation per label = 2000 examples per label

**Model config:**
```
hparams = gesture_recognizer.HParams(learning_rate=0.001,export_dir="exported_model_2", epochs=15, shuffle=True, batch_size=16, gamma=3)
model_options = gesture_recognizer.ModelOptions(dropout_rate=0.1,layer_widths=[256, 128])
```

**Training results:**

Epoch 15/15
425/425 [==============================] - 8s 20ms/step - loss: 0.1517 - categorical_accuracy: 0.8529 - val_loss: 0.1513 - val_categorical_accuracy: 0.8732 - lr: 8.6875e-04

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

Epoch 30/30
58/58 [==============================] - 9s 153ms/step - loss: 0.1617 - categorical_accuracy: 0.8803 - val_loss: 0.1628 - val_categorical_accuracy: 0.8929 - lr: 1.4943e-04
```

**Test results:**
Test loss:0.1385858952999115, Test accuracy:0.9004237055778503 => **the best**

## Training on Hagrid dataset with 1400 examples per label + 600 data augmentation per label (30%) = 2000 examples per label

**Model config:**
```
hparams = gesture_recognizer.HParams(learning_rate=0.0002, export_dir="exported_model_2", epochs=40, shuffle=True, batch_size=64)
model_options = gesture_recognizer.ModelOptions(dropout_rate=0.2, layer_widths=[1024, 512, 256, 128, 64])
```

**Training result:**
```
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
Epoch 40/40
120/120 [==============================] - 13s 105ms/step - loss: 0.1793 - categorical_accuracy: 0.8695 - val_loss: 0.1353 - val_categorical_accuracy: 0.9084 - lr: 1.3515e-04
```

**Test result:**
Test loss:0.17035436630249023, Test accuracy:0.8772112131118774