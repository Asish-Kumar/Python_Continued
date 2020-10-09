def factorial(num):
    if num < 0:
        return 0
    if num == 0:
        return 1
    print(num, end=" ")
    return num * factorial(num - 1)


#print("\n", factorial(3))

import numpy as np

mat = np.array([[1, 2, 3], [3, 4, 5]])
print(mat.shape)

