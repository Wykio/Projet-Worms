# -*-coding:Latin-1 -*
# Auteur: Antoine

import pygame

import Animation
import Asset
import Constant
import Init, Event_Listener

# Initialisation de la fenêtre du jeu
screen = Init.init_game(Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
# Chargement des assets
Init.load_game()

while 1:
    Event_Listener.event_listener()

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

    Animation.update_player_weapon(screen, Asset.player1)

    # Affiche l'image
    pygame.display.flip()




