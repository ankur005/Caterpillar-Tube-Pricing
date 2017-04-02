import pandas as pd
inDir = "./Raw Data"
outDir = "./Model1"

def yesNotoBinary(df, feature):

    for row in range(0,len(df)):
        if df.get_value(row,feature) in {'Yes','Y','yes','y','YES'}:
            df.set_value(row,feature,1)
        elif df.get_value(row,feature) in {'NO','No','no','N','n'}:
            