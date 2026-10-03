import tensorflow as tf
import numpy as np

prices = np.array([90,91,93,92,95], dtype=float)

X = prices[:-1].reshape(-1,1)
y = prices[1:].reshape(-1,1)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(
    optimizer='adam',
    loss='mse'
)

model.fit(X, y, epochs=100)

prediction = model.predict(
    np.array([[95]], dtype=float)
)

print("Next Price:", prediction[0][0])

