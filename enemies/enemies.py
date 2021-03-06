import pygame
import math
import os

class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.animation_count = 0
        self.health = 6
        self.vel = 3
        self.path = [(5, 318), (53, 346), (113, 401), (172, 414), (227, 366), (276, 284), (320, 284), (383, 292), (434, 247), (492, 214), (550, 206), (611, 216), (668, 246), (706, 303), (724, 354), (717, 375), (682, 428), (638, 455), (589, 471), (540, 472), (487, 463), (496, 419), (507, 378), (531, 347)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        self.imgs = []
        self.completed=False

        self.flipped = False
        self.max_health = 0
        self.speed_increase = 1.2


    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        self.img = self.imgs[self.animation_count//15]
        win.blit(self.img,(self.x-self.enemySize[0]//2, self.y-self.enemySize[1]//2))
        self.draw_health_bar(win)
        

    def draw_health_bar(self, win):
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """
        length = 50
        health_bar=round(self.health/self.max_health*length)
        pygame.draw.rect(win, (255, 0, 20), (self.x-self.enemySize[0]//2, self.y-(self.enemySize[1]+15)//2,length, 7) ,0)
        pygame.draw.rect(win, (20, 255, 20), (self.x-self.enemySize[0]//2, self.y-(self.enemySize[1]+15)//2,health_bar, 7) ,0)


    def collide(self, X, Y):
        """
        Returns if position has hit enemy
        :param x: int
        :param y: int
        :return: Bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self):
        """
        Move enemy
        :return: None
        """
        self.animation_count+=1
        if(self.animation_count>=len(self.imgs)*15):
            self.animation_count=0

        if(self.path_pos<len(self.path)):
            if(self.x<(self.path[self.path_pos])[0]):
                self.x+=self.speed
            elif(self.x>(self.path[self.path_pos])[0]):
                self.x-=self.speed
            if(self.y<(self.path[self.path_pos])[1]):
                self.y+=self.speed
            elif(self.y>(self.path[self.path_pos])[1]):
                self.y-=self.speed
            z=(self.path[self.path_pos][0]-self.x, self.path[self.path_pos][1]-self.y)

            if(z[0]<=0 and not(self.flipped)):
                self.flipped=True
                for count, img in enumerate(self.imgs):
                    self.imgs[count]=pygame.transform.flip(img, True, False)
            elif(z[0]>0 and self.flipped):
                self.flipped=False
                for count, img in enumerate(self.imgs):
                    self.imgs[count]=pygame.transform.flip(img, True, False)
            if(abs(z[0])//self.speed, abs(z[1])//self.speed)==(0,0):
                self.path_pos+=1
        else:
            self.completed=True

    def hit(self, damage):
        """
        Returns if an enemy has died and removes one health
        each call
        :return: Bool
        """
        self.health -= damage
        if self.health <= 0:
            return True
        return False
