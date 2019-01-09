#iterators vs iterable iterable = lists,strings,dict,file connections iterators produces next value with next()
word = 'data'
it = iter(word)
print(next(it))
print(next(it))
#iterating at once with*
me = "congratulations"
it = iter(me)
print(*it)
# create a list
avengers = ["hawkeye", "iron man", "thor", "quicksilver"]
e = enumerate(avengers, start=1)
e_list = list(e)
print(e_list)
for index, value in enumerate(avengers, start=1):
	print(index, value)
#using zip() function 
names = ["barte", "stark", "odison", "manomoff"]
z = zip(avengers, names)
print(list(z))
for z1, z2 in zip(avengers, names):
	print(z1, z2)
#print zip with *
z = zip(avengers, names)
print(*z)
#list comprehensions(collapses for loops)
nums = [12,34,56]
new_nums = [num+2 for num in nums]
print(new_nums)
pairs_2 = [(num1, num2) for num1 in range(0,4) for num2 in range(4,6)]
print(pairs_2)
matrix = [[col for col in range(6)] for row in range(4)]
for row in matrix :
	print(row)
#conditional in comprehension (advance comprehension)
print([num**2 for num in range(19) if num%2==0])
sqr = [num**2 if num%2==0 else 0 for num in range(45)]
print(sqr)
mod_avengers = [member for member in avengers if len(member)>5]
print(mod_avengers)
len_avengers = {member:len(member) for member in avengers}
print(len_avengers)
#GENEgen = (num**2 for num in range(20))
#RATOR EXPRESSION use() instead of [] same as list comprehinsion it returnns an objectEgen = (num**2 for num in range(20))
gen = (num**2 for num in range(20))
print(gen)
print(list(gen))
print(type(gen))
#print first 2no in range
gen = (num**2 for num in range(20))
print(next(gen))
print(next(gen))
print(next(gen))
#use yield instead of return it gives a sequence
avengers = ["hawkeye", "iron man", "thor", "quicksilver"]
def get_length(input_list):
	for person in input_list:
		yield len(person)
for value in get_length(avengers):
	print(value)

