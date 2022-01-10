import pygame
from lib.player.animatesprite import Player_Sprite
from lib.player.action.CanWalk import CanWalk
from lib.units.unit import Unit
from lib.player.action.canjump import CanJump
from lib.player.action.canattack import CanAttack
from support import import_folder


class Player(Unit, CanWalk, CanJump, CanAttack):
    def __init__(self):
        Unit.__init__(self, Player_Sprite(),
                      current_health=100, max_health=100)
        CanWalk.__init__(self, self.rect, speed_walk=3)
        CanJump.__init__(
            self,
            self.rect,
            jump=0,
            jump_high=0,
            jump_down=5,
            number_jump=0,
            to_jump=False,
        )
        CanAttack.__init__(self, attack_damage=3)

    def animate(self):
        Player_Sprite.animate(self)
