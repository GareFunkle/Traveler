

class CanWalk:
    # Must be attached to unit
    def __init__(self, rect, speed_walk=3):
        self.rect = rect
        self.speed_walk = speed_walk

    def move_right(self):
        self.rect.x += self.speed_walk
        self.sprite.facing_right = True
        self.sprite.status = 'run'

    def move_left(self):
        self.rect.x -= self.speed_walk
        self.sprite.facing_right = False
        self.sprite.status = 'run'
