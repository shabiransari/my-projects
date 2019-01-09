#opposite of melting , multiple variable stored in same column
import pandas as pd 
import numpy as np 
df = pd.read_csv('E:\csvdhf5xlsxurlallfiles/airquality.csv')
print(df.head())
airquality_melt= pd.melt(frame=df, id_vars=['Month', 'Day'], var_name= 'Meaurement', value_name='reading')
print(airquality_melt.head())
#when duplicat entries available in table use aggfunc=np.mean,np.meaian....
airquality_melt_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='Meaurement', values='reading', aggfunc=np.mean)
print(airquality_melt_pivot.head())
#beyond melt and pivot
#Another common - columns contain multiple bits of information as M014-it contains str as well as int
ebola_df = pd.read_csv('E:\csvdhf5xlsxurlallfiles/ebola.csv')
print(ebola_df.head())
print(ebola_df.columns)
ebola_df_melt = pd.melt(ebola_df, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')
print(ebola_df_melt.head())
ebola_df_melt['str_split']=ebola_df_melt.type_country.str.split('_')
ebola_df_melt['type']=ebola_df_melt.str_split.str.get(0)
ebola_df_melt['country']=ebola_df_melt.str_split.str.get(1)
print(ebola_df_melt.head())
print(ebola_df_melt.info())




