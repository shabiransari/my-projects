import matplotlib.pyplot as plt 
import pandas as pd 
df= pd.read_csv('E:\csvdhf5xlsxurlallfiles\percent-bachelors-degrees-women-usa.csv')
print(df.shape)
year=df['Year']
computer_science=df['Computer Science']
physical_science=df['Physical Sciences']
plt.plot(year, computer_science, color='red')
plt.plot(year, physical_science, color='blue')
plt.axis((1990, 2010, 0, 50))
plt.show()
plt.savefig('axis_limits.png')
plt.plot(year, computer_science, color='red', label='Computer science')
plt.plot(year, physical_science, color='blue', label='Physical science')
plt.legend(loc='lower right')
import matplotlib.pyplot as plt 
cs_max=computer_science.max()
yr_max=year[computer_science.argmax()]
plt.annotate('maximum', xy=(yr_max, cs_max), xytext=(yr_max+6, cs_max+6), arrowprops=dict(facecolor='black'))
plt.subplot(2,1,1)
plt.plot(year, computer_science, color)
plt.xlabel('year')
plt.ylabel('Enroliment(%)')
plt.title('Unndergraduate Enroliment of women')
plt.show()

