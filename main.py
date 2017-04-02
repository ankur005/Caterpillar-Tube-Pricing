from Helper import inDir, outDir, yesNotoBinary
import os
import pandas as pd

def main():
    trainData = pd.read_csv(os.path.join(outDir,'train_data.csv'))

    trainData = yesNotoBinary(trainData,'bracket_pricing')
    trainData = yesNotoBinary(trainData, 'end_a_1x')
    trainData = yesNotoBinary(trainData, 'end_a_2x')
    trainData = yesNotoBinary(trainData, 'end_x_1x')
    trainData = yesNotoBinary(trainData, 'end_x_2x')
    trainData = yesNotoBinary(trainData, 'end_a_forming')
    trainData = yesNotoBinary(trainData, 'end_x_forming')
    trainData.to_csv(os.path.join(outDir,'train_data.csv'))

main()