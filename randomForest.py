import pandas as pd
from Helper import inDir, outDir, yesNotoBinary, rmsle
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

trainData = pd.read_csv(os.path.join(outDir, 'train_data_new.csv'), header=0)
testData = pd.read_csv(os.path.join(outDir, 'test_data_new.csv'), header=0)
predictors = list(trainData)[1:21]
#print predictors
x_train = trainData.iloc[:,1:21]
y_train = trainData['cost'].tolist()
x_test = testData.iloc[:,1:21]
rfDict = {}
#print x_train
rf = RandomForestRegressor()
rf = rf.fit(x_train, y_train)
j = 0
for item in predictors:
    rfDict[item] = rf.feature_importances_[j]
    j = j + 1
plt.bar(range(len(predictors)), rf.feature_importances_)
plt.xticks(range(len(predictors)), predictors, rotation='vertical')
plt.show()
result = rf.predict(x_test)
resultDict = {}
for i in range(0,len(result)):
    resultDict[i+1]=result[i]
#predictedCosts = pd.DataFrame(resultDict.items(), columns=['id','cost'])
#file = open(os.path.join(outDir,'submission_rf.csv'),'w')
#predictedCosts.to_csv(file)

#print rf.score(x_train, y_train)
# print rf.predict(x_train)