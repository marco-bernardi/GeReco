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