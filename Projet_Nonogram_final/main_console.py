"""Programme complet du jeu Nonogram: Version console"""
import os
from functions import octavie as Oct
from functions import theo as T
from functions import wael as W


def choose_grid(taille):
    """
    Cette fonction permet de choisir de manière aléatoire une grille
    pour le jeu Nonogram, elle sera soit en 5x5 soit en 7x7
    """
    reelgrid = W.create_grid(taille)
    reelgridabs = W.coord_grid_abs(reelgrid)
    reelgridord = W.coord_grid_ord(reelgrid)
    solutions = Oct.trouver_solutions(reelgridabs, reelgridord, taille)
    while len(solutions) != 1:
        reelgrid = W.create_grid(taille)
        reelgridabs = W.coord_grid_abs(reelgrid)
        reelgridord = W.coord_grid_ord(reelgrid)
        solutions = Oct.trouver_solutions(reelgridabs, reelgridord, taille)
    return reelgrid


def afficher_regles():
    """Affiche les règles du jeu"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Règles du Nonogram ===")
    print("1. Vous devez remplir la grille en respectant les indices.")
    print("2. Les nombres indiquent la longueur des séquences de cases remplies.")
    print("3. Séparez les séquences par au moins une case vide.")
    print("4. Remplissez correctement toute la grille pour gagner.")
    input("Appuyez sur Entrée pour revenir au menu...")


def menu():
    """Affiche un menu textuel pour choisir l'action"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Menu Nonogram ===")
        print("1. Jouer en 5x5")
        print("2. Jouer en 7x7")
        print("3. Règles")
        print("4. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            taille = 5
            lg = len(T.gridvide(taille)) - 1
            gridog = T.gridvide(taille)
            vraiegrille = choose_grid(taille)
            game(gridog, lg, vraiegrille, taille)

        elif choix == "2":
            taille = 7
            lg = len(T.gridvide(taille)) - 1
            gridog = T.gridvide(taille)
            vraiegrille = choose_grid(taille)
            game(gridog, lg, vraiegrille, taille)

        elif choix == "3":
            afficher_regles()

        elif choix == "4":
            print("Au revoir !")


def game(grid, lg, gridog, taille):
    """lance le jeu principal"""
    win = False
    while not win:
        # Calcul des indices à partir de la grille solution (gridog)
        abs_ind = W.coord_grid_abs(gridog)  # indices des lignes
        col_ind = W.coord_grid_ord(gridog)  # indices des colonnes

        # Affichage des ordonnées
        # On détermine le nombre maximum d'indices sur une colonne
        max_col_ind = max(len(ind) for ind in col_ind)
        for i in range(max_col_ind):
            print(" " * 10, end="")
            # Pour chaque colonne, on affiche l'indice adéquat ou des espaces si inexistant
            for ind in col_ind:
                if len(ind) >= max_col_ind - i:
                    # Calcul de l'index dans la liste d'indices
                    index = i - (max_col_ind - len(ind))
                    print(str(ind[index]).rjust(3), end=" ")
                else:
                    print("   ", end=" ")
            print()  # fin de la ligne des indices

        # Affichage de la grille avec les abscisses
        for i in range(lg + 1):
            # Préparation et affichage des indices de la ligne i
            abs_str = " ".join(str(x) for x in abs_ind[i])
            print(abs_str.ljust(10), end="| ")
            # Affichage de la ligne de la grille
            print("   ".join(str(cell) for cell in grid[i]))

        print()  # Pour aérer

        nb, ch = T.change(lg)  # demande l'entrée du joueur
        grid = T.test(grid, nb, ch)  # modifie la grille en fonction du coup
        win = T.verif(grid, gridog, lg)  # vérifie si la grille correspond à la solution
        if win:
            if T.rejouer():  # propose de rejouer
                os.system('cls' if os.name == 'nt' else 'clear')  # clear le terminal
                gridog = T.gridvide(taille)
                vraiegrille = choose_grid(taille)
                game(gridog, lg, vraiegrille, taille)
        os.system('cls' if os.name == 'nt' else 'clear')  # clear le terminal


menu()
