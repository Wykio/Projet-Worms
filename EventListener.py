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
                        if Worms.player1_character == 1:
                            Menu.player1character1.move_left()
                        elif Worms.player1_character == 2:
                            Menu.player1character2.move_left()
                if keys[pygame.K_d]:
                    if Worms.player1_character == 1:
                        Menu.player1character1.move_right()
                    elif Worms.player1_character == 2:
                        Menu.player1character2.move_right()

                # Gestion des armes
                if keys[pygame.K_q]:
                    if Worms.player1_character == 1:
                        Menu.player1character1.select_weapon(Worms.screen)
                    elif Worms.player1_character == 2:
                        Menu.player1character2.select_weapon(Worms.screen)
                if keys[pygame.K_SPACE]:
                    if Worms.player1_character == 1:
                        Menu.player1character1.shoot(Worms.screen)
                    elif Worms.player1_character == 2:
                        Menu.player1character2.shoot(Worms.screen)

            elif Worms.player2_turn:
                # Gestion des déplacements
                if keys[pygame.K_a]:
                    if Worms.player2_character == 1:
                        Menu.player2character1.move_left()
                    if Worms.player2_character == 2:
                        Menu.player2character2.move_left()
                if keys[pygame.K_d]:
                    if Worms.player2_character == 1:
                        Menu.player2character1.move_right()
                    if Worms.player2_character == 2:
                        Menu.player2character2.move_right()

                # Gestion des armes
                if keys[pygame.K_q]:
                    if Worms.player2_character == 1:
                        Menu.player2character1.select_weapon(Worms.screen)
                    if Worms.player2_character == 2:
                        Menu.player2character2.select_weapon(Worms.screen)
                if keys[pygame.K_SPACE]:
                    if Worms.player2_character == 1:
                        Menu.player2character1.shoot(Worms.screen)
                    if Worms.player2_character == 2:
                        Menu.player2character2.shoot(Worms.screen)

            elif Worms.player3_turn:
                # Gestion des déplacements
                if keys[pygame.K_a]:
                    if Worms.player3_character == 1:
                        Menu.player3character1.move_left()
                    if Worms.player3_character == 2:
                        Menu.player3character2.move_left()
                if keys[pygame.K_d]:
                    if Worms.player3_character == 1:
                        Menu.player3character1.move_right()
                    if Worms.player3_character == 2:
                        Menu.player3character2.move_right()

                # Gestion des armes
                if keys[pygame.K_q]:
                    if Worms.player3_character == 1:
                        Menu.player3character1.select_weapon(Worms.screen)
                    if Worms.player3_character == 2:
                        Menu.player3character2.select_weapon(Worms.screen)
                if keys[pygame.K_SPACE]:
                    if Worms.player3_character == 1:
                        Menu.player3character1.shoot(Worms.screen)
                    if Worms.player3_character == 2:
                        Menu.player3character2.shoot(Worms.screen)

    while Worms.game_pause_screen:
        pause_screen()

    # Efface l'image et la remplace par la bonne
    Worms.screen.fill(Constant.BLACK)
    Worms.screen.blit(Menu.background['surface'], Menu.background['rect'])

    #Dessine le sol
    pygame.draw.rect(Worms.screen, Constant.GROUND_COLOR, Constant.GROUND_POSITION)

    #Gestion de plus d'un seul personnage par joueur
    if Worms.character == 2:
        if Worms.player1_turn:
            if Worms.player1_character == 1:
                Menu.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO,
                            Constant.LIGHT_GREEN, "joueur 1 personnage 1")
                Menu.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK,
                            Constant.LIGHT_GREEN, "joueur 1 personnage 2")
            elif Worms.player1_character == 2:
                Menu.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK,
                            Constant.LIGHT_GREEN, "joueur 1 personnage 1")
                Menu.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO,
                            Constant.LIGHT_GREEN, "joueur 1 personnage 2")
        elif Worms.player2_turn:
            if Worms.player2_character == 1:
                Menu.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO,
                            Constant.LIGHT_GREEN, "joueur 2 personnage 1")
                Menu.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK,
                            Constant.LIGHT_GREEN, "joueur 2 personnage 2")
            elif Worms.player2_character == 2:
                Menu.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK,
                            Constant.LIGHT_GREEN, "joueur 2 personnage 1")
                Menu.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO,
                            Constant.LIGHT_GREEN, "joueur 2 personnage 2")
        elif Worms.player3_turn:
            if Worms.player2_character == 1:
                Menu.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO,
                            Constant.LIGHT_GREEN, "joueur 3 personnage 1")
                Menu.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK,
                            Constant.LIGHT_GREEN, "joueur 3 personnage 2")
            elif Worms.player2_character == 2:
                Menu.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK,
                            Constant.LIGHT_GREEN, "joueur 3 personnage 1")
                Menu.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO,
                            Constant.LIGHT_GREEN, "joueur 3 personnage 2")

    # update windforce display
    Worms.hud.set_text(
        "[Alpha angle : " + str(Worms.alpha) + "][V0 : " + str(Worms.v0) + "][Gravity : " + str(
            round(Worms.gravity, 2)) + "][Wind force : " + str(Worms.wind_force) + "]",
        Constant.BLACK)
    Worms.hud.update(Worms.screen)

    # Update players
    if Menu.player1character1.life_point:
        Menu.player1character1.update(Worms.screen, Menu.player1character1,  Menu.all_players, Worms.alpha,
                                      Worms.v0, Worms.gravity, Worms.wind_force)
    if Menu.player1character2.life_point:
        Menu.player1character2.update(Worms.screen, Menu.player1character2, Menu.all_players, Worms.alpha,
                                      Worms.v0, Worms.gravity, Worms.wind_force)
    if Menu.player2character1.life_point:
        Menu.player2character1.update(Worms.screen, Menu.player2character1, Menu.all_players, Worms.alpha,
                                      Worms.v0, Worms.gravity, Worms.wind_force)
    if Menu.player2character2.life_point:
        Menu.player2character2.update(Worms.screen, Menu.player2character2, Menu.all_players, Worms.alpha,
                                      Worms.v0, Worms.gravity, Worms.wind_force)
    if Menu.player3character1.life_point:
        Menu.player3character1.update(Worms.screen, Menu.player3character1, Menu.all_players, Worms.alpha,
                                      Worms.v0, Worms.gravity, Worms.wind_force)
    if Menu.player3character2.life_point:
        Menu.player3character2.update(Worms.screen, Menu.player3character2, Menu.all_players, Worms.alpha,
                                      Worms.v0, Worms.gravity, Worms.wind_force)

    # Affichage du tour
    Worms.screen.blit(pygame.font.SysFont(pygame.font.get_default_font(), 20).render(str(Worms.turn), True, Constant.WHITE), \
                     (Constant.SCREEN_WIDTH - 630, Constant.SCREEN_HEIGHT - 475))
    if Worms.counter <= 0:
        Worms.screen.blit(pygame.font.SysFont(pygame.font.get_default_font(), 20).render("Tour suivant", True, Constant.WHITE), \
                         (Constant.SCREEN_WIDTH - 630, Constant.SCREEN_HEIGHT - 475))

    # Affichage du timer
    Menu.button(str(Worms.counter), Constant.SCREEN_WIDTH - 635, Constant.SCREEN_HEIGHT - 35, 30, 30,
                Constant.LIGHT_DARK, Constant.DARK)

    # Affichage du joueur courant
    if Worms.player1_turn:
        Worms.screen.blit(pygame.font.SysFont(pygame.font.get_default_font(), 20).render("Joueur 1", True, Constant.WHITE), \
                          (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 33))
    if Worms.player2_turn:
        Worms.screen.blit(pygame.font.SysFont(pygame.font.get_default_font(), 20).render("Joueur 2", True, Constant.WHITE), \
                          (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 33))
    if Worms.player3_turn:
        Worms.screen.blit(pygame.font.SysFont(pygame.font.get_default_font(), 20).render("Joueur 3", True, Constant.WHITE), \
                          (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 33))

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
