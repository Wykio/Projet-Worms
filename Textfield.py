# -*-coding:Latin-1 -*
# Auteur: Antoine

import pygame
import Constant


class Textfield:
    def __init__(self, title, color):
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
        self.surface = self.font.render(title, False, color)
        self.rect = self.surface.get_rect()

    def __str__(self):
        return "{ " + str(self.surface) + " : " + str(self.rect) + " }"

    def update(self, screen):
        screen.blit(self.surface, self.rect)

    def set_text(self, text, color):
        self.surface = self.font.render(text, False, color)

    def set_position(self, x, y):
        self.rect[0] = x
        self.rect[1] = y