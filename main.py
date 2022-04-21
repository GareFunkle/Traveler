import pygame
import math
from pygame import sprite
from game import Game
import Data.data as data
from pygame.constants import KEYDOWN


pygame.init()


# generer la fenetre de notre jeu
pygame.display.set_caption(data.GAME_NAME)
screen = pygame.display.set_mode((1280, 720))


# importer de charger l'arriere plan
background = pygame.image.load(data.BACKGROUND)
background2 = pygame.image.load(data.BACKGROUND2)

# importer ou charger notre banniere
banner = pygame.image.load(data.BANNER)
banner = pygame.transform.scale(banner, (500, 550))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.60)

# import chatger notre bouton pour lancer la partie
play_button = pygame.image.load(data.PLAY_BUTTON)
play_button = pygame.transform.scale(play_button, (300, 300))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.80)
play_button_rect.y = math.ceil(screen.get_height() / 1.80)

x_background = 0
# chargement du jeux
game = Game()

running = True

# boucle tant que cette condition est vrai
while running:

    x_background = game.world_shift

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (x_background, 0))
    screen.blit(background2, (x_background+5120, 0))
    screen.blit(background2, (x_background-5120, 0))
    screen.blit(background, (x_background+10240, 0))

    # verifier si notre jeu a commencer ou non
    if game.is_playing:
        # declancher les instruction de la partie
        game.update(screen)
    # verifier si notre jeu na pas commencer
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre a jour l'ecran
    pygame.display.flip()

    # verifier si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # pour verifier que levent et fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.player.sprite.status = 'idle'
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier si notre souris est en colision avec notre bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                game.start()
