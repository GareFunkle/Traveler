from turtle import speed
import Data.config as config
from Maps.collision.collision import get_rect
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
        self.is_playing = False
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player()
        self.all_players.add(self.player.sprite)
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
        self.fps = config.FPS
        self.plateform_group = pygame.sprite.Group()
        self.screen_width = screen_width
        self.world_shift = 0


    def start(self):
        self.is_playing = True
        self.spawn_npc()

    def game_over(self):
        # remettre le jeu a neuf, retirer les monstres remmetre le joueurs a 100 point de vie , jeu en attentes
        self.all_monsters = pygame.sprite.Group()
        self.player.current_health = self.player.max_health
        self.is_playing = False

    def update(self, screen):       
# -------------------------- Partie Jeux -----------------------------------------------------------------------------------------------


        # appliquer une limite des FPS
        self.clock.tick(self.fps)

# ----------------------------------------- End ------------------------------------------------------------------------------------------

# -------------------------- Partie Player -----------------------------------------------------------------------------------------------       
       
               # appliquer le sol pour le joueur
        self.sol.afficher(screen)
        if self.sol.rect.colliderect(self.player.rect):
            self.resistance = (0, -10)
            self.collision_sol = True

        else:
            self.resistance = (0, 0)

        if self.player.to_jump and self.collision_sol:
            self.player.move_jump()
            
        # appliquer la gravite pour le joueur et les NPC
        self.gravity_game()
       
        # appliquer limage du joueur
        screen.blit(self.player.sprite.image, self.player.rect)
        
        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)
        
        # actualiser l'animation du joueur
        self.player.sprite.animate()
        


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

        # verifier si le joueur saute 
        if self.pressed.get(pygame.K_SPACE):
            self.player.sprite.status = 'attack'
            
# ---------------------------------------------- End -------------------------------------------------------------------------------------            
            
            
# -------------------------- Partie NPC -----------------------------------------------------------------------------------------------
        
        # actualiser l'animation du monstre
        self.npc.sprite.animate()
        
        # appliquer l'image du npc
        screen.blit(self.npc.sprite.image, self.npc.rect)
        
        # appliquer l'ensemble des images de mon groupe de monstres
        self.all_npc.draw(screen)
        
         # récuperer les monstres de notre jeu
        self.npc.update_health_bar(screen)
            # self.npc.damage()
        # self.forward()
        # self.player.damage(self.player)
        # if not self.check_collision(self, self.all_players):
        #     print("colision")
        self.npc.move_right
        
        # appliquer le sol pour les monstre
        if self.sol.rect.colliderect(self.npc.rect):
            self.resistance = (0, -10)
            self.collision_sol = True

        else:
            self.resistance = (0, 0)
        
            
        
        
# ----------------------------------------- End ------------------------------------------------------------------------------------------
        

    
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(
            sprite, group, False, pygame.sprite.collide_mask
        )
        

    def spawn_npc(self):
        self.all_npc.add(self.npc.sprite)
        # self.all_npc.add(npc_class_name.__call__(self))
        
        
            
        

    def gravity_game(self):
        self.player.rect.y += self.gravity[1] + self.resistance[1]

    def scroll_x(self):
        # if self.player.rect.x + self.player.rect.width < self.screen_width / 4 and self.player.rect.x:
        self.world_shift -= self.player.speed_walk
        self.player.rect.x = self.player.speed_walk
        self.player.rect.x = self.screen_width / 2.30

    # def forward(self):
    #     le deplacement ne se fait qie si il ny a pas de colision avec un groupe de joueur
    #     if not self.check_collision(self, self.all_players):
    #       self.npc.rect.x -= self.npc.speed_walk
    #       self.npc.sprite.status = 'run'
        # si le monstre est en colision avec le joueur
        # else:
        # # infliger des degats au joeur
        #   self.player.damage(self.player)
