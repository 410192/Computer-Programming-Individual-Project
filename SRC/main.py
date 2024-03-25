import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de la fenêtre
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

# Chargement des images
start_screen_image = pygame.image.load('start_screen.png')
maze_image = pygame.image.load('Maze1.png')

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Labyrinthe")

# Fonction pour afficher l'écran de démarrage
def show_start_screen():
    screen.blit(start_screen_image, (0, 0))
    pygame.display.flip()

# Boucle principale du jeu
show_start_screen()
waiting_for_click = True
while waiting_for_click:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            waiting_for_click = False

# Boucle principale du jeu (labyrinthe)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacement de l'écran
    screen.fill((255, 255, 255))

    # Affichage de l'image du labyrinthe
    screen.blit(maze_image, (0, 0))

    # Rafraîchissement de l'écran
    pygame.display.flip()

pygame.quit()