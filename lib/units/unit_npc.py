import pygame
import random
from pygame.draw import rect


class Unit:
    def __init__(self, sprite, current_health=100, max_health=100, offset=0):
        self.sprite = sprite
        self.rect = self.sprite.image.get_rect()
        self.rect.x = 1280 + random.randint(0, 300)
        self.rect.y = 250 - offset
        self.current_health = current_health
        self.max_health = max_health

    def get_rect(self):
        self.sprite.get_rect()

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
        self.current_health -= amount
        # verifier si le nouveau nombre de pdv est inferieur ou egal a 0
        if self.current_health <= 0:
            # reaparetre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.speed_walk = random.randint(1, 3)
            self.current_health = self.max_health
