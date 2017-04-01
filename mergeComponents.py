import os
import pandas as pd
from Helper import inDir, outDir

def mergeComponents():
    adaptorComponents = pd.read_csv(os.path.join(inDir, "comp_adaptor.csv"))
    bossComponents = pd.read_csv(os.path.join(inDir, "comp_boss.csv"))
    elbowComponents = pd.read_csv(os.path.join(inDir, "comp_elbow.csv"))
    floatComponents = pd.read_csv(os.path.join(inDir, "comp_float.csv"))
    hflComponents = pd.read_csv(os.path.join(inDir, "comp_hfl.csv"))
    nutComponents = pd.read_csv(os.path.join(inDir, "comp_nut.csv"))
    otherComponents = pd.read_csv(os.path.join(inDir, "comp_other.csv"))
    sleeveComponents = pd.read_csv(os.path.join(inDir, "comp_sleeve.csv"))
    straightComponents = pd.read_csv(os.path.join(inDir, "comp_straight.csv"))
    teeComponents = pd.read_csv(os.path.join(inDir, "comp_tee.csv"))
    threadedComponents = pd.read_csv(os.path.join(inDir, "comp_threaded.csv"))

    components = pd.read_csv(os.path.join(inDir,"components.csv"))

    # Dataframe to be concatenated
    comps = [adaptorComponents[['component_id','weight']],
             bossComponents[['component_id','weight']],
             elbowComponents[['component_id','weight']],
             floatComponents[['component_id','weight']],
             hflComponents[['component_id','weight']],
             nutComponents[['component_id','weight']],
             otherComponents[['component_id','weight']],
             sleeveComponents[['component_id','weight']],
             straightComponents[['component_id','weight']],
             teeComponents[['component_id','weight']],
             threadedComponents[['component_id','weight']]
             ]

    concatComponents = pd.concat(comps)
    compData = pd.merge(concatComponents,components, on="component_id")

    file = open(os.path.join(outDir,'components.csv'),'w')
    compData[['component_id','weight','name']].to_csv(file)

mergeComponents()



