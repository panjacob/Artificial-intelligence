import numpy as np


def function_fermi(x):
    return 1 / (1 + np.exp(-1 * x))


class Input:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


class Neuron:
    def __init__(self, bias, activation_f):
        self.inputs = []
        self.bias = bias
        self.activation_f = activation_f

    def add_input(self, input):
        self.inputs.append(input)

    def output(self):
        sum_input = 0
        for input in self.inputs:
            sum_input += input.value * input.weight
        return self.activation_f(sum_input + self.bias)


neuron1 = Neuron(bias=1, activation_f=function_fermi)
neuron2 = Neuron(bias=1, activation_f=function_fermi)
neuron1.add_input(Input(0.8, 1))
neuron1.add_input(Input(0.25, 1))
neuron2.add_input(Input(0.5, 0.88))
neuron2.add_input(Input(0.8, 0.47))
neuron2.add_input(Input(1, 1))

neuron3 = Neuron(bias=1, activation_f=function_fermi)
neuron3.add_input(Input(neuron1.output(), 0.8))
neuron3.add_input(Input(neuron2.output(), 0.2))
output3 = neuron3.output()
print(output3)
