# -*-coding:Latin-1 -*
# Auteur: Antoine

import pygame, sys
import Init, Asset, Animation


def event_listener():
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

            if event.key == pygame.K_q:
                # On change le repeat key temporairement pour pas que ca spam les grenades autant que les d�placements
                pygame.key.set_repeat(500, 30)
                Asset.player1 = Animation.player_select_grenade(Asset.player1)
                pygame.key.set_repeat(30, 30)

            if event.key == pygame.K_SPACE:
                pygame.key.set_repeat(500, 30)
                # Seulement si la grenade est affich�e on peut la lancer
                if Asset.player1['Throw_grenade']:
                    Animation.grenade_launch(Asset.grenade)
                pygame.key.set_repeat(30, 30)
