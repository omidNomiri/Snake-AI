import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.losses import sparse_categorical_crossentropy

# Load dataset
data = pd.read_csv("dataset/snake_state_dataset.csv")

# Prepare input features and target variable
X = data[['wall_up', 'wall_right', 'wall_down', 'wall_left', 'meat_up',
          'meat_right', 'meat_down', 'meat_left', 'distance_x', 'distance_y']]
Y = data['direction']

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# Define the neural network model
model = Sequential([
    Dense(len(x_train.columns), activation="relu"),  # Input layer with ReLU activation
    Dense(64, activation="relu"),                   # Hidden layer with 64 units
    Dense(32, activation="relu"),                   # Hidden layer with 32 units
    Dense(4, activation="softmax")                  # Output layer with Softmax for multi-class classification
])

# Compile the model
model.compile(optimizer=Adam(),
              loss=sparse_categorical_crossentropy, metrics=['accuracy'])

# Train the model
output_history = model.fit(x_train, y_train, epochs=60, validation_split=0.2)

# Save the trained model
model.save("model/snake_direction_model.h5")

# Evaluate the model on test data
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Loss: {loss}, Accuracy: {accuracy}")

# Plot training loss and accuracy
plt.plot(output_history.history['loss'], label="Loss")
plt.plot(output_history.history['accuracy'], label="Accuracy")
plt.title("Model Training Loss and Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Value")
plt.legend()
plt.show()
