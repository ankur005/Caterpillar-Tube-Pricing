import pandas as pd
import os
from Helper import inDir, outDir

def mergeExcelTables():
    trainData = pd.read_csv(os.path.join(inDir, "train_set.csv"))
    testData = pd.read_csv(os.path.join(inDir, "test_set.csv"))
    tubeData = pd.read_csv(os.path.join(inDir, "tube.csv"))
    # specsData = pd.read_csv(os.path.join(inDir, "specs.csv"))
    bomData = pd.read_csv(os.path.join(outDir, "bom_processed.csv"))
    tubeEndFormData = pd.read_csv(os.path.join(inDir, "tube_end_form.csv"))

    print "Train Set : " + str(len(trainData))
    newTrainData = pd.merge(trainData, tubeData, on="tube_assembly_id")
    newTrainData = pd.merge(newTrainData, tubeEndFormData, left_on="end_a", right_on="end_form_id")
    newTrainData = newTrainData.rename(columns={"forming":"end_a_forming"})
    newTrainData = newTrainData.drop("end_form_id", axis=1)
    newTrainData = pd.merge(newTrainData, tubeEndFormData, left_on="end_x", right_on="end_form_id")
    newTrainData = newTrainData.rename(columns={'forming': 'end_x_forming'})
    newTrainData = newTrainData.drop("end_form_id", axis=1)
    newTrainData = pd.merge(newTrainData, bomData[['tube_assembly_id','no_of_components','total_component_weight']], on="tube_assembly_id")

    newTestData = pd.merge(testData, tubeData, on="tube_assembly_id")
    newTestData = pd.merge(newTestData, tubeEndFormData, left_on="end_a", right_on="end_form_id")
    newTestData = newTestData.rename(columns={"forming": "end_a_forming"})
    newTestData = newTestData.drop("end_form_id", axis=1)
    newTestData = pd.merge(newTestData, tubeEndFormData, left_on="end_x", right_on="end_form_id")
    newTestData = newTestData.rename(columns={'forming': 'end_x_forming'})
    newTestData = newTestData.drop("end_form_id", axis=1)
    newTestData = pd.merge(newTestData, bomData[['tube_assembly_id', 'no_of_components', 'total_component_weight']], on="tube_assembly_id")

    newTrainFile = open(os.path.join(outDir, "train_data.csv"),'w')
    newTrainData.to_csv(newTrainFile)

    newTestFile = open(os.path.join(outDir, "test_data.csv"),'w')
    newTestData.to_csv(newTestFile)

mergeExcelTables()


