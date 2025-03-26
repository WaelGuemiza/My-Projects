import random
import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions et nom de la fenêtre
screen = pygame.display.set_mode((650, 700))
pygame.display.set_caption("Colorfle")

# Chargement de l'arrière-plan
background = pygame.image.load("assets/Bg.jpg")

# Couleurs de base
GRAY = (50, 50, 50)
WHITE = (200, 200, 200)
DARK_GRAY = (30, 30, 30)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Limite d'essais
essais_max = 7

# Historique des coups joués
historique = []

def creer_couleurs():
    """Crée les 15 couleurs et retourne une liste de ces couleurs."""
    couleurs = [
        [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        for _ in range(15)
    ]
    return couleurs

def couleurs_a_trouver(c):
    """Sélectionne 3 couleurs au hasard des 15 et retourne une liste des couleurs à trouver."""
    ran1 = c[random.randint(0, 14)]
    ran2 = c[random.randint(0, 14)]
    while ran2 == ran1:
        ran2 = c[random.randint(0, 14)]
    ran3 = c[random.randint(0, 14)]
    while ran3 == ran2 or ran3 == ran1:
        ran3 = c[random.randint(0, 14)]
    return [ran1, ran2, ran3]

def true_color(colors):
    """Crée la couleur cible à partir de 3 couleurs et la retourne."""
    t_color = [(colors[0][i] // 2) + (colors[1][i] * 3 // 10) + (colors[2][i] // 5) for i in range(3)]
    return t_color

def verif_color(lst, tc, colors):
    """Vérifie si les couleurs trouvées sont correctes."""
    t_col = [False, False, False]
    b_place = [False, False, False]

    for i in range(3):
        if colors[lst[i]] == tc[i]:
            t_col[i] = True
        elif colors[lst[i]] in tc:
            b_place[i] = True

    return True if t_col == [True, True, True] else (t_col, b_place)

def afficher_couleurs(couleurs, choix_joueur):
    """Affiche les couleurs sous forme de carrés et entoure les couleurs sélectionnées."""
    largeur_case = 70
    espace = 30
    x_debut = 60
    y_debut = 400
    
    for index, couleur in enumerate(couleurs):
        x = x_debut + (index % 5) * (largeur_case + espace)
        y = y_debut + (index // 5) * (largeur_case + espace)
        
        # Entourer le carré si sélectionné
        if index in choix_joueur:
            pygame.draw.rect(screen, WHITE, (x - 3, y - 3, largeur_case + 6, largeur_case + 6))  # Contour blanc
        pygame.draw.rect(screen, couleur, (x, y, largeur_case, largeur_case))

def gestion_clics(couleurs, choix_joueur):
    """Gère les clics sur les carrés de couleurs et met à jour la sélection de l'utilisateur."""
    largeur_case = 70
    espace = 30
    x_debut = 60
    y_debut = 400
    
    # Récupérer la position du clic
    pos = pygame.mouse.get_pos()
    
    for index in range(len(couleurs)):
        x = x_debut + (index % 5) * (largeur_case + espace)
        y = y_debut + (index // 5) * (largeur_case + espace)
        
        # Vérifier si le clic est sur un carré
        rect = pygame.Rect(x, y, largeur_case, largeur_case)
        if rect.collidepoint(pos):
            if index not in choix_joueur:
                choix_joueur.append(index)  # Ajouter la couleur si elle n'est pas déjà sélectionnée
            if len(choix_joueur) > 3:
                choix_joueur.pop(0)  # Limiter le choix à 3 couleurs

def afficher_couleur_cible(couleur):
    """Affiche la couleur cible sous forme de cercle."""
    pygame.draw.circle(screen, couleur, (200, 150), 100)  # Cercle pour la couleur cible

def afficher_historique(essais_restants, historique):
    """Affiche le nombre d'essais restants et l'historique des coups joués."""
    font = pygame.font.Font(None, 36)
    essais_text = font.render(f"Essais restants : {essais_restants}", True, WHITE)
    screen.blit(essais_text, (400, 50))
    
    # Afficher les choix de couleur dans l'historique avec indicateurs de position
    y_offset = 100
    case_taille = 20
    for essai, (choix, t_col, b_place) in enumerate(historique):
        x_offset = 400
        for i, couleur in enumerate(choix):
            # Déterminer la couleur de fond : vert si bien placé, jaune si correct mais mal placé
            fond = GREEN if t_col[i] else YELLOW if b_place[i] else GRAY
            pygame.draw.rect(screen, fond, (x_offset - 3, y_offset - 3, case_taille + 6, case_taille + 6))  # Fond
            pygame.draw.rect(screen, couleur, (x_offset, y_offset, case_taille, case_taille))  # Couleur de l'essai
            x_offset += case_taille + 10
        y_offset += case_taille + 10

def afficher_selection_couleur(choix_joueur, couleurs):
    """Affiche la sélection de couleurs en cours."""
    x_debut = 60
    y_debut = 300
    largeur_case = 40
    espace = 10
    
    for i, index in enumerate(choix_joueur):
        x = x_debut + i * (largeur_case + espace)
        pygame.draw.rect(screen, couleurs[index], (x, y_debut, largeur_case, largeur_case))

def afficher_bouton_retour():
    """Affiche un bouton pour revenir en arrière."""
    font = pygame.font.Font(None, 36)
    texte = font.render("Retour", True, WHITE)
    bouton = pygame.Rect(500, 330, 100, 40)
    pygame.draw.rect(screen, DARK_GRAY, bouton)
    screen.blit(texte, (510, 340))
    return bouton

def afficher_message(message):
    """Affiche un message de fin de partie."""
    font = pygame.font.Font(None, 48)
    text = font.render(message, True, WHITE)
    screen.blit(text, (150, 300))
    pygame.display.flip()
    pygame.time.delay(2000)

def rejouer():
    """Demande au joueur s'il souhaite rejouer."""
    font = pygame.font.Font(None, 36)
    text = font.render("Voulez-vous rejouer ? (O/N)", True, WHITE)
    screen.blit(text, (150, 350))
    pygame.display.flip()
    attendre_reponse = True
    while attendre_reponse:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:  # Oui
                    attendre_reponse = False
                    main()
                elif event.key == pygame.K_n:  # Non
                    pygame.quit()
                    sys.exit()

def main():
    """Génère les couleurs et initialise la liste des choix pour lancer le jeu principal."""
    global essais_max, historique
    essais_restants = essais_max
    historique = []
    couleurs = creer_couleurs()
    choix_joueur = []
    bonnes_couleurs = couleurs_a_trouver(couleurs)
    la_couleur = true_color(bonnes_couleurs)

    # Boucle principale
    running = True
    while running:
        # Appliquer l'arrière-plan du jeu
        screen.blit(background, (0, 0))

        # Afficher la couleur cible en haut sous forme de cercle
        afficher_couleur_cible(la_couleur)

        # Afficher les couleurs disponibles avec les choix du joueur
        afficher_couleurs(couleurs, choix_joueur)

        # Afficher le nombre d'essais restants et l'historique
        afficher_historique(essais_restants, historique)

        # Afficher la sélection de couleurs en cours
        afficher_selection_couleur(choix_joueur, couleurs)

        # Afficher le bouton retour
        bouton_retour = afficher_bouton_retour()

        # Vérifier la sélection si l'utilisateur a choisi 3 couleurs
        if len(choix_joueur) == 3:
            resultat = verif_color(choix_joueur, bonnes_couleurs, couleurs)
            
            # Ajouter le choix à l'historique avec les informations de vérification
            if resultat == True:
                historique.append(([couleurs[i] for i in choix_joueur], [True, True, True], [False, False, False]))
                afficher_message("Vous avez gagné !")
                running = False
            else:
                t_col, b_place = resultat
                historique.append(([couleurs[i] for i in choix_joueur], t_col, b_place))
            
            # Réduire le nombre d'essais restants
            essais_restants -= 1
            choix_joueur.clear()  # Réinitialiser les choix pour permettre de rejouer

            # Vérifier si le joueur a perdu
            if essais_restants == 0 and resultat != True:
                afficher_message("Vous avez perdu.")
                running = False

        # Mettre à jour l'écran
        pygame.display.flip()

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if bouton_retour.collidepoint(pos) and choix_joueur:
                    choix_joueur.pop()  # Retirer la dernière couleur choisie
                else:
                    gestion_clics(couleurs, choix_joueur)  # Gérer la sélection de couleur au clic

    # Proposer de rejouer
    rejouer()

# Lancer le jeu
main()
