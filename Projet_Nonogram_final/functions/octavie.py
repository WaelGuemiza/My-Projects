# Créé par octavie.belin, le 17/01/2025 en Python 3.7
"""
NONOGRAM
"""

from itertools import product

def ligne_valide(ligne, contraintes):
    """
    Vérifie si une ligne donnée satisfait les contraintes.
    ligne: liste de 0 et 1 représentant une ligne.
    contraintes: liste des contraintes (par exemple, [2, 1] signifie deux cases
    pleines, une case vide, une case pleine).
    """
    segments = []
    compteur = 0

    for cellule in ligne:
        if cellule == 1: # si la case est noir
            compteur += 1 # on incrémente le compteur
        elif compteur > 0:
            segments.append(compteur) # on ajoutele compteur à la liste
            compteur = 0 # on le remet à 0

    if compteur > 0:
        segments.append(compteur)

    return segments == contraintes # si la liste est égale aux contraintes de
# la ligne alors elle les respectes et est valide


def generer_lignes_possibles(contraintes, longueur):
    """
    Génère toutes les lignes possibles qui respectent les contraintes.
    contraintes: Liste des contraintes pour une ligne donnée.
    longueur: Longueur de la ligne.
    """
    toutes_possibilites = product([0, 1], repeat=longueur) # genere toutes les
    # lignes possibles pour une ligne et ses contraintes
    return [list(ligne) for ligne in toutes_possibilites if ligne_valide(ligne, contraintes)]


def verifier_grille(grille, contraintes_lignes, contraintes_colonnes):
    """
    Vérifie si une grille satisfait les contraintes des lignes et colonnes.
    grille: Grille 2D (liste de listes).
    contraintes_lignes: Contraintes des lignes.
    contraintes_colonnes: Contraintes des colonnes.
    Retourne True si la grille est valide, sinon False.
    """
    # Vérification des lignes
    for ligne, contraintes in zip(grille, contraintes_lignes):
        if not ligne_valide(ligne, contraintes):
            return False

    # Vérification des colonnes
    for indice_colonne, contraintes in enumerate(contraintes_colonnes):
        colonne = [grille[indice_ligne][indice_colonne] for indice_ligne in range(len(grille))]
        if not ligne_valide(colonne, contraintes):
            return False

    return True


def trouver_solutions(contraintes_lignes, contraintes_colonnes, taille):
    """
    Trouve toutes les solutions possibles pour une grille.
    contraintes_lignes: Contraintes des lignes.
    contraintes_colonnes: Contraintes des colonnes.
    taille: Taille de la grille.
    Retourne une liste de toutes les solutions possibles.
    """
    lignes_possibles = [
        generer_lignes_possibles(contraintes, taille)
        for contraintes in contraintes_lignes
        ]
    solutions = []

    def backtracking(grille, ligne):
        if ligne == taille: # condition d'arrêt
            if verifier_grille(grille, contraintes_lignes, contraintes_colonnes):
            # si la grille satisfait les contraintes
                solutions.append([row[:] for row in grille])
                # on ajoute la solution aux solutions
            return

        for ligne_candidate in lignes_possibles[ligne]:
            grille.append(ligne_candidate)
            backtracking(grille, ligne + 1)
            grille.pop()
            # on verifie si il y a d'autres solutions

    backtracking([], 0)
    return solutions


def resoudre_nonogram(contraintes_lignes, contraintes_colonnes, taille):
    """
    Résout le Nonogram en vérifiant d'abord sa validité (une seule solution possible).
    contraintes_lignes: Contraintes des lignes.
    contraintes_colonnes: Contraintes des colonnes.
    taille: Taille de la grille.
    Retourne la solution unique ou None si la grille est invalide.
    """
    solutions = trouver_solutions(contraintes_lignes, contraintes_colonnes, taille)
    if len(solutions) == 1: # si il y a qu'une seule solution
        return solutions[0] # on la retourne
    return None
