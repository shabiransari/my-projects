#logical operator
import numpy as np 
np_height = np.array([1.78, 1.99, 1.45])
np_weight = np.array([45.5, 65.0, 67.09])
bmi = np_weight/np_height**2
print(bmi)
print(np.logical_and(bmi<21, bmi>19))
print(np.logical_or(bmi<21, bmi>19))
print(np.logical_not(bmi<21, bmi>19))
#control programing
z=4
if z%2==0 :
	print("z is even")
else :
	print("z is odd")
#use if elif else
z=3
if z%2==0 :
	print("z is divisible by 2")
elif z%3==0 :
	print("z is divisible by 3")
else :
	print("z is neither divisible by 2 nor 3")
#Filtering pandas DataFrame
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }
import pandas as pd 
brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)
#step1 Get Column
print(brics["area"])
print(brics["area"]>8.0)
is_huge = brics["area"]>8.0
print(is_huge)
print(brics[is_huge])
print(brics[brics["area"]>8.0])
And =brics[np.logical_and(brics["area"]>8, brics["area"]>10)]
print(And)
#for loop
fam = [1.73, 1.68, 1.71, 1.89]
for height in fam :
	print(height)
for index, height in enumerate(fam) :
	print("index"+" "+str(index+1)+" "+":"+" "+str(height))#we can change the index no. as index+1
c = "family"
for p in c :
	print(p.capitalize())
#looping and datastructure part1
world = {"agghanistan":30.50,
         "albania":2.77,
         "algeria":39.21}
for key, value in world.items():
	print(key+"---"+str(value))
#use of iterrow()
for lab, row in brics.iterrows():
	print(lab)
	print(row)
#add column 
brics.loc[lab, "name_length"] = len(row["country"])
print(brics)
#effective method to add new column
brics["name_length"] = brics["country"].apply(len)







   
