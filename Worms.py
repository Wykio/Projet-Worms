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
game_home_screen = True
game_settings_screen = False
game_playing_screen = False
game_pause_screen = False

while game_is_open:
    while game_home_screen:
        EventListener.home_screen()

    while game_settings_screen:
        EventListener.settings_screen()

    # Initialisation de donnée lié à la partie
    clock = pygame.time.Clock()
    counter = 5
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    turn = 0
    player1_turn = True
    player2_turn = False
    while game_playing_screen:
        EventListener.playing_screen()

