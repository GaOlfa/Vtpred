import numpy as np

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))


def df_mutation(data):
  df = data[(data['Vt'] > 30)]
  index = list(df.index)
  #print(index)
  columns = list(data.columns[1:35])
  features = data[columns]
  main_df = data.copy()
  for i in index:
    L = []
    for j in range(features.shape[0]):
      L.append(manhattan(features.iloc[i],features.iloc[j]))
    L = np.array(L)
    nearest_idx = np.argsort(L)[1:3]
    if nearest_idx[0] in index:
      nearest_idx = np.argsort(L)[2:4]
    elif nearest_idx[1] in index:
      nearest_idx = np.argsort(L)[1:5:2]
    #print(nearest_idx)
    main_df['Vt'].iloc[i] = (main_df['Vt'].iloc[nearest_idx[0]] + main_df['Vt'].iloc[nearest_idx[1]])/2

  return(main_df)
