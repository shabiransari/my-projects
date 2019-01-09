#basic plots with matplotlib
import matplotlib.pyplot as plt 
year = [1950, 1960, 1970, 1945]
pop = [2.99, 1.66, 1.90, 1.78]
plt.plot(year, pop)#for line plot
plt.xlabel('YEAR')
plt.ylabel('POP')
plt.title('POPULATION INDEX')
plt.show()
print(year[-1])
plt.scatter(year, pop)#for scattter plot
plt.show()
#Historam (type of visualization) explore dataset, get idea about distribution
values= [0, 0.6, 1.4, 1.6, 2.5, 2.6, 3.2, 3.5, 4.2, 6]
plt.hist(values, bins=5)
plt.show()
plt.clf()
plt.hist(values, bins=20)
plt.show()
plt.clf()
year = [1950, 1951, 1952, 2100]
pop = [2.538, 2.57, 2.62, 10.85]
plt.plot(year, pop)
plt.xlabel('YEAR')
plt.ylabel('pop')
plt.title('World Population Projections')
plt.show()
plt.yticks([0, 2, 4, 6,], ['0', '2B', '4B', '6B'])
plt.plot(year, pop)
plt.show()
#create a dictionary
europe = {'Spain':'Madrid', 'France':'Parish', 'Germany':'Berlin', 'Norway':'Oslo'}
europe['Italy']='Rome'
europe['Poland']='Wasow'
print(europe)
#dictionaries are inherently unordered
del(europe['Poland'])
print(europe)
import pandas as pd 
brics = pd.read_csv('E:\csvdhf5xlsxurlallfiles/brics.csv')
print(brivs)




