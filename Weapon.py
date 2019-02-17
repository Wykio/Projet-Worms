# -*-coding:Latin-1 -*
# Auteur: Antoine
# Modification : Attika

import math
import Constant
from Asset import Asset


class Weapon(Asset):

    def __init__(self, weapon_surface, shot_surface):
        self.weapon = Asset(weapon_surface)
        self.shot = Asset(shot_surface)
        self.is_shooting = False
        self.time = 0.0
        self.x = 0.0
        self.y = 0.0
        self.x0 = 0
        self.y0 = 0

    def update(self, screen, me, other, looking_left, alpha, v0, gravity, wind_force):
        self.update_shot_position(looking_left, alpha, v0, gravity, wind_force)
        self.shot.set_position(int(self.x), int(self.y))
        screen.blit(self.shot.surface, self.shot.rect)
        if (self.shot.rect.right >= Constant.SCREEN_WIDTH) or (self.shot.rect.left <= 0):
            self.is_shooting = False
        if self.shot.rect[1] > Constant.GROUND_LEVEL:
            self.is_shooting = False
        for i in other:
            if self.shot.rect.colliderect(i.rect) and i is not me:
                self.is_shooting = False
                print("hit")
                i.life_point -= 1
            self.time += 0.1

    def update_shot_position(self, looking_left, alpha, v0, gravity, wind_force):
        if looking_left:
            self.x = -v0 * math.cos((alpha * math.pi)/180) * self.time + self.x0
            self.y = -(((gravity / 2) + wind_force) * self.time * self.time) - (
                        v0 * math.sin((alpha * math.pi)/180) * self.time) + self.y0
        else:
            self.x = v0 * math.cos((alpha * math.pi)/180) * self.time + self.x0
            self.y = -(((gravity / 2) + wind_force) * self.time * self.time) - (
                    v0 * math.sin((alpha * math.pi)/180) * self.time) + self.y0

    def weapon_set_position(self, x, y):
        self.weapon.rect[0] = x
        self.weapon.rect[1] = y

    def shot_set_position(self, x, y):
        self.shot.rect[0] = x
        self.shot.rect[1] = y
