

# [ [1,5,6], [1,22,55], [69, 55, 22] ] 3x3 Matrix

import random
import numpy as np

matrix = []

for i in range(3):
    row = []

    for number in range(3):
        random_number = random.randint(1, 100)
        row.append(random_number)

    matrix.append(row)

print(matrix)

# Novijim standardima
matrix_full = [ [random.randint(1,100) for _ in range(3)] for _ in range(3) ]
print(matrix_full)


# Primer matrixa sa Numpy
matrix_numpy = np.random.randint(1, 11, size=(3, 3))
print(matrix_numpy)