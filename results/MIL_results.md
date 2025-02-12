# Model config

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-3),
    loss=keras.losses.CategoricalCrossentropy(),  # Use categorical crossentropy for multi-class classification
    metrics=['accuracy']
)

history = model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)

Epoch 1/10
28/28 ━━━━━━━━━━━━━━━━━━━━ 98s 3s/step - accuracy: 0.2706 - loss: 2.3731 - val_accuracy: 0.6457 - val_loss: 1.0870
Epoch 2/10
28/28 ━━━━━━━━━━━━━━━━━━━━ 147s 4s/step - accuracy: 0.7249 - loss: 0.8151 - val_accuracy: 0.8430 - val_loss: 0.5092
Epoch 3/10
28/28 ━━━━━━━━━━━━━━━━━━━━ 136s 3s/step - accuracy: 0.9002 - loss: 0.3011 - val_accuracy: 0.8744 - val_loss: 0.4451
Epoch 4/10
28/28 ━━━━━━━━━━━━━━━━━━━━ 142s 3s/step - accuracy: 0.9520 - loss: 0.1603 - val_accuracy: 0.8744 - val_loss: 0.4380
Epoch 5/10
28/28 ━━━━━━━━━━━━━━━━━━━━ 147s 4s/step - accuracy: 0.9838 - loss: 0.0673 - val_accuracy: 0.9058 - val_loss: 0.2993
Epoch 6/10
28/28 ━━━━━━━━━━━━━━━━━━━━ 136s 3s/step - accuracy: 0.9821 - loss: 0.0449 - val_accuracy: 0.9103 - val_loss: 0.3470
Epoch 7/10
28/28 ━━━━━━━━━━━━━━━━━━━━ 95s 3s/step - accuracy: 0.9994 - loss: 0.0076 - val_accuracy: 0.9193 - val_loss: 0.3269
Epoch 8/10
28/28 ━━━━━━━━━━━━━━━━━━━━ 140s 3s/step - accuracy: 0.9975 - loss: 0.0106 - val_accuracy: 0.9238 - val_loss: 0.3215
Epoch 9/10
28/28 ━━━━━━━━━━━━━━━━━━━━ 143s 3s/step - accuracy: 1.0000 - loss: 0.0051 - val_accuracy: 0.9148 - val_loss: 0.3046
Epoch 10/10
28/28 ━━━━━━━━━━━━━━━━━━━━ 99s 4s/step - accuracy: 0.9982 - loss: 0.0054 - val_accuracy: 0.9148 - val_loss: 0.3200

Test Loss: 0.3317
Test Accuracy: 0.9204

# Data Hands crop, right dataset split 

model = keras.models.Sequential()

model.add(keras.layers.LSTM(2048,
                            activation='tanh',
                            recurrent_activation='sigmoid',
                            dropout=0.5,
                            recurrent_dropout=0.5,
                            kernel_regularizer=keras.regularizers.l2(1e-4),
                            input_shape=(X.shape[1], 2048)))

# Aggiunta di Batch Normalization dopo LSTM
model.add(keras.layers.BatchNormalization())

model.add(keras.layers.Dense(512, activation='relu', kernel_regularizer=keras.regularizers.l2(1e-3)))

# Aggiunta di Batch Normalization dopo Dense
model.add(keras.layers.BatchNormalization())

model.add(keras.layers.Dropout(0.5))

model.add(keras.layers.Dense(6, activation='softmax'))

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-5),
    loss=keras.losses.CategoricalCrossentropy(),  # Use categorical crossentropy for multi-class classification
    metrics=['accuracy']
)

early_stopping = keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=20,  # Numero di epoche senza miglioramenti prima di fermarsi
)

history = model.fit(
    X,
    y,
    epochs=300,
    batch_size=64,
    validation_split=0.1,
    shuffle=True,
    callbacks=[early_stopping]
)

Epoch 128/300
16/16 ━━━━━━━━━━━━━━━━━━━━ 2s 143ms/step - accuracy: 0.9156 - loss: 0.6274 - val_accuracy: 0.7544 - val_loss: 1.0415
Epoch 129/300
16/16 ━━━━━━━━━━━━━━━━━━━━ 2s 138ms/step - accuracy: 0.9193 - loss: 0.6302 - val_accuracy: 0.7719 - val_loss: 1.0244
Epoch 130/300
16/16 ━━━━━━━━━━━━━━━━━━━━ 3s 138ms/step - accuracy: 0.9238 - loss: 0.6042 - val_accuracy: 0.7456 - val_loss: 1.0522
Epoch 131/300
16/16 ━━━━━━━━━━━━━━━━━━━━ 3s 144ms/step - accuracy: 0.9252 - loss: 0.5917 - val_accuracy: 0.7456 - val_loss: 1.0654
Epoch 132/300
16/16 ━━━━━━━━━━━━━━━━━━━━ 2s 148ms/step - accuracy: 0.9278 - loss: 0.5974 - val_accuracy: 0.7544 - val_loss: 1.0670
Epoch 133/300
16/16 ━━━━━━━━━━━━━━━━━━━━ 2s 141ms/step - accuracy: 0.9348 - loss: 0.5996 - val_accuracy: 0.7544 - val_loss: 1.0720
Epoch 134/300
16/16 ━━━━━━━━━━━━━━━━━━━━ 2s 139ms/step - accuracy: 0.9295 - loss: 0.5878 - val_accuracy: 0.7544 - val_loss: 1.0716

3/3 ━━━━━━━━━━━━━━━━━━━━ 0s 46ms/step - accuracy: 0.8490 - loss: 0.7567
Test Loss: 0.8669
Test Accuracy: 0.8152