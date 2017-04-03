import pandas as pd
from Helper import inDir, outDir, yesNotoBinary
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
import pickle

trainData = pd.read_csv(os.path.join(outDir, 'train_data_new.csv'), header=0)
testData = pd.read_csv(os.path.join(outDir, 'test_data_new.csv'), header=0)
# predictors = list(trainData)[4:23]
regressionCoeffDict = {}
#print predictors
x_train = trainData.iloc[:,1:21]
# print x_train
y_train = trainData['cost'].tolist()
x_test = testData.iloc[:,1:21]
y_test = []
lm = SVR(kernel='poly', degree=2)
lm.fit(x_train, y_train)
# filename = 'finalized_model.sav'
# pickle.dump(lm, open(filename, 'wb'))
# loaded_model = pickle.load(open(filename, 'rb'))
result = lm.predict(x_test)
print result

plt.scatter(x_test, result)
plt.show()

resultDict = {}
for i in range(0,len(result)):
    resultDict[i+1]=result[i]

predictedCosts = pd.DataFrame(resultDict.items(), columns=['id','cost'])
file = open(os.path.join(outDir,'submission2.csv'),'w')
predictedCosts.to_csv(file)
#plt.bar(range(len(predictors)), lm.coef_)
#plt.xticks(range(len(predictors)), predictors, rotation='vertical')
#plt.scatter(y, lm.predict(x))
#plt.xlabel("Other")
#plt.ylabel("Cost")
#plt.show()