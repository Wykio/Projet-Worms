# -*-coding:Latin-1 -*
import pygame

import Constant

#Auteur : Antoine

# Bouge un objet dans tout les sens
def animate_rect(rect):
    speed = Constant.SPEED
    rect = rect.move(speed)
    if rect.left < 0 or rect.right > Constant.SCREEN_WIDTH:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > Constant.SCREEN_HEIGHT:
        speed[1] = -speed[1]

    return rect


# Tentative de simulation de gravité
def gravity_rect(rect):
    if rect[1] < Constant.GROUND_HEIGHT:
        rect = rect.move([0, 1])
    return rect


# Bouge un objet vers la gauche
def move_left(rect):
    if rect.left > 0:
        rect = rect.move([-1, 0])
    return rect


# Bouge un objet vers la droite
def move_right(rect):
    if rect.right < Constant.SCREEN_WIDTH:
        rect = rect.move([1, 0])
    return rect


# Bouge le joueur et son sprite
def player_move_left(player):
    if player['looking_left']:
        player["rect"] = move_left(player["rect"])
    else:
        player["surface"] = pygame.transform.flip(player["surface"], 1, 0)
        player["rect"] = move_left(player["rect"])
        player['looking_left'] = True
    return player


def player_move_right(player):
    if player['looking_left']:
        player["surface"] = pygame.transform.flip(player["surface"], 1, 0)
        player["rect"] = move_right(player["rect"])
        player['looking_left'] = False
    else:
        player["rect"] = move_right(player["rect"])
    return player


def update_player_title(player, player_title):
    player_title['rect'] = player['rect'].move(-player_title['rect'][2] / 2, -player_title['rect'][3])






