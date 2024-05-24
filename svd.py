import numpy as np

X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
U, S, V = np.linalg.svd(X)

print(U*S@V)

print(U[:,0].reshape(-1, 1)*S[0]@V[0,:].reshape(1, -1))

print(U[:,0:3]*S[0:3]@V[0:3,:])
