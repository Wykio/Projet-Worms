# Auteurs : Benoît et Attika

import pygame
import sys

import Init
import Menu
import Constant

def home_screen():
    import Worms
    # Boucle d'événement
    for event in pygame.event.get():
        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

    Worms.screen.blit(Menu.home_background['surface'], Menu.home_background['rect'])
    Menu.button("Play", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 - 100, 150, 50, Constant.DARK,
                Constant.LIGHT_GREEN, "settings")
    Menu.button("Quit", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 + 50, 150, 50, Constant.DARK_RED,
                Constant.LIGHT_GREEN, "quit")

    pygame.display.update()
    pygame.display.flip()

def settings_screen():
    import Worms
    for event in pygame.event.get():
        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

    Worms.screen.blit(Menu.pause_background['surface'], Menu.pause_background['rect'])
    Menu.button("Start", Constant.SCREEN_WIDTH - 165, Constant.SCREEN_HEIGHT / 2 + 175, 150, 50, Constant.DARK,
                Constant.LIGHT_GREEN, "play")
    Menu.button("Home", Constant.SCREEN_WIDTH - 625, Constant.SCREEN_HEIGHT / 2 + 175, 150, 50, Constant.LIGHT_DARK,
                Constant.LIGHT_GREEN, "home")

    Worms.screen.blit(
        pygame.font.SysFont(pygame.font.get_default_font(), 20).render("Nombre de joueurs", True, Constant.WHITE),
        (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 450))
    if Worms.player == 2:
        Menu.button("2", Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.INDIGO,
                    Constant. LIGHT_GREEN, "2 players")
        Menu.button("3", Constant.SCREEN_WIDTH - 550, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.DARK,
                    Constant. LIGHT_GREEN, "3 players")
    elif Worms.player == 3:
        Menu.button("2", Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.DARK,
                    Constant.LIGHT_GREEN, "2 players")
        Menu.button("3", Constant.SCREEN_WIDTH - 550, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.INDIGO,
                    Constant.LIGHT_GREEN, "3 players")

    Worms.screen.blit(
        pygame.font.SysFont(pygame.font.get_default_font(), 20).render("Nombre de personnages", True, Constant.WHITE),
        (Constant.SCREEN_WIDTH - 260, Constant.SCREEN_HEIGHT - 450))
    if Worms.character == 1:
        Menu.button("1", Constant.SCREEN_WIDTH - 260, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.INDIGO,
                    Constant.LIGHT_GREEN, "1 character")
        Menu.button("2", Constant.SCREEN_WIDTH - 200, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.DARK,
                    Constant.LIGHT_GREEN, "2 characters")
    elif Worms.character == 2:
        Menu.button("1", Constant.SCREEN_WIDTH - 260, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.DARK,
                    Constant.LIGHT_GREEN, "1 character")
        Menu.button("2", Constant.SCREEN_WIDTH - 200, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.INDIGO,
                    Constant.LIGHT_GREEN, "2 characters")

    pygame.display.update()
    pygame.display.flip()


def playing_screen():
    import Worms
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
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                if not Worms.game_pause_screen:
                    Menu.game_pause_screen = True

            # Gestion des données de calcul de trajectoire
            if keys[pygame.K_r]:
                Worms.alpha += 1
            if keys[pygame.K_f]:
                Worms.alpha -= 1
            if keys[pygame.K_t]:
                Worms.v0 += 1
            if keys[pygame.K_g]:
                Worms.v0 -= 1
            if keys[pygame.K_y]:
                Worms.gravity += 1
            if keys[pygame.K_y]:
                Worms.gravity -= 1
            if keys[pygame.K_u]:
                Worms.wind_force += 1
            if keys[pygame.K_j]:
                Worms.wind_force -= 1

            if Worms.player1_turn:
                # Gestion des déplacements
                if keys[pygame.K_a]:
                    Menu.player1.move_left()
                if keys[pygame.K_d]:
                    Menu.player1.move_right()

                # Gestion des armes
                if keys[pygame.K_q]:
                    Menu.player1.select_weapon(Worms.screen)
                if keys[pygame.K_SPACE]:
                    Menu.player1.shoot(Worms.screen)

            elif Worms.player2_turn:
                # Gestion des déplacements
                if keys[pygame.K_a]:
                    Menu.player2.move_left()
                if keys[pygame.K_d]:
                    Menu.player2.move_right()

                # Gestion des armes
                if keys[pygame.K_q]:
                    Menu.player2.select_weapon(Worms.screen)
                if keys[pygame.K_SPACE]:
                    Menu.player2.shoot(Worms.screen)

    while Worms.game_pause_screen:
        pause_screen()

    pygame.draw.rect(Worms.screen, Constant.GROUND_COLOR, Constant.GROUND_POSITION)

    pygame.display.update()
    pygame.display.flip()

    Worms.clock.tick(60)


def pause_screen():
    import Worms
    # Boucle d'événement
    for event in pygame.event.get():
        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

    Worms.screen.blit(Menu.pause_background['surface'], Menu.pause_background['rect'])

    Menu.button("Return", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 - 100, 150, 50, Constant.DARK,
                Constant.LIGHT_GREEN, "return")
    Menu.button("Home", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 - 25, 150, 50, Constant.LIGHT_DARK,
                Constant.LIGHT_GREEN, "home")
    Menu.button("Quit", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 + 50, 150, 50, Constant.DARK_RED,
                Constant.LIGHT_GREEN, "quit")

    pygame.display.update()
    pygame.display.flip()
