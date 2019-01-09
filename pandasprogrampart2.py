#index and select data .loc labeled as location .iloc labeled as index no.
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }
import pandas as pd 
brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)
#column access
print(brics["country"])
print(brics["capital"])
print(brics["area"])
print(brics["population"])
print(type(brics["country"]))
print(brics[["country"]])
print(type(brics[["country"]]))
print(brics[["country", "capital"]])
#row access
print(brics[0:3])
#row access using loc
print(brics.loc["IN"])
print(brics.loc[["IN"]])
#we can print multiple ros
print(brics.loc[["BR", "RU", "CH"]])
#ROW AND COLUMN ACCESS
print(brics.loc[["BR", "IN", "SA"],["country", "capital"]])
print(brics.loc[ : ,["country", "population"]])
#row access iloc
print(brics.iloc[[1]])
print(brics.iloc[[1, 2, 3,4]])
print(brics.iloc[[1, 2, 3, 4], [0, 1]])
print(brics.iloc[:,[0,1]])
