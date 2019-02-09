# -*-coding:Latin-1 -*
# Auteur: Antoine

import Constant
from Asset import Asset


class Weapon(Asset):

    def __init__(self, weapon_surface, shot_surface):
        self.weapon = Asset(weapon_surface)
        self.shot = Asset(shot_surface)

    def weapon_set_position(self, x, y):
        self.weapon.rect[0] = x
        self.weapon.rect[1] = y

    def shot_set_position(self, x, y):
        self.shot.rect[0] = x
        self.shot.rect[1] = y