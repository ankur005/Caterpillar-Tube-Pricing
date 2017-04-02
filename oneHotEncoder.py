from sklearn.preprocessing import LabelEncoder
from Helper import inDir, outDir
import pandas as pd
import os

trainData = pd.read_csv((os.path.join(outDir,"train_set.csv")))

labelEnc = LabelEncoder()
labelEnc.fit(trainData[['bracket_pricing']])
