import matplotlib.pyplot as plt 
img=plt.imread('E:\csvdhf5xlsxurlallfiles\sunflower_PNG13409.png')
print(img.shape)
plt.imshow(img)
plt.axis('off')
plt.show()
collapsed=img.mean(axis=2)
plt.set_cmap('gray')
plt.imshow(collapsed, cmap='gray')
plt.axis('off')
plt.show()
unneven=collapsed[::4,::2]
plt.imshow(unneven)
plt.axis('off')
plt.show()
plt.imshow(unneven, aspect=200)
plt.axis('off')
plt.show()
plt.imshow(unneven, cmap='summer', extent=(0,640,0,480))
plt.axis('off')
plt.show()


