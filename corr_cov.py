import numpy as np
import time

n = 3000
p = 5

mean_mat = np.zeros(p)
cov_mat = np.eye(p)

def pre_proc(X):
    X = np.array(X)
    
    m = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    
    X = (X-m)/std
    return X

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
        
X = np.random.multivariate_normal(mean_mat, cov_mat, n)

X = pre_proc(X) 

print(np.var(X, axis = 0))

print(np.cov(X, rowvar=False, bias=True ))
