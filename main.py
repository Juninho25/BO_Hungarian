import numpy as np
import copy
from part4 import find_new_zeros
from reduction import reduction
from find_indpendent_zeros import find_indep_zeros
from zeros_cross_out import cross_out_zeros


def print_matrix_dep(M, indep):
    M = copy.deepcopy(M)
    M = M.astype(str)
    for i in indep:
        M[i[0],i[1]] = "0*"
    print("Macierz z zerami niezależnymi:\n",M, "\n")

def main():
    matrix = np.array([[20, 40, 10, 50], [100, 80, 30, 40], [10, 5, 60, 20], [70, 30, 10, 25]])
    n = len(matrix)
    print("Macierz początkowa:\n", matrix,"\n")
    
    matrix, fi = reduction(matrix)
    print("Macierz po redukcji:\n", matrix,"\n")
    
    while True:

        indep, dep = find_indep_zeros(matrix)
        print_matrix_dep(matrix, indep)
        
        if len(indep) >= n:
            print("Macierz końcowa:\n", matrix, "\n")
            print("Przydział(indeksy):", indep)
            print("Koszt:", fi)
            break
        crossed = cross_out_zeros(matrix, indep, dep)

        temp = find_new_zeros(matrix, crossed)
        fi = fi + temp
        
        

main()