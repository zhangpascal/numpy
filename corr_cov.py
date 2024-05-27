import numpy as np

n = 3
p = 5

mean_mat = np.zeros(p)
cov_mat = np.eye(p)

def my_var(x):
    var = 0
    mean = np.mean(x)
    for i in range(len(x)):
        var += (x[i]-mean)**2
    return var/(len(x)-1)    

def var_mat(X):
    v = np.zeros(len(X[0]))
    for i in range(len(X[0])):
        v[i] = my_var(X[:,i])
    return v
    
def my_cov(x,y):
    cov = 0
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    for i in range(len(x)):
        cov += (x[i]-x_mean)*(y[i]-y_mean)
    return cov/(len(x)-1)

def cova_mat(X):
    cov = np.zeros([len(X[0]), len(X[0])])
    for i in range(len(X[0])):
        for j in range(len(X[0])):
            cov[i, j] = my_cov(X[:,i], X[:,j])
    return cov
        
'''
X = np.array([[ 0.52119361,  0.72812349,  1.00937058],
 [-0.3287213,  -1.4603776,  -0.35621871],
 [ 0.23889542, -0.2778421,   0.21981612],
 [ 0.1965268,  -0.2019031,   1.23445598],
 [-1.1454827,   0.51868746, -0.5976506 ]])
 '''

X = np.random.multivariate_normal(mean_mat, cov_mat, n)

print(var_mat(X))
print(np.var(X, axis = 0))

print(cova_mat(X))
print(np.cov(X, rowvar=False))
