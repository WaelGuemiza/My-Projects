"""Recherche interface graphique nonogram:"""

import pygame

pygame.init()

fenetre = pygame.display.set_mode((900, 850))

# Variables pour les rectangles
NOIR = (0, 0, 0)
GRIS = (48, 48, 48)
BEIGE = (245, 245, 220)
ROUGE = (255, 0, 0)
LARGEUR_REC = 650
HAUTEUR_REC = 650

# Variables globals
CELL_SIZE = 0
CASES = 0
font_local = pygame.font.SysFont(None, 40)  # Taille de la police
CELL_NUM = 0
CURRENT_VIEW = "menu"

# Pour l'affichage du texte en general
font_1 = pygame.font.SysFont('Kristen ITC', 70)
font_2 = pygame.font.SysFont('Kristen ITC', 50)
font_3 = pygame.font.SysFont('Kristen ITC', 40)
font_4 = pygame.font.SysFont('Kristen ITC', 30)
font_5 = pygame.font.SysFont('Kristen ITC', 45)
TEXTE_COL = NOIR
TEXTE_COL_ALT = (94, 17, 30)
TEXTE_COL_ALT_2 = (178, 93, 97)

pygame.display.set_caption("Nonogramme")

# Cette partie peu creer une erreur si le dossier n'est pas ouvert
# avec le reste du programme, elle sert juste a afficher l'icon du jeu
"""image = pygame.image.load("Image/image_nonogramme.png").convert()
pygame.display.set_icon(image)"""


# fonctions pour l'interface du menu
def draw_text(text, font, text_col, x, y):
    """
    Cette fonction permet de écrire un texte sur
    une fenetre pygame
    """
    img = font.render(text, True, text_col)
    fenetre.blit(img, (x, y))


def show_button_rules():
    """
    Cette fonction permet d'afficher le bouton
    qui mène aux regle du jeu (c'est une fonction
    qui fait gagner de l'espace pour pylint/pylama)
    """
    bouton = pygame.Rect(20, 150, 340, 70)
    pygame.draw.rect(fenetre, (179, 117, 96), bouton)
    pygame.draw.rect(fenetre, TEXTE_COL_ALT, bouton, 2)
    draw_text('Règles du jeu', font_2, TEXTE_COL_ALT, 25, 150)


def show_button_gmode_1():
    """
    Cette fonction sert à afficher le bouton qui mène
    à la première grille de jeu (c'est une fonction
    qui fait gagner de l'espace pour pylint/pylama)
    """
    bouton = pygame.Rect(20, 380, 290, 60)
    pygame.draw.rect(fenetre, (179, 117, 96), bouton)
    pygame.draw.rect(fenetre, TEXTE_COL_ALT, bouton, 2)
    draw_text('Niveau Simple', font_3, TEXTE_COL_ALT, 25, 380)


def show_button_gmode_2():
    """
    Cette fonction sert à afficher le bouton qui mène
    à la deuxième grille de jeu (c'est une fonction
    qui fait gagner de l'espace pour pylint/pylama)
    """
    bouton = pygame.Rect(20, 480, 300, 60)
    pygame.draw.rect(fenetre, (179, 117, 96), bouton)
    pygame.draw.rect(fenetre, TEXTE_COL_ALT, bouton, 2)
    draw_text('Niveau Normal', font_3, TEXTE_COL_ALT, 25, 480)


def show_button_gmode_3():
    """
    Cette fonction sert à afficher le bouton qui mène
    à la troisième grille de jeu (c'est une fonction
    qui fait gagner de l'espace pour pylint/pylama)
    """
    bouton = pygame.Rect(20, 580, 325, 60)
    pygame.draw.rect(fenetre, (179, 117, 96), bouton)
    pygame.draw.rect(fenetre, TEXTE_COL_ALT, bouton, 2)
    draw_text('Niveau Difficile', font_3, TEXTE_COL_ALT, 25, 580)


