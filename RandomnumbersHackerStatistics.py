import numpy as np 
print(np.random.rand())
print(np.random.rand())
#Coin Toss
np.random.seed(123)#it ensure the reproducibility always fixed the output
coin = np.random.randint(0, 2)
if coin==0:
	print('head')
else:
	print('Tail')
dice=np.random.randint(1, 7)
print(dice)
print(dice)
step=50
if dice<=2:
	step -=1
elif dice<=5:
	step +=1
else:
	step +=dice
print(dice)
print(step)
outcomes=[]
tails=[]
for x in range(10):
	coin = np.random.randint(0,2)
	if coin==0:
		outcomes.append('head')
	else :
		outcomes.append('tail')
print(outcomes)
all_walk=[]
random_walk=[0]
for x in range(100):
	step=random_walk[-1]
	dice=np.random.randint(1, 7)
	if dice<=2:
		step = max(0, step-1)
	elif dice<=5:
		step +=1
	else:
		step +=dice
	random_walk.append(step)
import matplotlib.pyplot as plt 
plt.plot(random_walk)
plt.show()
all_walk.append(random_walk)
print(all_walk)




