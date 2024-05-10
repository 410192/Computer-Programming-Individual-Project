import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de la fenêtre
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960

# Chargement des images
key_image = pygame.image.load('Key.png')
key_image = pygame.transform.scale(key_image, (32, 32))
start_screen_image = pygame.image.load('start_screen.png')
maze_path_image = pygame.image.load('Path.png')  # Charger l'image du chemin du labyrinthe
maze_wall_image = pygame.image.load('Wall.png')  # Charger l'image des murs du labyrinthe
player_image = pygame.image.load('player.png')  # Charger l'image du joueur
win_image = pygame.image.load('WinScreen.png')
end_image = pygame.image.load('End.png')
door_image = pygame.image.load('Door.png') 
# Création de la classe Player
key_collected = False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image  # Utiliser l'image chargée pour le joueur
        self.rect = self.image.get_rect()
        self.rect.midtop = (SCREEN_WIDTH // 2 - 60, 0)
        self.speed = 5  # Vitesse initiale du joueur

    def update(self, keys):
        global key_collected  # Utiliser la variable globale key_collected

        # Déplacement du joueur en fonction des touches appuyées
        if self.collides_with_key():
            key_collected = True

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

        # Vérifier les collisions avec les murs du labyrinthe
        if self.collides_with_wall():
            # Si le joueur entre en collision avec un mur, annuler le mouvement
            self.rect.x -= move_x
            self.rect.y -= move_y

        # Vérifier si le joueur possède la clé et entre en contact avec la porte
        if key_collected and self.collides_with_door():
            # Si le joueur a la clé et entre en contact avec la porte, supprimer la porte
            door_rect.x = -1000  # Déplacer la porte en dehors de l'écran

    def collides_with_wall(self):
        # Créer les masques de collision pour le joueur et les murs
        player_mask = pygame.mask.from_surface(self.image)
        maze_wall_mask = pygame.mask.from_surface(maze_wall_image)

        # Obtenir les offsets pour le masque du mur
        offset_x = self.rect.x - maze_wall_rect.x
        offset_y = self.rect.y - maze_wall_rect.y

        # Vérifier si les masques se chevauchent
        overlap = maze_wall_mask.overlap(player_mask, (offset_x, offset_y))

        return bool(overlap)

    def collides_with_key(self):
        if not key_collected:
            player_mask = pygame.mask.from_surface(self.image)
            key_mask = pygame.mask.from_surface(key_image)

            offset_x = self.rect.x - key_rect.x
            offset_y = self.rect.y - key_rect.y

            overlap = key_mask.overlap(player_mask, (offset_x, offset_y))

            return bool(overlap)
        return False

    def collides_with_end(self):
        # Créer les masques de collision pour le joueur et les murs
        player_mask = pygame.mask.from_surface(self.image)
        end_mask = pygame.mask.from_surface(end_image)

        # Obtenir les offsets pour le masque du mur
        offset_x = self.rect.x - end_rect.x
        offset_y = self.rect.y - end_rect.y

        # Vérifier si les masques se chevauchent
        overlap = end_mask.overlap(player_mask, (offset_x, offset_y))

        return bool(overlap)

    def collides_with_door(self):
    # Créer les masques de collision pour le joueur et la porte
        player_mask = pygame.mask.from_surface(self.image)
        door_mask = pygame.mask.from_surface(door_image)

        # Obtenir les offsets pour le masque de la porte
        offset_x = self.rect.x - door_rect.x
        offset_y = self.rect.y - door_rect.y

    # Vérifier si les masques se chevauchent et si le joueur possède la clé
        if key_collected:
            overlap = door_mask.overlap(player_mask, (offset_x, offset_y))
            return bool(overlap)
        else:
            return False


# Fonction pour afficher l'écran de démarrage
def show_start_screen():
    screen.blit(start_screen_image, (0, 0))
    pygame.display.flip()

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Labyrinthe")

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

# Obtention des coordonnées du rectangle entourant le mur du labyrinthe
maze_wall_rect = maze_wall_image.get_rect()
end_rect = end_image.get_rect()
key_rect = key_image.get_rect()
key_rect.topleft = (30, SCREEN_HEIGHT - key_rect.height - 20)   
door_rect = door_image.get_rect()
door_rect.bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Création du joueur
player = Player()

# Boucle principale du jeu (labyrinthe)
running = True
while running:
    keys = pygame.key.get_pressed()  # Récupérer les touches appuyées
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour du joueur en fonction des touches appuyées et des collisions avec les murs
    player.update(keys)

    # Effacement de l'écran
    screen.fill((255, 255, 255))

    # Affichage de l'image du chemin du labyrinthe
    screen.blit(maze_path_image, (0, 0))

    # Affichage de l'image des murs du labyrinthe
    screen.blit(maze_wall_image, maze_wall_rect)

    # Affichage de l'image de la fin du labyrinthe
    screen.blit(end_image, end_rect)

    # Affichage de la porte
    screen.blit(door_image, door_rect)

    # Affichage du joueur
    screen.blit(player.image, player.rect)

    # Affichage de la clé si elle n'a pas encore été ramassée
    if not key_collected:
        screen.blit(key_image, key_rect)

    # Rafraîchissement de l'écran
    pygame.display.flip()

pygame.quit()