def menu():
    """
    Cette fonction permet d'afficher le menu du jeu Nonogram,
    elle affiche le titre du jeu, les boutons pour afficher
    les règles et pour sélectionner le mode de jeu
    """
    draw_text('Nonogram', font_1, TEXTE_COL, 250, 10)
    show_button_rules()
    draw_text('Voici les modes de jeu disponibles :', font_2, TEXTE_COL, 10, 265)
    show_button_gmode_1()
    show_button_gmode_2()
    show_button_gmode_3()


def bouton_retour():
    """
    Cette fonction permet de créer un bouton nommé "retour" qui
    servira à retourner au menu du jeu si il est appuyé
    """
    bouton = pygame.Rect(5, 50, 155, 60)
    pygame.draw.rect(fenetre, (202, 178, 163), bouton)
    pygame.draw.rect(fenetre, NOIR, bouton, 2)
    draw_text('Retour', font_3, NOIR, 10, 50)


# Fonctions pour option du menu
def show_rules():
    """
    Cette fonction permet d'afficher les règles du jeu Nonogram
    """
    texte = "Il s'agit de colorier les cases d'une grille, appellée Nonogram."
    texte2 = "Les chiffres placés en tête de ligne et de colonne indiquent"
    texte3 = "combien de cases doivent être noircies."
    texte4 = "Par exemple sur la grille ci-dessous, la 2ème colonne : 3 - 2."
    texte5 = "Cela signifie que cette colonne peut avoir de haut en bas 3"
    texte6 = "cases coloriées puis 2 autres."
    texte7 = "Ces groupes de cases à colorier doivent être séparés d'au"
    texte8 = "minimum une case blanche."
    texte9 = "C'est le même principe donc pour les lignes."
    draw_text('Nonogram Règle', font_1, TEXTE_COL, 210, 10)
    draw_text(texte, font_4, TEXTE_COL, 10, 140)
    draw_text(texte2, font_4, TEXTE_COL, 10, 180)
    draw_text(texte3, font_4, TEXTE_COL, 10, 220)
    draw_text(texte4, font_4, TEXTE_COL, 10, 270)
    draw_text(texte5, font_4, TEXTE_COL, 10, 305)
    draw_text(texte6, font_4, TEXTE_COL, 10, 340)
    draw_text(texte7, font_4, TEXTE_COL, 10, 390)
    draw_text(texte8, font_4, TEXTE_COL, 10, 425)
    draw_text(texte9, font_4, TEXTE_COL, 10, 480)


def show_consigne():
    """
    Cette fonction sert à afficher les consigne du jeu Nonogram
    """
    texte_1 = "- Pour colorier une case en noir, faite un clic gauche"
    texte_2 = "- Pour enlever une case noir, faite un clic gauche sur"
    texte_3 = "  une case déjà noircie"
    texte_4 = "- Pour afficher une croix (case rouge) dans une case,"
    texte_5 = "  faite un clic droit sur une case"
    draw_text(texte_1, font_4, TEXTE_COL, 10, 530)
    draw_text(texte_2, font_4, TEXTE_COL, 10, 575)
    draw_text(texte_3, font_4, TEXTE_COL, 10, 605)
    draw_text(texte_4, font_4, TEXTE_COL, 10, 655)
    draw_text(texte_5, font_4, TEXTE_COL, 10, 685)
    bouton_retour()


# fonction pour l'affichage des grilles
def show_outer_grid():
    """
    Cette fonction nous sert à afficher de manière fixe les coté
    éxterieur des grilles du nonogramme, elle ne varie pas peut
    importe le mode de jeu selectionné
    """
    pygame.draw.rect(fenetre, BEIGE, [240, 190, LARGEUR_REC, HAUTEUR_REC])
    pygame.draw.rect(fenetre, NOIR, [240, 190, LARGEUR_REC, HAUTEUR_REC], 4)
    bouton_retour()


