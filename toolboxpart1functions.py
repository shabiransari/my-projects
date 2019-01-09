#defining a function
def square():
	new_value = 4**2
	print(new_value)
square()
#function with single parameter
def square(value) :
	new_value = value**2
	print(new_value)
square(5)
#return value from function
def square(value):
	new_value=value**2
	return new_value
num = square(24)
print(num)
def shout(word):
	new_word = word + "!!!"
	return new_word
hi = shout('congratulations')
print(hi)
#multiple parameter and return single value
def raise_both(value1, value2):
	new_value = value1**value2
	return new_value
power = raise_both(8, 3)
print(power)
#tuples return multiple values
def raise_to_power1(value1, value2) :
	new_value1 = value1**value2
	new_value2 = value2**value1
	new_tuple = (new_value1, new_value2)
print(raise_to_power1(2, 3))
#flexible and default arguments
def power(number, pow=1):
	new_value5 = number**pow
	return new_value5


print(power(5,2))
print(power(3,2))
#flexible arguments *args
#lambda functions
raise_to_power = lambda x,y:x**y
print(raise_to_power(2,3))
powerboth = lambda x,y:x**y
print(powerboth(2,4))
#anonymous functions map()
nums = [46, 35, 9, 11]
square_all = map(lambda num : num**2, nums)
print(square_all)
print(list(square_all))
echo_word = lambda word1, echo:word1*echo
result = echo_word('hey',5)
print(result)
spells = ["protego", "china", "india"]
shout_spells = map(lambda spells:spells[:]+"!!!",spells)
print(shout_spells)
print(list(shout_spells))
#filter() functions 
result = filter(lambda spells:len(spells[:])>4, spells)
print(result)
print(list(result))
#reduce() functions and lambda functions from functions import reduce stark = ["robb" "sansa", "rickon"]result = reduce(lambda item1,item2:item1+item2, stark)print(result)
#introduction to error handling
#print(float("hello"))ValueError: could not convert string to float: 'hello'
def sqrt(x):
	return x**0.5
print(sqrt(16))
#print(sqrt("hello"))TypeError: TypeError unsupported operand type(s) for ** or pow(): 'str' and 'float'
#Errors and exceptions
def sqrt(x):
	try:
		return x**0.5
	except:
		print("x must be an int or float")
sqrt(4)
sqrt("hi")  
def sqrt1(x):
	try:
		return x**0.5
	except TypeError:
		print("x must be an int or float")
sqrt1("nm")
def sqrt2(x):
	if x<0:
		#raise
		ValueError("x must be non negative")

	try:
		return x**0.5
	except TypeError:
		print("x must be int or flot")

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
avengers = ["hawkeye"]



