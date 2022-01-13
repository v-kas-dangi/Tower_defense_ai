import pygame
import os
from .enemies import Enemy
imgs=[]
enemySize=(55,55)
for x in range(20):
    imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/Enemies/2", "rick"+str(x)+".png")),enemySize))
class Rick(Enemy):
        
    def __init__(self):
        super().__init__()
        self.imgs=imgs[:]
        self.speed=1
        self.enemySize=enemySize
