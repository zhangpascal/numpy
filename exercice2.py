import numpy as np
import matplotlib.pyplot as plt

sum = np.sum(np.arange(0, 10001, 1)[(np.arange(0, 10001, 1)%4 != 0) * (np.arange(0, 10001, 1)%7 != 0)])
print(sum) 