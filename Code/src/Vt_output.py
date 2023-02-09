from src import config
import pandas as pd


def Extract_Vt(subjects, Pmod_data):
    Vt = []
    for subject in subjects:
      pmod_results = pd.read_excel(Pmod_data+str(subject)+'.xlsx')
      pmod_results.at[0,'Region'] = 'Rfrontal(1)'
      Vt.append(pmod_results)

    return (Vt)

#All_subjects = [config.CHABs_subjects_id, config.CMABs_subjects_id, config.PDHABs_subjects_id,
                    #config.PDMABs_subjects_id]
#All_Pmod_results = [config.CHABs_PMOD_data, config.CMABs_PMOD_data, config.PDHABs_PMOD_data,
                        #config.PDMABs_PMOD_data]

#def Extract_all_Vt(subjects_list, Pmod_data_list):
    #i = 0
    #for l in subjects_list:
        #print(str(i + 1) + ' group done!')
        #Vt = Extract_Vt(l, Pmod_data_list[i])
        #i += 1

#Extract_all_Vt(All_subjects, All_Pmod_results)






#Vt = Extract_Vt(config.CHABs_PMOD_data, config.CHABs_subjects_id)
#print(Vt.head())
