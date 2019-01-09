#create a dictionary as dict{}
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }
import pandas as pd 
brics = pd.DataFrame(dict)
print(brics)
#how to do indexing
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)
#we can import csv file as (brics=pd.read_csv("path/to/brics.csv", index_col=0))
row_label = ["BR", "RU", "IN", "CH", "SA"]
brics.index = row_label
print(brics) 