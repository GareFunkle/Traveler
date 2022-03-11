import pygame
from pygame import surface
from pygame.draw import rect


class Unit:
    def __init__(self, sprite, current_health=100, max_health=100):
        self.sprite = sprite

        self.rect = self.sprite.image.get_rect()

        self.rect.x = 570
        self.rect.y = 0
        self.current_health = current_health
        self.max_health = max_health

    def get_rect(self):
        self.sprite.get_rect()

    def damage(self, amount):
        self.current_health -= amount

    def update_health_bar(self, surface):
        # dessiner la bar de vie
        pygame.draw.rect(
            surface,
            (60, 63, 60),
            [self.rect.x + 20, self.rect.y - 20, self.max_health, 7],
        )
        pygame.draw.rect(
            surface,
            (111, 210, 46),
            [self.rect.x + 20, self.rect.y - 20, self.current_health, 7],
        )
