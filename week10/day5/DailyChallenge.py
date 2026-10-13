import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Set seeds for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

# ==========================================
# 1. LOAD THE MNIST DATASET
# ==========================================
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print("--- Dataset Shapes ---")
print(f"x_train shape: {x_train.shape} | y_train shape: {y_train.shape}")
print(f"x_test shape:  {x_test.shape}  | y_test shape:  {y_test.shape}")


# ==========================================
# 2. PREPROCESS DATA FOR FULLY CONNECTED NETWORK (FCNN)
# ==========================================
# Flatten images from (28, 28) to 784 1D vectors
x_train_fcnn = x_train.reshape((60000, 784)).astype("float32") / 255.0
x_test_fcnn = x_test.reshape((10000, 784)).astype("float32") / 255.0

# One-hot encode the target labels
y_train_cat = keras.utils.to_categorical(y_train, 10)
y_test_cat = keras.utils.to_categorical(y_test, 10)


# ==========================================
# 3. BUILD AND TRAIN FULLY CONNECTED NEURAL NETWORK
# ==========================================
fcnn_model = keras.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

fcnn_model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("\nTraining Fully Connected Neural Network...")
fcnn_model.fit(
    x_train_fcnn, y_train_cat,
    epochs=5,
    batch_size=64,
    validation_data=(x_test_fcnn, y_test_cat)
)

fcnn_loss, fcnn_acc = fcnn_model.evaluate(x_test_fcnn, y_test_cat, verbose=0)
print(f"FCNN Test Accuracy: {fcnn_acc * 100:.2f}%")


# ==========================================
# 4. PREPROCESS DATA FOR CONVOLUTIONAL NEURAL NETWORK (CNN)
# ==========================================
# Reshape images to (28, 28, 1) to include the channel dimension
x_train_cnn = x_train.reshape((60000, 28, 28, 1)).astype("float32") / 255.0
x_test_cnn = x_test.reshape((10000, 28, 28, 1)).astype("float32") / 255.0


# ==========================================
# 5. BUILD AND TRAIN CONVOLUTIONAL NEURAL NETWORK
# ==========================================
cnn_model = keras.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

cnn_model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("\nTraining Convolutional Neural Network...")
cnn_model.fit(
    x_train_cnn, y_train_cat,
    epochs=5,
    batch_size=64,
    validation_data=(x_test_cnn, y_test_cat)
)

cnn_loss, cnn_acc = cnn_model.evaluate(x_test_cnn, y_test_cat, verbose=0)
print(f"CNN Test Accuracy: {cnn_acc * 100:.2f}%")


# ==========================================
# 6. COMPARE PERFORMANCE
# ==========================================
print("\n--- Performance Comparison ---")
print(f"Fully Connected Network Test Accuracy: {fcnn_acc * 100:.2f}% (Loss: {fcnn_loss:.4f})")
print(f"Convolutional Neural Network Test Accuracy: {cnn_acc * 100:.2f}% (Loss: {cnn_loss:.4f})")

"""
Observations:
- The Fully Connected Network flattens 2D spatial information into a 1D vector, treating pixels independently.
- The CNN uses 2D spatial filters (Conv2D + MaxPool2D) that extract local spatial features (edges, curves, shapes),
  allowing it to achieve higher test accuracy (~99% vs ~97.5%) with fewer parameters and greater spatial invariance.
"""