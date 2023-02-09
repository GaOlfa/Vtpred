from scipy.interpolate import interp1d
import pandas as pd
import numpy as np


def interpolate(df):
  newdf = pd.DataFrame()
  for region in df.columns[:-1]:
    x = df['time[seconds]']
    y = df[region]
    predict = interp1d(x, y, kind="quadratic", fill_value="extrapolate")
    xi = np.linspace(60, 7200, 119)
    yi = np.array([predict(x) for x in xi])
    newdf['time[seconds]'] = xi
    newdf[region] = yi
  return(newdf)
