import numpy as np
import matplotlib.pyplot as plt


x= np.linspace(0, 10, 10000)  
y = np.exp(-x/10) * np.sin(x)  #function

y_sub = y[(x>=4) * (x<=7)] #extract y with x in [4,7]

mean = np.mean(y_sub) #mean between 4 and 7
std = np.std(y_sub) #std between 4 and 7

print(mean, std)

ym = np.percentile(y_sub, 80) # value such that 80% of y are less than in [4,7]

dydx = np.gradient(y, x) #derivative

fig = plt.figure()

plt.plot(x, y, 'red')
plt.plot(x, dydx, 'blue')
plt.show()

zeros = x[1:][dydx[1:] * dydx[:-1]<0] #zeros of the function
print(zeros)
