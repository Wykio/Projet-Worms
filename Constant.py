# -*-coding:Latin-1 -*
# Auteur: Antoine
# Modification : Attika et Beno�t

# format d'�cran de type VGA
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

#D�finition des sprites du menu
MAIN_MENU = 300

# D�finition du Sol
GROUND_LEVEL = 300
GROUND_HEIGHT = SCREEN_HEIGHT - GROUND_LEVEL
GROUND_POSITION = 0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT

# D�finition du sprite du personnage
PLAYER_BODY_RECT1 = 4, 0, 31, 36
PLAYER_BODY_RECT2 = 35, 0, 31, 36
PLAYER_BODY_RECT3 = 67, 0, 31, 36

GRENADE_RECT = 60, 132, 20, 23
BAZOOKA_RECT = 59, 104, 52, 28
ROCKET_RECT = 133, 108, 13, 15

# D�finition de la vitesse
SPEED = [1, 1]
GRAVITY = -9.81

# Couleurs du jeu
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GROUND_COLOR = 191, 128, 64
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

# Position de d�part joueurs
PLAYER1_START_X = 200
PLAYER2_START_X = 400

# Constantes grenade
GRENADE_V0 = 60
GRENADE_ALPHA_ANGLE = 45

