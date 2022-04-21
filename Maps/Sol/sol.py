import pygame


class Sol(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 360, 5120, 10)

    def afficher(self, surface):
        # pygame.draw.rect(surface, (255, 255, 255), self.rect)
        pygame.draw.rect(surface, [255, 255, 255], [0, 0, 0, 180], 1)
