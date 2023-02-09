from src import config, Explore_TAC, Vt_output, Groups_data
import pandas as pd

All_subjects = [config.CHABs_subjects_id, config.CMABs_subjects_id, config.TestRetest_subjects_id, config.PDHABs_subjects_id,
                    config.PDMABs_subjects_id, config.ALZH_subjects_id]
All_TAC_data = [config.CHABs_TAC_data, config.CMABs_TAC_data, config.TestRetest_TAC_data, config.PDHABs_TAC_data, config.PDMABs_TAC_data, config.ALZH_TAC_data]
All_Pmod_data = [config.CHABs_PMOD_data, config.CMABs_PMOD_data,  config.TestRetest_PMOD_data, config.PDHABs_PMOD_data,
                        config.PDMABs_PMOD_data, config.ALZH_PMOD_data]


def data_construction(subjects_list, TAC_data_list, Pmod_data_list):
    #i = 0
    df_list = []
    features_var = 0
    for i in range(len(subjects_list)):
        subjects = subjects_list[i]
        groupdf = Explore_TAC.Explore_TAC(subjects, TAC_data_list[i])
        groupVt = Vt_output.Extract_Vt(subjects, Pmod_data_list[i])

        if i > 2:
            features_var = 1
        if i == 5:
            features_var = 2
        df = Groups_data.Group_data_construction(subjects, groupdf, groupVt, features_var)
        print(i)
        print('done')
        df_list.append(df)
    final_Cdf = pd.concat([df_list[0], df_list[1]])
    final_PDdf = pd.concat([df_list[2], df_list[3]])
    final_test_alzhdf = pd.concat([df_list[4], df_list[5]])
    final_df = pd.concat([final_PDdf, final_Cdf, final_test_alzhdf], ignore_index=True)
    shuffled_final_df = final_df.sample(frac=1, random_state=1).reset_index()
    shuffled_final_df = shuffled_final_df.drop('index', axis=1)
    shuffled_final_df.to_csv(config.Final_df_path, index=False, header=True)
    return(shuffled_final_df)

final_data = data_construction(All_subjects, All_TAC_data, All_Pmod_data)
print(final_data.head())


