import pygame
import random
from characters.Npc.Grec.animate_grec_npc.animate_grec_npc import Grec_Sprite
from lib.units.unit_npc import Unit
from characters.Npc.Grec.action.canwalk import Can_Walk
from characters.Npc.Grec.action.canattack import Can_Attack


class NPC(Unit, Can_Walk, Can_Attack):
    def __init__(self):
        Unit.__init__(self, Grec_Sprite(), current_health=100,
                      max_health=100, offset=0)
        Can_Walk.__init__(self, self.rect, speed_walk=random.randint(1, 3))
        Can_Attack.__init__(self, attack_damage=5)
