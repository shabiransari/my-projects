import pandas as pd 
import matplotlib.pyplot as plt 
airquality_df=pd.read_csv('E:\csvdhf5xlsxurlallfiles/airquality.csv')
print(airquality_df.head())
month=airquality_df['Month']
temperature=airquality_df['Temp']
#using axes()
plt.axes([0.05,0.05,0.425,0.9])
plt.plot(airquality_df, month, 'r')
plt.axes([0.05,0.05,0.425,0.9])
plt.plot(airquality_df, temperature, 'b')
plt.show()
#using subplot()
plt.subplot(2,1,1)
plt.plot(airquality_df, month, 'r')
plt.subplot(2,1,2)
plt.plot(airquality_df, temperature, 'b')
plt.tight_layout()
plt.show()


