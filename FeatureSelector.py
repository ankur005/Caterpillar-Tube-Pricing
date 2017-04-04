# import csv
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
import Helper
# from sklearn.ensemble import ExtraTreesClassifier as ETC
# from sklearn.feature_selection import SelectFromModel

# def readCSV(filename):
#     with open(filename, "rb") as f_obj:
#         reader = csv.reader(f_obj)
#         return reader

def selectFeatures(filename):

    dataset = pd.read_csv(filename, index_col=0)

    data = dataset
    data = data.drop('cost',axis=1)

    data = data.drop('tube_assembly_id',axis=1)
    data = data.drop('supplier', axis=1)
    data = data.drop('quote_date', axis=1)

    data_columns = list(data)
    print "data columns: " + str(list(data))
    print "data shape: " + str(data.shape)

    target = dataset['cost']
    print "target shape: " + str(target.shape)

    # clf = ETC()
    # clf = clf.fit(data, target)
    # print "Feature importances: " + clf.feature_importances_
    #
    # model = SelectFromModel(clf, prefit=True)
    # data_new = model.transform(data)
    # print "selected data shape: " + data_new.shape

    feature_select = SelectKBest(f_regression,k=20)

    # print "Feature scores: " + feature_select.feature_importances
    data_new = feature_select.fit_transform(data,target)
    print "selected data shape: " + str(data_new.shape)

    data_new_frame = pd.DataFrame(data_new)

    selected_feat_indices = feature_select.get_support(indices=True)
    data_new_frame.columns = [data_columns[i] for i in selected_feat_indices]

    data_new_frame['cost'] = target

    # data_new_frame.merge(target,left_index=True,right_index=True)
    writeToCSV(data_new_frame)

def writeToCSV(dataframe):
    with open(Helper.outDir + '/selected_train_data.csv','w') as f_obj:
        dataframe.to_csv(f_obj)

selectFeatures(Helper.outDir + '/train_data.csv')