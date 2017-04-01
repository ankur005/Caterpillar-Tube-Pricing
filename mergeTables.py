import pandas as pd
import os

def mergeExcelTables(inDir, outDir):
    trainData = pd.read_csv(os.path.join(inDir, "train_set.csv"))
    testData = pd.read_csv(os.path.join(inDir, "test_set.csv"))
    tubeData = pd.read_csv(os.path.join(inDir, "tube.csv"))
    specsData = pd.read_csv(os.path.join(inDir, "specs.csv"))
    bomData = pd.read_csv(os.path.join(inDir, "bill_of_materials.csv"))
    tubeEndFormData = pd.read_csv(os.path.join(inDir, "tube_end_form.csv"))
    componentData = pd.read_csv(os.path.join(inDir, "components.csv"))

    compTypes = ["adaptor","boss","elbow","float","hfl","nut","other","sleeve","straight","tee","threaded"]
    types = ["component","connection","end_form"]
    compTypeDatasets = []
    typeDatasets = []

    for compType in compTypes:
        compTypeDatasets.append(os.path.join(inDir, "comp_" + compType + ".csv"))

    for type in types:
        typeDatasets.append(os.path.join(inDir, "type_" + type + ".csv"))


    print "Train Set : " + str(len(trainData))
    newTrainData = pd.merge(trainData,specsData, on="tube_assembly_id")
    print "Train Set : " + str(len(newTrainData))
    newTrainData = pd.merge(newTrainData, tubeData, on="tube_assembly_id")
    print "Train Set : " + str(len(newTrainData))
    newTrainData = pd.merge(newTrainData, bomData, on="tube_assembly_id")
    newTrainFile = open(os.path.join(outDir, "train_data_tube_assembly_merge.csv"), 'w')
    newTrainData.to_csv(newTrainFile)
    print "Train Set : " + str(len(newTrainData))
    newTrainData = pd.merge(newTrainData, tubeEndFormData, left_on="end_a", right_on="end_form_id")
    print "Train Set : " + str(len(newTrainData))
    newTrainData = pd.merge(newTrainData, tubeEndFormData, left_on="end_x", right_on="end_form_id")
    print "Train Set : " + str(len(newTrainData))
    print "Test Set : " + str(len(testData))
    newTestData = pd.merge(testData, specsData, on="tube_assembly_id")
    newTestData = pd.merge(newTestData, tubeData, on="tube_assembly_id")
    newTestData = pd.merge(newTestData, bomData, on="tube_assembly_id")
    newTestData = pd.merge(newTestData, tubeEndFormData, left_on="end_a", right_on="end_form_id")
    newTestData = pd.merge(newTestData, tubeEndFormData, left_on="end_x", right_on="end_form_id")
    print "Test Set : " + str(len(newTestData))

    newTrainFile = open(os.path.join(outDir, "train_data.csv"),'w')
    newTrainData.to_csv(newTrainFile)

    newTestFile = open(os.path.join(outDir, "test_data.csv"),'w')
    newTestData.to_csv(newTestFile)

mergeExcelTables("./Raw Data","./Processed Data")


