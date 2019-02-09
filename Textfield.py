# -*-coding:Latin-1 -*
# Auteur: Antoine

import pygame
import Constant


class Textfield:
    def __init__(self, title, color):
        font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
        self.surface = font.render(title, False, color)
        self.rect = self.surface.get_rect()

    def __str__(self):
        return "{ " + str(self.surface) + " : " + str(self.rect) + " }"

    def update(self, screen):
        screen.blit(self.surface, self.rect)


