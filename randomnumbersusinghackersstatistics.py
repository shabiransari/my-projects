import numpy as np 
coin = np.random.randint(0, 2)
print(coin)
if coin == 0:
	print("Heads")
else:
	print("Tails")
np.random.seed(123)
first = np.random.randint(1, 7)
second = np.random.randint(1, 7)
third = np.random.randint(1, 7)
print(first)
print(second)
print(third)
step = 50
dice = np.random.randint(1, 7)
if dice<=2 :
	step = step-1
elif dice<=5 :
	step = step+1
else :
	step = step+dice
print(dice)
print(step)
outcomes = []
for x in range(10) :
	coin = np.random.randint(0, 2)
	if coin==0:
		outcomes.append("Heads")
	else :
		outcomes.append("Tails")
print(outcomes)
tails = [0]
for x in range(10) :
	coin = np.random.randint(0, 2)
	tails.append(tails[x]+coin)
print(tails)
random_walk = [0]
for x in range(100):
	step = random_walk[-1]
	dice = np.random.randint(1, 7)
	if dice<=2 :
		step=max(0,step-1)
	elif dice<=5 :
		step=step+1
	else:
		step=step+dice
	random_walk.append(step)
print(random_walk)
import matplotlib.pyplot as plt 
plt.plot(random_walk)
plt.show()
plt.hist(random_walk, bins=15)
plt.show()