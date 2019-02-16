# -*-coding:Latin-1 -*
# Auteur: Antoine

import pygame, sys

from Asset import Asset
from Textfield import Textfield
from Player import Player
import Constant
import Init


def main():
    # Initialisation de la fenêtre du jeu
    screen = Init.init_game(Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
    background = Asset(pygame.image.load("Assets/beach_background.gif"))
    gameSprite = Asset(pygame.image.load("Assets/player_sprite_35x35.gif"))
    player1 = Player("Player 1", Constant.RED, gameSprite)
    player2 = Player("Player 2", Constant.BLUE, gameSprite)
    # x = moitier de l'écran, y de la position du sol - taille du sprite
    player1.set_position(Constant.PLAYER1_START_X, Constant.GROUND_POSITION[1] - 35)
    player2.set_position(Constant.PLAYER2_START_X, Constant.GROUND_POSITION[1] - 35)
    alpha = Constant.GRENADE_ALPHA_ANGLE
    v0 = Constant.GRENADE_V0
    gravity = Constant.GRAVITY
    wind_force = 0
    hud = Textfield(None, Constant.BLACK)


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
                if event.key == pygame.K_a:
                    player1.move_left()

                if event.key == pygame.K_d:
                    player1.move_right()

                if event.key == pygame.K_LEFT:
                    player2.move_left()

                if event.key == pygame.K_RIGHT:
                    player2.move_right()

                if event.key == pygame.K_q:
                    # On change le repeat key temporairement pour pas que ca spam les grenades autant que les déplacements
                    pygame.key.set_repeat(500, 30)
                    player1.select_weapon(screen)
                    pygame.key.set_repeat(30, 30)

                if event.key == pygame.K_SPACE:
                    pygame.key.set_repeat(500, 30)
                    player1.shoot(screen)
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


        # Efface l'image et affiche le fond
        background.update(screen)

        # Dessine le sol
        pygame.draw.rect(screen, Constant.GROUND_COLOR, Constant.GROUND_POSITION)

        # update windforce display
        hud.set_text(
            "[Alpha angle : " + str(alpha) + "][V0 : " + str(v0) + "][Gravity : " + str(round(gravity, 2)) + "][Wind force : " + str(wind_force) + "]",
            Constant.BLACK)
        hud.update(screen)

        # Update players
        if player1.life_point:
            player1.update(screen, player2, alpha, v0, gravity, wind_force)
        if player2.life_point:
            player2.update(screen, player1, alpha, v0, gravity, wind_force)

        # Affiche l'image
        pygame.display.flip()

        # temp
        pygame.time.wait(5)


# call the "main" function if running this script
if __name__ == '__main__': main()