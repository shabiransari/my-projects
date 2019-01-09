#Gives a way for formating our data "standard way to organize data values within a dataset"
#principles of tiday data
#.columns represet represent separate variables , .rows represent individual observation, .observational units from tables
#tidy data makes easer to fix common data problems
#the data problem we are trying to fix, .columns containig values , instead of variables
# Solutation pd.melt()
import pandas as pd 
df = pd.read_csv('E:\csvdhf5xlsxurlallfiles/airquality.csv')
print(df)
print(df.head())
airquality_melt= pd.melt(frame = df, id_vars=['Month', 'Day'])
print(airquality_melt.head())
airquality_melt1=pd.melt(df , id_vars=['Month', 'Day'], var_name='Measurement', value_name='reading')
print(airquality_melt1.head())
airquality = pd.concat([airquality_melt, airquality_melt1])
print(airquality.head())
#



