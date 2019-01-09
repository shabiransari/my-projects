#iteratirs{iter(iterables), produces next value with next()} vs iterables{ex-lists,strings,dictionaries,file connections}
word = 'datacamp'
it = iter(word)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#iterating at once with *
print(*it)
values=range(10,21)
print(values)
print(list(values))
print(sum(values))
#using enumerate
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
e =enumerate(avengers)
e_list=list(e)
print(e_list)#returns  tuples
#enumerate() and unpack
for index, value in enumerate(avengers):
	print(index, value)
for index, value in enumerate(avengers, start=10):
	print(index, value)
#using zip() returns tuples
avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
names = ['barter', 'stark', 'odinson', 'mannonoff']
z = zip(avengers, names)
print(z)
print(list(z))
#zip an unpack
for z1, z2 in list(z):
	print(z1, z2)
print(*z)
#using iterators to load large files
#loading data into chuncks
import pandas as pd 
counts_dict ={}
for chunk in pd.read_csv('E:\csvdhf5xlsxurlallfiles/tweets.csv', chunksize=10):
	for entry in chunk['lang']:
		if entry in counts_dict.keys():
			counts_dict[entry] +=1
		else:
			counts_dict[entry]=1
		print(counts_dict)
#list comprehension more efficient than for loop
#create list from other list, dataframe
nums = [10, 11,12, 13, 14]
add_num = [num+1 for num in nums]
print(add_num)
#list comprehension with range
ranG = [num for num in range(10)]
print(ranG)
pairs_2 = [(num1, num2) for num1 in range(11,22) for num2 in range(23, 46)]
print(pairs_2)
squares = [i**2 for i in range(0, 10)]
print(squares)
matrix=[[col for col in range(5)] for row in range(5)]
print(matrix)
for row in matrix:
	print(row)
#advanced comprehensions
#conditions in comprehensions
evennum = [num**2 for num in range(100) if num%2 ==0]
print(evennum)
even_num = [num**2 if num%2==0 else 0 for num in range(100)]
print(even_num)
#dictionary comprehension
neg_comp = {num:-num for num in range(10)}
print(neg_comp)
#intro to generator comprehension
#list comprehension returns a list, generators returns a generators object , same as list comprehension but, use () instead of []
result = (num*2 for num in range(11))
print(result)
print(list(result))
#Generators for the large data limit
#use agenetor  to load a file line by line, works on streaming data,, read and process the file untill all lines are exhausted
def num_sequence(n):
	i=0
	while i<n:
		yield i
		i +=1
print(list(num_sequence(4)))
import pandas as pd 
df_reader = pd.read_csv('E:\csvdhf5xlsxurlallfiles/world_ind_pop_data.csv',  chunksize=100)
print(next(df_reader))
print(next(df_reader))
print(next(df_reader))
print(next(df_reader))
print(next(df_reader))
print(next(df_reader))
print(next(df_reader))
print(next(df_reader))
print(next(df_reader))
