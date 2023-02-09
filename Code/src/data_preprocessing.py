
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def data_filtering(data):
    #data = pd.read_csv(df_path)
    #print(data.head())
    print("Descriptive statistics summary of Vt output : \n", data['Vt'].describe())
    sns.boxplot(data['Vt'])
    plt.show()
    #Q1 = percentile25, Q3 = percentile75
    Q1 = data['Vt'].quantile(0.25)
    Q3 = data['Vt'].quantile(0.75)
    print(Q1, Q3)
    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR
    new_data = data[(data['Vt'] < upper_limit)]
    print("Shape of new data after filtering ", new_data.shape)
    #sns.boxplot(new_data['Vt'])
    #plt.show()
    return (new_data)

#newdf = data_filtering(config.Final_df_path[3:])
#print(newdf.head())
