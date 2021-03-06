# -*-coding:Latin-1 -*
# Auteur : Antoine

import pygame
import Asset
import Constant


def init_game(width, height):
    resolution = (width, height)
    # Initialise le module display de Pygame
    pygame.display.init()
    # Initialise le module font de Pygame
    pygame.font.init()

    # Chargement de l'image de l'icone
    icon = pygame.image.load("Assets/icon.gif")
    # D�finition de la couleur de transparence de l'icone
    icon.set_colorkey(Constant.WHITE)
    # Application de l'icone de la fen�tre
    pygame.display.set_icon(icon)

    # Application du nom de la fen�tre
    pygame.display.set_caption("Worms by Attika, Benoit and Antoine")
    # Cr�e une fen�tre avec la r�solution et le double buffer (voir les autres flags) enlever le resizable � la fin
    screen = pygame.display.set_mode(resolution, pygame.DOUBLEBUF | pygame.RESIZABLE)
    # Initialise le temps d'acquisition quand une touche du clavier reste enfonc�
    pygame.key.set_repeat(30, 30)
    # Enleve la souris
    # pygame.mouse.set_visible(0)

    return screen


def quit_game():
    # D�charge de la m�moire le module display de Pygame
    pygame.display.quit()
    pygame.font.quit()
