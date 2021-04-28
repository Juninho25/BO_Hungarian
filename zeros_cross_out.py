#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from typing import Tuple, List


def cross_out_zeros(matr: np.array, indep: List[Tuple[int, int]], dep: List[Tuple[int, int]]):
    """

    :param matr: Macierz kosztów
    :param indep: lista współrzędnych zer niezależnych
    :param dep: lista współrzędnych zer zależnych
    :return:
    """
    # Oznaczenie symbolem x danej kolumny lub
    # wiersza oznacza dodanie do listy x_rows lub x_cols
    x_rows = []
    x_cols = []
    indep_rows = [el[0] for el in indep]  # Wiersze, w których są zera niezależne

    # Oznaczenie symbolem x wierszy
    # nie posiadających zera niezależnego.
    for i in range(matr.shape[0]):
        if i not in indep_rows:
            x_rows.append(i)

    make_loop = True
    while make_loop:

        # Oznaczenie symbolem x kolumn
        # mających zero zależne w oznaczonym wierszu.
        for i in x_rows:
            for j in range(matr.shape[1]):
                if (i,j) in dep:
                    x_cols.append(j)

        # Oznaczenie symbolem x każdy wiersz mający
        # w oznakowanej kolumnie niezależne zero.
        new_rows_added = []
        for j in x_cols:
            for i in range(matr.shape[0]):
                if i not in x_rows and (i,j) in indep:
                    new_rows_added.append(i)
                    x_rows.append(i)

        # Sprawdzenie, czy w nowo dodanych
        # wierszach są zera niezależne. Jeśli nie
        # to kończy się pętla.
        make_loop = False
        for new_row in new_rows_added:
            if new_row in indep_rows:
                make_loop = True
                break

