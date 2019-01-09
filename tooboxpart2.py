#defining a function without parameter
def square():
	new_value = 4**2
	print(new_value)
square()
#function with parameter
def square(new_value):
	new_value1=new_value**2
	print(new_value1)
square(67)
print(type(square(67)))
square(34)
#Return from functions
def square(value):
	new_value=value**2
	return new_value
print(square(4))
print(type(square(4)))
def shout():
	shout_word = str('congratulations')+str('!!!')
	print(shout_word)
shout()
#function with parameter
def shout(word):
	new_word = word+str('!!!')
	print(new_word)
shout('congratulations')
def shout(word):
	new_word = word+str('!!!')
	return new_word
print(shout('congratulations'))
print(type(shout('congratulations')))
#multiple parameters and returns values accept more than one parameter
def raise_to_power(value1, value2):
	val = value1**value2
	return val
print(raise_to_power(5, 3))
#tuples
even_num=(2, 4, 6)#tuple constructed with ()
print(type(even_num))
a, b, c = even_num#unpack the tuple
print(a)
print(b)
print(c)
#returning multiple value
def raise_both(val1, val2):
	new_value1= val1**val2
	new_value2= val2**val1
	new_tuple=(new_value1, new_value2)
	return new_tuple
print(raise_both(2,3))
import pandas as pd
df = pd.read_csv('E:\csvdhf5xlsxurlallfiles/tweets.csv')
print(df)
print(df.columns)
langs_count ={}
col = df['lang']
for entry in col:
	if entry in langs_count.keys():
		langs_count[entry] +=1
	else:
		langs_count[entry]=1
print(langs_count)
print(df['lang'].count)
print(df.info())
#Globle vs local scope()
new_val = 10
def square(value):
	new_val=value**2
	return new_val
print(square(10))
print(new_val)
#part 3
new_value = 10
def square(value):
	new_value2=new_value**2
	return new_value2
print(square(3))
#nested function
def mod2plus5(x1, x2, x3):
	new_x1=x1%2+5
	new_x2=x2%2+5
	new_x3=x3%2+5
	return(new_x1, new_x2, new_x3)
print(mod2plus5(4, 5, 6))
#we can do above code with nested function
def mod2plus5(x1, x2, x3):
	def inner(x):
		return x%2+5
	return(inner(x1), inner(x2), inner(x3))
print(mod2plus5(4, 5, 6))
#default and flexible arguments
def power(number, pow=1):
	new_power = number**pow
	return new_power
print(power(5, 3))
print(power(15, 7))
#flexible arguments
def add_all(*args):
	sum_all=0
	for num in args:
		sum_all +=num
	return sum_all
print(add_all(1, 2, 3, 10))
def mul_all(*args):
	multi=1
	for num in args:
		multi =multi*num
	return multi
print(mul_all(1,2,3,4))
#flexible arguments **kwargs
def report_status(**kwargs):
	print('\n BEGIN:REPORT\n')
	for key, value in kwargs.items():
		print(key+':'+value)
	print('\n END REPORT')
report_status(name='luke', affiliation='jedi', status='missing')
#lambda function
raise_to_power = lambda x, y:x**y
print(raise_to_power(3, 5))
#map() function works on sequence
nums = [12,34,13]
square_all=map(lambda num : num**2, nums)
print(square_all)
print(list(square_all))
echo_word = lambda word1, echo:word1*echo
result = echo_word('hey',5)
print(result)
spells=['protego', 'accio', 'expecto', 'legilimens']
shout_spells = map(lambda spell:spell[:]+'!!!', spells)
print(shout_spells)
print(list(shout_spells))
#filter() function 
felloship = ['frado', 'sumwise', 'merry', 'gimili']
result = filter(lambda felloships:len(felloships[:])>5, felloship)
print(result)
print(list(result))
#reduce() function
from functools import reduce
results=reduce(lambda item1,item2:item1+item2, felloship)
print(list(results))
print(results)
#error handling
#Error and exceptions
def sqrt(x):
	try:
		return x**0.5
	except:
		print('x must be an int or float')
print(sqrt(4))
print(sqrt('j'))
def sqrt(x):
	try:
		return x**0.5
	except TypeError:
		print('x must be an int or float')

print(sqrt('hh'))
