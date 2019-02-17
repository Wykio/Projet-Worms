# -*-coding:Latin-1 -*

import pygame
import Constant


def init_scren_info():
    # Récupérer les informations de l'écran
    screen_info = pygame.display.Info()


def init_game(width, height):
    resolution = (width, height)
    # Initialise le module display de Pygame
    pygame.display.init()
    # Initialise le module font de Pygame
    pygame.font.init()

    # Chargement de l'image de l'icone
    icon = pygame.image.load("Assets/icon.gif")
    # Définition de la couleur de transparence de l'icone
    icon.set_colorkey(Constant.WHITE)
    # Application de l'icone de la fenêtre
    pygame.display.set_icon(icon)

    # Application du nom de la fenêtre
    pygame.display.set_caption("Worms by Attika, Benoit and Antoine")
    # Crée une fenêtre avec la résolution et le double buffer (voir les autres flags) enlever le resizable à la fin
    screen = pygame.display.set_mode(resolution, pygame.DOUBLEBUF | pygame.RESIZABLE)
    # Initialise le temps d'acquisition quand une touche du clavier reste enfoncé
    pygame.key.set_repeat(30, 30)
    # Enleve la souris
    # pygame.mouse.set_visible(0)

    return screen


def quit_game():
    # Décharge de la mémoire le module display de Pygame
    pygame.display.quit()
    pygame.font.quit()