def afficher_coordonnees(grille_indices):
    """
    Affiche les indices pour un nonogramme
    param grille_indices: Liste contenant les indices des colonnes et des lignes
                         [indices_colonnes, indices_lignes]
    """
    indices_colonnes = grille_indices[0]
    indices_lignes = grille_indices[1]
    x_start = 240
    y_start = 190

    global CELL_SIZE

    font_indices = pygame.font.SysFont(None, 30)
    for i, indices in enumerate(indices_colonnes):
        pos_x = x_start + i * CELL_SIZE + CELL_SIZE // 2
        indices_inverses = indices[::-1]
        start_y = y_start - 30
        for j, indice in enumerate(indices_inverses):
            pos_y = start_y - j * 30
            texte = font_indices.render(str(indice), True, NOIR)
            texte_rect = texte.get_rect(center=(pos_x, pos_y))
            fenetre.blit(texte, texte_rect)

    for i, indices in enumerate(indices_lignes):
        pos_y = y_start + i * CELL_SIZE + CELL_SIZE // 2
        indices_inverses = indices[::-1]
        start_x = x_start - 30
        for j, indice in enumerate(indices_inverses):
            pos_x = start_x - j * 30
            texte = font_indices.render(str(indice), True, NOIR)
            texte_rect = texte.get_rect(center=(pos_x, pos_y))
            fenetre.blit(texte, texte_rect)


def modele_1():
    """
    Cette fonction permet d'afficher une grille en 5 - 5
    """
    show_outer_grid()
    x = 240
    y = 190
    global CELL_SIZE, CELL_NUM
    CELL_SIZE = 130
    CELL_NUM = 5  # Corrigé de 7 à 5
    for _ in range(1, 6):
        for _ in range(1, 6):
            pygame.draw.rect(fenetre, NOIR, [x, y, CELL_SIZE, CELL_SIZE], 2)
            x += CELL_SIZE
        x = 240
        y += CELL_SIZE


def modele_2():
    """
    Cette fonction permet d'afficher une grille en 7 - 7
    """
    show_outer_grid()
    x = 240
    y = 190
    global CELL_SIZE, CELL_NUM
    CELL_SIZE = 93
    CELL_NUM = 7
    for _ in range(1, 8):
        for _ in range(1, 8):
            pygame.draw.rect(fenetre, NOIR, [x, y, CELL_SIZE, CELL_SIZE], 2)
            x += CELL_SIZE
        x = 240
        y += CELL_SIZE


def modele_3():
    """
    Cette fonction permet d'afficher un message
    """
    texte = "Ce mode de jeu n'est pas fonctionnel"
    texte_2 = "pour l'instant"
    show_outer_grid()
    x = 240
    y = 190
    global CELL_SIZE, CELL_NUM
    CELL_SIZE = 65
    CELL_NUM = 10
    for _ in range(1, 11):
        for _ in range(1, 11):
            pygame.draw.rect(fenetre, NOIR, [x, y, CELL_SIZE, CELL_SIZE], 2)
            x += CELL_SIZE
        x = 240
        y += CELL_SIZE
    draw_text(texte, font_5, ROUGE, 50, 330)
    draw_text(texte_2, font_5, ROUGE, 340, 430)


# gestion des clics
def clic_retour():
    """
    Cette fonction permet de gérer les clics sur le bouton
    retour,si le joueur clic sur le bouton retour, il sert
    renvoyer sur le menu du jeu
    """
    global CURRENT_VIEW
    pos = pygame.mouse.get_pos()
    if pos[0] > 5 and pos[0] < 160 and pos[1] > 50 and pos[1] < 110:
        fenetre.fill((200, 173, 127))
        CURRENT_VIEW = "menu"
        menu()
        pygame.display.flip()


