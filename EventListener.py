# Auteur : Benoît


def pause_screen():
    import pygame
    import sys
    import Worms
    import Init
    import Constant
    import Asset

    # Boucle d'événement
    for event in pygame.event.get():
        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

    # screen.fill(Constant.WHITE)

    # Affichage de l'image de pause
    Worms.screen.blit(Asset.pause_background['surface'], Asset.pause_background['rect'])

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

    # Boucle d'événement
    for event in pygame.event.get():
        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

    # screen.fill(Constant.WHITE)

    # Affichage de l'image de settings
    Worms.screen.blit(Asset.pause_background['surface'], Asset.pause_background['rect'])

    # Affichage des bouttons
    Asset.button("Start", Constant.SCREEN_WIDTH - 165, Constant.SCREEN_HEIGHT / 2 + 175, 150, 50, Constant.DARK, Constant.LIGHT_GREEN, "play")
    Asset.button("Home", Constant.SCREEN_WIDTH - 625, Constant.SCREEN_HEIGHT / 2 + 175, 150, 50, Constant.LIGHT_DARK, Constant.LIGHT_GREEN, "home")

    textFont = pygame.font.SysFont("comicsansms", 20)
    # Sélection nombre de joueurs
    Worms.screen.blit(textFont.render("Nombre de joueurs", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 450))
    if Worms.player == 2:
        Asset.button("2", Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "2 players")
        Asset.button("3", Constant.SCREEN_WIDTH - 550, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "3 players")
    elif Worms.player == 3:
        Asset.button("2", Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "2 players")
        Asset.button("3", Constant.SCREEN_WIDTH - 550, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "3 players")

    # Sélection nombre de personnages par joueur
    Worms.screen.blit(textFont.render("Nombre de personnages", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 260, Constant.SCREEN_HEIGHT - 450))
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

    # Boucle d'événement
    for event in pygame.event.get():
        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

    # screen.fill(Constant.WHITE)

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

    # Boucle d'événement
    for event in pygame.event.get():
        # Contrôle du timer
        if event.type == pygame.USEREVENT:
            if Worms.counter <= 0:
                Worms.counter = 6
                Worms.turn += 1
                if Worms.player1_turn:
                    Worms.player1_turn = False
                    Worms.player2_turn = True
                elif Worms.player2_turn:
                    Worms.player1_turn = True
                    Worms.player2_turn = False
            Worms.counter -= 1

        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not Worms.game_pause_screen:
                    Worms.game_pause_screen = True

            # A qui de jouer ?
            if Worms.player1_turn:
                if event.key == pygame.K_a:
                    Asset.player1 = Animation.player_move_left(Asset.player1)

                if event.key == pygame.K_d:
                    Asset.player1 = Animation.player_move_right(Asset.player1)
            elif Worms.player2_turn:
                if event.key == pygame.K_LEFT:
                    Asset.player2 = Animation.player_move_left(Asset.player2)

                if event.key == pygame.K_RIGHT:
                    Asset.player2 = Animation.player_move_right(Asset.player2)

    while Worms.game_pause_screen:
        pause_screen()

    Animation.update_player_title(Asset.player1, Asset.player1_title)
    Animation.update_player_title(Asset.player2, Asset.player2_title)

    # Efface l'image
    Worms.screen.fill(Constant.BLACK)
    # Affichage de l'image de jeu
    Worms.screen.blit(Asset.background['surface'], Asset.background['rect'])
    # Dessine le sol
    pygame.draw.rect(Worms.screen, Constant.GROUND_COLOR, Constant.GROUND_POSITION)

    # Affiche le joueur 1 sur l'écran
    Worms.screen.blit(Asset.player1['surface'], Asset.player1['rect'])
    Worms.screen.blit(Asset.player1_title['surface'], Asset.player1_title['rect'])
    # Affiche le joueur 2 sur l'écran
    Worms.screen.blit(Asset.player2['surface'], Asset.player2['rect'])
    Worms.screen.blit(Asset.player2_title['surface'], Asset.player2_title['rect'])

    # Affiche le tour
    Worms.screen.blit(Worms.font.render(str(Worms.turn), True, Constant.WHITE), (Constant.SCREEN_WIDTH - 630, Constant.SCREEN_HEIGHT - 475))
    if Worms.counter <= 0:
        Worms.screen.blit(Worms.font.render("Tour suivant", True, Constant.WHITE), (Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT - 450))

    # Affiche le timer
    Asset.button(str(Worms.counter), Constant.SCREEN_WIDTH - 635, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.LIGHT_DARK, Constant.DARK)
    # Si joueur 1
    if Worms.player1_turn:
        Worms.screen.blit(Worms.font.render("Joueur 1", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 33))
    # Si joueur 2
    elif Worms.player2_turn:
        Worms.screen.blit(Worms.font.render("Joueur 2", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 33))

    # Affiche l'image
    pygame.display.flip()

    # Clock tick
    Worms.clock.tick(60)

