# -*-coding:Latin-1 -*

import random

# Format d'�cran de type VGA
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# D�finition du Sol
GROUND_HEIGHT = SCREEN_HEIGHT - 300
GROUND_POSITION = 0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT

# D�finition du sprite du personnage
PLAYER_BODY_RECT = 0, 0, 35, 35
GRENADE_RECT = 60, 132, 20, 23

# D�finition de la vitesse
SPEED = [1, 1]

# Couleurs du jeu
GROUND_COLOR = 191, 128, 64
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREEN = 0, 255, 0
DARK_GREEN = 0, 200, 0
RED = 255, 0, 0
DARK_RED = 200, 0, 0
BLUE = 0, 0, 255
DARK_BLUE = 0, 0, 200
DARK = 27, 28, 35
LIGHT_DARK = 94, 97, 112
LIGHT_GREEN = 43, 187, 173
INDIGO = 81, 45, 168

# Position de d�part des personnages des joueurs
player_location = random.randint(40, 600)
PLAYER1_CHARACTER1_START_X = player_location

player_location = random.randint(40, 600)
PLAYER1_CHARACTER2_START_X = player_location

player_location = random.randint(40, 600)
PLAYER2_CHARACTER1_START_X = player_location

player_location = random.randint(40, 600)
PLAYER2_CHARACTER2_START_X = player_location

player_location = random.randint(40, 600)
PLAYER3_CHARACTER1_START_X = player_location

player_location = random.randint(40, 600)
PLAYER3_CHARACTER2_START_X = player_location

