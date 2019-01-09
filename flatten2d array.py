import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
image=plt.imread('E:\csvdhf5xlsxurlallfiles/sunflower_PNG13409.png')
red, green, blue=image[:,:,0], image[:,:,1], image[:,:,2]
red_pixels=red.flatten()
green_pixels=green.flatten()
blue_pixels=blue.flatten()
plt.title('Histogram from color image')
plt.xlim((0, 256))
plt.hist(red_pixels, bins=64, normed=True, color='red', alpha=0.2)
plt.hist(green_pixels, bins=64, normed=True, color='green', alpha=0.2)
plt.hist(blue_pixels, bins=64, normed=True, color='blue', alpha=0.2)
plt.show()


