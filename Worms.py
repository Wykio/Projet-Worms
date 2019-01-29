# -*-coding:Latin-1 -*
import pygame
import sys

import Init
import Constant
import Asset
import Animation

# Initialisation de la fen�tre du jeu
screen = Init.init_game(Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)

# Chargement des assets
Init.load_game()

# Statut du jeu
game_is_open = True
game_home = True
game_settings = False
game_playing = False
game_pause = False

while game_is_open:
    while game_home:
        # Boucle d'�v�nement
        for event in pygame.event.get():
            # Si on d�tecte l'�v�nement "quitter"
            if event.type == pygame.QUIT:
                # D�charge les modules de la m�moire
                Init.quit_game()
                # Quitte le programme
                sys.exit()

        # Efface l'image
        screen.fill(Constant.BLACK)
        # Affichage de l'image de l'accueil sur l'�cran
        screen.blit(Asset.home_background['surface'], Asset.home_background['rect'])

        # Affichage des bouttons
        Asset.button("Play", Constant.SCREEN_WIDTH / 2, Constant.SCREEN_HEIGHT / 2 - 100, 100, 50, Constant.GREEN, Constant.DARK_GREEN, "play")
        Asset.button("Quit", Constant.SCREEN_WIDTH / 2, Constant.SCREEN_HEIGHT / 2, 100, 50, Constant.RED, Constant.DARK_RED, "quit")

        # Mise � jour de l'affichage
        pygame.display.update()
        # Affiche l'image
        pygame.display.flip()

    while game_playing:
        # Boucle d'�v�nement
        for event in pygame.event.get():
            # Si on d�tecte l'�v�nement "quitter"
            if event.type == pygame.QUIT:
                # D�charge les modules de la m�moire
                Init.quit_game()
                # Quitte le programme
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Asset.player2 = Animation.player_move_left(Asset.player2)

                if event.key == pygame.K_RIGHT:
                    Asset.player2 = Animation.player_move_right(Asset.player2)

                if event.key == pygame.K_a:
                    Asset.player1 = Animation.player_move_left(Asset.player1)

                if event.key == pygame.K_d:
                    Asset.player1 = Animation.player_move_right(Asset.player1)

        Animation.update_player_title(Asset.player1, Asset.player1_title)
        Animation.update_player_title(Asset.player2, Asset.player2_title)

        # Efface l'image
        screen.fill(Constant.BLACK)
        # Affichage de l'image de jeu
        screen.blit(Asset.background['surface'], Asset.background['rect'])
        # Dessine le sol
        pygame.draw.rect(screen, Constant.GROUND_COLOR, Constant.GROUND_POSITION)

        # Affiche le joueur 1 sur l'�cran
        screen.blit(Asset.player1['surface'], Asset.player1['rect'])
        screen.blit(Asset.player1_title['surface'], Asset.player1_title['rect'])
        # Affiche le joueur 2 sur l'�cran
        screen.blit(Asset.player2['surface'], Asset.player2['rect'])
        screen.blit(Asset.player2_title['surface'], Asset.player2_title['rect'])

        # Affiche l'image
        pygame.display.flip()

