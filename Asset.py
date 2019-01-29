# -*-coding:Latin-1 -*
import pygame

import Constant

background = {'surface': None, 'rect': None}
playerSpriteSheet = {'surface': None, 'rect': None}
player1 = {'surface': None, 'rect': None, 'looking_left': True}
player1_title = {'surface': None, 'rect': None}
player2 = {'surface': None, 'rect': None, 'looking_left': True}
player2_title = {'surface': None, 'rect': None}
grenade = {'surface': None, 'rect': None}
home_background = {'surface': None, 'rect': None}


def init_background():
    background['surface'] = pygame.image.load("Assets/beach_background.gif")
    background['rect'] = background['surface'].get_rect()


def init_home_background():
    home_background['surface'] = pygame.image.load("Assets/home_background.jpg")
    home_background['rect'] = home_background['surface'].get_rect()


# Dessiner les boutons et le texte
def text_objects(text, font):
    textSurface = font.render(text, True, Constant.BLACK)
    return textSurface, textSurface.get_rect()


# Dessiner les boutons et le texte
def button(msg, x, y, w, h, ic, ac, action =  None):
    import sys
    import Worms
    import Init
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(Worms.screen, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            if action == "play":
                Worms.game_home = False
                Worms.game_playing = True
            elif action == "quit":
                Worms.game_home = False
                # Décharge les modules de la mémoire
                Init.quit_game()
                # Quitte le programme
                sys.exit()
            elif action == "return":
                Worms.game_pause = False
    else:
        pygame.draw.rect(Worms.screen, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)) )
    Worms.screen.blit(textSurf, textRect)


def init_playerSpriteSheet():
    # Chargement de l'image sprite du joueur et des armes
    playerSpriteSheet['surface'] = pygame.image.load("Assets/player_sprite_35x35.gif")
    # Définition de la couleur de transparence de l'icone
    playerSpriteSheet['surface'].set_colorkey(Constant.GREEN)
    # Enregistrer [xMin, yMin, xMax, yMax] de la surface "player"
    playerSpriteSheet['rect'] = playerSpriteSheet['surface'].get_rect()


def init_player1():
    player1['surface'] = playerSpriteSheet['surface'].subsurface(Constant.PLAYER_BODY_RECT)
    player1['rect'] = player1['surface'].get_rect()
    # x = moitier de l'écran
    player1['rect'][0] = Constant.PLAYER1_START_X
    # y = y de la position du sol - taille du sprite
    player1['rect'][1] = Constant.GROUND_POSITION[1] - 35


def init_player1_title():
    font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    player1_title['surface'] = font.render('Player 1', False, Constant.RED)
    player1_title['rect'] = player1_title['surface'].get_rect()


def init_player2():
    player2['surface'] = playerSpriteSheet['surface'].subsurface(Constant.PLAYER_BODY_RECT)
    player2['rect'] = player2['surface'].get_rect()
    # x = moitier de l'écran
    player2['rect'][0] = Constant.PLAYER2_START_X
    # y = y de la position du sol - taille du sprite
    player2['rect'][1] = Constant.GROUND_POSITION[1] - 35


def init_player2_title():
    font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    player2_title['surface'] = font.render('Player 2', False, Constant.BLUE)
    player2_title['rect'] = player2_title['surface'].get_rect()

def init_grenade():
    grenade['surface'] = playerSpriteSheet['surface'].subsurface(Constant.PLAYER_BODY_RECT)
