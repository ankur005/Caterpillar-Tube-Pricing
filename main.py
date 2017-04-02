from Helper import inDir, outDir, yesNotoBinary
import os
import pandas as pd

def main():
    testData = pd.read_csv(os.path.join(outDir,'test_data.csv'))
    # trainData = yesNotoBinary(trainData,'bracket_pricing')
    # trainData = yesNotoBinary(trainData, 'end_a_1x')
    # trainData = yesNotoBinary(trainData, 'end_a_2x')
    # trainData = yesNotoBinary(trainData, 'end_x_1x')
    # trainData = yesNotoBinary(trainData, 'end_x_2x')
    # trainData = yesNotoBinary(trainData, 'end_a_forming')
    # trainData = yesNotoBinary(trainData, 'end_x_forming')
    # trainData.to_csv(os.path.join(outDir,'train_data.csv'))

    testData = yesNotoBinary(testData, 'bracket_pricing')
    testData = yesNotoBinary(testData, 'end_a_1x')
    testData = yesNotoBinary(testData, 'end_a_2x')
    testData = yesNotoBinary(testData, 'end_x_1x')
    testData = yesNotoBinary(testData, 'end_x_2x')
    testData = yesNotoBinary(testData, 'end_a_forming')
    testData = yesNotoBinary(testData, 'end_x_forming')
    testData.to_csv(os.path.join(outDir, 'test_data.csv'))

main()