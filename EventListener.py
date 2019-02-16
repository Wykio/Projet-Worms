# Auteurs : Benoît et Attika

import pygame
import sys

import Init
import Worms
import Menu
import Constant

def home_screen():
    # Boucle d'événement
    for event in pygame.event.get():
        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

    Menu.screen.blit(Menu.home_background['surface'], Menu.home_background['rect'])
    Menu.button("Play", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 - 100, 150, 50, Constant.DARK,
                Constant.LIGHT_GREEN, "settings")
    Menu.button("Quit", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 + 50, 150, 50, Constant.DARK_RED,
                Constant.LIGHT_GREEN, "quit")

    pygame.display.update()
    pygame.display.flip()

def settings_screen():
    for event in pygame.event.get():
        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

    Menu.screen.blit(Menu.pause_background['surface'], Menu.pause_background['rect'])
    Menu.button("Start", Constant.SCREEN_WIDTH - 165, Constant.SCREEN_HEIGHT / 2 + 175, 150, 50, Constant.DARK,
                Constant.LIGHT_GREEN, "play")
    Menu.button("Home", Constant.SCREEN_WIDTH - 625, Constant.SCREEN_HEIGHT / 2 + 175, 150, 50, Constant.LIGHT_DARK,
                Constant.LIGHT_GREEN, "home")

    pygame.display.update()
    pygame.display.flip()


def playing_screen():
    for event in pygame.event.get():
        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

        if event.type == pygame.USEREVENT:
            # Contrôle du timer
            if Worms.counter <= 0:
                Worms.counter = 6
                Worms.turn += 1
                if Worms.player == 2:
                    if Worms.player1_turn:
                        Worms.player1_turn = False
                        Worms.player2_turn = True
                    elif Worms.player2_turn:
                        Worms.player1_turn = True
                        Worms.player2_turn = False
                elif Worms.player == 3:
                    if Worms.player1_turn:
                        Worms.player1_turn = False
                        Worms.player2_turn = True
                        Worms.player3_turn = False
                    elif Worms.player2_turn:
                        Worms.player1_turn = False
                        Worms.player2_turn = False
                        Worms.player3_turn = True
                    elif Worms.player3_turn:
                        Worms.player1_turn = True
                        Worms.player2_turn = False
                        Worms.player3_turn = False
            Worms.counter -= 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not Menu.game_pause_screen:
                    Menu.game_pause_screen = True

            if Worms.player1_turn:
                # Gestion des données de calcul de trajectoire
                if event.key == pygame.K_r:
                    Worms.alpha += 1
                if event.key == pygame.K_f:
                    Worms.alpha -= 1
                if event.key == pygame.K_t:
                    Worms.v0 += 1
                if event.key == pygame.K_g:
                    Worms.v0 -= 1
                if event.key == pygame.K_y:
                    Worms.gravity += 1
                if event.key == pygame.K_h:
                    Worms.gravity -= 1
                if event.key == pygame.K_u:
                    Worms.wind_force += 1
                if event.key == pygame.K_j:
                    Worms.wind_force -= 1

                # Gestion des déplacements
                if event.key == pygame.K_a:
                    Menu.player1.move_left()
                if event.key == pygame.K_d:
                    Menu.player1.move_right()

                # Gestion des armes
                if event.key == pygame.K_q:
                    # On change le repeat key temporairement pour pas que ca spam les grenades autant que les déplacements
                    pygame.key.set_repeat(500, 30)
                    Menu.player1.select_weapon(Menu.screen)
                    pygame.key.set_repeat(30, 30)
                if event.key == pygame.K_SPACE:
                    pygame.key.set_repeat(500, 30)
                    Menu.player1.shoot(Menu.screen)
                    pygame.key.set_repeat(30, 30)

            elif Worms.player2_turn:
                # Gestion des données de calcul de trajectoire
                if event.key == pygame.K_r:
                    Worms.alpha += 1
                if event.key == pygame.K_f:
                    Worms.alpha -= 1
                if event.key == pygame.K_t:
                    Worms.v0 += 1
                if event.key == pygame.K_g:
                    Worms.v0 -= 1
                if event.key == pygame.K_y:
                    Worms.gravity += 1
                if event.key == pygame.K_h:
                    Worms.gravity -= 1
                if event.key == pygame.K_u:
                    Worms.wind_force += 1
                if event.key == pygame.K_j:
                    Worms.wind_force -= 1

                # Gestion des déplacements
                if event.key == pygame.K_a:
                    Menu.player2.move_left()
                if event.key == pygame.K_d:
                    Menu.player2.move_right()

                # Gestion des armes
                if event.key == pygame.K_q:
                    # On change le repeat key temporairement pour pas que ca spam les grenades autant que les déplacements
                    pygame.key.set_repeat(500, 30)
                    Menu.player2.select_weapon(Menu.screen)
                    pygame.key.set_repeat(30, 30)
                if event.key == pygame.K_SPACE:
                    pygame.key.set_repeat(500, 30)
                    Menu.player2.shoot(Menu.screen)
                    pygame.key.set_repeat(30, 30)

    while Menu.game_pause_screen:
        pause_screen()

    pygame.draw.rect(Menu.screen, Constant.GROUND_COLOR, Constant.GROUND_POSITION)

    pygame.display.update()
    pygame.display.flip()

    Worms.clock.tick(60)


def pause_screen():
    # Boucle d'événement
    for event in pygame.event.get():
        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

    Menu.screen.blit(Menu.pause_background['surface'], Menu.pause_background['rect'])

    Menu.button("Return", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 - 100, 150, 50, Constant.DARK,
                Constant.LIGHT_GREEN, "return")
    Menu.button("Home", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 - 25, 150, 50, Constant.LIGHT_DARK,
                Constant.LIGHT_GREEN, "home")
    Menu.button("Quit", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 + 50, 150, 50, Constant.DARK_RED,
                Constant.LIGHT_GREEN, "quit")

    pygame.display.update()
    pygame.display.flip()
