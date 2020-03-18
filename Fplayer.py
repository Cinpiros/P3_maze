
# player regroupe tout les déplacement du personage et interaction avec le labyrinthe
import pygame
import Fmap


class Player:
    #récupération des différent placement , nombre d'objet ect servant au déplacement du player et a ses intéraction
    def __init__(self, jeux, screen, floor_picture, player_picture,you_win_picture,you_lose_picture):
        self.screen = screen
        self.floor_picture = floor_picture
        self.player_picture = player_picture
        self.you_win_picture = you_win_picture
        self.you_lose_picture = you_lose_picture
        self.map = jeux.getmap()
        self.gamestop = jeux.getgamestop()
        self.gamecontinue = jeux.getgamecontinue()
        self.obj_recup = jeux.getobj_recup()
        self.nbr_obj = jeux.getnbr_obj()
        self.pose_obj_x = jeux.getpose_obj_x()
        self.pose_obj_y = jeux.getpose_obj_y()
        self.player_pose_y = jeux.getplayer_pose_y()
        self.player_pose_x = jeux.getplayer_pose_x()
        self.end_pose_y = jeux.getend_pose_y()
        self.end_pose_x = jeux.getend_pose_x()

    #déplacement a droite
    def player_move_right(self):
        #test si le jeux est terminer avec l'arriver sur le garde
        if self.gamestop == False:
            #test si le joueur est arriver sur la case du garde
            if self.map[self.player_pose_y +1][self.player_pose_x] == "a":
                #si le player a tout les objet il gagne sinon il perd
                if self.obj_recup == self.nbr_obj:
                    self.player_win()
                else:
                    self.player_lose()
            #test si le player se déplace sur une case sol
            if self.map[self.player_pose_y +1][self.player_pose_x] == "s":
                # vérification si le player se trouve sur une case objet si oui il récupère l'objet
                for ct in range(self.nbr_obj):
                    if self.pose_obj_x[ct] == self.player_pose_x and self.pose_obj_y[ct] == self.player_pose_y +1:
                        self.obj_recup = self.obj_recup + 1
                        self.pose_obj_x[ct] = 0
                        self.pose_obj_y[ct] = 0
                        #reaffichage du nombre d'objet récupérer sur le nombre d'objet a récupérer
                        pygame.draw.rect(self.screen, (0, 0, 0), (0, 300, 300, 20))
                        txt_nbr_obj = "objet : %s / %s" % (self.obj_recup,self.nbr_obj)
                        font = pygame.font.SysFont(None, 20)
                        text = font.render(txt_nbr_obj,1,(255,255,255))
                        self.screen.blit(text, (0, 300))
                #déplacement du joueur dans le tableau et visuellement 
                self.map[self.player_pose_y][self.player_pose_x] = "s"
                self.map[self.player_pose_y +1][self.player_pose_x] = "p"
                py = self.player_pose_y * 20
                px = self.player_pose_x * 20
                self.screen.blit(self.floor_picture, (py, px))
                self.screen.blit(self.player_picture, (py+20, px))
                self.player_pose_y = self.player_pose_y + 1
        else:
            self.stopgame()
    #déplacement a gauche
    def player_move_left(self):
        #test si le jeux est terminer avec l'arriver sur le garde
        if self.gamestop == False:
            #test si le joueur est arriver sur la case du garde
            if self.map[self.player_pose_y -1][self.player_pose_x] == "a":
                #si le player a tout les objet il gagne sinon il perd
                if self.obj_recup == self.nbr_obj:
                    self.player_win()
                else:
                    self.player_lose()
            #test si le player se déplace sur une case sol
            if self.map[self.player_pose_y -1][self.player_pose_x] == "s":
                # vérification si le player se trouve sur une case objet si oui il récupère l'objet
                for ct in range(self.nbr_obj):
                    if self.pose_obj_x[ct] == self.player_pose_x and self.pose_obj_y[ct] == self.player_pose_y -1:
                        self.obj_recup = self.obj_recup + 1
                        self.pose_obj_x[ct] = 0
                        self.pose_obj_y[ct] = 0
                        #reaffichage du nombre d'objet récupérer sur le nombre d'objet a récupérer
                        pygame.draw.rect(self.screen, (0, 0, 0), (0, 300, 300, 20))
                        txt_nbr_obj = "objet : %s / %s" % (self.obj_recup,self.nbr_obj)
                        font = pygame.font.SysFont(None, 20)
                        text = font.render(txt_nbr_obj,1,(255,255,255))
                        self.screen.blit(text, (0, 300))
                #déplacement du joueur dans le tableau et visuellement
                self.map[self.player_pose_y][self.player_pose_x] = "s"
                self.map[self.player_pose_y -1][self.player_pose_x] = "p"
                py = self.player_pose_y * 20
                px = self.player_pose_x * 20
                self.screen.blit(self.floor_picture, (py, px))
                self.screen.blit(self.player_picture, (py-20, px))
                self.player_pose_y = self.player_pose_y - 1
        else:
            self.stopgame()
    #déplacement au dessus
    def player_move_up(self):
        #test si le jeux est terminer avec l'arriver sur le garde
        if self.gamestop == False:
            #test si le joueur est arriver sur la case du garde
            if self.map[self.player_pose_y][self.player_pose_x -1] == "a":
                #si le player a tout les objet il gagne sinon il perd
                if self.obj_recup == self.nbr_obj:
                    self.player_win()
                else:
                    self.player_lose()
            #test si le player se déplace sur une case sol
            if self.map[self.player_pose_y][self.player_pose_x -1] == "s":
                # vérification si le player se trouve sur une case objet si oui il récupère l'objet
                for ct in range(self.nbr_obj):
                    if self.pose_obj_x[ct] == self.player_pose_x -1 and self.pose_obj_y[ct] == self.player_pose_y:
                        self.obj_recup = self.obj_recup + 1
                        self.pose_obj_x[ct] = 0
                        self.pose_obj_y[ct] = 0
                        #reaffichage du nombre d'objet récupérer sur le nombre d'objet a récupérer
                        pygame.draw.rect(self.screen, (0, 0, 0), (0, 300, 300, 20))
                        txt_nbr_obj = "objet : %s / %s" % (self.obj_recup,self.nbr_obj)
                        font = pygame.font.SysFont(None, 20)
                        text = font.render(txt_nbr_obj,1,(255,255,255))
                        self.screen.blit(text, (0, 300))
                #déplacement du joueur dans le tableau et visuellement
                self.map[self.player_pose_y][self.player_pose_x] = "s"
                self.map[self.player_pose_y][self.player_pose_x -1] = "p"
                py = self.player_pose_y * 20
                px = self.player_pose_x * 20
                self.screen.blit(self.floor_picture, (py, px))
                self.screen.blit(self.player_picture, (py, px-20))
                self.player_pose_x = self.player_pose_x - 1
        else:
            self.stopgame()
    #déplacement en dessous 
    def player_move_down(self):
        #test si le jeux est terminer avec l'arriver sur le garde
        if self.gamestop == False:
            #test si le joueur est arriver sur la case du garde
            if self.map[self.player_pose_y][self.player_pose_x +1] == "a":
                #si le player a tout les objet il gagne sinon il perd
                if self.obj_recup == self.nbr_obj:
                    self.player_win()
                else:
                    self.player_lose()
            #test si le player se déplace sur une case sol
            if self.map[self.player_pose_y][self.player_pose_x +1] == "s":
                # vérification si le player se trouve sur une case objet si oui il récupère l'objet
                for ct in range(self.nbr_obj):
                    if self.pose_obj_x[ct] == self.player_pose_x +1 and self.pose_obj_y[ct] == self.player_pose_y:
                        self.obj_recup = self.obj_recup + 1
                        self.pose_obj_x[ct] = 0
                        self.pose_obj_y[ct] = 0
                        #reaffichage du nombre d'objet récupérer sur le nombre d'objet a récupérer
                        pygame.draw.rect(self.screen, (0, 0, 0), (0, 300, 300, 20))
                        txt_nbr_obj = "objet : %s / %s" % (self.obj_recup,self.nbr_obj)
                        font = pygame.font.SysFont(None, 20)
                        text = font.render(txt_nbr_obj,1,(255,255,255))
                        self.screen.blit(text, (0, 300))
                #déplacement du joueur dans le tableau et visuellement
                self.map[self.player_pose_y][self.player_pose_x] = "s"
                self.map[self.player_pose_y][self.player_pose_x +1] = "p"
                py = self.player_pose_y * 20
                px = self.player_pose_x * 20
                self.screen.blit(self.floor_picture, (py, px))
                self.screen.blit(self.player_picture, (py, px+20))
                self.player_pose_x = self.player_pose_x + 1
        else:
            self.stopgame()
    
    #affichage de you win et arrèt du programme
    def player_win(self):
        self.screen.blit(self.you_win_picture, (0, 0))
        self.gamestop = True
    #affichage de you lose et arrèt du programme
    def player_lose(self):
        self.screen.blit(self.you_lose_picture, (0, 0))
        self.gamestop = True
    #arrèt de la boucle principale 
    def stopgame(self):
        self.gamecontinue = False