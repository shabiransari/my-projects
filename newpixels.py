import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
image=plt.imread('E:\csvdhf5xlsxurlallfiles/sunflower_PNG13409.png')
plt.subplot(2,1,1)
plt.imshow(image, cmap='gray')
plt.title('original image')
plt.axis('off')
pixels=image.flatten()#image into 1d
cdf, bins, patches=plt.hist(pixels, bins=256, range=(0, 256), normed=True, cumulative=True)
new_pixels=np.interp(pixels, bins[:-1], cdf*255)
new_image=new_pixels.reshape(image.shape)
plt.subplot(2,2,1)
plt.title('Equalised image')
plt.axis('off')
#pdf=plt.subplot(new_pixels, bins=64, range=(0, 255), normed=False, color='red', alpha=0.4)
plt.grid('off')
plt.twinx()
plt.xlim((0,256))
plt.title('PDF&CDF(Equalised)')
cdf=plt.hist(new_pixels, bins=64, range=(0, 256), cumulative=True, normed=True, color='blue', alpha=0.4)
plt.show()
