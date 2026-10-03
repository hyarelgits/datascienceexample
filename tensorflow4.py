import tensorflow as tf
import numpy as np

hours = np.array([1,2,3,4,5], dtype=float).reshape(-1,1)
marks = np.array([30,45,60,75,90], dtype=float).reshape(-1,1)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(1)
])

model.compile(
    optimizer='adam',
    loss='mean_squared_error'
)

model.fit(hours, marks, epochs=500)

prediction = model.predict(
    np.array([[6]], dtype=float)
)

print("Predicted Marks:", prediction[0][0])

