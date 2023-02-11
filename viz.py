from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

a = np.array([5,4,3,2,1])
b = np.array([30,60,80,90,10,30,50,10])

a, b = np.meshgrid(a, b)

print(a.shape, b.shape)

fig = plt.figure()
axes = fig.add_subplot(projection = '3d')
axes.plot_surface(a, b, a+b, cmap = 'coolwarm')
plt.show()

a = np.arange(-1, 1, 0.02)
b = a
a, b = np.meshgrid(a, b)

fig = plt.figure()
axes = fig.add_subplot(projection = '3d')
axes.plot_surface(a, b, a**2+b**2, cmap = 'rainbow')
plt.show()

fig = plt.figure()
axes = fig.add_subplot(projection = '3d')
axes.contour(a, b, a**2+b**2, cmap = 'rainbow')
plt.show()