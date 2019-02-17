# -*-coding:Latin-1 -*

import pygame
import Constant

background = {'surface': None, 'rect': None}
home_background = {'surface': None, 'rect': None}
pause_background = {'surface': None, 'rect': None}


def load_menu():
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

