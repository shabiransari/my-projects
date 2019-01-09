#matplotlib 
import matplotlib.pyplot as plt 
year = [1950, 1940, 1960, 1955]
pop = [2.99, 1.66, 2.11, 1.55]
plt.xlabel("YEAR")
plt.ylabel("POPULATION")
plt.title("POPULATION INDEX")
#we cqn show particular name on scatter - plt.scatter(x=year, y= pop, s=np.array(pop)*2, c = col, alpha=.8)
plt.plot(year, pop)
plt.show()
plt.title("POPULATION INDEX")
plt.scatter(year, pop)
plt.show()
values = [0, 0.5, 0.66, 0.45, 0.44, 0.34, 5, 7]
plt.hist(values, bins=200)
