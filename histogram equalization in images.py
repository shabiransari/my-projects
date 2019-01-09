import pandas as pd 
import matplotlib.pyplot as plt 
orignal=plt.imread('E:\csvdhf5xlsxurlallfiles/sunflower_PNG13409.png')
pixels = orignal.flatten()
plt.hist(pixels, bins=3, range=(0, 256), normed=True, color='red', alpha=0.3)
plt.show()
minval, maxval=orignal.min(), orignal.max()
print(minval, maxval)
rescaled=(255/(maxval-minval)*(pixels-minval)
