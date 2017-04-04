import pandas as pd
import numpy as np
from sklearn import ensemble, preprocessing
from Helper import inDir, outDir, yesNotoBinary, rmsle
import os
import xgboost as xgb
import matplotlib.pyplot as plt

# load training and test datasets
train = pd.read_csv(os.path.join(outDir, 'train_data_new.csv'))
test = pd.read_csv(os.path.join(outDir, 'test_data_new.csv'))

print("train columns")
print(train.columns)
print("test columns")
print(test.columns)

print(train.columns.to_series().groupby(train.dtypes).groups)

labels = train.cost.values
#'tube_assembly_id', 'supplier', 'bracket_pricing', 'material_id', 'end_a_1x', 'end_a_2x', 'end_x_1x', 'end_x_2x', 'end_a', 'end_x'
#for some reason material_id cannot be converted to categorical variable
idx = test.id.values.astype(int)
test = test.drop(['id'], axis = 1)
train = train.drop(['cost'], axis = 1)


print("train columns")
print(train.columns)
print("test columns")
print(test.columns)

# convert data to numpy array
train = np.array(train)
test = np.array(test)

# object array to float
train = train.astype(float)
test = test.astype(float)

# i like to train on log(1+x) for RMSLE ;)
# The choice is yours :)
label_log = np.log1p(labels)

# fit a random forest model

params = {}
params["objective"] = "reg:linear"
params["eta"] = 0.05
params["min_child_weight"] = 5
params["subsample"] = 0.8
params["colsample_bytree"] = 0.8
params["scale_pos_weight"] = 1.0
params["silent"] = 1
params["max_depth"] = 7

plst = list(params.items())

xgtrain = xgb.DMatrix(train, label=label_log)
xgtest = xgb.DMatrix(test)


num_rounds = 2000
model = xgb.train(plst, xgtrain, num_rounds)
preds1 = model.predict(xgtest)

num_rounds = 3000
model = xgb.train(plst, xgtrain, num_rounds)
preds2 = model.predict(xgtest)

num_rounds = 1000
model = xgb.train(plst, xgtrain, num_rounds)
preds4 = model.predict(xgtest)


num_rounds = 500
model = xgb.train(plst, xgtrain, num_rounds)
preds7 = model.predict(xgtest)

label_log = np.power(labels,1/16)

xgtrain = xgb.DMatrix(train, label=label_log)
xgtest = xgb.DMatrix(test)
num_rounds = 5000
model = xgb.train(plst, xgtrain, num_rounds)
preds3 = model.predict(xgtest)



#for loop in range(2):
#    model = xgb.train(plst, xgtrain, num_rounds)
#    preds1 = preds1 + model.predict(xgtest)
preds = (np.expm1( (preds1+preds2+preds4+preds7)/4)+np.power(preds3,16))/2

preds = pd.DataFrame({"id": idx, "cost": preds})
preds.to_csv('benchmark_mod_1.csv', index=False)