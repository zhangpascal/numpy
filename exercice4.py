import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 1000)
y = np.linspace(-2, 2, 1000)
xv, yv = np.meshgrid(x, y) #transform in grid
f = np.exp(-(xv**2 + yv**2)) * np.sin(xv)

fig = plt.figure()
plt.contourf(xv, yv, f, levels=100)
plt.colorbar()
plt.show()

vol1 = np.abs(f.ravel()).sum() * np.diff(x)[0] * np.diff(y)[0]
print(vol1)

vol2 = np.abs(f[np.sqrt(xv**2 + yv**2)>0.5].ravel()).sum() *np.diff(x)[0] * np.diff(y)[0]
print(vol2)