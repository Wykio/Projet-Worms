# -*-coding:Latin-1 -*
import pygame
import sys

import Init
import Constant
import Asset
import Animation
import EventListener

# Initialisation de la fen�tre du jeu
screen = Init.init_game(Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)

# Chargement des assets
Init.load_game()

# Statut du jeu
game_is_open = True
game_home_screen = True
game_settings_screen = False
game_playing_screen = False
game_pause_screen = False

while game_is_open:
    while game_home_screen:
        EventListener.home_screen()

    while game_settings_screen:
        EventListener.settings_screen()

    while game_playing_screen:
        EventListener.playing_screen()

