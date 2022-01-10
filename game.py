from pygame import sprite
from lib.player.animatesprite import Player_Sprite
from lib.player.player import Player
from lib.monsters.monster import Gaulois
from lib.sol.sol import Sol

# from plateform import Plateform
import pygame


# creer une seconde class
class Game:
    def __init__(self, screen_width=1280):
        # definir si notre jeu a commencer ou non
        self.is_playing = False
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player()
        self.all_players.add()
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        # sol et gravite plus colision avec sol
        self.sol = Sol()
        self.gravity = (0, 10)
        self.resistance = (0, 0)
        self.collision_sol = False
        # gestion des fps
        self.clock = pygame.time.Clock()
        self.fps = 90
        self.plateform_group = pygame.sprite.Group()
        self.screen_width = screen_width
        self.world_shift = 0

    def start(self):
        self.is_playing = True
        self.spawn_monster(Gaulois)

    def game_over(self):
        # remettre le jeu a neuf, retirer les monstres remmetre le joueurs a 100 point de vie , jeu en attentes
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):

        self.scroll_x()

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser lanimation du joueur
        self.player.sprite.animate()

        # appliquer le sol pour le joueur et les monstres
        self.sol.afficher(screen)
        if self.sol.rect.colliderect(self.player.rect):
            self.resistance = (0, -10)
            self.collision_sol = True

        else:
            self.resistance = (0, 0)

        if self.player.to_jump and self.collision_sol:
            self.player.move_jump()

        # appliquer la gravite
        self.gravity_game()

        # appliquer une limite des FPS
        self.clock.tick(self.fps)

        # récuperer les monstres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # appliquer l'ensemble des images de mon groupe de monstres
        self.all_monsters.draw(screen)

        # appliquer limage du joueur
        screen.blit(self.player.sprite.image, self.player.rect)

        # verifier si le joueur souhaite aller a hauche ou a droite
        if self.pressed.get(pygame.K_RIGHT):
            # and self.player.rect.x + self.player.rect.width < screen.get_width()):
            self.player.move_right()

        if self.pressed.get(pygame.K_LEFT):
            self.player.move_left()

        # verifier si le joueur saute
        if self.pressed.get(pygame.K_UP):
            self.player.to_jump = True
            self.player.number_jump += 1

        if self.pressed.get(pygame.K_SPACE):
            self.player.sprite.status = 'attack'

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(
            sprite, group, False, pygame.sprite.collide_mask
        )

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))

    def gravity_game(self):
        self.player.rect.y += self.gravity[1] + self.resistance[1]

    def scroll_x(self):
        player = self.player.sprite
        player_x = self.player.rect.x + self.player.rect.width
        direction_x = self.player.rect.x

        if player_x < self.screen_width / 4 and direction_x < 0:
            self.world_shift += 1
            player.speed_walk = 0

        elif player_x > self.screen_width - (self.screen_width / 4) and direction_x > 0:
            self.world_shift -= 1
            player.speed_walk = 0

        else:
            self.world_shift = 0
            player.speed_walk = 3
