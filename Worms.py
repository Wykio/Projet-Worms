# -*-coding:Latin-1 -*
# Auteur: Antoine et Attika

import pygame

import Constant
import EventListener
import Init
import Menu
from Textfield import Textfield

# Initialisation de la fenêtre du jeu
screen = Init.init_game(Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
Menu.init_game()

# Définition des états
game_is_open = True
game_home_screen = True
game_playing_screen = False
game_settings_screen = False
game_pause_screen = False

# Variables pour le calcul de trajectoire
alpha = Constant.GRENADE_ALPHA_ANGLE
v0 = Constant.GRENADE_V0
gravity = Constant.GRAVITY
wind_force = 0
hud = Textfield(None, Constant.BLACK)

# Variables des données liées à la création de partie
player = 2
character = 1
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

while game_is_open:
    # Boucle d'événement
    while game_home_screen:
        EventListener.home_screen()

    while game_settings_screen:
        EventListener.settings_screen()

    while game_playing_screen:
        EventListener.playing_screen()

        # temp
        pygame.time.wait(5)
