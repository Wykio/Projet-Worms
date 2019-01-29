# -*-coding:Latin-1 -*
import pygame
import sys

import Init
import Constant
import Asset
import Animation
import EventListener

# Initialisation de la fenêtre du jeu
screen = Init.init_game(Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)

# Chargement des assets
Init.load_game()

# Statut du jeu
game_is_open = True
game_home = True
game_settings = False
game_playing = False
game_pause = False

while game_is_open:
    while game_home:
        EventListener.game_home()

    while game_settings:
        EventListener.game_settings()

    while game_playing:
        EventListener.game_playing()
