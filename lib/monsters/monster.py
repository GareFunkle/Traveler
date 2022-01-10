import pygame
import random
import lib.animation.animation as animation


class Unit:
    def __init__(self, sprite, current_health=100, max_health=100, offset=0):
        self.sprite = sprite
        self.rect = self.sprite.image.get_rect()
        self.rect.x = 1280 + random.randint(0, 300)
        self.rect.y = 250 - offset
        self.current_health = current_health
        self.max_health = max_health
        pass


class Can_Walk:
    def __init__(self, rect, speed_walk=random.randint(1, 3)):
        self.rect = rect
        self.speed_walk = speed_walk
        pass


class Can_Attack:
    def __init__(self, attack_damage=5):
        self.attack_damage = attack_damage
        pass


class NPC(Unit, Can_Walk, Can_Attack):
    def __init__(self):
        Unit.__init__(self, current_health=100, max_health=100, offset=0)
        Can_Walk.__init__(self, self.rect, speed_walk=random.randint(1, 3))
        Can_Attack.__init__(self, attack_damage=5)
        pass

# creer une classe qui va gerer la notion de monstre sur notre jeux


class Monster(animation.AnimateSprite):
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1280 + random.randint(0, 300)
        self.rect.y = 250 - offset
        self.velocity = random.randint(1, 3)
        self.start_animation()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # dessiner la bar de vie
        pygame.draw.rect(
            surface,
            (60, 63, 60),
            [self.rect.x + 10, self.rect.y - 20, self.max_health, 5],
        )
        pygame.draw.rect(
            surface,
            (111, 210, 46),
            [self.rect.x + 10, self.rect.y - 20, self.health, 5],
        )

    def damage(self, amount):
        # infliger les degat
        self.health -= amount
        # verifier si le nouveau nombre de pdv est inferieur ou egal a 0
        if self.health <= 0:
            # reaparetre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

    def forward(self):
        # le deplacement ne se fait qie si il ny a pas de colision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en colision avec le joueur
        else:
            # i,fliger des degat au joeur
            self.game.player.sprite.damage(self.attack)


# definir une class pour chacun des monstre que l'on veux ajouter.
class Gaulois(Monster):
    def __init__(self, game):
        super().__init__(game, "gaulois", (130, 130))


# class Gaulois_Archer(Monster):
# def __init__(self, game):
# super().__init__(game, "gaulois_archer", (130, 130))
