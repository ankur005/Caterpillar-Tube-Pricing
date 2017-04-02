from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from Helper import inDir, outDir
import pandas as pd
import os

def one_hot_encoding(columnName):
    # trainData = pd.read_csv((os.path.join(outDir, 'train_data.csv')))
    # trainData = pd.concat([trainData, pd.get_dummies(trainData[columnName])], axis=1);
    #
    # file = open(os.path.join(outDir,'train_data.csv'),'w')
    # trainData.to_csv(file)

    testData = pd.read_csv((os.path.join(outDir, 'test_data.csv')))
    testData = pd.concat([testData, pd.get_dummies(testData[columnName])], axis=1);

    file = open(os.path.join(outDir, 'test_data.csv'), 'w')
    testData.to_csv(file)

one_hot_encoding('material_id')