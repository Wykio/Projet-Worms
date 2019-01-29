# Auteur : Benoît


def game_pause():
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
    Asset.button("Return", Constant.SCREEN_WIDTH / 2 - 50, Constant.SCREEN_HEIGHT / 2 - 100, 100, 50, Constant.GREEN,
                 Constant.DARK_GREEN, "return")
    Asset.button("Quit", Constant.SCREEN_WIDTH / 2 - 50, Constant.SCREEN_HEIGHT / 2 + 50, 100, 50, Constant.RED,
                 Constant.DARK_RED, "quit")

    # Mise à jour de l'affichage
    pygame.display.update()
    # Affiche l'image
    pygame.display.flip()


def game_home():
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
    Asset.button("Play", Constant.SCREEN_WIDTH / 2 - 50, Constant.SCREEN_HEIGHT / 2 - 100, 100, 50, Constant.GREEN, Constant.DARK_GREEN, "play")
    Asset.button("Quit", Constant.SCREEN_WIDTH / 2 - 50, Constant.SCREEN_HEIGHT / 2 + 50, 100, 50, Constant.RED, Constant.DARK_RED, "quit")

    # Mise à jour de l'affichage
    pygame.display.update()
    # Affiche l'image
    pygame.display.flip()


def game_playing():
    import pygame
    import sys
    import Worms
    import Init
    import Constant
    import Asset
    import Animation
    # Boucle d'événement
    for event in pygame.event.get():
        # Si on détecte l'événement "quitter"
        if event.type == pygame.QUIT:
            # Décharge les modules de la mémoire
            Init.quit_game()
            # Quitte le programme
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Worms.game_pause = True

            if event.key == pygame.K_LEFT:
                Asset.player2 = Animation.player_move_left(Asset.player2)

            if event.key == pygame.K_RIGHT:
                Asset.player2 = Animation.player_move_right(Asset.player2)

            if event.key == pygame.K_a:
                Asset.player1 = Animation.player_move_left(Asset.player1)

            if event.key == pygame.K_d:
                Asset.player1 = Animation.player_move_right(Asset.player1)

    while Worms.game_pause:
        game_pause()

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

    # Affiche l'image
    pygame.display.flip()
