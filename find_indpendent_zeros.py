import numpy as np
import copy

#funkcja szuka w pętli takiego zera w macierzy którego kolumna i wiersz 
#zawierają łącznie najmniej zer. Jak znajdzie to dodaje do zer niezależnych i 
#wypełnia wiersz i kol -1. Robi tak aż niebędzie już zer w macierzy i wtedy kończy

#indep to lista krotek indeksów zer niezależnych
#dep to lista krotek indeksów zer zależnych
#funkcja zwraca krotkę powyższych list
def find_indep_zeros(G):
    indep = []
    dep = []
    min_zer = 1
    found = False
    G_copy = copy.deepcopy(G)

    while np.any((G_copy == 0)):
        found = False
        for i in range(len(G_copy)):
            for k in range(len(G_copy)):
                
                if G_copy[i,k] == 0:
                    
                    ile_zer = np.count_nonzero(G_copy[:,k] == 0)
                    ile_zer = ile_zer + np.count_nonzero(G_copy[i,:] == 0)-1
                    
                    if ile_zer <= min_zer:
                        found = True
                        indep.append((i,k))

                        G_copy[:,k] = -1
                        G_copy[i,:] = -1
                        
                        ile_zer = 0
                        min_zer = 1
                        break
                    ile_zer = 0
        if not found:
            min_zer = min_zer + 1

    #wszystkie zera które nie są niezależne oznaczam jako zależne
    for i in range(len(G)):
        for k in range(len(G)):
            if G[i,k] == 0:
                if (i,k) not in indep:
                    dep.append((i,k))
        
    print(indep,dep)
    return indep,dep
        








if __name__ == "__main__":
    #testowane na:
    #https://zasoby1.open.agh.edu.pl/dydaktyka/matematyka/c_badania_operacyjne/krok/krok8_03.html
    
    G = np.matrix([[5, 30, 0, 30], 
                   [65, 50, 0, 0],
                   [0, 0,  55, 5],
                   [55, 20, 0, 5]])
    
    
    zera_zal_niezal(G)

 