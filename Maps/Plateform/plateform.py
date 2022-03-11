import pygame


class Plateform():
    
    def __init__(self, rect):
        super().__init__()
        
        self.rect = rect
        
    def stream(self, surface):
        
        pygame.draw.rect(surface, (0, 255, 0), self.rect)
        
