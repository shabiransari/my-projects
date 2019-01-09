import matplotlib.pyplot as plt 
import numpy as np 
u=np.linspace(-2,2,200)
v=np.linspace(-1,1,100)
X,Y=np.meshgrid(u,v)
z=X**2/25+Y**2/4
#create a filled contour plots with  colormaps
plt.subplot(2,2,1)
plt.contourf(X,Y,z, cmap='summer')
plt.colorbar()
plt.title('SUMMER')
plt.subplot(2,2,2)
plt.contourf(X,Y,z, cmap='autumn')
plt.colorbar()
plt.title('AUTUMN')
plt.subplot(2,2,3)
plt.contourf(X,Y,z, cmap='winter')
plt.colorbar()
plt.title('WINTER')
plt.subplot(2,2,4)
plt.contourf(X,Y,z, cmap='spring')
plt.colorbar()
plt.title('SPRING')
plt.show()
