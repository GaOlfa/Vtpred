from src import config
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce
from src import interpolation
#from interpolation import interpolate

#bloodTAC = pd.read_csv(config.CHABsdata + config.CHABs_subjects_id[0]+'/as_blood__deconv_16.0_manual.smpl', delimiter='\t',  engine='python')
#plasmaTAC = pd.read_csv(config.CHABsdata + config.CHABs_subjects_id[0]+'/as_plasma__deconv_16.0_manual.smpl', delimiter='\t',  engine='python')

#bloodTAC = pd.read_csv('data/Controls/HABs/AS/as_blood__deconv_16.0_manual.smpl', delimiter='\t',  engine='python')
#plasmaTAC = pd.read_csv('data/Controls/HABs/AS/as_PLASMA__deconv_16.0_manual.smpl', delimiter='\t',  engine='python')

#print(bloodTAC.head())
#print(plasmaTAC.head())
#print(plasmaTAC.columns)

#fig, ax = plt.subplots()
#plt.plot(bloodTAC['Time[seconds]'], bloodTAC['Blood[nCi/cc]'], color = 'green', label = 'AS_BloodTAC')
#plt.plot(plasmaTAC['Time[seconds]'], plasmaTAC['Plasma[nCi/cc]'], color = 'red', label = 'AS_PlasmaTAC')
#ax.legend(loc = 'upper right')
#ax.set_xlabel("Time[seconds]")
#ax.set_ylabel(r"Corrected activity[nCi/cc]")
#plt.show()

def Explore_TAC (subjects, TAC_data):

  groupdf = []
  TAC_columns = []
  inter = []
  for subject in subjects:
    brainTAC = pd.read_csv(TAC_data + str(subject) +'.tac', delimiter='\t',  engine='python')
    brainTAC['time[seconds]'] = (brainTAC['start[seconds]'] + brainTAC['end[nCi/cc]']) / 2
    df = brainTAC.iloc[:, 2:]
    newdf = interpolation.interpolate(df)
    groupdf.append(newdf)
    TAC_columns.append(brainTAC.columns)
    inter = list(reduce(set.intersection, [set(item) for item in TAC_columns]))
  #print("Dimensions of brain TAC dataframes", dim)
  print('There are '+str(len(inter))+' TAC of these brain regions commonly for all subjects', inter)
  return(groupdf)


#Explore_TAC(config.CHABs_TAC_data,config.CHABs_subjects_id)

#todo boucle for that explore_TAC for all the data types