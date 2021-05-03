import numpy as np
from typing import Dict


def find_new_zeros(matrix: np.ndarray, crossed: Dict):
    size = matrix.shape[0]
    temp = float('inf')

    for i in range(size):
        if i not in crossed["rows"]:
            for j in range(size):
                if j not in crossed["cols"]:
                    if matrix[i][j] < temp:
                        temp = matrix[i][j]

    for i in range(size):
        for j in range(size):
            if i not in crossed["rows"] and j not in crossed["cols"]:
                matrix[i, j] -= temp
            elif i in crossed["rows"] and j in crossed["cols"]:
                matrix[i, j] += temp
    return temp
    #self.fi += temp
    #return wywołanie funkcji z kroku 2 z argumentem matrix