

class CanWalk:
    # Must be attached to unit
    def __init__(self, rect, speed_walk=3):
        self.rect = rect
        self.speed_walk = speed_walk
        self.position = 0

    def move_right(self):
        self.sprite.facing_right = True
        self.speed_walk = 3
        self.move()
        print(self.position)

    def move_left(self):
        self.sprite.facing_right = False
        self.speed_walk = -3
        self.move()
        print(self.position)

    def move(self):
        self.rect.x += self.speed_walk
        self.sprite.status = 'run'
        self.sprite.animation_speed = 0.23
