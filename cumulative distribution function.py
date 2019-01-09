import pandas as pd 
import matplotlib.pyplot as plt 
image=plt.imread('E:\csvdhf5xlsxurlallfiles/sunflower_PNG13409.png')
plt.subplot(2,1,1)
plt.imshow(image, cmap='gray')
plt.title('original image')
plt.axis('off')
pixels=image.flatten()
plt.subplot(2,1,2)
pdf=plt.hist(pixels, bins=64, range=(0,5), normed=False, color='red', alpha=0.4)
plt.grid('off')
plt.twinx()
cdf=plt.hist(pixels, bins=64, range=(0, 5), normed=True, cumulative=True, color='blue', alpha=0.4)
plt.xlim((0, 5))
plt.grid('off')
plt.title('pdf&cdf(original image)')
plt.show()

