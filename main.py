#!/usr/bin/env python3
# coding: utf-8

#main

import pygame
import Fimportmap
import Fplayer
import Fmap


# fonction main qui contien les event de déplacement et fermeture 
def main():
    map_height = 15
    nbr_obj = 3

    #import de la carte 
    ip_map = Fimportmap.LoadingMap(map_height)
    #formatage de la carte
    map = ip_map.ep_map()

    #import des sprite
    screen = pygame.display.set_mode((map_height *20, map_height *20+20))
    you_win_picture = pygame.image.load("ressource/you_win.png").convert_alpha()
    you_lose_picture = pygame.image.load("ressource/you_lose.png").convert_alpha()
    floor_picture = pygame.image.load("ressource/floor.png").convert_alpha()
    wall_picture = pygame.image.load("ressource/wall.png").convert_alpha()
    player_picture = pygame.image.load("ressource/player.png").convert_alpha()
    guard_picture = pygame.image.load("ressource/guard.png").convert_alpha()
    objet_picture = pygame.image.load("ressource/objet.png").convert_alpha()
    sword_picture = pygame.image.load("ressource/sword.png").convert_alpha()
    shield_picture = pygame.image.load("ressource/shield.png").convert_alpha()
    armor_picture = pygame.image.load("ressource/armor.png").convert_alpha()
    #création jeux
    jeux = Fmap.PrintMap(map_height)
    # création des objet du labyrinthe 
    jeux.smap(map,nbr_obj)
    #init pygame
    pygame.init()
    #premiere affichage de la carte
    jeux.print_map(screen,map_height,floor_picture,wall_picture,player_picture,guard_picture,objet_picture,sword_picture,shield_picture,armor_picture)
    #création Pmove 
    Pmove = Fplayer.Player(jeux,screen,floor_picture,player_picture,you_win_picture,you_lose_picture)
    #boucle principale pygame
    while Pmove.gamecontinue:
        #différent évent de déplacement
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Pmove.player_move_left()
                if event.key == pygame.K_RIGHT:
                    Pmove.player_move_right()
                if event.key == pygame.K_UP:
                    Pmove.player_move_up()
                if event.key == pygame.K_DOWN:
                    Pmove.player_move_down()
            #évent cliquer sur la croix pour stoper le programme
            if event.type == pygame.QUIT:  
                Pmove.stopgame()
        pygame.display.flip()

    pygame.quit()

main()

