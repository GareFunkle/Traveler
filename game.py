from pygame import sprite
from characters.Npc.GeneralNpc.npc import NPC
from characters.Npc.Grec.animate_grec_npc.animate_grec_npc import Grec_Sprite
from characters.Player.AnimatePlayer.animatesprite import Player_Sprite
from characters.Player.player import Player
from Maps.Sol.sol import Sol

# from plateform import Plateform
import pygame


# creer une seconde class
class Game:
    def __init__(self, screen_width=1280):
        # definir si notre jeu a commencer ou non
        self.is_playing = True
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player()
        self.all_players.add()
        # groupe de monstre
        self.npc = NPC()
        self.all_npc = pygame.sprite.Group()
        self.pressed = {}
        # sol et gravite plus colision avec sol
        self.sol = Sol()
        self.gravity = (0, 10)
        self.resistance = (0, 0)
        self.collision_sol = False
        # gestion des fps
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.plateform_group = pygame.sprite.Group()
        self.screen_width = screen_width
        self.world_shift = 0

    def start(self):
        self.is_playing = True
        self.spawn_monster()

    def game_over(self):
        # remettre le jeu a neuf, retirer les monstres remmetre le joueurs a 100 point de vie , jeu en attentes
        self.all_monsters = pygame.sprite.Group()
        self.player.current_health = self.player.max_health
        self.is_playing = False

    def update(self, screen):

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser l'animation du joueur
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
        for npc in self.all_npc:
            npc.update_health_bar(screen)

        # appliquer l'ensemble des images de mon groupe de monstres
        self.all_npc.draw(screen)

        # appliquer limage du joueur
        screen.blit(self.player.sprite.image, self.player.rect)

        # verifier si le joueur souhaite aller a hauche ou a droite
        if self.pressed.get(pygame.K_RIGHT):
            self.player.move_right()
            self.scroll_x()

        if self.pressed.get(pygame.K_LEFT):
            self.player.move_left()
            self.scroll_x()

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

    def spawn_monster(self, npc_class_name):
        self.all_npc.add(npc_class_name.__call__(self))

    def gravity_game(self):
        self.player.rect.y += self.gravity[1] + self.resistance[1]

    def scroll_x(self):
        # if self.player.rect.x + self.player.rect.width < self.screen_width / 4 and self.player.rect.x:
        self.world_shift -= self.player.speed_walk
        self.player.rect.x = self.player.speed_walk
        self.player.rect.x = self.screen_width / 2.30

    # def forward(self):
        # le deplacement ne se fait qie si il ny a pas de colision avec un groupe de joueur
        # if not self.check_collision(self, self.all_players):
        #   self.npc.rect.x -= self.npc.speed_walk
        # si le monstre est en colision avec le joueur
        # else:
        # i,fliger des degat au joeur
        #   self.player.damage(self.attack_damage)
