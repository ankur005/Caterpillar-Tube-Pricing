from Helper import inDir, outDir, yesNotoBinary
import os
import pandas as pd

def main():
    trainData = pd.read_csv(os.path.join(outDir,'train_data.csv'))
    yesNotoBinary(trainData,'bracket_pricing')


main()