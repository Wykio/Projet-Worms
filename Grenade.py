# -*-coding:Latin-1 -*


def player_select_grenade(player):
    if player['hold_grenade']:
        player['hold_grenade'] = False
    else:
        player['hold_grenade'] = True
    return player


def update_player_weapon(screen, player):
    if player['hold_grenade']:
        Asset.grenade['rect'] = Asset.player1['rect'].move(7, 15)
        screen.blit(Asset.grenade['surface'], Asset.grenade['rect'])

def grenade_launch(grenade):

    print("grenade Throw")