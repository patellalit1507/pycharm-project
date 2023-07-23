import numpy as np
a=np.array([[1,2],
            [3,4]])
b=np.array([[2,5],
            [6,7]])
print(np.vstack((a,b)))
print("")
print(np.hstack((a,b)))