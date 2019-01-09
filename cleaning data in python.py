#cleaning data in python
#full_stack data analysis
#data analysis is more than just fitting models 1.understand, 2.Tidy/reshape, 3.clean, 4.combine
#steps of data cleaning 
#look at your data,Tiday/reshape your data, clean and prepare your data
#data analysis 
#the course focuses on cleaning data
#End goal:producing a data set that can be used to fit a model
#common data problems
#inconsistent column names, missing data, outliers, duplicate rows, untidy, need to process data, columns types can signal unexpected data values
import pandas as pd 
df = pd.read_csv('E:\csvdhf5xlsxurlallfiles/all_medalists.csv')
print(df)
print(df.head())
print(df.tail())
print(df.head(10))
print(df.tail(10))
print(df.columns)#.shape , and .shape are attributes not methods don't need to follow these with parenthesis 
print(df.shape)
print(df.info())
print(df[['Medal']])
print(df.iloc[29213])#pandas series
print(df.iloc[[29213]])#pandas dataframe
#Exploratory data analysis
#frequency counts
print(df['Sport'].value_counts(dropna=False))
print(df['City'].value_counts(dropna=True))
print(df['City'].value_counts(dropna=False).head())
print(df.describe())#describe() only with numeric data
print(df['City'].describe())
#visual Exploratory data analysis
#bar plots used for descrete data counts,histograms for continious data counts
import matplotlib.pyplot as plt 
print(df.describe())
print(df.info())
df.Edition.plot('hist')
df.hist('Edition')
plt.show()
print(df.Edition>1980)
print(df[df.Edition>1980])
#Boxplots , visualizebasic summary statics, .outliers, .min/max, 25th, 50th, 75th, percentiles
df.boxplot(column='Edition')
plt.show()
df['Edition'].plot(kind='hist',rot=70, logx=True, logy=True)
plt.plot()
df.boxplot(column='Edition', rot=70)
plt.show()


