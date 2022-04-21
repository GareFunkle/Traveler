import pygame
from characters.Player.AnimatePlayer.animatesprite import Player_Sprite
from characters.Player.action.CanWalk import CanWalk
from lib.units.unit import Unit
from characters.Player.action.canjump import CanJump
from characters.Player.action.canattack import CanAttack
from Support_Animation.support import import_folder


class Player(Unit, CanWalk, CanJump, CanAttack):
    def __init__(self):
        Unit.__init__(self, Player_Sprite(),
                      current_health=100, max_health=100)
        CanWalk.__init__(self, self.rect, speed_walk=3, speed_run=5)
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
