from urllib.request import urlopen, Request
url = 'http://www.wikipedia.org/'
request = Request(url)
response = urlopen(request)
html = response.read()
response.close()
print(html)
from urllib.request import urlretrieve
import pandas as pd 
import matplotlib.pyplot as plt 
url =  'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
#save file locally
urlretrieve(url, 'winequality-red.csv')
df = pd.read_csv('winequality-red.csv', sep=',')
print(df.head())
url =  'http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv'
urlretrieve(url, 'C2ImportCalEventSample.csv')
df = pd.read_csv('C2ImportCalEventSample.csv', sep=',')
print(df.head())
pd.DataFrame.hist(df)
plt.xlabel('fixed acidity')
plt.ylabel('count')
plt.show()
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
xl = pd.read_excel(url, sheetname = None)
print(xl.keys())
print(xl['1700'].head())
from urllib.request import urlopen, Request
url = 'http://www.wikipedia.org/'
request = Request(url)
response = urlopen(request)
html = response.read()
response.close()
print(html)
 


