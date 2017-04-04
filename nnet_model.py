from lasagne.layers import InputLayer, DenseLayer
from lasagne.nonlinearities import linear, rectify


def build_model(inputNum=20,input_var=None):
    net = {}
    net['input'] = InputLayer((inputNum,1), input_var)
    net['linear'] = DenseLayer(net['input'],
                               num_units=inputNum,
                               num_leading_axes=0,
                                nonlinearity=linear)
    net['output'] = DenseLayer(net['linear'],
                                num_units=1,
                                num_leading_axes=0,
                                nonlinearity=rectify)
    return net