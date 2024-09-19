import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class FeedforwardNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.bias_hidden = np.random.rand(hidden_size)
        self.bias_output = np.random.rand(output_size)
        
    def train(self, X, y, learning_rate, epochs):
        for epoch in range(epochs):
            hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
            hidden_output = sigmoid(hidden_input)
            final_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
            final_output = sigmoid(final_input)
            
            # Backpropagation
            output_error = y - final_output
            output_delta = output_error * sigmoid_derivative(final_output)

            hidden_error = output_delta.dot(self.weights_hidden_output.T)
            hidden_delta = hidden_error * sigmoid_derivative(hidden_output)
            
            # Update weights and biases
            self.weights_hidden_output += hidden_output.T.dot(output_delta) * learning_rate
            self.weights_input_hidden += X.T.dot(hidden_delta) * learning_rate
            self.bias_output += np.sum(output_delta, axis=0) * learning_rate
            self.bias_hidden += np.sum(hidden_delta, axis=0) * learning_rate

    def predict(self, X):
        hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        hidden_output = sigmoid(hidden_input)
        final_input = np.dot(hidden_output, self.weights_hidden_output) + self.bias_output
        final_output = sigmoid(final_input)
        return np.argmax(final_output, axis=1)

X, y = make_moons(n_samples=500, noise=0.2, random_state=42)

encoder = OneHotEncoder(sparse_output=False)
y_onehot = encoder.fit_transform(y.reshape(-1, 1))

X_train, X_test, y_train, y_test = train_test_split(X, y_onehot, test_size=0.2, random_state=42)

input_size = X_train.shape[1]
hidden_size = 5
output_size = y_onehot.shape[1]
nn = FeedforwardNeuralNetwork(input_size, hidden_size, output_size)

nn.train(X_train, y_train, learning_rate=0.1, epochs=10000)

y_pred = nn.predict(X_test)

y_test_labels = np.argmax(y_test, axis=1)

accuracy = accuracy_score(y_test_labels, y_pred)
print(f'Accuracy: {accuracy:.2f}')
