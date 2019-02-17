# -*-coding:Latin-1 -*

import pygame
import Constant

playerSpriteSheet = {'surface': None, 'rect': None}

player1Character1 = {'surface': None, 'rect': None, 'looking_left': True}
player1_character1_title = {'surface': None, 'rect': None}
player1Character2 = {'surface': None, 'rect': None, 'looking_left': True}
player1_character2_title = {'surface': None, 'rect': None}

player2Character1 = {'surface': None, 'rect': None, 'looking_left': True}
player2_character1_title = {'surface': None, 'rect': None}
player2Character2 = {'surface': None, 'rect': None, 'looking_left': True}
player2_character2_title = {'surface': None, 'rect': None}

player3Character1 = {'surface': None, 'rect': None, 'looking_left': True}
player3_character1_title = {'surface': None, 'rect': None}
player3Character2 = {'surface': None, 'rect': None, 'looking_left': True}
player3_character2_title = {'surface': None, 'rect': None}


def load_player_asset():
    init_playerSpriteSheet()

    init_player1_character1()
    init_player1_character1_title()
    init_player1_character2()
    init_player1_character2_title()

    init_player2_character1()
    init_player2_character1_title()
    init_player2_character2()
    init_player2_character2_title()

    init_player3_character1()
    init_player3_character1_title()
    init_player3_character2()
    init_player3_character2_title()


def init_playerSpriteSheet():
    # Chargement de l'image sprite du joueur et des armes
    playerSpriteSheet['surface'] = pygame.image.load("Assets/player_sprite_35x35.gif")
    # Définition de la couleur de transparence de l'icone
    playerSpriteSheet['surface'].set_colorkey(Constant.GREEN)
    # Enregistrer [xMin, yMin, xMax, yMax] de la surface "player"
    playerSpriteSheet['rect'] = playerSpriteSheet['surface'].get_rect()


def init_player1_character1():
    player1Character1['surface'] = playerSpriteSheet['surface'].subsurface(Constant.PLAYER_BODY_RECT)
    player1Character1['rect'] = player1Character1['surface'].get_rect()
    # x = moitier de l'écran
    player1Character1['rect'][0] = Constant.PLAYER1_CHARACTER1_START_X
    # y = y de la position du sol - taille du sprite
    player1Character1['rect'][1] = Constant.GROUND_POSITION[1] - 35


def init_player1_character1_title():
    font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    player1_character1_title['surface'] = font.render('Player 1', False, Constant.RED)
    player1_character1_title['rect'] = player1_character1_title['surface'].get_rect()


def init_player1_character2():
    player1Character2['surface'] = playerSpriteSheet['surface'].subsurface(Constant.PLAYER_BODY_RECT)
    player1Character2['rect'] = player1Character2['surface'].get_rect()
    # x = moitier de l'écran
    player1Character2['rect'][0] = Constant.PLAYER1_CHARACTER2_START_X
    # y = y de la position du sol - taille du sprite
    player1Character2['rect'][1] = Constant.GROUND_POSITION[1] - 35


def init_player1_character2_title():
    font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    player1_character2_title['surface'] = font.render('Player 1', False, Constant.RED)
    player1_character2_title['rect'] = player1_character2_title['surface'].get_rect()


def init_player2_character1():
    player2Character1['surface'] = playerSpriteSheet['surface'].subsurface(Constant.PLAYER_BODY_RECT)
    player2Character1['rect'] = player2Character1['surface'].get_rect()
    # x = moitier de l'écran
    player2Character1['rect'][0] = Constant.PLAYER2_CHARACTER1_START_X
    # y = y de la position du sol - taille du sprite
    player2Character1['rect'][1] = Constant.GROUND_POSITION[1] - 35


def init_player2_character1_title():
    font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    player2_character1_title['surface'] = font.render('Player 2', False, Constant.BLUE)
    player2_character1_title['rect'] = player2_character1_title['surface'].get_rect()


def init_player2_character2():
    player2Character2['surface'] = playerSpriteSheet['surface'].subsurface(Constant.PLAYER_BODY_RECT)
    player2Character2['rect'] = player2Character2['surface'].get_rect()
    # x = moitier de l'écran
    player2Character2['rect'][0] = Constant.PLAYER2_CHARACTER2_START_X
    # y = y de la position du sol - taille du sprite
    player2Character2['rect'][1] = Constant.GROUND_POSITION[1] - 35


def init_player2_character2_title():
    font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    player2_character2_title['surface'] = font.render('Player 2', False, Constant.BLUE)
    player2_character2_title['rect'] = player2_character2_title['surface'].get_rect()


def init_player3_character1():
    player3Character1['surface'] = playerSpriteSheet['surface'].subsurface(Constant.PLAYER_BODY_RECT)
    player3Character1['rect'] = player3Character1['surface'].get_rect()
    # x = moitier de l'écran
    player3Character1['rect'][0] = Constant.PLAYER3_CHARACTER1_START_X
    # y = y de la position du sol - taille du sprite
    player3Character1['rect'][1] = Constant.GROUND_POSITION[1] - 35


def init_player3_character1_title():
    font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    player3_character1_title['surface'] = font.render('Player 3', False, Constant.GREEN)
    player3_character1_title['rect'] = player3_character1_title['surface'].get_rect()


def init_player3_character2():
    player3Character2['surface'] = playerSpriteSheet['surface'].subsurface(Constant.PLAYER_BODY_RECT)
    player3Character2['rect'] = player3Character2['surface'].get_rect()
    # x = moitier de l'écran
    player3Character2['rect'][0] = Constant.PLAYER3_CHARACTER2_START_X
    # y = y de la position du sol - taille du sprite
    player3Character2['rect'][1] = Constant.GROUND_POSITION[1] - 35


def init_player3_character2_title():
    font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    player3_character2_title['surface'] = font.render('Player 3', False, Constant.GREEN)
    player3_character2_title['rect'] = player3_character2_title['surface'].get_rect()

