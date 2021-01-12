from neuron import Neuron, NeuronInput, Input
import functions

input1 = NeuronInput(0.8, 'Input1')
input2 = NeuronInput(0.25, 'Input2')

neuron1 = Neuron(bias=1, activation_f=functions.fermi, name='Neuron1')
neuron1.connect(input1, 0.2)

neuron2 = Neuron(bias=1, activation_f=functions.fermi, name='Neuron2')
neuron2.connect(input2, 1)

neuron3 = Neuron(bias=1, activation_f=functions.fermi, name='Neuron3')
neuron3.connect(neuron1, 0.8)
neuron3.connect(neuron2, 0.5)

neuron3.print_info()
