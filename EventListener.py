# Auteur : Benoît


def pause_screen():
    import pygame
    import sys
    import Worms
    import Init
    import Constant
    import Asset
    import Menu

    # Boucle d'événement
    for event in pygame.event.get():
        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

    # Affichage de l'image de pause
    Worms.screen.blit(Asset.pause_background['surface'], Asset.pause_background['rect'])

    Worms.screen.blit(Worms.comicSansMsFont.render("Pause", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 350, Constant.SCREEN_HEIGHT - 400))
    # Affichage des bouttons
    Asset.button("Return", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 - 100, 150, 50, Constant.DARK, Constant.LIGHT_GREEN, "return")
    Asset.button("Home", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 - 25, 150, 50, Constant.LIGHT_DARK, Constant.LIGHT_GREEN, "home")
    Asset.button("Quit", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 + 50, 150, 50, Constant.DARK_RED, Constant.LIGHT_GREEN, "quit")

    # Mise à jour de l'affichage
    pygame.display.update()

    # Affiche l'image
    pygame.display.flip()


def settings_screen():
    import pygame
    import sys
    import Worms
    import Init
    import Constant
    import Asset
    import Menu

    # Boucle d'événement
    for event in pygame.event.get():
        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

    # Affichage de l'image de settings
    Worms.screen.blit(Asset.pause_background['surface'], Asset.pause_background['rect'])

    # Affichage des bouttons
    Asset.button("Start", Constant.SCREEN_WIDTH - 165, Constant.SCREEN_HEIGHT / 2 + 175, 150, 50, Constant.DARK, Constant.LIGHT_GREEN, "play")
    Asset.button("Home", Constant.SCREEN_WIDTH - 625, Constant.SCREEN_HEIGHT / 2 + 175, 150, 50, Constant.LIGHT_DARK, Constant.LIGHT_GREEN, "home")

    # Sélection nombre de joueurs
    Worms.screen.blit(Worms.comicSansMsFont.render("Nombre de joueurs", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 450))
    if Worms.player == 2:
        Asset.button("2", Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "2 players")
        Asset.button("3", Constant.SCREEN_WIDTH - 550, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "3 players")
    elif Worms.player == 3:
        Asset.button("2", Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "2 players")
        Asset.button("3", Constant.SCREEN_WIDTH - 550, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "3 players")

    # Sélection nombre de personnages par joueur
    Worms.screen.blit(Worms.comicSansMsFont.render("Nombre de personnages", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 260, Constant.SCREEN_HEIGHT - 450))
    if Worms.character == 1:
        Asset.button("1", Constant.SCREEN_WIDTH - 260, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "1 character")
        Asset.button("2", Constant.SCREEN_WIDTH - 200, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "2 characters")
    elif Worms.character == 2:
        Asset.button("1", Constant.SCREEN_WIDTH - 260, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "1 character")
        Asset.button("2", Constant.SCREEN_WIDTH - 200, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "2 characters")

    # Mise à jour de l'affichage
    pygame.display.update()
    # Affiche l'image
    pygame.display.flip()


def home_screen():
    import pygame
    import sys
    import Worms
    import Init
    import Constant
    import Asset
    import Menu

    # Boucle d'événement
    for event in pygame.event.get():
        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

    # Affichage de l'image de l'accueil
    Worms.screen.blit(Asset.home_background['surface'], Asset.home_background['rect'])

    # Affichage des bouttons
    Asset.button("Play", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 - 100, 150, 50, Constant.DARK, Constant.LIGHT_GREEN, "settings")
    Asset.button("Quit", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 + 50, 150, 50, Constant.DARK_RED, Constant.LIGHT_GREEN, "quit")

    # Mise à jour de l'affichage
    pygame.display.update()
    # Affiche l'image
    pygame.display.flip()


