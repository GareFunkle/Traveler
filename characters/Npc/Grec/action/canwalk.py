import random


class Can_Walk:
    def __init__(self, rect, speed_walk=random.randint(1, 3)):
        self.rect = rect
        self.speed_walk = speed_walk
