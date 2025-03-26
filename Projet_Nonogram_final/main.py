"""Programme complet du jeu Nonogram: Version graphique"""
import pygame
from functions import octavie as Oct
from functions import wael as W
from functions import kenza as K

pygame.init()


def choose_grid(taille):
    """choisit une grille qui est vérifiée"""
    reel_grid = W.create_grid(taille)
    reel_gridabs = W.coord_grid_abs(reel_grid)
    reel_gridord = W.coord_grid_ord(reel_grid)
    solutions = Oct.trouver_solutions(reel_gridabs, reel_gridord, taille)
    while len(solutions) != 1:
        reel_grid = W.create_grid(taille)
        reel_gridabs = W.coord_grid_abs(reel_grid)
        reel_gridord = W.coord_grid_ord(reel_grid)
        solutions = Oct.trouver_solutions(reel_gridabs, reel_gridord, taille)
    return [reel_gridabs, reel_gridord]


def savoir():
    """
    Fonction qui permet de savoir dans quel mode on est.
    Retourne "mode_1", "mode_2" ou None si aucun mode n'est actif.
    """
    # On utilise la variable CURRENT_VIEW de kenza.py pour vérifier le mode actuel
    mode_actuel = ""
    if K.CURRENT_VIEW == "mode_1":
        mode_actuel = "mode_1"
    if K.CURRENT_VIEW == "mode_2":
        mode_actuel = "mode_2"
    return mode_actuel


def verifier_victoire_s(taille, grille_actuelle, indices_colonnes):
    # Vérifier les colonnes
    for col in range(taille):
        blocs_colonne = []
        compteur = 0

        # Compter les blocs dans cette colonne
        for ligne in range(taille):
            if grille_actuelle[ligne][col] == 1:  # Case noircie
                compteur += 1
            elif compteur > 0:
                blocs_colonne.append(compteur)
                compteur = 0

        # Ne pas oublier le dernier bloc s'il existe
        if compteur > 0:
            blocs_colonne.append(compteur)

        # Si les blocs trouvés ne correspondent pas aux indices, la grille n'est pas correcte
        if blocs_colonne != indices_colonnes[col]:
            return False

    # Si toutes les vérifications sont passées, la grille est correcte


def verifier_victoire(solution, taille):
    """
    Vérifie si le joueur a complété correctement la grille Nonogram.
    :param solution: Liste contenant les indices [indices_colonnes, indices_lignes]
    :param taille: Taille de la grille (5 ou 7)
    :return: True si la grille est correctement complétée, False sinon
    """
    # Récupérer la grille actuelle depuis l'interface
    grille_actuelle = recuperer_grille_actuelle(taille)

    # Vérifier que la grille générée par les indices correspond à la grille actuelle
    indices_colonnes = solution[0]
    indices_lignes = solution[1]

    # Vérifier les lignes
    for ligne in range(taille):
        blocs_ligne = []
        compteur = 0

        # Compter les blocs dans cette ligne
        for col in range(taille):
            if grille_actuelle[ligne][col] == 1:  # Case noircie
                compteur += 1
            elif compteur > 0:
                blocs_ligne.append(compteur)
                compteur = 0

        # Ne pas oublier le dernier bloc s'il existe
        if compteur > 0:
            blocs_ligne.append(compteur)

        # Si les blocs trouvés ne correspondent pas aux indices, la grille n'est pas correcte
        if blocs_ligne != indices_lignes[ligne]:
            return False

        verifier_victoire_s(taille, grille_actuelle, indices_colonnes)
    return True


def recuperer_grille_actuelle(taille):
    """
    Récupère l'état actuel de la grille depuis l'interface graphique.
    :param taille: Taille de la grille (5 ou 7)
    :return: Liste 2D représentant la grille (1 pour case noircie, 0 pour case vide ou X)
    """
    grille = [[0 for _ in range(taille)] for _ in range(taille)]

    # Position initiale de la grille sur l'écran
    x_debut = 240
    y_debut = 190
    cell_size = 130 if taille == 5 else 93  # Taille des cellules selon le mode

    # Parcourir chaque cellule de la grille
    for ligne in range(taille):
        for col in range(taille):
            # Calculer le centre de la cellule
            x_centre = x_debut + col * cell_size + (cell_size // 2)
            y_centre = y_debut + ligne * cell_size + (cell_size // 2)

            # Vérifier la couleur de la cellule
            try:
                couleur = K.fenetre.get_at((x_centre, y_centre))

                # Vérifier si la couleur correspond à une case noircie (GRIS)
                if couleur[0] <= 50 and couleur[1] <= 50 and couleur[2] <= 50:
                    grille[ligne][col] = 1
            except:
                pass  # Ignorer les erreurs d'index si hors limites

    return grille


def afficher_message_victoire():
    """
    Affiche un message de victoire sur l'écran.
    """
    # Créer un rectangle pour le message de victoire
    rect_victoire = pygame.Rect(230, 310, 450, 150)
    pygame.draw.rect(K.fenetre, (255, 223, 186), rect_victoire)
    pygame.draw.rect(K.fenetre, K.NOIR, rect_victoire, 2)

    # Afficher le texte de victoire
    font_victoire = pygame.font.SysFont('Kristen ITC', 70)
    texte_victoire = font_victoire.render("VICTOIRE !", True, (94, 17, 30))
    K.fenetre.blit(texte_victoire, (250, 325))


def inmain():
    if savoir() == "mode_1":
        K.CURRENT_VIEW = "Encours"
        vraiegrille = choose_grid(5)
        K.modele_1()
        K.afficher_coordonnees(vraiegrille)
        victoire_affichee = False

    elif savoir() == "mode_2":
        K.CURRENT_VIEW = "Encours"
        vraiegrille = choose_grid(7)
        K.modele_2()
        K.afficher_coordonnees(vraiegrille)
        victoire_affichee = False

    if K.CURRENT_VIEW == "Encours" and vraiegrille and not victoire_affichee:
        taille = 5 if K.CELL_NUM == 5 else 7
        if verifier_victoire(vraiegrille, taille):
            print("Bravo ! Vous avez complété la grille !")
            afficher_message_victoire()
            victoire_affichee = True


def main():
    """
    Fonction principale qui lance le menu textuel.
    """
    continuer = True
    K.fenetre.fill((200, 173, 127))
    K.menu()
    vraiegrille = None
    victoire_affichee = False

    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continuer = False
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                K.clic_retour()
                K.clics_menu()
                K.clic_grid(event)
                victoire_affichee = False  # Réinitialiser l'affichage de victoire lors d'un clic

            if savoir() == "mode_1":
                K.CURRENT_VIEW = "Encours"
                vraiegrille = choose_grid(5)
                K.modele_1()
                K.afficher_coordonnees(vraiegrille)
                victoire_affichee = False

            elif savoir() == "mode_2":
                K.CURRENT_VIEW = "Encours"
                vraiegrille = choose_grid(7)
                K.modele_2()
                K.afficher_coordonnees(vraiegrille)
                victoire_affichee = False

            if K.CURRENT_VIEW == "Encours" and vraiegrille and not victoire_affichee:
                taille = 5 if K.CELL_NUM == 5 else 7
                if verifier_victoire(vraiegrille, taille):
                    print("Bravo ! Vous avez complété la grille !")
                    afficher_message_victoire()
                    victoire_affichee = True

        pygame.display.flip()

    pygame.display.quit()


if __name__ == "__main__":
    main()
