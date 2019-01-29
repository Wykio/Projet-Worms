import pygame
import sys

import Worms
import Constant
import Init
import Asset
import Animation

#Auteur : Benoît

def home_state():
    global game_home
    while game_home:
        # Boucle d'événement
        for event in pygame.event.get():
            # Si on détecte l'événement "quitter"
            if event.type == pygame.QUIT:
                # Décharge les modules de la mémoire
                Init.quit_game()
                # Quitte le programme
                sys.exit()

        # screen.fill(Constant.WHITE)

        # Affiche de l'accueil sur l'écran
        Worms.screen.blit(Asset.home_background['surface'], Asset.home_background['rect'])

        Asset.button("Play", Constant.SCREEN_WIDTH / 2, Constant.SCREEN_HEIGHT / 2 - 100, 100, 50, Constant.GREEN, Constant.DARK_GREEN, "play")
        Asset.button("Quit", Constant.SCREEN_WIDTH / 2, Constant.SCREEN_HEIGHT / 2, 100, 50, Constant.RED, Constant.DARK_RED, "quit")

        pygame.display.update()
        # Affiche l'image
        pygame.display.flip()


def game_playing():
    while game_playing:
        # Boucle d'événement
        for event in pygame.event.get():
            # Si on détecte l'événement "quitter"
            if event.type == pygame.QUIT:
                # Décharge les modules de la mémoire
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
        Worms.screen.fill(Constant.BLACK)
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

