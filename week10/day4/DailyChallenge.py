import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

# Set random seed for reproducibility
tf.random.set_seed(42)
np.random.seed(42)

# ==========================================
# 2. DATASET CREATION AND VISUALIZATION
# ==========================================
samples = 1000
X, y = make_circles(samples, noise=0.03, random_state=42)

print(f"X shape: {X.shape}, y shape: {y.shape}")

# Visualize the raw concentric circle dataset
plt.figure(figsize=(6, 5))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdYlBu, edgecolors='k')
plt.title("Concentric Circles Dataset")
plt.xlabel("X1")
plt.ylabel("X2")
plt.show()

# ==========================================
# 5. DECISION BOUNDARY FUNCTION
# ==========================================
def plot_decision_boundary(model, X, y, title="Decision Boundary"):
    """Plots the decision boundary for a Keras classification model."""
    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    grid = np.c_[xx.ravel(), yy.ravel()]
    
    preds = model.predict(grid, verbose=0)
    
    if preds.shape[-1] > 1:
        preds = np.argmax(preds, axis=1)
    else:
        preds = np.round(preds)
        
    preds = preds.reshape(xx.shape)
    
    plt.contourf(xx, yy, preds, alpha=0.7, cmap=plt.cm.RdYlBu)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.RdYlBu, edgecolors='k')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title(title)

# ==========================================
# 3. BUILD A BASIC NEURAL NETWORK MODEL
# ==========================================
# Single Dense Layer (Linear Classifier)
model_1 = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model_1.compile(
    loss=tf.keras.losses.BinaryCrossentropy(),
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.01),
    metrics=['accuracy']
)

model_1.fit(X, y, epochs=100, verbose=0)
loss_1, acc_1 = model_1.evaluate(X, y, verbose=0)
print(f"Model 1 (Single Layer Linear) - Accuracy: {acc_1 * 100:.2f}%")

# ==========================================
# 4. IMPROVE MODEL CAPACITY & OPTIMIZER
# ==========================================
# Deeper model without non-linear activation functions (Linear Stack)
model_2 = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model_2.compile(
    loss=tf.keras.losses.BinaryCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
    metrics=['accuracy']
)

model_2.fit(X, y, epochs=200, verbose=0)
loss_2, acc_2 = model_2.evaluate(X, y, verbose=0)
print(f"Model 2 (Deep Linear Architecture) - Accuracy: {acc_2 * 100:.2f}%")

# ==========================================
# 6 & 7. ACTIVATION FUNCTIONS & TRAIN/TEST SPLIT
# ==========================================
# 80/20 Train-Test Data Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model incorporating non-linear activations (ReLU + Sigmoid)
model_3 = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model_3.compile(
    loss=tf.keras.losses.BinaryCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
    metrics=['accuracy']
)

# Train on train set
history = model_3.fit(X_train, y_train, epochs=200, verbose=0)

# ==========================================
# 8. EVALUATE & VISUALIZE FINAL MODEL
# ==========================================
train_loss, train_acc = model_3.evaluate(X_train, y_train, verbose=0)
test_loss, test_acc = model_3.evaluate(X_test, y_test, verbose=0)

print(f"\nModel 3 (Non-Linear ReLU Model) Train Accuracy: {train_acc * 100:.2f}%")
print(f"Model 3 (Non-Linear ReLU Model) Test Accuracy:  {test_acc * 100:.2f}%")

# Plot Decision Boundaries Comparison
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plot_decision_boundary(model_1, X, y, title=f"Model 1 (Linear SGD)\nAcc: {acc_1 * 100:.1f}%")

plt.subplot(1, 3, 2)
plot_decision_boundary(model_2, X, y, title=f"Model 2 (Deep Linear Adam)\nAcc: {acc_2 * 100:.1f}%")

plt.subplot(1, 3, 3)
plot_decision_boundary(model_3, X_test, y_test, title=f"Model 3 (ReLU Non-Linear Test)\nAcc: {test_acc * 100:.1f}%")

plt.tight_layout()
plt.show()