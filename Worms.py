# -*-coding:Latin-1 -*
# Auteur: Antoine

import pygame, sys

from Asset import Asset
from Textfield import Textfield
from Player import Player
import Constant
import Init
import Menu
import EventListener

def main():

    Menu.init_game()

    while Menu.game_is_open:
        # Boucle d'événement
        while Menu.game_home_screen:
            EventListener.home_screen()

        # Variables des données liées à la création de partie
        player = 2
        character = 1
        clock = pygame.time.Clock()
        counter = 5
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        turn = 1
        player1_turn = True
        player2_turn = False
        player3_turn = False
        player1_character = 1
        player2_character = 1
        player3_character = 1

        while Menu.game_settings_screen:
            EventListener.settings_screen()

        # Variables pour le calcul de trajectoire
        alpha = Constant.GRENADE_ALPHA_ANGLE
        v0 = Constant.GRENADE_V0
        gravity = Constant.GRAVITY
        wind_force = 0
        hud = Textfield(None, Constant.BLACK)

        while Menu.game_playing_screen:
            EventListener.playing_screen()

            # update windforce display
            hud.set_text(
            "[Alpha angle : " + str(alpha) + "][V0 : " + str(v0) + "][Gravity : " + str(round(gravity, 2)) + "][Wind force : " + str(wind_force) + "]",
            Constant.BLACK)
            hud.update(Menu.screen)

            # Update players
            if Menu.player1.life_point:
                Menu.player1.update(Menu.screen, Menu.player2, alpha, v0, gravity, wind_force)
            if Menu.player2.life_point:
                Menu.player2.update(Menu.screen, Menu.player1, alpha, v0, gravity, wind_force)

            # temp
            pygame.time.wait(5)


# call the "main" function if running this script
if __name__ == '__main__': main()
