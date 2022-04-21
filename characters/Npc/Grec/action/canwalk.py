import random


class Can_Walk:
    def __init__(self, rect, speed_walk=random.randint(1, 3)):
        self.rect = rect
        self.speed_walk = speed_walk




    def move_left(self):
        self.rect.x -= self.speed_walk
        self.sprite.status = 'run'
        self.sprite.animation_speed = 0.23
        self.sprite.facing_right = True
        self.speed_walk = random.randint(1, 3)
        # self.move_npc()
        
    def move_right(self):
        self.sprite.facing_right = False
        self.speed_walk = random.randint(1, 3)
        self.move_npc()
        
    def move_npc(self):
        self.rect.x += self.speed_walk
        self.sprite.status = 'run'
        self.sprite.animation_speed = 0.23
    