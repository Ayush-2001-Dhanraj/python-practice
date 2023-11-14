import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()
# initialize seed
# np.random.seed(0)

X, y = spiral_data(5, 3)  

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        """
        n_inputs represents the no of features
        n_neurons represents the no of neurons we want in this particular layer

        weights are inputs x no of neurons - helps avoid transpose operation in dot product
        weights range between -1 to +1 so tht they are close to each other and NN doesn't explode
        
        biases is set to zero initially and if we encounter error where the entore output of
        NN is zero we cqan intialize it to some value to avoid dead ANN
        """
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)



layer1 = Layer_Dense(2, 5)
activarion1 = Activation_ReLU()
layer1.forward(X)
# print(layer1.output)
activarion1.forward(layer1.output)
print(activarion1.output)
