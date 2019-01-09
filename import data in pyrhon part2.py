#your data is online you have to perform on on line data
from urllib.request import urlretrieve
import pandas as pd 
url = 'http://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
urlretrieve(url, 'winequality-red.csv')
df=pd.read_csv('winequality-red.csv', sep=';')
print(df)
print(df.head())
print(df.columns)
import matplotlib.pyplot as plt 
pd.DataFrame.hist(df[['alcohol']])
pd.DataFrame.hist(df[['free sulfur dioxide']], bins=20)
plt.ylabel('Count')
plt.show()
#from urllib.request import urlopen, Request
#url='https://www.wikipidia.org'
#request = Request(url)
#response = urlopen(request)
#html = response.read()
#response.close()
from urllib.request import urlopen
page = urlopen('http://nullshell.com')
contents=page.read()
print(contents)
print(page.info())













