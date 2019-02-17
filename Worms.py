# -*-coding:Latin-1 -*

import pygame
import sys

from Asset import Asset
from Textfield import Textfield
from Player import Player
import Constant
import Init

import Menu
import PlayerAsset
import Animation

def main():
    # Initialisation de la fenêtre du jeu
    screen = Init.init_game(Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)

    background = Asset(pygame.image.load("Assets/beach_background.gif"))
    gameSprite = Asset(pygame.image.load("Assets/player_sprite_35x35.gif"))

    player1_character1 = Player("Player 1", Constant.RED, gameSprite)
    player1_character2 = Player("Player 1", Constant.RED, gameSprite)

    player2_character1 = Player("Player 2", Constant.BLUE, gameSprite)
    player2_character2 = Player("Player 2", Constant.BLUE, gameSprite)

    player3_character1 = Player("Player 3", Constant.GREEN, gameSprite)
    player3_character2 = Player("Player 3", Constant.GREEN, gameSprite)

    # x = moitier de l'écran, y de la position du sol - taille du sprite
    player1_character1.set_position(Constant.PLAYER1_CHARACTER1_START_X, Constant.GROUND_POSITION[1] - 35)
    player1_character2.set_position(Constant.PLAYER1_CHARACTER2_START_X, Constant.GROUND_POSITION[1] - 35)

    player2_character1.set_position(Constant.PLAYER2_CHARACTER1_START_X, Constant.GROUND_POSITION[1] - 35)
    player2_character2.set_position(Constant.PLAYER2_CHARACTER2_START_X, Constant.GROUND_POSITION[1] - 35)

    player3_character1.set_position(Constant.PLAYER3_CHARACTER1_START_X, Constant.GROUND_POSITION[1] - 35)
    player3_character2.set_position(Constant.PLAYER3_CHARACTER2_START_X, Constant.GROUND_POSITION[1] - 35)

    alpha = Constant.GRENADE_ALPHA_ANGLE
    v0 = Constant.GRENADE_V0
    gravity = Constant.GRAVITY
    wind_force = 0
    hud = Textfield(None, Constant.BLACK)

    # Chargement des assets
    Menu.load_menu()
    PlayerAsset.load_player_asset()

    # Police d'écriture
    comicSansMsFont = pygame.font.SysFont("comicsansms", 20)
    consolasFont = pygame.font.SysFont('Consolas', 20)

    # Statut du jeu
    game_is_open = True
    game_home_screen = True
    game_settings_screen = False
    game_playing_screen = False
    game_pause_screen = False

    while game_is_open:
        while game_home_screen:
            # Boucle d'événement
            for event in pygame.event.get():
                # Si on détecte l'événement "quitter"
                if event.type == pygame.QUIT:
                    # Décharge les modules de la mémoire
                    Init.quit_game()
                    # Quitte le programme
                    sys.exit()

            # Affichage de l'image de l'accueil
            screen.blit(Menu.home_background['surface'], Menu.home_background['rect'])

            # Affichage des bouttons
            Menu.button("Play", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 - 100, 150, 50, Constant.DARK, Constant.LIGHT_GREEN, "settings")
            Menu.button("Quit", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 + 50, 150, 50, Constant.DARK_RED, Constant.LIGHT_GREEN, "quit")

            # Mise à jour de l'affichage
            pygame.display.update()

            # Affiche l'image
            pygame.display.flip()

        # Initialisation de donnée lié à la création de partie
        player = 2
        character = 1
        while game_settings_screen:
            # Boucle d'événement
            for event in pygame.event.get():
                # Si on détecte l'événement "quitter"
                if event.type == pygame.QUIT:
                    # Décharge les modules de la mémoire
                    Init.quit_game()
                    # Quitte le programme
                    sys.exit()

            # Affichage de l'image de settings
            screen.blit(Asset.pause_background['surface'], Asset.pause_background['rect'])

            # Affichage des bouttons
            Menu.button("Start", Constant.SCREEN_WIDTH - 165, Constant.SCREEN_HEIGHT / 2 + 175, 150, 50, Constant.DARK, Constant.LIGHT_GREEN, "play")
            Menu.button("Home", Constant.SCREEN_WIDTH - 625, Constant.SCREEN_HEIGHT / 2 + 175, 150, 50, Constant.LIGHT_DARK, Constant.LIGHT_GREEN, "home")

            # Sélection nombre de joueurs
            screen.blit(comicSansMsFont.render("Nombre de joueurs", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 450))
            if player == 2:
                Menu.button("2", Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "2 players")
                Menu.button("3", Constant.SCREEN_WIDTH - 550, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "3 players")
            elif player == 3:
                Menu.button("2", Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "2 players")
                Menu.button("3", Constant.SCREEN_WIDTH - 550, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "3 players")

            # Sélection nombre de personnages par joueur
            screen.blit(comicSansMsFont.render("Nombre de personnages", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 260, Constant.SCREEN_HEIGHT - 450))
            if character == 1:
                Menu.button("1", Constant.SCREEN_WIDTH - 260, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "1 character")
                Menu.button("2", Constant.SCREEN_WIDTH - 200, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "2 characters")
            elif character == 2:
                Menu.button("1", Constant.SCREEN_WIDTH - 260, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "1 character")
                Menu.button("2", Constant.SCREEN_WIDTH - 200, Constant.SCREEN_HEIGHT - 400, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "2 characters")

            # Mise à jour de l'affichage
            pygame.display.update()

            # Affiche l'image
            pygame.display.flip()

        # Initialisation de donnée lié à la partie
        clock = pygame.time.Clock()
        counter = 5
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        turn = 1
        player1_turn = True
        player2_turn = False
        player3_turn = False
        player1_character = 1
        player2_character = 1
        player3_character = 1
        while game_playing_screen:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            # Boucle d'événement
            for event in pygame.event.get():
                # Contrôle du timer
                if event.type == pygame.USEREVENT:
                    if counter <= 0:
                        counter = 6
                        turn += 1
                        if player == 2:
                            if player1_turn:
                                player1_turn = False
                                player2_turn = True
                            elif player2_turn:
                                player1_turn = True
                                player2_turn = False
                        elif player == 3:
                            if player1_turn:
                                player1_turn = False
                                player2_turn = True
                                player3_turn = False
                            elif player2_turn:
                                player1_turn = False
                                player2_turn = False
                                player3_turn = True
                            elif player3_turn:
                                player1_turn = True
                                player2_turn = False
                                player3_turn = False
                    counter -= 1

                # Si on détecte l'événement "quitter"
                if event.type == pygame.QUIT:
                    # Décharge les modules de la mémoire
                    Init.quit_game()
                    # Quitte le programme
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    # Ouvrir le menu pause
                    if event.key == pygame.K_ESCAPE:
                        if not game_pause_screen:
                            game_pause_screen = True

                    # A qui de jouer ?
                    if player1_turn:
                        if player1_character == 1:
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
                        elif player1_character == 2:
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
                    elif player2_turn:
                        if player2_character == 1:
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
                        elif player2_character == 2:
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
                    elif player3_turn:
                        if player3_character == 1:
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
                        elif player3_character == 2:
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
                            # player1.bazooka.weapon.surface = pygame.transform.rotate(player1.bazooka.weapon.surface, 1)
                        if event.key == pygame.K_f:
                            alpha -= 1
                            # player1.bazooka.weapon.surface = pygame.transform.rotate(player1.bazooka.weapon.surface, -1)

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

            while game_pause_screen:
                # Boucle d'événement
                for event in pygame.event.get():
                    # Si on détecte l'événement "quitter"
                    if event.type == pygame.QUIT:
                        # Décharge les modules de la mémoire
                        Init.quit_game()
                        # Quitte le programme
                        sys.exit()

                # Affichage de l'image de pause
                screen.blit(Menu.pause_background['surface'], Menu.pause_background['rect'])

                screen.blit(comicSansMsFont.render("Pause", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 350, Constant.SCREEN_HEIGHT - 400))
                # Affichage des bouttons
                Menu.button("Return", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 - 100, 150, 50, Constant.DARK, Constant.LIGHT_GREEN, "return")
                Menu.button("Home", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 - 25, 150, 50, Constant.LIGHT_DARK, Constant.LIGHT_GREEN, "home")
                Menu.button("Quit", Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT / 2 + 50, 150, 50, Constant.DARK_RED, Constant.LIGHT_GREEN, "quit")

                # Mise à jour de l'affichage
                pygame.display.update()

                # Affiche l'image
                pygame.display.flip()

            Animation.update_player_title(PlayerAsset.player1Character1, PlayerAsset.player1_character1_title)
            Animation.update_player_title(PlayerAsset.player2Character1, PlayerAsset.player2_character1_title)
            if player == 3:
                Animation.update_player_title(PlayerAsset.player3Character1, PlayerAsset.player3_character1_title)

            if character == 2:
                Animation.update_player_title(PlayerAsset.player1Character2, PlayerAsset.player1_character2_title)
                Animation.update_player_title(PlayerAsset.player2Character2, PlayerAsset.player2_character2_title)
                if player == 3:
                    Animation.update_player_title(PlayerAsset.player3Character2, PlayerAsset.player3_character2_title)

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
            if character == 2:
                if player1_turn:
                    if player1_character == 1:
                        Menu.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "joueur 1 personnage 1")
                        Menu.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "joueur 1 personnage 2")
                    elif player1_character == 2:
                        Menu.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "joueur 1 personnage 1")
                        Menu.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "joueur 1 personnage 2")
                elif player2_turn:
                    if player2_character == 1:
                        Menu.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "joueur 2 personnage 1")
                        Menu.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "joueur 2 personnage 2")
                    elif player2_character == 2:
                        Menu.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "joueur 2 personnage 1")
                        Menu.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "joueur 2 personnage 2")
                elif player3_turn:
                    if player3_character == 1:
                        Menu.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "joueur 3 personnage 1")
                        Menu.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "joueur 3 personnage 2")
                    elif player3_character == 2:
                        Menu.button("P1", Constant.SCREEN_WIDTH - 100, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.DARK, Constant.LIGHT_GREEN, "joueur 3 personnage 1")
                        Menu.button("P2", Constant.SCREEN_WIDTH - 50, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.INDIGO, Constant.LIGHT_GREEN, "joueur 3 personnage 2")

            # Affiche le personnage 1 du joueur 1 sur l'écran
            screen.blit(PlayerAsset.player1Character1['surface'], PlayerAsset.player1Character1['rect'])
            screen.blit(PlayerAsset.player1_character1_title['surface'], PlayerAsset.player1_character1_title['rect'])
            # Affiche le personnage 1 du joueur 2 sur l'écran
            screen.blit(PlayerAsset.player2Character1['surface'], PlayerAsset.player2Character1['rect'])
            screen.blit(PlayerAsset.player2_character1_title['surface'], PlayerAsset.player2_character1_title['rect'])
            if player == 3:
                # Affiche le personnage 1 du joueur 3 sur l'écran
                screen.blit(PlayerAsset.player3Character1['surface'], PlayerAsset.player3Character1['rect'])
                screen.blit(PlayerAsset.player3_character1_title['surface'], PlayerAsset.player3_character1_title['rect'])

            if character == 2:
                # Affiche le personnage 2 du joueur 1 sur l'écran
                screen.blit(PlayerAsset.player1Character2['surface'], PlayerAsset.player1Character2['rect'])
                screen.blit(PlayerAsset.player1_character2_title['surface'], PlayerAsset.player1_character2_title['rect'])
                # Affiche le personnage 2 du joueur 2 sur l'écran
                screen.blit(PlayerAsset.player2Character2['surface'], PlayerAsset.player2Character2['rect'])
                screen.blit(PlayerAsset.player2_character2_title['surface'], PlayerAsset.player2_character2_title['rect'])
                if player == 3:
                    # Affiche le personnage 2 du joueur 3 sur l'écran
                    screen.blit(PlayerAsset.player3Character2['surface'], PlayerAsset.player3Character2['rect'])
                    screen.blit(PlayerAsset.player3_character2_title['surface'], PlayerAsset.player3_character2_title['rect'])

            # Affiche le tour
            screen.blit(comicSansMsFont.render(str(turn), True, Constant.WHITE), (Constant.SCREEN_WIDTH - 630, Constant.SCREEN_HEIGHT - 475))
            if counter <= 0:
                screen.blit(comicSansMsFont.render("Tour suivant", True, Constant.WHITE), (Constant.SCREEN_WIDTH / 2 - 75, Constant.SCREEN_HEIGHT - 450))

            # Affiche le timer
            Menu.button(str(counter), Constant.SCREEN_WIDTH - 635, Constant.SCREEN_HEIGHT - 35, 30, 30, Constant.LIGHT_DARK, Constant.DARK)
            # Si joueur 1
            if player1_turn:
                screen.blit(comicSansMsFont.render("Joueur 1", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 33))
            # Si joueur 2
            elif player2_turn:
                screen.blit(comicSansMsFont.render("Joueur 2", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 33))
            # Si joueur 3
            elif player3_turn:
                screen.blit(comicSansMsFont.render("Joueur 3", True, Constant.WHITE), (Constant.SCREEN_WIDTH - 600, Constant.SCREEN_HEIGHT - 33))

            # Affiche l'image
            pygame.display.flip()

            # temp
            pygame.time.wait(5)

            # Clock tick
            clock.tick(60)

# call the "main" function if running this script
if __name__ == '__main__': main()

