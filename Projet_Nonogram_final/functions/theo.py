"""
Fonctions Back-end du programme
"""

from random import randint


def choicegrid(nb):
    """
    Fonction qui permet de choisir une grille aléatoirement
    Possède nb (int) en paramètre
    Return gridnb(Liste)
    """
    gridnb = randint(0, nb)
    return gridnb
    # Importer le fichier CSV avec les listes suivant la difficulter


def gridvide(taille):
    """
    Crée la grille de jeux vide que le joueur utilise pour jouer
    Possède taille (int) en paramètre
    Return t (int)
    """
    t = [[0] * taille for _ in range(taille)]
    return t


def showgrid(grid):
    """
    Permet d'afficher la grille du joueur
    Possède grid(list) en paramètre
    Ne possède aucun return
    """
    for i in grid:
        print(i)


def test(grid, nb, ch):
    """
    Permet de tester l'état de la case choisit par le joueur, et de la changer
    en conséquence
    Possède grid (Liste), nb (int) et ch (int) en paramètres
    Return grid (Liste)
    """
    if grid[nb][ch] == 0:
        grid[nb][ch] = 1
        # Change une case vide en une case valide
    elif grid[nb][ch] == 1:
        grid[nb][ch] = 2
        # Change une case valide en une case croix
    elif grid[nb][ch] == 2:
        grid[nb][ch] = 0
        # Change une case croix en case vide
    return grid


def verif(grid, gridog, lg):
    """
    Permet de comparer la grille du joueur avec la grille gagnante pour définir
    une victoire ou non
    Possède grid (Liste), gridog (Liste) et lg (int) en paramètres
    Return un bool
    """
    win = 0
    i = 0
    for a in grid:
        # Permet de naviguer dans les lignes
        j = 0
        for _ in a:
            # Permet de naviguer dans les collones de chaque lignes
            if grid[i][j] == gridog[i][j]:
                # Permet de vérifier si les cases du joueur sont identique à
                # l'original
                win += 1
            elif grid[i][j] == 2 and gridog[i][j] == 0:
                # Permet de prendre en compte les croix comme cases vide
                win += 1
            j += 1
        i += 1
    if win == (lg + 1) ** 2:
        return True
    return False


def rejouer():
    """
    Permet au joueur de relancé la partie
    Ne possède aucun paramètres
    Return un bool
    """
    print("Vouler vous rejouer ? (1 : Oui, 0 : Non)")
    nb = 0
    while nb != 1 or nb != 0:
        nb = int(input())
        if nb == 1:
            return True
        return False
    return None


def changeerror(lg, result):
    """
    Permet de transformer les coordonées donner par le joueur en deux indices
    Possède lg (int) et result (str) en paramètres
    Return nb (int), ch (int) et un bool
    """
    nb = int(result[1]) - 1
    # Permet de changer nb pour le transformer en un indice
    ch = int(ord(result[0].upper()) - 65)
    # Permet de transformer une lettre en un chiffre avec A = indice 0
    if nb >= 0 and ch >= 0:
        if nb <= lg and ch <= lg:
            return nb, ch, False
    print("Votre valeur ne fait pas partie du tableau de jeu")
    return nb, ch, True


def change(lg):
    """
    Cette fonction permet au joueur de choisir la case à selectionner et changer
    Possède lg (int) en paramètre
    Return nb (int) et ch (int)
    """
    game = True
    while game is True:
        print("Ou veux tu jouer (Répondre sous la forme : B2)")
        result = str(input())
        if len(result) == 2:
            # Permet une première gestion d'erreurs pour empecher le joueur de
            # jouer à un endroit invalide
            nb, ch, game = changeerror(lg, result)
        else:
            print("Votre valuer n'est pas bonne, elle doit être sous la forme",
                  " : Lettre Chiffre (Exemple : A1, D5, B4")
    return nb, ch
