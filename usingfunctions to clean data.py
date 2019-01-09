#using functins to clean data
#complex cleaning
#   Extract number from string
#   perform transformation on extracted number
# 1  .apply(), df.apply(np.mean, axis=0), axis=0 perform operations columns wise, axis=1 performs opr. row wise
import pandas as pd
tips = pd.read_csv('E:\csvdhf5xlsxurlallfiles/tips.csv')
print(tips)
print(tips['sex'])
print(tips.columns)
print(tips.iloc[230])
import matplotlib.pyplot as plt 
plt.plot(tips['total_bill'], color='yellow')
plt.hist(tips['total_bill'], bins = 20, color='green')
plt.show()







