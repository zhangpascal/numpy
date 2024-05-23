import numpy as np
 
A = np.array([[3, 2, 3, 10], [2, -2, 5, 8], [3, 3, 4, 9], [3, 4, -3, -7]])
b = np.array([4, 1, 3, 2])

X = np.linalg.solve(A, b)
print(X)