def clics_menu():
    """
    Cette fonction permet de rediriger le joueur sur le mode de jeu
    qu'il a sélectionné ou sur les règles du jeu.
    """
    global CURRENT_VIEW

    if CURRENT_VIEW in ["mode_1", "mode_2", "mode_3", "rules", "Encours"]:
        return

    clic = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()

    if clic[0] == 1:
        if 10 < pos[0] < 300 and 380 < pos[1] < 440:
            fenetre.fill((200, 173, 127))
            CURRENT_VIEW = "mode_1"
            modele_1()
            pygame.display.flip()
            return "5"

        elif 10 < pos[0] < 310 and 480 < pos[1] < 540:
            fenetre.fill((200, 173, 127))
            CURRENT_VIEW = "mode_2"
            modele_2()
            pygame.display.flip()
            return "7"

        elif 10 < pos[0] < 330 and 580 < pos[1] < 640:
            fenetre.fill((200, 173, 127))
            CURRENT_VIEW = "mode_3"
            modele_3()
            pygame.display.flip()

        elif 10 < pos[0] < 350 and 150 < pos[1] < 220:
            fenetre.fill((200, 173, 127))
            CURRENT_VIEW = "rules"
            show_rules()
            show_consigne()
            pygame.display.flip()


def clic_grid(event):
    """
    Cette fonction sert à gerer les clics de chaque grille,
    un clic gauche pour colorier la grille en gris, un clic
    droit pour la colorier en rouge (l'équivalant de la croix)
    """
    global CURRENT_VIEW
    if CURRENT_VIEW in ["menu", "rules"]:
        return
    x, y = event.pos
    col = (x - 240) // CELL_SIZE
    row = (y - 190) // CELL_SIZE
    cases = (col, row)
    inc_col = (240 + col * CELL_SIZE) + 2
    inc_row = (190 + row * CELL_SIZE) + 2
    if cases[0] >= 0 and cases[1] >= 0:
        if cases[0] < CELL_NUM and cases[1] < CELL_NUM:
            if event.button == 1:
                if fenetre.get_at((x, y)) == GRIS:
                    pygame.draw.rect(fenetre, BEIGE, [inc_col, inc_row,
                    CELL_SIZE - 3, CELL_SIZE - 3])
                else:
                    pygame.draw.rect(fenetre, GRIS, [inc_col, inc_row,
                    CELL_SIZE - 3, CELL_SIZE - 3])
            if event.button == 3:
                pygame.draw.rect(fenetre, ROUGE, [inc_col, inc_row,
                                CELL_SIZE - 3, CELL_SIZE - 3])


def get_current_grid():
    """
    Récupère l'état actuel de la grille affichée sous forme de liste 2D.
    Retourne 1 pour une case colorée (grise) et 0 pour une case vide (beige) ou rouge (X).
    """
    global CELL_SIZE, CELL_NUM

    # Déterminer la taille réelle de la grille
    actual_size = 5 if CURRENT_VIEW == "mode_1" else 7

    grid = []
    for row in range(actual_size):
        ligne = []
        for col in range(actual_size):
            # Calcul de la position de la case (centre de la case)
            x_pos = 240 + col * CELL_SIZE + (CELL_SIZE // 2)
            y_pos = 190 + row * CELL_SIZE + (CELL_SIZE // 2)

            # Obtention de la couleur au centre de la case
            try:
                pixel_color = fenetre.get_at((x_pos, y_pos))

                # Vérification si la couleur est proche du GRIS (case noircie)
                if (abs(pixel_color[0] - GRIS[0]) < 10 and
                    abs(pixel_color[1] - GRIS[1]) < 10 and
                    abs(pixel_color[2] - GRIS[2]) < 10):
                    ligne.append(1)  # Case colorée (grise)
                else:
                    ligne.append(0)  # Case vide (beige) ou croix rouge
            except IndexError:
                # Si on est hors limites, considérer comme case vide
                ligne.append(0)
        grid.append(ligne)
    return grid


def affiche_nono():
    """
    Cette fonction est la boucle principale de l'affichage graphique
    """
    continuer = True

    fenetre.fill((200, 173, 127))
    menu()

    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continuer = False
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clic_retour()
                clics_menu()
                clic_grid(event)

        pygame.display.flip()

    pygame.display.quit()
