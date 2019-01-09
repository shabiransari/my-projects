#combining data , Data may not come in 1 huge file.
#.5 milion row dataset may be broken into 5 seprate dataset
#.easy to store and share , may have new data for each day
#.important to be able to combine then clean or vice versa
import pandas as pd 
ebola= pd.read_csv('E:\csvdhf5xlsxurlallfiles/ebola.csv')
print(ebola.head())
print(ebola.columns)
#ebola_melt = pd.melt(ebola, )
airquality = pd.read_csv('E:\csvdhf5xlsxurlallfiles/airquality.csv')
print(airquality.head())
#concatenate Dataframe
concat_ebola_airquality1=pd.concat([ebola, airquality], axis=1)#DataFtrame must be in a list
print(concat_ebola_airquality1.head())
concat_ebola_airquality=pd.concat([ebola, airquality], axis=0)
print(concat_ebola_airquality.head())
#if there are thousands of dataframe
#solution:-glob funtion to find files based on a pattern
#pattern matching for file names
#wildcards:?
     # .any csv file: *.csv
     #any single character:file_?.csv
#returns a list of file names, can use this list to load into separate DataFrame
import glob
csv_files = glob.glob('*.csv')
print(csv_files) 
#list_data = []
#(for filename in csv_files:
	#data = pd.read_csv(filename)
	#list_data.append(data)
csv2= pd.read_csv(csv_files[1])
print(csv2.head())
csv3= pd.read_csv(csv_files[2])
print(csv3.head())
#concatenation is not the only way data can be combined
#solution merging data #similar to joining table in sql
print(pd.merge(left=airquality, right=ebola, on = None, left_on='Wind', right_on='Day'))
#conveting data types
#df['treatmenta']=df['ttreatmenta'].astype(str)
#df['sex']=df['sex'].astype('category')874
#df.dtypes
tips=pd.read_csv('E:\csvdhf5xlsxurlallfiles/tips.csv', index_col=0)
print(tips.head())
print(tips)
print(tips.info())
#string manipulation
#most of the world's data is unstrucured text
#also have to do sting manipulation to make datasets consistent with one another
#'re' library for rgular expressions
#   a formalway of specifying a pattern, sequence of characters, pattern maching similar to globbing
import re
pattern = re.compile('\&\d*\.d{12}')
result = pattern.match('&17.89')
print(bool(result))
prog=re.compile('\d{3}-\d{3}-\d{4}')
result = prog.match('123-456-7890')
print(bool(result))
prog1=re.compile('\d{3}-\d{3}-\d{4}')
result1 = prog.match('1232-456-7890')
print(bool(result1))
matches=re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')
print(matches)
pattern = bool(re.match(pattern='\&\d*\.\d{2}', string='&123.42'))
print(pattern)
pattern0=bool(re.match(pattern='\w*', string = 'Australia1'))
print(pattern0)














