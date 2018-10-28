import numpy as np
import matplotlib.pyplot as plt
l=[(0,0.1),(1,0.2),(2,0.3)]
for (i,j) in l:
    x=np.random.normal(i,j,1000)
    count,bins,ignored=plt.hist(x,14,density=True)
    plt.show()

