import numpy as np 
import matplotlib.pyplot as plt 
u=np.linspace(-2,2,3)
v=np.linspace(-1,1,5)
X,Y=np.meshgrid(u,v)
z=X**2/25+Y**2/4
print(X)
print(Y)
print('z:\n',z)
plt.set_cmap('gray')
plt.pcolor(z)
plt.show()
y=np.array([[1,2,3], [4,5,6]])
print('z:\n',z)
plt.pcolor(y)
plt.show()
