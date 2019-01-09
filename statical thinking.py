#Exploratory data analysis(EDA)
#the process of organizing, ploting, and Summarizing a data set.
import pandas as pd 
import matplotlib.pyplot as plt 
df_swing=pd.read_csv('E:\csvdhf5xlsxurlallfiles/2008_swing_states.csv')
print(df_swing.columns)
print(df_swing.head())
_=plt.hist(df_swing['dem_share'])
_=plt.xlabel('percent of vote for obama')
_=plt.ylabel('number 0f country')
plt.show()
#setting the bins of a histogram.
bin_edges=[0,10,20,30,40,50,60,70,80,90,100]
_=plt.hist(df_swing['dem_share'], bins=bin_edges)
plt.show()
#setting seaborn styling 
import seaborn as sns 
sns.set()
_=plt.hist(df_swing['dem_share'])
_=plt.xlabel('percent of vote for obama')
_=plt.ylabel('number of countries')
plt.show()
import numpy as  np 
n_data = len(df_swing['dem_share'])
n_bins=np.sqrt(n_data)
n_bins=int(n_bins)
_=plt.hist(df_swing['dem_share'], bins=n_bins)
plt.plot()