import theano
import os
import pickle
import lasagne
from lasagne.layers import set_all_param_values, get_all_param_values

import Helper
import nnet_model as nnet
import theano.tensor as T
import pandas as pd
import numpy as np

def get_model_weights():
    # with open('blvc_googlenet.pkl', 'rb') as f:
    with open('nnet.pkl', 'rb') as f:
        params = pickle.load(f)
    # print "pkl weights: ",params
    return params


def init_model(input_var=None):
    net = nnet.build_model(input_var=input_var)

    if(os.path.exists('nnet.pkl')):
        params = get_model_weights()
        set_all_param_values(net['output'], params['param values'])
    return net

def train(inputFile, numEpochs):
    training_batch = get_dataset(inputFile)
    inputNum = len(training_batch[0][0])

    input_var = T.col('inputs')
    target_var = T.scalar('output')
    net = init_model(input_var=input_var)

    # create loss function
    output = net['output']
    prediction = lasagne.layers.get_output(output, deterministic=True)
    loss = lasagne.objectives.squared_error(prediction, target_var)
    loss = T.sum(loss)

    # create parameter update expressions
    params = lasagne.layers.get_all_params(output, trainable=True)
    updates = lasagne.updates.sgd(loss, params, learning_rate=0.8)

    train_fn = theano.function([input_var, target_var], loss, updates=updates, allow_input_downcast=True)

    for epoch in range(numEpochs):
        loss = 0
        count = 1

        for record in training_batch:
            input = record[0][0:len(record)-2]
            out = record[len(record)-1]
            loss = loss + train_fn(np.reshape(input,(len(input),1)), out)
            print "Epoch, Record num: ", (epoch + 1), ", ", count
            count = count + 1

        print("Epoch %d: Loss %g" % (epoch + 1, loss / len(training_batch)))

        param_vals = get_all_param_values(output)
        save_params(param_vals)

    save_params(param_vals)
    return param_vals

def save_params(param_vals):
	f = open('nnet.pkl', 'wb')
	pickle.dump(param_vals, f, protocol=pickle.HIGHEST_PROTOCOL)
	f.close()

def get_dataset(csvFile):
    dataset = []

    dataset_df = pd.read_csv(csvFile)
    input_df = dataset_df.drop('cost',axis=1)
    output_df = dataset_df['cost']

    inputs = [list(x) for x in input_df.to_records(index=False)]
    outputs = output_df.tolist()

    for i in range(len(inputs)):
        dataset.append((inputs[i],outputs[i]))

    dataset = np.array(dataset)

    return dataset

train(Helper.outDir + '/selected_train_data.csv', 1)