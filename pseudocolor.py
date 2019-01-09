import matplotlib.pyplot as plt 
import numpy as np 
u=np.linspace(-2,2,200)
v=np.linspace(-1,1,100)
X,Y=np.meshgrid(u,v)
z=X**2/25+Y**2/4
plt.pcolor(z)#for pseudocolor
plt.colorbar()
plt.show()
plt.pcolor(z, cmap='gray')
plt.colorbar()
plt.show()
plt.pcolor(z, cmap='autumn')
plt.colorbar()
plt.show()
plt.pcolor(z)
plt.colorbar()
plt.axis('tight')
plt.show()

plt.pcolor(X,Y,z)
plt.colorbar()
plt.show()
plt.contour(z)
plt.show()
plt.contour(z,30)
plt.contour(X,Y,z, 30)
plt.show()