def Grille():
    """
    Crée et renvoie une grille de morpion vide (3x3).
    """
    G = [["", "A", "B", "C"],
         ["1", ".", ".", "."],
         ["2", ".", ".", "."],
         ["3", ".", ".", "."]]
    return G

def Affiche(G):
    """
    Affiche la grille G comme un tableau.

    Paramètres :
    - G : liste de listes représentant la grille de morpion.
    """
    for ligne in range(len(G)):
        for colonne in range(len(G[ligne])):
            print(G[ligne][colonne], end="\t")
        print()
    print()

def Joue(G, l, c, j):
    """
    Place le symbole du joueur j dans la case de la ligne l et de la colonne c de la grille G.

    Paramètres :
    - G : liste de listes représentant la grille de morpion.
    - l : numéro de ligne (0, 1, ou 2).
    - c : numéro de colonne (0, 1, ou 2).
    - j : numéro du joueur (1 ou 2).
    """
    # Vérifier si la case est libre
    if G[l][c] == ".":
        # La case est libre, placer le symbole du joueur
        G[l][c] = "X" if j == 1 else "O"
    else:
        # La case est déjà occupée, demander au joueur de choisir une autre case
        print("Case déjà occupée. Choisissez une autre case.")
        # Vous pouvez ajouter une boucle ici pour redemander la saisie de l'utilisateur
        # jusqu'à ce qu'une case libre soit choisie.

def Gagne(G):
    """
    Vérifie si la grille G est gagnante.

    Paramètres :
    - G : liste de listes représentant la grille de morpion.

    Renvoie :
    - True si la grille est gagnante, False sinon.
    """
    # Vérifier les lignes, les colonnes et les diagonales
    for i in range(1, 4):
        # Vérifier les lignes
        if G[i][1] == G[i][2] == G[i][3] != ".":
            return True
        # Vérifier les colonnes
        if G[1][i] == G[2][i] == G[3][i] != ".":
            return True
    # Vérifier les diagonales
    if G[1][1] == G[2][2] == G[3][3] != "." or G[1][3] == G[2][2] == G[3][1] != ".":
        return True
    return False

def DemanderRejouer():
    """
    Demande aux joueurs s'ils veulent rejouer.

    Renvoie :
    - True si les joueurs veulent rejouer, False sinon.
    """
    while True:
        choix = input("Voulez-vous rejouer? (O/N): ")
        if choix == "O":
            return True
        elif choix == "N":
            return False
        else:
            print("Choix non valide. Veuillez répondre par 'Oui' (O) ou 'Non' (N).")

def PartieMorpion():
    """
    Fonction principale pour jouer au morpion.
    """
    Continuer = True
    while Continuer:
        # Initialisation de la grille
        grille = Grille()

        # Variables pour suivre le tour actuel et le joueur actuel
        tour = 1
        joueur_actuel = 1
        Continuer = True

        # Boucle principale du jeu
        while Continuer:
            # Afficher la grille
            Affiche(grille)

            # Demander au joueur actuel de jouer
            print(f"Joueur {joueur_actuel}, c'est à vous de jouer!")

            # Demander la ligne et vérifier si c'est une entrée valide
            while True:
                try:
                    ligne = int(input("Entrez le numéro de ligne (1, 2, ou 3) : ")) - 1
                    if 0 <= ligne <= 2:
                        break
                    else:
                        print("Numéro de ligne non valide. Veuillez réessayer.")
                except ValueError:
                    print("Entrée non valide. Veuillez réessayer.")

            # Demander la colonne et vérifier si c'est une entrée valide
            while True:
                try:
                    colonne = ord(input("Entrez le numéro de colonne (A, B, ou C) : ")) - ord("A")
                    if 0 <= colonne <= 2:
                        break
                    else:
                        print("Numéro de colonne non valide. Veuillez réessayer.")
                except ValueError:
                    print("Entrée non valide. Veuillez réessayer.")

            # Vérifier si la case est libre, sinon demander à nouveau
            while grille[ligne + 1][colonne + 1] != ".":
                print("Case déjà occupée. Choisissez une autre case.")
                # Redemander la ligne et la colonne
                while True:
                    try:
                        ligne = int(input("Entrez le numéro de ligne (1, 2, ou 3) : ")) - 1
                        if 0 <= ligne <= 2:
                            break
                        else:
                            print("Numéro de ligne non valide. Veuillez réessayer.")
                    except ValueError:
                        print("Entrée non valide. Veuillez réessayer.")

            # Jouer le coup
            Joue(grille, ligne + 1, colonne + 1, joueur_actuel)

            # Vérifier si le joueur actuel a gagné
            if Gagne(grille):
                print(f"Félicitations Joueur {joueur_actuel}! Vous avez gagné!")
                break

            # Vérifier s'il y a match nul
            if tour == 9:
                print("Match nul!")
                break

            # Passer au tour suivant et changer de joueur
            tour += 1
            joueur_actuel = 3 - joueur_actuel  # Alterner entre 1 et 2

        # Afficher la grille à la fin du jeu
        Affiche(grille)

        # Demander aux joueurs s'ils veulent rejouer
        Continuer = DemanderRejouer()

# Appeler la fonction pour commencer une partie
PartieMorpion()