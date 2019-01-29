# -*-coding:Latin-1 -*

# format d'écran de type VGA
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Définition du Sol
GROUND_HEIGHT = SCREEN_HEIGHT - 300
GROUND_POSITION = 0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT

# Définition du sprite du personnage
PLAYER_BODY_RECT = 0, 0, 35, 35
GRENADE_RECT = 60, 132, 20, 23

# Définition de la vitesse
SPEED = [1, 1]

# Couleurs du jeu
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GROUND_COLOR = 191, 128, 64
GREEN = 0, 255, 0
RED = 255, 0, 0
BLUE = 0, 0, 255
DARK_RED = 200, 0, 0
DARK_GREEN = 0, 200, 0

# Position de départ joueurs
PLAYER1_START_X = 200
PLAYER2_START_X = 400

