import numpy as np
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))  #создание сетки
u = 1
v = -1
plt.quiver(x, y, v, u)
plt.savefig('vector_1.png')
plt.close()
u = x/np.sqrt(x**2+y**2)
v = y/np.sqrt(x**2+y**2)
plt.quiver(x, y, u, v)
plt.savefig('vector_2.png')
plt.close()
u = -y/np.sqrt(x**2+y**2)
v = x/np.sqrt(x**2+y**2)
plt.quiver(x, y, u, v)
plt.savefig('vector_3.png')
plt.close()