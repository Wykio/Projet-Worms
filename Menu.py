import pygame
import sys
import Constant
from Player import Player
import Init
from Asset import Asset
from Textfield import Textfield

# Auteurs : Benoit et Attika

# Initialisation de la fenêtre du jeu
screen = Init.init_game(Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)

# Définition des états
game_is_open = True
game_home_screen = True
game_playing_screen = False
game_settings_screen = False
game_pause_screen = False

background = {'surface': None, 'rect': None}
home_background = {'surface': None, 'rect': None}
pause_background = {'surface': None, 'rect': None}

gameSprite = Asset(pygame.image.load("Assets/player_sprite_35x35.gif"))
player1 = Player("Player 1", Constant.RED, gameSprite)
player2 = Player("Player 2", Constant.BLUE, gameSprite)

def init_game():
    screen = Init.init_game(Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
    # x = moitié de l'écran, y de la position du sol - taille du sprite
    player1.set_position(Constant.PLAYER1_START_X, Constant.GROUND_POSITION[1] - 35)
    player2.set_position(Constant.PLAYER2_START_X, Constant.GROUND_POSITION[1] - 35)
    load_game()
    game_is_open = True
    game_home_screen = False
    game_settings_screen = False
    game_playing_screen = True
    game_pause_screen = False

def load_game():
    init_background()
    init_home_background()
    init_pause_background()

def init_background():
    background['surface'] = pygame.image.load("Assets/beach_background.gif")
    background['rect'] = background['surface'].get_rect()

def init_home_background():
    home_background['surface'] = pygame.image.load("Assets/home_background.jpg")
    home_background['rect'] = home_background['surface'].get_rect()

def init_pause_background():
    pause_background['surface'] = pygame.image.load("Assets/pause_background.jpg")
    pause_background['rect'] = pause_background['surface'].get_rect()

def text_objects(text, font):
    text_surface = font.render(text, True, Constant.WHITE)
    return text_surface, text_surface.get_rect()

def button(txt, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1 and action is not None:
            if action == "settings":
                game_home_screen = False
                game_settings_screen = True
            elif action == "play":
                game_settings_screen = False
                game_playing_screen = True
            elif action == "return":
                game_pause_screen = False
            elif action == "home":
                game_playing_screen = False
                game_pause_screen = False
                game_settings_screen = False
                game_home_screen = True
            elif action == "quit":
                Init.quit_game()
                sys.exit()
        else:
            pygame.draw.rect(screen, ic, (x, y, w, h))

        font_text = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        text_surf, text_rect = text_objects(txt, font_text)
        text_rect.center = ((x + (w / 2)), (y + (h / 2)))
        screen.blit(text_surf, text_rect)


