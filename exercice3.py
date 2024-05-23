import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 1000) #petal angle
r = 1 + 3/4*np.sin(3*theta) #petal length

x = r*np.cos(theta) #coordinates
y = r*np.sin(theta)

fig = plt.figure()
plt.plot(x,y)
plt.show()

A = 1/2* np.sum(r**2)*(theta[1]-theta[0]) #calculus of area 
print(A)

L = np.sum( np.sqrt(r**2 + np.gradient(r,theta)**2))*(theta[1]-theta[0])
print(L)