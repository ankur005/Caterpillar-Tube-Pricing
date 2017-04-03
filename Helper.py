import pandas as pd
import seaborn
from pandas.tools import plotting
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import os
import math

inDir = "./Raw Data"
outDir = "./Model1"

def yesNotoBinary(df, feature):
    for row in range(0,len(df)):
        if str(df.get_value(row,feature)) in {'Yes','Y','yes','y','YES'}:
            df.set_value(row,feature,1)
        elif str(df.get_value(row,feature)) in {'NO','No','no','N','n','nan','NAN'}:
            df.set_value(row,feature,0)
    return df


#A function to calculate Root Mean Squared Logarithmic Error (RMSLE)
def rmsle(y, y_pred):
	assert len(y) == len(y_pred)
	terms_to_sum = [(math.log(y_pred[i] + 1) - math.log(y[i] + 1)) ** 2.0 for i,pred in enumerate(y_pred)]
	return (sum(terms_to_sum) * (1.0/len(y))) ** 0.5