def playing_screen():
    import pygame
    import sys
    import Worms
    import Init
    import Constant
    import Asset
    import Animation
    import Menu

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Boucle d'événement
    for event in pygame.event.get():
        # Contrôle du timer
        if event.type == pygame.USEREVENT:
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

        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # Ouvrir le menu pause
            if event.key == pygame.K_ESCAPE:
                if not Worms.game_pause_screen:
                    Worms.game_pause_screen = True

            # A qui de jouer ?
            if Worms.player1_turn:
                if Worms.player1_character == 1:
                    if event.key == pygame.K_a:
                        player1_character1.move_left()
                    if event.key == pygame.K_d:
                        player1_character1.move_right()
                    if event.key == pygame.K_q:
                        # On change le repeat key temporairement pour pas que ca spam les grenades autant que les déplacements
                        pygame.key.set_repeat(500, 30)
                        player1_character1.select_weapon(screen)
                        pygame.key.set_repeat(30, 30)
                    if event.key == pygame.K_SPACE:
                        pygame.key.set_repeat(500, 30)
                        player1_character1.shoot(screen)
                        pygame.key.set_repeat(30, 30)
                elif Worms.player1_character == 2:
                    if event.key == pygame.K_a:
                        player1_character2.move_left()
                    if event.key == pygame.K_d:
                        player1_character2.move_right()
                    if event.key == pygame.K_q:
                        # On change le repeat key temporairement pour pas que ca spam les grenades autant que les déplacements
                        pygame.key.set_repeat(500, 30)
                        player1_character2.select_weapon(screen)
                        pygame.key.set_repeat(30, 30)
                    if event.key == pygame.K_SPACE:
                        pygame.key.set_repeat(500, 30)
                        player1_character2.shoot(screen)
                        pygame.key.set_repeat(30, 30)
            elif Worms.player2_turn:
                if Worms.player2_character == 1:
                    if event.key == pygame.K_LEFT:
                        player2_character1.move_left()
                    if event.key == pygame.K_RIGHT:
                        player2_character1.move_right()
                    if event.key == pygame.K_q:
                        # On change le repeat key temporairement pour pas que ca spam les grenades autant que les déplacements
                        pygame.key.set_repeat(500, 30)
                        player2_character1.select_weapon(screen)
                        pygame.key.set_repeat(30, 30)
                    if event.key == pygame.K_SPACE:
                        pygame.key.set_repeat(500, 30)
                        player2_character1.shoot(screen)
                        pygame.key.set_repeat(30, 30)
                elif Worms.player2_character == 2:
                    if event.key == pygame.K_LEFT:
                        player2_character2.move_left()
                    if event.key == pygame.K_RIGHT:
                        player2_character2.move_right()
                    if event.key == pygame.K_q:
                        # On change le repeat key temporairement pour pas que ca spam les grenades autant que les déplacements
                        pygame.key.set_repeat(500, 30)
                        player2_character2.select_weapon(screen)
                        pygame.key.set_repeat(30, 30)
                    if event.key == pygame.K_SPACE:
                        pygame.key.set_repeat(500, 30)
                        player2_character2.shoot(screen)
                        pygame.key.set_repeat(30, 30)
            elif Worms.player3_turn:
                if Worms.player3_character == 1:
                    if event.key == pygame.K_j:
                        player3_character1.move_left()
                    if event.key == pygame.K_l:
                        player3_character1.move_right()
                    if event.key == pygame.K_q:
                        # On change le repeat key temporairement pour pas que ca spam les grenades autant que les déplacements
                        pygame.key.set_repeat(500, 30)
                        player3_character1.select_weapon(screen)
                        pygame.key.set_repeat(30, 30)
                    if event.key == pygame.K_SPACE:
                        pygame.key.set_repeat(500, 30)
                        player3_character1.shoot(screen)
                        pygame.key.set_repeat(30, 30)
                elif Worms.player3_character == 2:
                    if event.key == pygame.K_j:
                        player3_character2.move_left()
                    if event.key == pygame.K_l:
                        player3_character2.move_right()
                    if event.key == pygame.K_q:
                        # On change le repeat key temporairement pour pas que ca spam les grenades autant que les déplacements
                        pygame.key.set_repeat(500, 30)
                        player3_character2.select_weapon(screen)
                        pygame.key.set_repeat(30, 30)
                    if event.key == pygame.K_SPACE:
                        pygame.key.set_repeat(500, 30)
                        player3_character2.shoot(screen)
                        pygame.key.set_repeat(30, 30)

                if event.key == pygame.K_r:
                    alpha += 1
                    #player1.bazooka.weapon.surface = pygame.transform.rotate(player1.bazooka.weapon.surface, 1)
                if event.key == pygame.K_f:
                    alpha -= 1
                    #player1.bazooka.weapon.surface = pygame.transform.rotate(player1.bazooka.weapon.surface, -1)

                if event.key == pygame.K_t:
                    v0 += 1
                if event.key == pygame.K_g:
                    v0 -= 1

                if event.key == pygame.K_y:
                    gravity += 1
                if event.key == pygame.K_h:
                    gravity -= 1

                if event.key == pygame.K_u:
                    wind_force += 1
                if event.key == pygame.K_j:
                    wind_force -= 1

    while Worms.game_pause_screen:
        pause_screen()

    Animation.update_player_title(Asset.player1Character1, Asset.player1_character1_title)
    Animation.update_player_title(Asset.player2Character1, Asset.player2_character1_title)
    if Worms.player == 3:
        Animation.update_player_title(Asset.player3Character1, Asset.player3_character1_title)

    if Worms.character == 2:
        Animation.update_player_title(Asset.player1Character2, Asset.player1_character2_title)
        Animation.update_player_title(Asset.player2Character2, Asset.player2_character2_title)
        if Worms.player == 3:
            Animation.update_player_title(Asset.player3Character2, Asset.player3_character2_title)

    # Efface l'image et affiche le fond
    background.update(screen)

    # Dessine le sol
    pygame.draw.rect(screen, Constant.GROUND_COLOR, Constant.GROUND_POSITION)

    # update windforce display
    hud.set_text(
        "[Alpha angle : " + str(alpha) + "][V0 : " + str(v0) + "][Gravity : " + str(
            round(gravity, 2)) + "][Wind force : " + str(wind_force) + "]",
        Constant.BLACK)
    hud.update(screen)

    # Update players
    if player1_character1.life_point:
        player1_character1.update(screen, player2_character1, alpha, v0, gravity, wind_force)
    if player2_character1.life_point:
        player2_character1.update(screen, player1_character1, alpha, v0, gravity, wind_force)

    # Sélection du personnage du joueur
    if Worms.character == 2:
        if Worms.player1_turn:
            if Worms.player1_character == 1:
                Asset.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "joueur 1 personnage 1")
                Asset.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "joueur 1 personnage 2")
            elif Worms.player1_character == 2:
                Asset.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "joueur 1 personnage 1")
                Asset.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "joueur 1 personnage 2")
        elif Worms.player2_turn:
            if Worms.player2_character == 1:
                Asset.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "joueur 2 personnage 1")
                Asset.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "joueur 2 personnage 2")
            elif Worms.player2_character == 2:
                Asset.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "joueur 2 personnage 1")
                Asset.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "joueur 2 personnage 2")
        elif Worms.player3_turn:
            if Worms.player3_character == 1:
                Asset.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "joueur 3 personnage 1")
                Asset.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "joueur 3 personnage 2")
            elif Worms.player3_character == 2:
                Asset.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "joueur 3 personnage 1")
                Asset.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "joueur 3 personnage 2")

    # Affiche le personnage 1 du joueur 1 sur l'écran
    Worms.screen.blit(Asset.player1Character1['surface'], Asset.player1Character1['rect'])
    Worms.screen.blit(Asset.player1_character1_title['surface'], Asset.player1_character1_title['rect'])
    # Affiche le personnage 1 du joueur 2 sur l'écran
    Worms.screen.blit(Asset.player2Character1['surface'], Asset.player2Character1['rect'])
    Worms.screen.blit(Asset.player2_character1_title['surface'], Asset.player2_character1_title['rect'])
    if Worms.player == 3:
        # Affiche le personnage 1 du joueur 3 sur l'écran
        Worms.screen.blit(Asset.player3Character1['surface'], Asset.player3Character1['rect'])
        Worms.screen.blit(Asset.player3_character1_title['surface'], Asset.player3_character1_title['rect'])

    if Worms.character == 2:
        # Affiche le personnage 2 du joueur 1 sur l'écran
        Worms.screen.blit(Asset.player1Character2['surface'], Asset.player1Character2['rect'])
        Worms.screen.blit(Asset.player1_character2_title['surface'], Asset.player1_character2_title['rect'])
        # Affiche le personnage 2 du joueur 2 sur l'écran
        Worms.screen.blit(Asset.player2Character2['surface'], Asset.player2Character2['rect'])
        Worms.screen.blit(Asset.player2_character2_title['surface'], Asset.player2_character2_title['rect'])
        if Worms.player == 3:
            # Affiche le personnage 2 du joueur 3 sur l'écran
            Worms.screen.blit(Asset.player3Character2['surface'], Asset.player3Character2['rect'])
            Worms.screen.blit(Asset.player3_character2_title['surface'], Asset.player3_character2_title['rect'])

    # Affiche le tour
    Worms.screen.blit(Worms.comicSansMsFont.render(str(Worms.turn), True, Constant.WHITE), (Constant.SCREEN_WIDTH - 630, Constant.SCREEN_HEIGHT - 475))
    if Worms.counter <= 0:
        Worms.screen.blit(Worms.comicSansMsFont.render("Tour suivant", True, Constant.WHITE), (Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT - 450))

    # Affiche le timer
    Asset.button(str(Worms.counter), Constant.SCREEN_WIDTH - 635, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.LIGHT_DARK, Constant.DARK)
    # Si joueur 1
    if Worms.player1_turn:
        Worms.screen.blit(Worms.comicSansMsFont.render("Joueur 1", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 33))
    # Si joueur 2
    elif Worms.player2_turn:
        Worms.screen.blit(Worms.comicSansMsFont.render("Joueur 2", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 33))
    # Si joueur 3
    elif Worms.player3_turn:
        Worms.screen.blit(Worms.comicSansMsFont.render("Joueur 3", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 33))

    # Affiche l'image
    pygame.display.flip()

    # temp
    pygame.time.wait(5)

    # Clock tick
    Worms.clock.tick(60)

