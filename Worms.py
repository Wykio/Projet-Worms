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

# Police d'écriture
comicSansMsFont = pygame.font.SysFont("comicsansms", 20)
consolasFont = pygame.font.SysFont('Consolas', 20)

# Statut du jeu
game_is_open = True
game_home_screen = True
game_settings_screen = False
game_playing_screen = False
game_pause_screen = False

while game_is_open:
    while game_home_screen:
        EventListener.home_screen()

    # Initialisation de donnée lié à la création de partie
    player = 2
    character = 1
    while game_settings_screen:
        EventListener.settings_screen()

    # Initialisation de donnée lié à la partie
    clock = pygame.time.Clock()
    counter = 5
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    turn = 1
    player1_turn = True
    player2_turn = False
    player3_turn = False
    player1_character = 1
    player2_character = 1
    player3_character = 1
    while game_playing_screen:
        EventListener.playing_screen()

