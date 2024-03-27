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
player_image = pygame.image.load('player.png')  # Charger l'image du joueur

# Création de la classe Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image  # Utiliser l'image chargée pour le joueur
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 1  # Vitesse initiale du joueur

    def update(self, keys):
        # Déplacement du joueur en fonction des touches appuyées
        move_x = 0
        move_y = 0

        if keys[pygame.K_UP]:
            move_y -= self.speed
        if keys[pygame.K_DOWN]:
            move_y += self.speed
        if keys[pygame.K_LEFT]:
            move_x -= self.speed
        if keys[pygame.K_RIGHT]:
            move_x += self.speed

        # Vérifier les collisions avec les bords de l'écran
        if self.rect.left + move_x >= 0 and self.rect.right + move_x <= SCREEN_WIDTH:
            self.rect.x += move_x
        if self.rect.top + move_y >= 0 and self.rect.bottom + move_y <= SCREEN_HEIGHT:
            self.rect.y += move_y



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

# Création du joueur
player = Player()

# Boucle principale du jeu (labyrinthe)
running = True
while running:
    keys = pygame.key.get_pressed()  # Récupérer les touches appuyées
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour du joueur en fonction des touches appuyées
    player.update(keys)

    # Effacement de l'écran
    screen.fill((255, 255, 255))

    # Affichage de l'image du labyrinthe
    screen.blit(maze_image, (0, 0))

    # Affichage du joueur
    screen.blit(player.image, player.rect)

    # Rafraîchissement de l'écran
    pygame.display.flip()

pygame.quit()
