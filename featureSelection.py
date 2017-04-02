import pandas as pd
from Helper import inDir, outDir, yesNotoBinary
import os
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.svm import SVR
from sklearn.feature_selection import RFE
import numpy as np
import matplotlib.pyplot as plt

trainData = pd.read_csv(os.path.join(outDir, 'train_data.csv'))
predictors = list(trainData)[4:41]
selectKBestDict = {}
#print predictors
x = trainData.iloc[:, 4:41]
y = trainData['cost'].tolist()
selector = SelectKBest(score_func=f_regression, k=37)
x_new = selector.fit(x,y)
#print selector.pvalues_
scores = np.log10(selector.scores_)
j = 0
for item in predictors:
    selectKBestDict[item] = scores[j]
    j = j + 1
#print selectKBestDict
#plt.bar(range(len(predictors)), scores)
#plt.xticks(range(len(predictors)), predictors, rotation='vertical')
#plt.show()
clf = SVR(kernel="linear")
rfe = RFE(clf)
rfe = rfe.fit(x, y)
print(rfe.ranking_)
# print summaries for the selection of attributes
print(rfe.support_)