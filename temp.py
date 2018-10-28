import numpy as np
import matplotlib.pyplot as plt
l=[2,1,3]
for i in l:
    x=np.random.poisson(i,1000)
    count,bins,ignored=plt.hist(x,14,density=True)
    plt.show()