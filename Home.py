import Constant
import pygame
import Worms
import Init
import sys

#Author : Benoit

# Dessiner les boutons et le texte
def text_objects(text, font):
    textSurface = font.render(text, True, Constant.BLACK)
    return textSurface, textSurface.get_rect()

# Dessiner les boutons et le texte
def button(msg, x, y, w, h, ic, ac, action =  None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global game_home
    global game_playing

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(Worms.screen, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            if action == "play":
                game_playing = True
                game_home = False
            elif action == "quit":
                game_home = False
                # Décharge les modules de la mémoire
                Init.quit_game()
                # Quitte le programme
                sys.exit()
    else:
        pygame.draw.rect(Worms.screen, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)) )
    Worms.screen.blit(textSurf, textRect)