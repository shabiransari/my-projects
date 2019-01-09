import pandas as pd 
import matplotlib.pyplot as plt 
df=pd.read_csv('E:\csvdhf5xlsxurlallfiles\percent-bachelors-degrees-women-usa.csv')
print(df.head())
print(df.columns)
year=df[['Year']]
architecture=df[['Computer Science']]
print(architecture)
engineering=[['Physical Sciences']]
print(engineering)
plt.plot(year, architecture, color='blue', label='Architecture')
plt.plot(year, engineering, color='green', label='Engineering')
ar_max=architecture.max()
yr_max=year[architecture.max()]
plt.plot('maximum', xy=(ar_max, yr_max), xytext=(yr_max+5, ar_max+5), arrowprops=dict(facecolor='black'))
plt.xlabel('YEAR')
plt.ylabel('Enrolment(%)')
plt.title('Undergraduate Enrolment of women')
plt.show()
