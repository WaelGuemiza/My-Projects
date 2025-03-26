"""Fonctions de GUEMIZA Waël pour le projet Nonogram"""
from random import randint


gridtest = [[[1, 1], [1, 2], [3, 1], [1], [2]], #Absysses
         [[3], [1, 1], [2, 1], [2], [2]]] #Ordonnées
grid1 = [[1, 0, 1, 1, 1],
         [0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0],
         [0, 1, 1, 0, 0],
         [0, 0, 0, 1, 1]]

def create_grid(taille):
    """creer la grille de Nonogram aléatoirement"""
    grid =  [[] * taille for _ in range(taille)]
    for i in range(taille):
        grid[i] = [randint(0,1) for _ in range(taille)]
    return grid


def coord_grid_abs(grid):
    """renvoi l'abscisse de de la grille grid, paramètre de type list"""
    compte = len(grid)
    abscisse = []
    for i in range(compte):
        s = 0
        a = []
        for j in grid[i]:
            if j == 1 :
                s += 1
            else :
                if s != 0 :
                    a.append(s)
                    s = 0
        if s != 0 :
            a.append(s)
        abscisse.append(a)
    return abscisse


def coord_grid_ord(grid):
    """renvoi les ordonnées de la grille grid, paramètre de type list"""
    ordonnee = []
    num_cols = len(grid[0])
    for col in range(num_cols):
        s = 0
        a = []
        for i in grid:
            if i[col] == 1:
                s += 1
            else:
                if s != 0:
                    a.append(s)
                    s = 0
        if s != 0:
            a.append(s)
        ordonnee.append(a)
    return ordonnee

def all_coord_grid(grid):
    """
    renvoie les coordonnées de grid, paramètre de type list
    dans l'ordre Abscisse puis Ordonnées
    """
    return [coord_grid_abs(grid), coord_grid_ord(grid)]
