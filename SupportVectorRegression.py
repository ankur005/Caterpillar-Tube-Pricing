from Helper import outDir
from math import pi
from sklearn.svm import SVR
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import os


def generateDataWithNewFeatures(dataFrame, fileName, cost=True):
    dataFrame['volume'] = pi * dataFrame.diameter * dataFrame.diameter * 0.25 * dataFrame.length

    # Delete original 'diameter' and 'length' columns
    del dataFrame['diameter']
    del dataFrame['length']
    del dataFrame['end_a_1x']
    del dataFrame['end_x_1x']
    del dataFrame['end_a_2x']
    del dataFrame['end_x_2x']
    del dataFrame['end_a_forming']
    del dataFrame['end_x_forming']
    del dataFrame['num_bracket']
    del dataFrame['bracket_pricing']


    # Keep 'cost' as the last column
    columns = dataFrame.columns.tolist()
    if cost:
        columns.pop(columns.index('cost'))
        columns.append('cost')
    trainData = dataFrame[columns]
    file = open(os.path.join(outDir, fileName), 'w')
    trainData.to_csv(file)


def runSVR():
    trainData = pd.read_csv(os.path.join(outDir, 'train_data_new_updated_features.csv'), header=0)
    testData = pd.read_csv(os.path.join(outDir, 'test_data_new_updated_features.csv'), header=0)
    # predictors = list(trainData)[4:23]
    regressionCoeffDict = {}
    # print predictors
    x_train = trainData.iloc[:, 2:13]
    # print x_train
    y_train = trainData['cost'].tolist()
    x_test = testData.iloc[:, 2:13]
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
    for i in range(0, len(result)):
        resultDict[i + 1] = result[i]

    predictedCosts = pd.DataFrame(resultDict.items(), columns=['id', 'cost'])
    file = open(os.path.join(outDir, 'submission_svm.csv'), 'w')
    predictedCosts.to_csv(file)
    # plt.bar(range(len(predictors)), lm.coef_)
    # plt.xticks(range(len(predictors)), predictors, rotation='vertical')
    # plt.scatter(y, lm.predict(x))
    # plt.xlabel("Other")
    # plt.ylabel("Cost")
    # plt.show()
    print "Ended at:", datetime.datetime.now()

print "Started at:", datetime.datetime.now()
generateDataWithNewFeatures(pd.read_csv(os.path.join(outDir, 'train_data_new.csv')), 'train_data_new_updated_features.csv')
generateDataWithNewFeatures(pd.read_csv(os.path.join(outDir, 'test_data_new.csv')), 'test_data_new_updated_features.csv', cost=False)
runSVR()

