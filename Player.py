# -*-coding:Latin-1 -*
# Auteur: Antoine

import pygame
import Constant
from Asset import Asset
from Textfield import Textfield
from Weapon import Weapon


class Player(Asset, Textfield):
    # On fait l'init de cette maniere pour pouvoir effectuer les methodes héritées ( Asset.print() et Textfield.print())
    def __init__(self, name, color, sprite_sheet):
        self.sprite_sheet = sprite_sheet
        self.surface = sprite_sheet.surface.subsurface(Constant.PLAYER_BODY_RECT1)
        self.rect = self.surface.get_rect()
        self.title = Textfield(name, color)
        self.weapon_select = 0
        self.grenade = Weapon(sprite_sheet.surface.subsurface(Constant.GRENADE_RECT), sprite_sheet.surface.subsurface(Constant.GRENADE_RECT))
        self.looking_left = True
        self.is_shooting = False
        self.animationState = 1;

    def __str__(self):
        return "{ Player: " + str(self.surface) + " | " + str(self.rect) + " ; Title: " + str(self.title) + " }"

    def update(self, screen):
        self.title.rect = self.rect.move(-self.title.rect[2] / 2, -self.title.rect[3])
        screen.blit(self.surface, self.rect)
        screen.blit(self.title.surface, self.title.rect)
        self.update_weapon(screen)
        if self.is_shooting:
            self.update_shot(screen)

    def move_left(self):
        if self.looking_left:
            if self.animationState == 1:
                self.surface = self.sprite_sheet.surface.subsurface(Constant.PLAYER_BODY_RECT2)
                self.animationState = 2
            elif self.animationState == 2:
                self.surface = self.sprite_sheet.surface.subsurface(Constant.PLAYER_BODY_RECT3)
                self.animationState = 3
            else:
                self.surface = self.sprite_sheet.surface.subsurface(Constant.PLAYER_BODY_RECT1)
                self.animationState = 1
            Asset.move_left(self)
        else:
            self.surface = pygame.transform.flip(self.surface, 1, 0)
            self.looking_left = True
            Asset.move_left(self)

    def move_right(self):
        if not self.looking_left:
            if self.animationState == 1:
                self.surface = self.sprite_sheet.surface.subsurface(Constant.PLAYER_BODY_RECT2)
                self.surface = pygame.transform.flip(self.surface, 1, 0)
                self.animationState = 2
            elif self.animationState == 2:
                self.surface = self.sprite_sheet.surface.subsurface(Constant.PLAYER_BODY_RECT3)
                self.surface = pygame.transform.flip(self.surface, 1, 0)
                self.animationState = 3
            else:
                self.surface = self.sprite_sheet.surface.subsurface(Constant.PLAYER_BODY_RECT1)
                self.surface = pygame.transform.flip(self.surface, 1, 0)
                self.animationState = 1
            Asset.move_right(self)
        else:
            self.surface = pygame.transform.flip(self.surface, 1, 0)
            self.looking_left = False
            Asset.move_right(self)

    def select_weapon(self, screen):
        if self.weapon_select == 0:
            self.weapon_select = 1
        else:
            self.weapon_select = 0

    def update_weapon(self, screen):
        if self.weapon_select == 1:
            self.grenade.weapon_set_position(self.rect[0] + 7, self.rect[1] + 15)
            screen.blit(self.grenade.weapon.surface, self.grenade.weapon.rect)

    def shoot(self, screen):
        if self.weapon_select == 1:
            print("shot")
            self.is_shooting = True
            self.grenade.shot_set_position(self.rect[0] + 7, self.rect[1] + 15)

    def update_shot(self, screen):
        if self.weapon_select == 1:
            if self.is_shooting:
                if self.looking_left:
                    self.grenade.shot.move_left()
                else:
                    self.grenade.shot.move_right()
                screen.blit(self.grenade.shot.surface, self.grenade.shot.rect)
                if (self.grenade.shot.rect.right >= Constant.SCREEN_WIDTH) or (self.grenade.shot.rect.left <= 0):
                    self.is_shooting = False
                    print("stop")