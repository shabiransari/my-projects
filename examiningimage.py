import matplotlib.pyplot as plt 
img=plt.imread('E:\csvdhf5xlsxurlallfiles/astronaut_PNG69.png')
plt.imshow(img)
plt.axis('off')
plt.show()
intensity=img.sum(axis=2)
plt.imshow(intensity, cmap='gray')
plt.colorbar()
plt.show()