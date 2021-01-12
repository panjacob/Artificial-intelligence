class Input:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


class NeuronInput:
    def __init__(self, value, name):
        self.name = name
        self.value = value
        self.neuron_weights = []

    def output(self):
        return self.value

    def print_info(self):
        print('    Name: ', self.name)


class Neuron:
    def __init__(self, bias, activation_f, name):
        self.name = name
        self.bias = bias
        self.activation_f = activation_f
        self.neurons_weights = []
        self.activated = False

    def connect(self, neuron, weight):
        self.neurons_weights.append((neuron, weight))

    def output(self):
        sum_input = 0
        for neuron_weight in self.neurons_weights:
            neuron, weight = neuron_weight
            sum_input += neuron.output() * weight
        self.activated = True
        return self.activation_f(sum_input + self.bias)

    def print_inputs(self):
        print('    inputs: ')
        for neuron_weight in self.neurons_weights:
            neuron, weight = neuron_weight
            print('        value: ', neuron.output(), '  weight: ', weight)

    def activation_function_name(self):
        return self.activation_f.__name__

    def print_connected_neurons(self):
        print('connectend neurons: ')
        for neuron_weight in self.neurons_weights:
            neuron, weight = neuron_weight
            print('    Name: ', neuron.name, '  Weight', weight)
            neuron.print_info()

    def print_info(self):
        print(self.name, ": ")
        print('        activated: '.format(self.name), self.activated)
        print('        bias: '.format(self.name), self.bias)
        print('        activation function: '.format(self.name), self.activation_function_name())
        self.print_inputs()
        print('        output: '.format(self.name), self.output())
        self.print_connected_neurons()
