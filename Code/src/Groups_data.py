from src import config, Explore_TAC, Vt_output
import pandas as pd


def Group_data_construction(subjects, groupdf, groupVt, features_var):
    newdf = []
    dim = []
    i = 0
    #L = []
    #for j in range(1, 35):
        #L.append('interval ' + str(j))
    #CHAB_subjects = ['AS','HG','HI','JL','JP','MS','MW','PG','RC','SB','VH']
    for df in groupdf:
      subdf = df.iloc[:34,::]
      #subdf['Features'] = L
      subdf = subdf.dropna(how='all', axis=1)
      if features_var == 0:
          subdf = subdf[['time[seconds]', 'Rfrontal(1)', 'Rtemporal(2)',
               'RThalamus(3)', 'Lfrontal(4)', 'Ltemporal(5)', 'LThalamus(6)',
               'RCaudate(7)', 'LCaudate(8)', 'RPutamen(9)', 'LPutamen(10)',
               'Insula(11)', 'Lacingulate(12)', 'Racingulate(13)', 'Cerebellum(14)',
               'Ventral_str_right(15)', 'Ventral_str_left(16)', 'Hippocampus(18)',
               'Occipital(19)', 'Subst_Nigra(20)', 'Aqueduct(21)',
               'Middle_Brain_full(22)', 'Middle_Brain_34(23)', 'Caudate(24)',
               'Putamen(25)', 'Ventra_str(26)', 'Right_Striatum(27)',
               'Left_Striatum(28)', 'Thalamus(29)', 'WM_Aqueduct(235)',
               'WM_Subst_Nigra(236)', 'WM_Pons(239)']]
      elif features_var == 1:
          subdf = subdf[['time[seconds]', 'Rfrontal(1)', 'Rtemporal(2)',
                         'RThalamus(3)', 'Lfrontal(4)', 'Ltemporal(5)', 'LThalamus(6)',
                         'RCaudate(7)', 'LCaudate(8)', 'RPutamen(9)', 'LPutamen(10)',
                         'Insula(11)', 'Lacingulate(12)', 'Racingulate(13)', 'Hippocampus(15)',
                         'Occipital(16)', 'substantia_nigra(17)', 'aqueductum(18)',
                         'Cerebellum(19)', 'Amygdala(20)', 'Middle_Brain_34(21)', 'temporal(22)',
                         'frontal(23)', 'Caudate(24)', 'Putamen(25)', 'Striatum(26)',
                         'Middle_Brain_full(27)', 'thalamus(28)', 'cingulate(29)',
                         'frontotemporal(30)', 'WM_aqueductum(238)', 'WM_substantia_nigra(239)',
                         'WM_Pons(242)']]
      else:
          subdf = subdf[['time[seconds]', 'Right_MPFC(1)', 'Rtemporal(2)', 'RThalamus(3)',
                         'Left_MPFC(4)', 'Ltemporal(5)', 'LThalamus(6)', 'Insula(11)',
                         'Lacingulate(12)', 'Racingulate(13)', 'Ventral_str_right(15)',
                         'Ventral_str_left(16)', 'substantia_nigra(17)', 'aqueductum(18)',
                         'Cerebellum(19)', 'Amygdala(20)', 'RDLPFC(21)', 'LDLPFC(22)',
                         'R_ORB_FR(23)', 'L_ORB_FR(24)', 'Brodmann_25(25)', 'Hippocampus(26)',
                         'Occipital(27)', 'Inf_parietal(28)', 'Ventra_str(31)',
                         'Right_PreDCA(39)', 'Right_PostCA(40)', 'Right_PreDPU(41)',
                         'Right_PostPU(42)', 'Left_PreDCA(43)', 'Left_PostCA(44)',
                         'Left_PreDPU(45)', 'Left_PostPU(46)', 'PreDCA(50)', 'PostCA(51)',
                         'PreDPU(52)', 'PostPU(53)', 'Right_AST(54)', 'Left_AST(55)',
                         'Right_DCaudate(56)', 'Left_DCaudate(57)', 'Right_DPutamen(58)',
                         'Left_DPutamen(59)', 'Dorsal_Caudate(60)', 'Dorsal_Putamen(61)',
                         'Dorsal_Striatum(62)', 'AST(63)', 'LST(64)', 'SMST(65)',
                         'Full_Striatum(66)', 'MedialPreFrontalCtx(67)', 'PreFrontalCtx(68)',
                         'temporal(69)', 'Prefrontotemporal(70)', 'thalamus(71)',
                         'cingulate(72)', 'Middle_Brain_34(73)', 'WM_aqueductum(238)',
                         'WM_substantia_nigra(239)', 'WM_Pons(242)']]

      subdf.set_index('time[seconds]', inplace=True)
      #subdf['index'] = subdf['Time interval']
      subdf_transposed = subdf.T
      #subdf_transposed = subdf_transposed.iloc[2:]
      #subdf_transposed['Region'] = subdf_transposed.index
      subdf_transposed = subdf_transposed.rename_axis('Brain region').reset_index()
      subdf_transposed.index.names = ['index']
      dfinal = subdf_transposed.merge(groupVt[i][['Region', 'Vt']], how='inner', left_on='Brain region', right_on='Region')
      dfinal.drop('Region', axis=1, inplace=True)
      dfinal['Genetic subgroup'] = pd.Series('HAB', index=dfinal.index, dtype='category')
      dfinal['Health status'] = pd.Series('Control', index=dfinal.index, dtype='category')
      dfinal['Patient'] = pd.Series(subjects[i], index=dfinal.index, dtype='category')
      i+= 1
      newdf.append(dfinal)
      dim.append(dfinal.shape)

    final_groupdf = pd.concat(newdf, ignore_index=True)
    return(final_groupdf)

#subjects = config.CHABs_subjects_id
#groupdf = Explore_TAC.Explore_TAC(subjects, config.CHABs_TAC_data[3:])
#groupVt = Vt_output.Extract_Vt(subjects, config.CHABs_PMOD_data[3:])
#df = Group_data_construction(subjects, groupdf, groupVt)
#print(df.head())
