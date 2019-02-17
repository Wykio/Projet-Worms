# -*-coding:Latin-1 -*

import pygame
import Constant


class Asset:

    def __init__(self, surface):
        self.surface = surface
        self.surface.set_colorkey(Constant.GREEN)
        self.rect = self.surface.get_rect()

    def __str__(self):
        return "{ " + str(self.surface) + " : " + str(self.rect) + " }"

    def set_position(self, x, y):
        self.rect[0] = x
        self.rect[1] = y

    def update(self, screen):
        screen.blit(self.surface, self.rect)

    def move_left(self):
        if self.rect.left > 0:
            self.rect = self.rect.move([-1, 0])

    def move_right(self):
        if self.rect.right < Constant.SCREEN_WIDTH:
            self.rect = self.rect.move([1, 0])

    def move(self, x, y):
        if (self.rect.right < Constant.SCREEN_WIDTH) and (self.rect.left > 0):
            self.rect = self.rect.move([x, y])

