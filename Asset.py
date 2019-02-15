# -*-coding:Latin-1 -*
import pygame

import Constant

background = {'surface': None, 'rect': None}
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

grenade = {'surface': None, 'rect': None}
home_background = {'surface': None, 'rect': None}
pause_background = {'surface': None, 'rect': None}


def init_background():
    background['surface'] = pygame.image.load("Assets/beach_background.gif")
    background['rect'] = background['surface'].get_rect()


def init_home_background():
    home_background['surface'] = pygame.image.load("Assets/home_background.jpg")
    home_background['rect'] = home_background['surface'].get_rect()


def init_pause_background():
    pause_background['surface'] = pygame.image.load("Assets/pause_background.jpg")
    pause_background['rect'] = pause_background['surface'].get_rect()


# Affichage du texte
def text_objects(text, font):
    textSurface = font.render(text, True, Constant.WHITE)
    return textSurface, textSurface.get_rect()


# Dessiner les boutons et le texte
def button(msg, x, y, w, h, ic, ac, action=None):
    import sys
    import Worms
    import Init

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(Worms.screen, ac, (x, y, w, h))

        if click[0] == 1 and action is not None:
            if action == "settings":
                Worms.game_home_screen = False
                Worms.game_settings_screen = True
            elif action == "play":
                Worms.game_settings_screen = False
                Worms.game_playing_screen = True
            elif action == "return":
                Worms.game_pause_screen = False
            elif action == "home":
                Worms.game_playing_screen = False
                Worms.game_pause_screen = False
                Worms.game_settings_screen = False
                Worms.game_home_screen = True
            elif action == "quit":
                # Décharge les modules de la mémoire
                Init.quit_game()
                # Quitte le programme
                sys.exit()
            elif action == "2 players":
                Worms.player = 2
            elif action == "3 players":
                Worms.player = 3
            elif action == "1 character":
                Worms.character = 1
            elif action == "2 characters":
                Worms.character = 2
            elif action == "joueur 1 personnage 1":
                Worms.player1_character = 1
            elif action == "joueur 1 personnage 2":
                Worms.player1_character = 2
            elif action == "joueur 2 personnage 1":
                Worms.player2_character = 1
            elif action == "joueur 2 personnage 2":
                Worms.player2_character = 2
            elif action == "joueur 3 personnage 1":
                Worms.player3_character = 1
            elif action == "joueur 3 personnage 2":
                Worms.player3_character = 2
    else:
        pygame.draw.rect(Worms.screen, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    Worms.screen.blit(textSurf, textRect)


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


def init_grenade():
    grenade['surface'] = playerSpriteSheet['surface'].subsurface(Constant.PLAYER_BODY_RECT)

