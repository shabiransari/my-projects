import matplotlib.pyplot as plt 
import pandas as pd 
df = pd.read_csv('E:\csvdhf5xlsxurlallfiles\percent-bachelors-degrees-women-usa.csv')
year=df['Year']
physical_science=df['Physical Sciences']
computer_science=df['Computer Science']
plt.style.use('ggplot')
plt.subplot(2,2,1)
plt.plot(year, physical_science, color='blue')
plt.title('physical science')
plt.subplot(2,2,2)
plt.plot(year, computer_science, color='red')
plt.title('computer science')
#add annotation
cs_max=computer_science.max()
yr_max=year[computer_science.argmax()]
plt.annotate('maximum', xy=(yr_max, cs_max), xytext=(yr_max+5, cs_max+5), arrowprops=dict(facecolor='k'))
plt.show()
