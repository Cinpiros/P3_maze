#printmap est la gestion d'apparition aléatoire des objet et l'affichage de la map
from random import randint
import pygame

class PrintMap:
    #récupération des donnée concernant le joueur
    def getmap(self):
        return self.map
    
    def getgamestop(self):
        return self.gamestop

    def getgamecontinue(self):
        return self.gamecontinue

    def getobj_recup(self):
        return self.obj_recup

    def getnbr_obj(self):
        return self.nbr_obj

    def getpose_obj_x(self):
        return self.pose_obj_x

    def getpose_obj_y(self):
        return self.pose_obj_y

    def getplayer_pose_y(self):
        return self.player_pose_y

    def getplayer_pose_x(self):
        return self.player_pose_x

    def getend_pose_y(self):
        return self.end_pose_y

    def getend_pose_x(self):
        return self.end_pose_x

    # définition de la taille de la carte 
    def __init__(self, t_map):
        self.map_height = t_map
        self.gamecontinue = True
        self.gamestop = False
        self.obj_recup = 0
    #gestion des objet
    def smap(self,map,nbr_obj):
        self.nbr_obj = nbr_obj
        self.map = map
        self.num_floor = 0
        #conte du nombre de sol 
        for i in range (self.map_height):
            self.num_floor = self.num_floor + self.map[i].count("s")

        self.pose_obj_x = list()
        self.pose_obj_y = list()
        self.list_random = list()
        nbr_random = 0
        #random pour la position des objet et enregistrement des position dans une liste
        while nbr_random != self.nbr_obj:
            new_number = randint(1,self.num_floor)
            if self.list_random.count(new_number) == 0:
                self.list_random.append(new_number)
                nbr_random = nbr_random + 1

    #affichage du labyrinthe
    def print_map(self, screen, t_map, floor_picture, wall_picture, player_picture, guard_picture, objet_picture, sword_picture, shield_picture, armor_picture):
        ct_obj = 0
        num_obj = 1
        # boucle x et y (largeur et hauteur)
        for x in range(1, self.map_height +1):
            for y in range(1, self.map_height +1):
                px = x * 20
                py = y * 20
                px =  px - 20
                py =  py - 20
                #affichage d'un mur ou sol selon le tableau
                if self.map[y-1][x-1] == "m":
                    screen.blit(wall_picture, (py, px))
                if self.map[y-1][x-1] == "s":
                    ct_obj = ct_obj + 1
                    # test si a la place du sol il dit apparaitre un objet
                    if self.list_random.count(ct_obj) == 0:
                        screen.blit(floor_picture, (py, px))
                    else:
                        #affichage d'un objet et enregistrement des coordonée
                        if num_obj == 1:
                            screen.blit(sword_picture, (py, px))
                            num_obj = num_obj + 1
                        elif num_obj == 2:
                            screen.blit(shield_picture, (py, px))
                            num_obj = num_obj + 1
                        elif num_obj == 3:
                            screen.blit(armor_picture, (py, px))
                            num_obj = num_obj + 1
                        else:
                            screen.blit(objet_picture, (py, px))
                        self.pose_obj_x.append(x-1)
                        self.pose_obj_y.append(y-1)
                # si la case est le player affichage du joueur et enregistrement de sa position
                if self.map[y-1][x-1] == "p":
                    screen.blit(player_picture, (py, px))
                    self.player_pose_y = y-1
                    self.player_pose_x = x-1
                # si la case est le garde affichage du garde et enregistrement de sa position
                if self.map[y-1][x-1] == "a":
                    screen.blit(guard_picture, (py, px))
                    self.end_pose_y = y-1
                    self.end_pose_x = x-1
        #affichage du nombre d'objet récupérer sur le nombre d'objet a récupérer
        txt_nbr_obj = "objet : %s / %s" % (self.obj_recup,self.nbr_obj)
        font = pygame.font.SysFont(None, 20)
        text = font.render(txt_nbr_obj,1,(255,255,255))
        screen.blit(text, (0, 300))