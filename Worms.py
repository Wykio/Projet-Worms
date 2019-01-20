# -*-coding:Latin-1 -*
import pygame
import sys

import Animation
import Asset
import Constant
import Init

#Auteur: Antoine

# Initialisation de la fenêtre du jeu
screen = Init.init_game(Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
# Chargement des assets
Init.load_game()

while 1:
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
    screen.blit(Asset.background['surface'], Asset.background['rect'])
    # Dessine le sol
    pygame.draw.rect(screen, Constant.GROUND_COLOR, Constant.GROUND_POSITION)

    # Affiche le joueur 1 sur l'écran
    screen.blit(Asset.player1['surface'], Asset.player1['rect'])
    screen.blit(Asset.player1_title['surface'], Asset.player1_title['rect'])
    # Affiche le joueur 2 sur l'écran
    screen.blit(Asset.player2['surface'], Asset.player2['rect'])
    screen.blit(Asset.player2_title['surface'], Asset.player2_title['rect'])

    # Affiche l'image
    pygame.display.flip()




