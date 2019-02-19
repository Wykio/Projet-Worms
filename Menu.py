import pygame
import sys
import random
import Constant
from Player import Player
import Init
from Asset import Asset

# Auteurs : Benoit et Attika

background = {'surface': None, 'rect': None}
home_background = {'surface': None, 'rect': None}
pause_background = {'surface': None, 'rect': None}

gameSprite = Asset(pygame.image.load("Assets/player_sprite_35x35.gif"))
player1character1 = Player("Player 1_1", Constant.RED, gameSprite)
player1character2 = Player("Player 1_2", Constant.RED, gameSprite)
player2character1 = Player("Player 2_1", Constant.BLUE, gameSprite)
player2character2 = Player("Player 2_2", Constant.BLUE, gameSprite)
player3character1 = Player("Player 3_1", Constant.GREEN, gameSprite)
player3character2 = Player("Player 3_2", Constant.GREEN, gameSprite)
all_players = {player1character1, player1character2, player2character1,
               player2character2, player3character1, player3character2}

def init_game():
    import Worms
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

def init_characters():
    for j in all_players:
        pos = random.randint(40, 600)
        j.set_position(pos, Constant.GROUND_POSITION[1] - 35)
        j.life_point = 3
    erase_useless_players()
    pygame.display.update()
    pygame.display.flip()

def erase_useless_players():
    import Worms
    if Worms.player == 2:
        player3character1.life_point = 0
        player3character2.life_point = 0
    if Worms.character == 1:
        player1character2.life_point = 0
        player2character2.life_point = 0
        player3character2.life_point = 0

def init_background():
    background['surface'] = pygame.image.load("Assets/beach_background.gif")
    background['rect'] = background['surface'].get_rect()

def init_home_background():
    home_background['surface'] = pygame.image.load("Assets/home_background.jpg")
    home_background['rect'] = home_background['surface'].get_rect()

def init_pause_background():
    pause_background['surface'] = pygame.image.load("Assets/pause_background.jpg")
    pause_background['rect'] = pause_background['surface'].get_rect()

def reset_game():
    import Worms
    from Textfield import Textfield
    init_characters()

    Worms.game_is_open = True
    Worms.game_home_screen = True
    Worms.game_playing_screen = False
    Worms.game_settings_screen = False
    Worms.game_pause_screen = False

    Worms.alpha = Constant.GRENADE_ALPHA_ANGLE
    Worms.v0 = Constant.GRENADE_V0
    Worms.gravity = Constant.GRAVITY
    Worms.wind_force = 0
    Worms.hud = Textfield(None, Constant.BLACK)

    Worms.player = 2
    Worms.character = 1
    Worms.clock = pygame.time.Clock()
    Worms.counter = 21
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    Worms.turn = 1
    Worms.player1_turn = True
    Worms.player2_turn = False
    Worms.player3_turn = False
    Worms.player1_character = 1
    Worms.player2_character = 1
    Worms.player3_character = 1

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
                init_characters()
                Worms.game_playing_screen = True
                Worms.game_settings_screen = False
            elif action == "return":
                Worms.game_pause_screen = False
            elif action == "home":
                reset_game()
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


