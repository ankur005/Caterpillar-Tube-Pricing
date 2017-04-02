from Helper import inDir, outDir
import os
import pandas as pd

def calComponentWeight():
    mergedComponentFile = os.path.join(outDir,'components.csv')
    bomFile = os.path.join(outDir, 'bill_of_materials_processed.csv')

    comdf = pd.read_csv(mergedComponentFile)
    bomdf = pd.read_csv(bomFile)
    tubeComponentWeight = {}
    componentWeights = {}

    for cid in range(0,len(comdf)):
        componentWeights[comdf.get_value(cid, 'component_id')] = comdf.get_value(cid,'weight')
    print componentWeights

    for i in range(0,len(bomdf)):
        weight = 0
        for temp in range(1,9):
            compId = str(bomdf.get_value(i, 'component_id_' + str(temp)))
            if  compId != 'nan':
                curCompWeight = componentWeights[compId]
                quantity = bomdf.get_value(i, 'quantity_' + str(temp))
                weight = weight + curCompWeight*quantity
            else:
                break
        tubeComponentWeight[bomdf.get_value(i, 'tube_assembly_id')] = weight

    bomdf['total_component_weight'] = bomdf['tube_assembly_id'].map(tubeComponentWeight)

    file = open(os.path.join(outDir,'bom_processed.csv'),'w')
    bomdf.to_csv(file)

calComponentWeight()