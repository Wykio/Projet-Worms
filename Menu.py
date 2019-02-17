import pygame
import sys
import Constant
from Player import Player
import Init
from Asset import Asset

# Auteurs : Benoit et Attika

background = {'surface': None, 'rect': None}
home_background = {'surface': None, 'rect': None}
pause_background = {'surface': None, 'rect': None}

gameSprite = Asset(pygame.image.load("Assets/player_sprite_35x35.gif"))
player1 = Player("Player 1", Constant.RED, gameSprite)
player2 = Player("Player 2", Constant.BLUE, gameSprite)

def init_game():
    import Worms
    # x = moitié de l'écran, y de la position du sol - taille du sprite
    player1.set_position(Constant.PLAYER1_START_X, Constant.GROUND_POSITION[1] - 35)
    player2.set_position(Constant.PLAYER2_START_X, Constant.GROUND_POSITION[1] - 35)
    load_game()
    Worms.game_is_open = True
    Worms.game_home_screen = True
    Worms.game_settings_screen = False
    Worms.game_playing_screen = False
    Worms.game_pause_screen = False

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
    import Worms
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(Worms.screen, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            if action == "settings":
                Worms.game_settings_screen = True
                Worms.game_home_screen = False
            elif action == "play":
                Worms.game_playing_screen = True
                Worms.game_settings_screen = False
            elif action == "return":
                Worms.game_pause_screen = False
            elif action == "home":
                Worms.game_home_screen = True
                Worms.game_playing_screen = False
                Worms.game_pause_screen = False
                Worms.game_settings_screen = False
            elif action == "quit":
                Init.quit_game()
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

    font_text = pygame.font.SysFont(pygame.font.get_default_font(), 20)
    text_surf, text_rect = text_objects(txt, font_text)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    Worms.screen.blit(text_surf, text_rect)


